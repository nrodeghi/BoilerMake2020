import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from uiCode import Ui_MainWindow

class MyForm(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MyForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
