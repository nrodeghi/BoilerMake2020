import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from uiCode import Ui_MainWindow
from uiFootprint import Ui_mainWindow2
from uiTips import Ui_MainWindow3

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

        self.btnCalc.clicked.connect(lambda: self.carbonFootprint(self.leDrive.text(), self.lePlane.text(),
                                                                  self.leBeef.text(), self.leShop.text()))

        self.btnNext.clicked.connect(lambda: Controller.Show_Tips(self))
        self.btnNext.clicked.connect(lambda: self.hide())



    def carbonFootprint(self, milesDrove, flightHours, beefConsumed, shoppingTrips):
        # driving is the main way people travel in the US short-term
        # flying is the most common way people travel long distance
        # consumption of the beef has a higher carbon footprint than any other food
        # shopping in person produces a significant amount of CO2
        c1 = float(milesDrove) * 14.25 * 52
        c2 = float(flightHours) * 8818.49
        c3 = float(beefConsumed) * 26.44 * 4 * 52
        c4 = float(shoppingTrips) * 144 * 52
        c_total = c1 + c2 + c3 + c4
        c_total = c_total / 32000
        c_total = (c_total * 12) + 3.7

        self.leFoot.setText("You contribute %.2f tons of CO2 per year" % c_total)


class TipsWindow(QtWidgets.QMainWindow, Ui_MainWindow3):
    def __init__(self, parent=None):
        super(TipsWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow3()
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

    def Show_Tips(self):
        self.TipsWindow = TipsWindow()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.Show_MainWindow()
    sys.exit(app.exec_())


    # pyuic5 -x <.ui file> -o <output.py file>
