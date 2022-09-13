import sys, os, glob, platform, json, hou

from PySide2.QtWidgets import *
from PySide2 import QtCore
from PySide2 import QtGui

from uiHoudiniLoadHda import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.model = QtGui.QStandardItemModel(self)
        self.root = "/media/500GB_HDD_01/TST/otls"
        self.comment_path = os.path.join(self.root, ".usercomments")
        self.preset_path = os.path.join(self.root, ".userpresets")
        self.hda_paths = []
        self.hda_names = []
        self.loadedHda = []
        self.preset = {}
        self.comments = {}
        self.proxy = QtCore.QSortFilterProxyModel(self)
        self.readPreset()
        self.initList()
        self.updatePresetList()
        # self.loadPreset()
        
        self.lineEditFilter.textChanged.connect(self.filterList)
        self.checkBoxFilterChecked.stateChanged.connect(self.filterList)
        self.pushCheck.clicked.connect(self.checkSelected)
        self.pushUncheck.clicked.connect(self.uncheckSelected)
        self.pushLoadHda.clicked.connect(self.installAssets)
        self.pushSavePreset.clicked.connect(self.savePreset)
        # self.pushLoadPreset.clicked.connect(self.loadPreset)
        self.comboBox.currentTextChanged.connect(self.loadPreset)
        self.comboBox.highlighted.connect(self.loadPreset)

    def closeEvent(self, event):
        self.setParent(None)
        self.updateCommentsFile()

    def initList(self):
        self.hda_paths = glob.glob(os.path.join(self.root, "*.hda"))
        self.hda_paths.extend(glob.glob(os.path.join(self.root, "*.otl")))
        self.hda_names = [os.path.split(filepath)[1] for filepath in self.hda_paths]
        [self.loadedHda.append(os.path.split(path)[1]) for path in hou.hda.loadedFiles()]
        for row, file in enumerate(self.hda_names):
            item = QtGui.QStandardItem("{}".format(file))
            item.setCheckable(True)
            in_hda_folder = file in self.loadedHda
            if in_hda_folder:
                item.setCheckState(QtCore.Qt.CheckState.Checked)
            try:
                comment_text = self.comments["__comments"][file]
            except KeyError:
                comment_text = ""
            comment = QtGui.QStandardItem("{}".format(comment_text))
            comment.setEditable(True)
            item.setEditable(False)
            self.model.invisibleRootItem().appendRow([item, comment])
        self.proxy.setSourceModel(self.model)
        self.listView.setModel(self.proxy)
        self.listView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    def updateCommentsFile(self):
        comments_list = {}
        for row, file in enumerate(self.hda_names):
            index = self.model.index(row, 1)
            comment = self.model.itemFromIndex(index).text()
            comments_list[file] = comment
        with open(self.comment_path, 'w') as f:
            self.comments["__comments"] = comments_list
            jsn = json.dumps(self.comments, indent=4)
            f.write(jsn)

    def filterChecked(self):
        role_check = QtCore.Qt.CheckStateRole
        state = QtCore.Qt.CheckState.Checked
        rows_number = self.proxy.rowCount()
        start = self.proxy.index(0, 0)
        checked_list = self.proxy.match(start, role_check, state, rows_number)
        if self.checkBoxFilterChecked.isChecked():
            for row in range(self.proxy.rowCount()):
                index = self.proxy.index(row, 0)
                if index not in checked_list:
                    self.listView.hideRow(row)
                else:
                    self.listView.showRow(row)
        else:
            for row in range(self.proxy.rowCount()):
                self.listView.showRow(row)

    def filterList(self):
        text = self.lineEditFilter.text()
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        self.filterChecked()
        self.proxy.setFilterRegExp(search)

    def installAssets(self):
        for row, file in enumerate(self.hda_paths):
            index = self.model.index(row, 0)
            item = self.model.itemFromIndex(index)
            check_state = item.checkState()
            if check_state == QtCore.Qt.CheckState.Checked:
                hda_installed = self.hda_names[row] in self.loadedHda
                if not hda_installed:
                    print("Installing HDA {}".format(self.hda_names[row]))
                    try:
                        hou.hda.installFile(file)
                    except:
                        pass

    def checkSelected(self):
        selection_model = self.listView.selectionModel()
        selected = selection_model.selectedIndexes()
        for index in selected:
            src_index = self.proxy.mapToSource(index)
            if index.column() == 0:
                self.model.itemFromIndex(src_index).setCheckState(QtCore.Qt.CheckState.Checked)

    def uncheckSelected(self):
        selection_model = self.listView.selectionModel()
        selected = selection_model.selectedIndexes()
        for index in selected:
            src_index = self.proxy.mapToSource(index)
            self.model.itemFromIndex(src_index).setCheckState(QtCore.Qt.CheckState.Unchecked)

    def readPreset(self):
        try:
            with open(self.preset_path, 'r') as f:
                try:
                    self.preset = json.load(f)
                except ValueError:
                    self.preset = {}
        except IOError:
            self.preset = {}
        try:
            with open(self.comment_path, 'r') as f:
                try:
                    self.comments = json.load(f)
                except ValueError:
                    self.comments = {}
        except IOError:
            self.comments = {}

    def updatePresetList(self):
        keys = self.preset.keys()
        self.comboBox.clear()
        for key in keys:
            self.comboBox.addItem(key)

    def loadPreset(self):
        try:
            for row, file in enumerate(self.hda_paths):
                index = self.model.index(row, 0)
                item = self.model.itemFromIndex(index)
                list_of_checked_items = self.preset[self.comboBox.currentText()]
                if self.hda_names[row] in list_of_checked_items:
                    item.setCheckState(QtCore.Qt.CheckState.Checked)
                else:
                    item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        except KeyError:
            pass

    def savePreset(self):
        list_of_checked_items = []
        for row, file in enumerate(self.hda_paths):
            index = self.model.index(row, 0)
            item = self.model.itemFromIndex(index)
            check_state = item.checkState()
            if check_state == QtCore.Qt.CheckState.Checked:
                list_of_checked_items.append(self.hda_names[row])
        with open(self.preset_path, 'w') as f:
            self.preset[self.comboBox.currentText()] = list_of_checked_items
            jsn = json.dumps(self.preset, indent=4)
            f.write(jsn)
