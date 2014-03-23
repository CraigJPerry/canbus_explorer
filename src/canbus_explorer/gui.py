#!/usr/bin/env python
# encoding: utf-8


from PySide import QtGui
from canbus_explorer.autogen.main_window import Ui_MainWindow


class CanbusApplicationGUI(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(CanbusApplicationGUI, self).__init__(parent)
        self.setupUi(self)


def launch_gui_mainloop(argv):
    """Qt application entry point."""

    app = QtGui.QApplication(argv)

    window = CanbusApplicationGUI()
    window.show()

    return app.exec_()

