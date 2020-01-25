# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarbonFootprint.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow2(object):
    def setupUi(self, mainWindow2):
        mainWindow2.setObjectName("mainWindow2")
        mainWindow2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        mainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        mainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow2)
        self.statusbar.setObjectName("statusbar")
        mainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow2)
        QtCore.QMetaObject.connectSlotsByName(mainWindow2)

    def retranslateUi(self, mainWindow2):
        _translate = QtCore.QCoreApplication.translate
        mainWindow2.setWindowTitle(_translate("mainWindow2", "Carbon Footprint Calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_mainWindow2()
    ui.setupUi(mainWindow2)
    mainWindow2.show()
    sys.exit(app.exec_())
