import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from uiCode import Ui_MainWindow
from uiFootprint import Ui_mainWindow2
from uiTips import Ui_MainWindow3
from ModelTestingFinal import *

MD = 0.0
FH = 0.0
BC = 0.0
ST = 0.0
result = ""

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        #self.show()
        self.showMaximized()
        self.initialState()

        #self.btnSubmit.clicked.connect(lambda: self.switchWindow())
        self.btnSubmit.clicked.connect(lambda: self.sendData())

    def sendData(self):
        global result

        arr = [self.cbAge.currentText(), self.cbEdu.currentText(), self.cbWork.currentText(), self.chWalk.isChecked(),
               self.chBus.isChecked(), self.chCar.isChecked(), self.chNone.isChecked(),
               self.cbTime.currentText(), self.slEng.value(), self.cbYou.currentText(), self.slKnow.value(),
               self.slPrint.value(), self.chTry1.isChecked(), self.chTry2.isChecked(), self.chTry3.isChecked(),
               self.chTry4.isChecked(),
               self.chTry5.isChecked(), self.cbOthers.currentText()]
        # arr.append(self.cbAge.currentText())
        # arr.append(self.cbEdu.currentText())
        # arr.append(self.cbWork.currentText())
        # arr.append(self.chWalk.isChecked())
        # arr.append(self.chBus.isChecked())
        # arr.append(self.chCar.isChecked()) # modes of transport
        # arr.append(self.chNone.isChecked())
        # arr.append(self.cbTime.currentText())
        # arr.append(self.slEng.value()) # engagement
        # arr.append(self.cbYou.currentText())
        # arr.append(self.slKnow.value()) # aware of their footprint
        # arr.append(self.slPrint.value()) # how would you rate
        # arr.append(self.chTry1.isChecked())
        # arr.append(self.chTry2.isChecked())
        # arr.append(self.chTry3.isChecked())
        # arr.append(self.chTry4.isChecked())
        # arr.append(self.chTry5.isChecked())
        # arr.append(self.cbOthers.currentText()) # would they encourage others

        a, b, c = process_from_form(arr)
        a = a[0][0]
        b = b[0][0]
        c = c[0][0]
        result = str(a) + str(b) + str(c)
        print(result)
        #result = "011"
        self.callNext()

    def callNext(self):
        global result
        if result == "011":
            self.switchWindow()
        elif result == "110":
            self.switchWindow()
        elif result == "101":
            self.switchWindow()
        elif result == "011":
            self.switchWindow()
        elif result == "111":
            self.switchWindow()
        else:
            self.skipWindow()


    def initialState(self):
        self.cbAge.addItem("18-22")
        self.cbAge.addItem("23-27")
        self.cbAge.setCurrentIndex(-1)
        self.cbEdu.addItem("In full-time education")
        self.cbEdu.addItem("In part-time education")
        self.cbEdu.setCurrentIndex(-1)
        self.cbWork.addItem("Full-time")
        self.cbWork.addItem("Part-time")
        self.cbWork.addItem("Not working at all")
        self.cbWork.setCurrentIndex(-1)
        self.cbTime.addItem("Less than 5 minutes")
        self.cbTime.addItem("Less than 15 minutes")
        self.cbTime.addItem("Less than 1 hour")
        self.cbTime.addItem("More than 1 hour")
        self.cbTime.addItem("I dont travel")
        self.cbTime.setCurrentIndex(-1)
        self.cbYou.addItem("Yes")
        self.cbYou.addItem("No")
        self.cbYou.setCurrentIndex(-1)
        self.cbOthers.addItem("Yes")
        self.cbOthers.addItem("No")
        self.cbOthers.setCurrentIndex(-1)

    def switchWindow(self):
        self.CalculatorWindow = CalculatorWindow()
        self.CalculatorWindow.show()
        self.hide()

    def skipWindow(self):
        self.TipsWindow = TipsWindow()
        self.TipsWindow.show()
        self.hide()



class CalculatorWindow(QtWidgets.QMainWindow, Ui_mainWindow2):

    def __init__(self, parent=None):
        super(CalculatorWindow, self).__init__(parent=parent)
        self.ui = Ui_mainWindow2()
        self.setupUi(self)
        #self.show()
        self.showMaximized()

        self.btnCalc.clicked.connect(lambda: self.carbonFootprint(self.leDrive.text(), self.lePlane.text(),
                                                                  self.leBeef.text(), self.leShop.text()))

        self.btnNext.clicked.connect(lambda: self.switchWindow2())

    def switchWindow2(self):
        self.TipsWindow = TipsWindow()
        self.TipsWindow.show()
        self.hide()


    def carbonFootprint(self, milesDrove, flightHours, beefConsumed, shoppingTrips):
        global MD
        global FH
        global BC
        global ST

        MD = float(milesDrove)
        FH = float(flightHours)
        BC = float(beefConsumed)
        ST = float(shoppingTrips)

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
        #self.show()
        self.showMaximized()

        self.doThings()

        self.btnDone.clicked.connect(lambda: self.close())

    def doThings(self):
        global BC
        self.lbTip2.setText("")
        if BC > 5.0:
            self.lbTip.setText("If you cut out one serving of beef per week you will reduce your CO2 contribution by "
                               "one ton over the next 10 years.")
        elif FH > 30.0:
            self.lbTip.setText("You spend a lot of hours in the air. Consider participating in a carbon offset "
                               "program that plants trees like www.carbonfund.org")
        elif MD > 200.0:
            self.lbTip.setText("A typical passenger vehicle emits about 4.6 metric tons of carbon dioxide per year, "
                               "but taking public transportation can help reduce your carbon footprint by 10%")
        elif ST > 2:
            self.lbTip.setText("50 tons of CO2 are produced every 2 minutes in the clothing manufacturing industry. "
                               "Consider thrifting instead of buying new!")
        else:
            self.lbTip.setText("The past decade was the hottest ever recorded on the planet, according to NASA."
                               " Visit www.climate.nasa.gov for more information!")
        if result == "111" or result == "110":
            self.lbTip2.setText("Turning your AC up or heat down by 2 degrees saves 200 pounds of CO2 each year.")




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MainWindow()
    myApp.show()
    sys.exit(app.exec_())


    # pyuic5 -x <.ui file> -o <output.py file>
