# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculate2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import math

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    x1, x2, x3, y1, y2, y3 = "x1", "x2", "x3", "y1", "y2", "y3"
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 30, 721, 91))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 50, 611, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(70, 120, 151, 41))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(70, 160, 151, 41))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(70, 240, 151, 41))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_5.setGeometry(QtCore.QRect(70, 280, 151, 41))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_6 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(70, 320, 151, 41))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_8 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_8.setGeometry(QtCore.QRect(70, 360, 151, 41))
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(0)
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_9 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_9.setGeometry(QtCore.QRect(70, 400, 151, 41))
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.setColumnCount(0)
        self.tableWidget_9.setRowCount(0)
        self.tableWidget_10 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_10.setGeometry(QtCore.QRect(220, 120, 191, 41))
        self.tableWidget_10.setObjectName("tableWidget_10")
        self.tableWidget_10.setColumnCount(0)
        self.tableWidget_10.setRowCount(0)
        self.tableWidget_11 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_11.setGeometry(QtCore.QRect(410, 120, 191, 41))
        self.tableWidget_11.setObjectName("tableWidget_11")
        self.tableWidget_11.setColumnCount(0)
        self.tableWidget_11.setRowCount(0)
        self.tableWidget_12 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_12.setGeometry(QtCore.QRect(600, 120, 191, 41))
        self.tableWidget_12.setObjectName("tableWidget_12")
        self.tableWidget_12.setColumnCount(0)
        self.tableWidget_12.setRowCount(0)
        self.tableWidget_13 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_13.setGeometry(QtCore.QRect(410, 160, 191, 41))
        self.tableWidget_13.setObjectName("tableWidget_13")
        self.tableWidget_13.setColumnCount(0)
        self.tableWidget_13.setRowCount(0)
        self.tableWidget_31 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_31.setGeometry(QtCore.QRect(220, 360, 191, 41))
        self.tableWidget_31.setObjectName("tableWidget_31")
        self.tableWidget_31.setColumnCount(0)
        self.tableWidget_31.setRowCount(0)
        self.tableWidget_33 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_33.setGeometry(QtCore.QRect(410, 360, 191, 41))
        self.tableWidget_33.setObjectName("tableWidget_33")
        self.tableWidget_33.setColumnCount(0)
        self.tableWidget_33.setRowCount(0)
        self.tableWidget_34 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_34.setGeometry(QtCore.QRect(220, 400, 191, 41))
        self.tableWidget_34.setObjectName("tableWidget_34")
        self.tableWidget_34.setColumnCount(0)
        self.tableWidget_34.setRowCount(0)
        self.tableWidget_35 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_35.setGeometry(QtCore.QRect(410, 400, 191, 41))
        self.tableWidget_35.setObjectName("tableWidget_35")
        self.tableWidget_35.setColumnCount(0)
        self.tableWidget_35.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 360, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.calculate())
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 400, 191, 41))
        self.pushButton_2.clicked.connect(lambda: self.delets())
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 520, 55, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 120, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(680, 120, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 240, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 280, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(110, 320, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_7.setGeometry(QtCore.QRect(70, 200, 151, 41))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_29 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_29.setGeometry(QtCore.QRect(220, 200, 191, 41))
        self.tableWidget_29.setObjectName("tableWidget_29")
        self.tableWidget_29.setColumnCount(0)
        self.tableWidget_29.setRowCount(0)
        self.tableWidget_30 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_30.setGeometry(QtCore.QRect(410, 200, 191, 41))
        self.tableWidget_30.setObjectName("tableWidget_30")
        self.tableWidget_30.setColumnCount(0)
        self.tableWidget_30.setRowCount(0)
        self.tableWidget_32 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_32.setGeometry(QtCore.QRect(600, 200, 191, 41))
        self.tableWidget_32.setObjectName("tableWidget_32")
        self.tableWidget_32.setColumnCount(0)
        self.tableWidget_32.setRowCount(0)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(250, 190, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(640, 190, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(430, 190, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 160, 61, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 160, 61, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 160, 71, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(600, 160, 61, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(660, 160, 61, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(720, 160, 71, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(220, 240, 191, 41))
        self.lineEdit_7.setStyleSheet("background-color: rgb(217, 255, 210);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(410, 240, 191, 41))
        self.lineEdit_8.setStyleSheet("background-color: rgb(217, 255, 210);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(600, 240, 191, 41))
        self.lineEdit_9.setStyleSheet("background-color: rgb(217, 255, 210);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(220, 280, 191, 41))
        self.lineEdit_10.setStyleSheet("background-color: rgb(217, 255, 210);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(410, 280, 191, 41))
        self.lineEdit_11.setStyleSheet("background-color: rgb(217, 255, 210);")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(600, 280, 191, 41))
        self.lineEdit_12.setStyleSheet("background-color: rgb(217, 255, 210);")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(220, 320, 191, 41))
        self.lineEdit_13.setStyleSheet("background-color: rgb(217, 255, 210);")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(410, 320, 191, 41))
        self.lineEdit_14.setStyleSheet("background-color: rgb(217, 255, 210);")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(600, 320, 191, 41))
        self.lineEdit_15.setStyleSheet("background-color: rgb(217, 255, 210);")
        self.lineEdit_15.setObjectName("lineEdit_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 853, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def calculate(self):
        x1 = self.lineEdit.text()
        x2 = self.lineEdit_2.text()
        x3 = self.lineEdit_3.text()
        y1 = self.lineEdit_4.text()
        y2 = self.lineEdit_5.text()
        y3 = self.lineEdit_6.text()
        if len(x1) == 0 or x1 == "x1":
            return
        if len(x2) == 0 or x2 == "x2":
            return
        if len(x3) == 0 or x3 == "x3":
            return
        if len(y1) == 0 or y1 == "y1":
            return
        if len(y2) == 0 or y2 == "y2":
            return
        if len(y3) == 0 or y2 == "y3":
            return
        a1 = int(x1)
        a2 = int(x2)
        a3 = int(x3)
        b1 = int(y1)
        b2 = int(y2)
        b3 = int(y3)
        number = math.sqrt(((a1 - b1) ** 2) + ((a2 - b2) ** 2) + ((a3 - b3) ** 2))
        number1 = abs(a1 - b1) + abs(a2 - b2) + abs(a3 - b3)
        c1 = abs(a1 - b1)
        c2 = abs(a2 - b2)
        c3 = abs(a3 - b3)
        l = [c1, c2, c3]
        number2 = max(l)
        number3 = math.sqrt((a1**2)+(a2**2)+(a3**2))
        number4 = abs(a1)+abs(a2)+abs(a3)
        r1, r2, r3 = abs(a1),abs(a2), abs(a3)
        p= [r1, r2, r3]
        number5 = max(p)
        number6 = math.sqrt((b1 ** 2) + (b2 ** 2) + (b3 ** 2))
        number7 = abs(b1) + abs(b2) + abs(b3)
        r11, r12, r13 = abs(b1), abs(b2), abs(b3)
        p1 = [r11, r12, r13]
        number8 = max(p1)
        self.lineEdit_7.setText(str(number3))
        self.lineEdit_8.setText(str(number))
        self.lineEdit_9.setText(str(number6))
        self.lineEdit_10.setText(str(number4))
        self.lineEdit_11.setText(str(number1))
        self.lineEdit_12.setText(str(number7))
        self.lineEdit_13.setText(str(number5))
        self.lineEdit_14.setText(str(number2))
        self.lineEdit_15.setText(str(number8))

    def delets(self):
        s = ""
        s1="x1"
        s2 = "x2"
        s3 = "x3"
        s4 = "y1"
        s5 = "y2"
        s6 = "y3"
        self.lineEdit.setText(s1)
        self.lineEdit_2.setText(s2)
        self.lineEdit_3.setText(s3)
        self.lineEdit_4.setText(s4)
        self.lineEdit_5.setText(s5)
        self.lineEdit_6.setText(s6)
        self.lineEdit_7.setText(s)
        self.lineEdit_8.setText(s)
        self.lineEdit_9.setText(s)
        self.lineEdit_10.setText(s)
        self.lineEdit_11.setText(s)
        self.lineEdit_12.setText(s)
        self.lineEdit_13.setText(s)
        self.lineEdit_14.setText(s)
        self.lineEdit_15.setText(s)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Калькулятор норм та метрик розробила Дворова Олександра"))
        self.pushButton.setText(_translate("MainWindow", "Обрахувати"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистити"))
        self.label_3.setText(_translate("MainWindow", "V1"))
        self.label_4.setText(_translate("MainWindow", "V2"))
        self.label_5.setText(_translate("MainWindow", "тип"))
        self.label_6.setText(_translate("MainWindow", "Evklid"))
        self.label_7.setText(_translate("MainWindow", "City"))
        self.label_9.setText(_translate("MainWindow", "Cheb"))
        self.label_19.setText(_translate("MainWindow", "розмір V1"))
        self.label_20.setText(_translate("MainWindow", "розмір V2"))
        self.label_21.setText(_translate("MainWindow", "відстань V2- V1"))
        self.lineEdit.setText(_translate("MainWindow", "x1"))
        self.lineEdit_2.setText(_translate("MainWindow", "x2"))
        self.lineEdit_3.setText(_translate("MainWindow", "x3"))
        self.lineEdit_4.setText(_translate("MainWindow", "y1"))
        self.lineEdit_5.setText(_translate("MainWindow", "y2"))
        self.lineEdit_6.setText(_translate("MainWindow", "y3"))
        self.menu.setTitle(_translate("MainWindow", "Калькулятор для норм та метрик"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
