import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from uiCode import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.showMaximized()
        self.initialState()

    def initialState(self):
        self.cbAge.addItem("18-22")
        self.cbAge.addItem("23-27")
        self.cbAge.setCurrentIndex(-1)
        self.cbEdu.addItem("In full-time education")
        self.cbEdu.addItem("In part-time education")
        self.cbEdu.setCurrentIndex(-1)
        self.cbTime.addItem("Less than 5 minutes")
        self.cbTime.addItem("Less than 15 minutes")
        self.cbTime.addItem("Less than 1 hour")
        self.cbTime.addItem("More than 1 hour")
        self.cbTime.addItem("I dont travel")
        self.cbTime.setCurrentIndex(-1)
        self.cbOthers.addItem("Yes")
        self.cbOthers.addItem("No")
        self.cbOthers.setCurrentIndex(-1)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MainWindow()
    myApp.show()
    sys.exit(app.exec_())

    # pyuic5 -x <.ui file> -o <output.py file>
