import sys

from PyQt5 import QtCore, QtGui
from uiCode import Ui_MainWindow

class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
