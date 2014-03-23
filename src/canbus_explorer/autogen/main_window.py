# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/resources/main_window.ui'
#
# Created: Sun Mar 23 00:09:53 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.messagesTableView = QtGui.QTableView(self.centralwidget)
        self.messagesTableView.setFrameShape(QtGui.QFrame.Panel)
        self.messagesTableView.setFrameShadow(QtGui.QFrame.Plain)
        self.messagesTableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.messagesTableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.messagesTableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.messagesTableView.setProperty("showDropIndicator", False)
        self.messagesTableView.setAlternatingRowColors(True)
        self.messagesTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.messagesTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.messagesTableView.setSortingEnabled(True)
        self.messagesTableView.setObjectName("messagesTableView")
        self.gridLayout.addWidget(self.messagesTableView, 3, 0, 1, 3)
        self.consoleLogPlainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.consoleLogPlainTextEdit.sizePolicy().hasHeightForWidth())
        self.consoleLogPlainTextEdit.setSizePolicy(sizePolicy)
        self.consoleLogPlainTextEdit.setFrameShape(QtGui.QFrame.Panel)
        self.consoleLogPlainTextEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.consoleLogPlainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.consoleLogPlainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.consoleLogPlainTextEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.consoleLogPlainTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.consoleLogPlainTextEdit.setObjectName("consoleLogPlainTextEdit")
        self.gridLayout.addWidget(self.consoleLogPlainTextEdit, 4, 0, 1, 3)
        self.connectPushButton = QtGui.QPushButton(self.centralwidget)
        self.connectPushButton.setDefault(True)
        self.connectPushButton.setFlat(False)
        self.connectPushButton.setObjectName("connectPushButton")
        self.gridLayout.addWidget(self.connectPushButton, 0, 2, 1, 1)
        self.portComboBox = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portComboBox.sizePolicy().hasHeightForWidth())
        self.portComboBox.setSizePolicy(sizePolicy)
        self.portComboBox.setFrame(True)
        self.portComboBox.setObjectName("portComboBox")
        self.gridLayout.addWidget(self.portComboBox, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Canbus Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.connectPushButton.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))

