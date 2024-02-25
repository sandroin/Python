from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 361, 471))

        # Login Page
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.pushButton = QtWidgets.QPushButton(self.page_login)
        self.pushButton.setGeometry(QtCore.QRect(130, 350, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.page_login)
        self.label.setGeometry(QtCore.QRect(50, 160, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_login)
        self.label_2.setGeometry(QtCore.QRect(50, 240, 71, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit.setGeometry(QtCore.QRect(50, 190, 271, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 270, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_3 = QtWidgets.QLabel(self.page_login)
        self.label_3.setGeometry(QtCore.QRect(150, 80, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_login)


        # Redirected Page
        self.redirected_page = QtWidgets.QWidget()
        self.redirected_page.setObjectName("page_redirect")
        self.login_message = QtWidgets.QLabel(self.redirected_page)
        self.login_message.setGeometry(QtCore.QRect(127, 20, 300, 31))
        font.setPointSize(9)
        self.login_message.setFont(font)
        self.login_message.setObjectName("login_message")
        self.redirect_label = QtWidgets.QLabel(self.redirected_page)
        self.redirect_label.setGeometry(QtCore.QRect(60, 70, 300, 31))
        self.redirect_label.setObjectName("label_redirect")
        font.setPointSize(10)
        self.redirect_label.setFont(font)
        self.stackedWidget.addWidget(self.redirected_page)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 384, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.login)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.login_message.setText(_translate("MainWindow", "Successful Login!"))
        self.redirect_label.setText(_translate("MainWindow", "This Is Redirected Page Simulation"))

    def login(self):
        username = "Sandro"
        password = "sandro123"

        if username == self.lineEdit.text() and password == self.lineEdit_2.text():
            # QMessageBox.information(None, "Valid Login", "You logged in successfully!")
            self.stackedWidget.setCurrentIndex(1)
        else:
            QMessageBox.warning(None, "Invalid Login", "Login failed! Please try again!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
