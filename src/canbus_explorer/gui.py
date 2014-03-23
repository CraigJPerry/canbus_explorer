#!/usr/bin/env python
# encoding: utf-8


from PySide import QtCore, QtGui
from canbus_explorer.main_window import Ui_MainWindow


class MyApplication(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)


def launch_mainloop(argv):
    app = QtGui.QApplication(argv)
    window = MyApplication()
    window.show()
    return app.exec_()

