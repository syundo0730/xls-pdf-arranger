# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI.ui'
#
# Created: Wed Aug 07 01:08:54 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(281, 235)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 58, 161, 111))
		self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
		self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setMargin(0)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.modbar = QtGui.QSlider(self.verticalLayoutWidget)
		self.modbar.setMaximum(100)
		self.modbar.setProperty("value", 50)
		self.modbar.setOrientation(QtCore.Qt.Horizontal)
		self.modbar.setObjectName(_fromUtf8("modbar"))
		self.verticalLayout.addWidget(self.modbar)
		self.upmarginbar = QtGui.QSlider(self.verticalLayoutWidget)
		self.upmarginbar.setMaximum(10)
		self.upmarginbar.setProperty("value", 2)
		self.upmarginbar.setOrientation(QtCore.Qt.Horizontal)
		self.upmarginbar.setObjectName(_fromUtf8("upmarginbar"))
		self.verticalLayout.addWidget(self.upmarginbar)
		self.downmarginbar = QtGui.QSlider(self.verticalLayoutWidget)
		self.downmarginbar.setMaximum(10)
		self.downmarginbar.setProperty("value", 1)
		self.downmarginbar.setOrientation(QtCore.Qt.Horizontal)
		self.downmarginbar.setObjectName(_fromUtf8("downmarginbar"))
		self.verticalLayout.addWidget(self.downmarginbar)
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(200, 71, 50, 12))
		self.label.setObjectName(_fromUtf8("label"))
		self.label_1 = QtGui.QLabel(self.centralwidget)
		self.label_1.setGeometry(QtCore.QRect(200, 104, 50, 12))
		self.label_1.setObjectName(_fromUtf8("label_1"))
		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(200, 140, 50, 12))
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.rcsvbtn = QtGui.QPushButton(self.centralwidget)
		self.rcsvbtn.setGeometry(QtCore.QRect(20, 20, 75, 23))
		self.rcsvbtn.setCheckable(False)
		self.rcsvbtn.setObjectName(_fromUtf8("rcsvbtn"))
		self.wpdfbtn = QtGui.QPushButton(self.centralwidget)
		self.wpdfbtn.setGeometry(QtCore.QRect(170, 190, 75, 23))
		self.wpdfbtn.setObjectName(_fromUtf8("wpdfbtn"))
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.label.setText(_translate("MainWindow", "割合", None))
		self.label_1.setText(_translate("MainWindow", "上余白", None))
		self.label_2.setText(_translate("MainWindow", "下余白", None))
		self.rcsvbtn.setText(_translate("MainWindow", "CSV選択", None))
		self.wpdfbtn.setText(_translate("MainWindow", "書き出し", None))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

