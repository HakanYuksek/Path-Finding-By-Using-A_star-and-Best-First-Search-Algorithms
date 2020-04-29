from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog,QApplication,QMessageBox

import sys

import a_star_heap_yok as a_heap_yok
import a_star_heap_var as a_heap_var
import best_first_search as bfs
import best_first_search_with_heap as bfs_heap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(402, 400))
        MainWindow.setMaximumSize(QtCore.QSize(402, 400))
        MainWindow.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 281, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 281, 22))
        self.comboBox.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 160, 281, 30))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 200, 371, 15))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 220, 113, 19))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 260, 113, 19))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 300, 113, 19))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 340, 301, 30))
        self.pushButton_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 251, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 251, 20))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 251, 20))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 110, 361, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.pushButton.clicked.connect(self.openFile)
        self.pushButton_2.clicked.connect(self.exit)
        self.pushButton_3.clicked.connect(self.run)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resimlerde A star ve İlk En İyi Arama Algoritmaları"))
        self.pushButton.setText(_translate("MainWindow", "Dosyayı Aç"))
        self.comboBox.setItemText(0, _translate("MainWindow", "A Star ( Heap Var )"))
        self.comboBox.setItemText(1, _translate("MainWindow", "A Star ( Heap Yok )"))
        self.comboBox.setItemText(2, _translate("MainWindow", "İlk En İyi Arama ( Heap  Var )"))
        self.comboBox.setItemText(3, _translate("MainWindow", "İlk En İyi Arama ( Heap Yok )"))
        self.label.setText(_translate("MainWindow", "Sonuçlar---->"))
        self.pushButton_2.setText(_translate("MainWindow", "Çıkış"))
        self.label_2.setText(_translate("MainWindow", "Yığından Çekilen Eleman Sayısı"))
        self.label_3.setText(_translate("MainWindow", "Yığında Maksimum Eleman Sayısı"))
        self.label_4.setText(_translate("MainWindow", "Çalışma Zamanı (sn)"))
        self.pushButton_3.setText(_translate("MainWindow", "Çalıştır"))

    def openFile(self):
        fileName=QFileDialog.getOpenFileName(caption='Open file',filter="Image files (*.png *.jpeg *.jpg)")
        self.lineEdit.setText(fileName[0])

    def exit(self):
        sys.exit()

    def run(self):
        algorithmName = self.comboBox.currentText()
        picture = self.lineEdit.text()
        
        if algorithmName == "A Star ( Heap Var )":
            res = a_heap_var.run(picture)
            self.lineEdit_2.setText(str(res["total_stack"]))
            self.lineEdit_3.setText(str(res["Max_stack"]))
            time = str(res["time"])
            time = time[:12]
            self.lineEdit_4.setText(time)
            
        elif algorithmName == "A Star ( Heap Yok )":
            res = a_heap_yok.run(picture)
            self.lineEdit_2.setText(str(res["total_stack"]))
            self.lineEdit_3.setText(str(res["Max_stack"]))
            time = str(res["time"])
            time = time[:12]
            self.lineEdit_4.setText(time)
            
        elif algorithmName == "İlk En İyi Arama ( Heap  Var )":
            res = bfs_heap.run(picture)
            self.lineEdit_2.setText(str(res["total_stack"]))
            self.lineEdit_3.setText(str(res["Max_stack"]))
            time = str(res["time"])
            time = time[:12]
            self.lineEdit_4.setText(time)
            
        elif algorithmName == "İlk En İyi Arama ( Heap Yok )":
            res = bfs.run(picture)
            self.lineEdit_2.setText(str(res["total_stack"]))
            self.lineEdit_3.setText(str(res["Max_stack"]))
            time = str(res["time"])
            time = time[:12]
            self.lineEdit_4.setText(time)            
            
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
