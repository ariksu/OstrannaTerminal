# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Variables.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(517, 317)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.VarTab = QtWidgets.QWidget()
        self.VarTab.setObjectName("VarTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.VarTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LineName = QtWidgets.QLineEdit(self.VarTab)
        self.LineName.setObjectName("LineName")
        self.gridLayout_2.addWidget(self.LineName, 3, 2, 1, 1)
        self.LblValue = QtWidgets.QLabel(self.VarTab)
        self.LblValue.setObjectName("LblValue")
        self.gridLayout_2.addWidget(self.LblValue, 3, 3, 1, 1)
        self.LblName = QtWidgets.QLabel(self.VarTab)
        self.LblName.setObjectName("LblName")
        self.gridLayout_2.addWidget(self.LblName, 3, 1, 1, 1)
        self.LineValue = QtWidgets.QLineEdit(self.VarTab)
        self.LineValue.setObjectName("LineValue")
        self.gridLayout_2.addWidget(self.LineValue, 3, 4, 1, 1)
        self.BtnAdd = QtWidgets.QPushButton(self.VarTab)
        self.BtnAdd.setObjectName("BtnAdd")
        self.gridLayout_2.addWidget(self.BtnAdd, 3, 5, 1, 1)
        self.ListVariables = QtWidgets.QListWidget(self.VarTab)
        self.ListVariables.setObjectName("ListVariables")
        item = QtWidgets.QListWidgetItem()
        self.ListVariables.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListVariables.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListVariables.addItem(item)
        self.gridLayout_2.addWidget(self.ListVariables, 1, 0, 1, 7)
        self.LblTitle = QtWidgets.QLabel(self.VarTab)
        self.LblTitle.setObjectName("LblTitle")
        self.gridLayout_2.addWidget(self.LblTitle, 0, 0, 1, 2)
        self.tabWidget.addTab(self.VarTab, "")
        self.RangeTab = QtWidgets.QWidget()
        self.RangeTab.setObjectName("RangeTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.RangeTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 5, 1, 1, 1)
        self.LblVarName = QtWidgets.QLabel(self.RangeTab)
        self.LblVarName.setObjectName("LblVarName")
        self.gridLayout_3.addWidget(self.LblVarName, 0, 0, 1, 1)
        self.SliderVar = QtWidgets.QSlider(self.RangeTab)
        self.SliderVar.setOrientation(QtCore.Qt.Horizontal)
        self.SliderVar.setObjectName("SliderVar")
        self.gridLayout_3.addWidget(self.SliderVar, 2, 0, 1, 6)
        self.LineCurrent = QtWidgets.QLineEdit(self.RangeTab)
        self.LineCurrent.setObjectName("LineCurrent")
        self.gridLayout_3.addWidget(self.LineCurrent, 0, 4, 1, 2)
        self.LblCurrent = QtWidgets.QLabel(self.RangeTab)
        self.LblCurrent.setObjectName("LblCurrent")
        self.gridLayout_3.addWidget(self.LblCurrent, 0, 3, 1, 1)
        self.LineVarName = QtWidgets.QLineEdit(self.RangeTab)
        self.LineVarName.setObjectName("LineVarName")
        self.gridLayout_3.addWidget(self.LineVarName, 0, 1, 1, 2)
        self.LblMin = QtWidgets.QLabel(self.RangeTab)
        self.LblMin.setObjectName("LblMin")
        self.gridLayout_3.addWidget(self.LblMin, 1, 0, 1, 1)
        self.SpinMin = QtWidgets.QSpinBox(self.RangeTab)
        self.SpinMin.setMinimum(-999999)
        self.SpinMin.setMaximum(999999)
        self.SpinMin.setObjectName("SpinMin")
        self.gridLayout_3.addWidget(self.SpinMin, 1, 1, 1, 1)
        self.LblMax = QtWidgets.QLabel(self.RangeTab)
        self.LblMax.setObjectName("LblMax")
        self.gridLayout_3.addWidget(self.LblMax, 1, 2, 1, 1)
        self.SpinMax = QtWidgets.QSpinBox(self.RangeTab)
        self.SpinMax.setMinimum(-99999999)
        self.SpinMax.setMaximum(99999999)
        self.SpinMax.setProperty("value", 100)
        self.SpinMax.setObjectName("SpinMax")
        self.gridLayout_3.addWidget(self.SpinMax, 1, 3, 1, 1)
        self.LblStep = QtWidgets.QLabel(self.RangeTab)
        self.LblStep.setObjectName("LblStep")
        self.gridLayout_3.addWidget(self.LblStep, 1, 4, 1, 1)
        self.SpinStep = QtWidgets.QSpinBox(self.RangeTab)
        self.SpinStep.setMinimum(-9999999)
        self.SpinStep.setMaximum(9999999)
        self.SpinStep.setProperty("value", 1)
        self.SpinStep.setObjectName("SpinStep")
        self.gridLayout_3.addWidget(self.SpinStep, 1, 5, 1, 1)
        self.LblCommand = QtWidgets.QLabel(self.RangeTab)
        self.LblCommand.setObjectName("LblCommand")
        self.gridLayout_3.addWidget(self.LblCommand, 3, 0, 1, 1)
        self.LineCommand = QtWidgets.QLineEdit(self.RangeTab)
        self.LineCommand.setObjectName("LineCommand")
        self.gridLayout_3.addWidget(self.LineCommand, 4, 0, 1, 6)
        self.BtnSend = QtWidgets.QPushButton(self.RangeTab)
        self.BtnSend.setObjectName("BtnSend")
        self.gridLayout_3.addWidget(self.BtnSend, 3, 5, 1, 1)
        self.CBAuto = QtWidgets.QCheckBox(self.RangeTab)
        self.CBAuto.setChecked(True)
        self.CBAuto.setObjectName("CBAuto")
        self.gridLayout_3.addWidget(self.CBAuto, 3, 1, 1, 2)
        self.tabWidget.addTab(self.RangeTab, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 1, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Variables"))
        self.LblValue.setText(_translate("Form", "Variable Value"))
        self.LblName.setText(_translate("Form", "Variable Name"))
        self.BtnAdd.setText(_translate("Form", "Add variable"))
        __sortingEnabled = self.ListVariables.isSortingEnabled()
        self.ListVariables.setSortingEnabled(False)
        item = self.ListVariables.item(0)
        item.setText(_translate("Form", "$length = <selected file length>"))
        item = self.ListVariables.item(1)
        item.setText(_translate("Form", "$crc = <selected file crc>"))
        item = self.ListVariables.item(2)
        item.setText(_translate("Form", "$file_data = <selected file binary data>"))
        self.ListVariables.setSortingEnabled(__sortingEnabled)
        self.LblTitle.setText(_translate("Form", "List of variables"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VarTab), _translate("Form", "Variables"))
        self.LblVarName.setText(_translate("Form", "Variable Name"))
        self.LblCurrent.setText(_translate("Form", "Current value"))
        self.LblMin.setText(_translate("Form", "Min Value:"))
        self.LblMax.setText(_translate("Form", "Max Value:"))
        self.LblStep.setText(_translate("Form", "Step:"))
        self.LblCommand.setText(_translate("Form", "Command: "))
        self.BtnSend.setText(_translate("Form", "Send"))
        self.CBAuto.setText(_translate("Form", "AutoSend"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RangeTab), _translate("Form", "Variable Range"))
