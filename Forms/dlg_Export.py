# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rammc\Documents\PycharmProjects\BDO_Enhancement_Tool\Forms\dlg_Export.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Export(object):
    def setupUi(self, Dialog_Export):
        Dialog_Export.setObjectName("Dialog_Export")
        Dialog_Export.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_Export)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog_Export)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_csv = QtWidgets.QWidget()
        self.tab_csv.setObjectName("tab_csv")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_csv)
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chk_fs = QtWidgets.QCheckBox(self.tab_csv)
        self.chk_fs.setObjectName("chk_fs")
        self.verticalLayout_2.addWidget(self.chk_fs)
        self.tabWidget.addTab(self.tab_csv, "")
        self.tab_excel = QtWidgets.QWidget()
        self.tab_excel.setObjectName("tab_excel")
        self.tabWidget.addTab(self.tab_excel, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Export)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_Export)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog_Export.accept)
        self.buttonBox.rejected.connect(Dialog_Export.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Export)

    def retranslateUi(self, Dialog_Export):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Export.setWindowTitle(_translate("Dialog_Export", "Export Files"))
        self.chk_fs.setText(_translate("Dialog_Export", "Fail Stack List"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_csv), _translate("Dialog_Export", "CSV Files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_excel), _translate("Dialog_Export", "Excel File"))

