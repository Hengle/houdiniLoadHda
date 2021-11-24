# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiHoudiniLoadHdaueoAtS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(715, 777)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEditFilter = QLineEdit(Form)
        self.lineEditFilter.setObjectName(u"lineEditFilter")

        self.horizontalLayout.addWidget(self.lineEditFilter)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushLoadHda = QPushButton(Form)
        self.pushLoadHda.setObjectName(u"pushLoadHda")
        self.pushLoadHda.setMinimumSize(QSize(100, 0))
        self.pushLoadHda.setMaximumSize(QSize(120, 16777215))
        self.pushLoadHda.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_2.addWidget(self.pushLoadHda)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)

        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_2.addWidget(self.tableView, 1, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(200, 0))
        self.comboBox.setEditable(True)

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushSavePreset = QPushButton(Form)
        self.pushSavePreset.setObjectName(u"pushSavePreset")

        self.horizontalLayout_3.addWidget(self.pushSavePreset)

        self.pushLoadPreset = QPushButton(Form)
        self.pushLoadPreset.setObjectName(u"pushLoadPreset")
        self.pushLoadPreset.setMinimumSize(QSize(100, 0))
        self.pushLoadPreset.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.pushLoadPreset)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Filter", None))
        self.pushLoadHda.setText(QCoreApplication.translate("Form", u"Load HDA", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"NewPreset", None))

        self.pushSavePreset.setText(QCoreApplication.translate("Form", u"Save Preset", None))
        self.pushLoadPreset.setText(QCoreApplication.translate("Form", u"Load Preset", None))
    # retranslateUi

