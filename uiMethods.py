import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from uiCode import Ui_MainWindow
from uiFootprint import Ui_mainWindow2

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

        self.btnSubmit.clicked.connect(lambda: Controller.Show_CalcWindow(self))
        self.btnSubmit.clicked.connect(lambda: self.hide())



class CalculatorWindow(QtWidgets.QMainWindow, Ui_mainWindow2):

    def __init__(self, parent=None):
        super(CalculatorWindow, self).__init__(parent=parent)
        self.ui = Ui_mainWindow2()
        self.setupUi(self)
        self.show()
        self.showMaximized()



class Controller():

    def __init__(self):
        pass

    def Show_MainWindow(self):
        self.MainWindow = MainWindow()


    def Show_CalcWindow(self):
        self.CalculatorWindow = CalculatorWindow()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.Show_MainWindow()
    sys.exit(app.exec_())


    # pyuic5 -x <.ui file> -o <output.py file>
