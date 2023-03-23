import sqlite3

import utils as u
import logging as log
import sys

from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox
from design import logInDesign
from design import regDesign
from design import mainDesign
from database import database

u.logStart("../../log/log.log")


class MainWindow(QtWidgets.QMainWindow, mainDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icons/main.ico"))
        self.bttnCustomers.setIcon(QIcon("icons/customers.ico"))
        self.bttnStorage.setIcon(QIcon("icons/storage.ico"))
        self.bttnStatic.setIcon(QIcon("icons/statistic.ico"))
        self.bttnJil.setIcon(QIcon("icons/jil.ico"))
        self.bttnObj.setIcon(QIcon("icons/obj.ico"))
        self.bttnSyroi.setIcon(QIcon("icons/syroi.ico"))
        self.bttnDebtors.setIcon(QIcon("icons/debtors.ico"))
        self.bttnRequests.setIcon(QIcon("icons/requests.ico"))
        self.bttnClient.setIcon(QIcon("icons/client.ico"))
        self.bttnSearch.setIcon(QIcon("icons/search.ico"))
        self.bttnDel.setIcon(QIcon("icons/del.ico"))
        self.bttnAdd.setIcon(QIcon("icons/add.ico"))
        self.bttnChange.setIcon(QIcon("icons/change.ico"))


class LogInWindow(QtWidgets.QMainWindow, logInDesign.Ui_LogInWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icons/log-in.ico"))
        self.bttnExit.clicked.connect(self.close)
        self.bttnLog.clicked.connect(self.openMainWindow)

    def openMainWindow(self):
        self.close()
        mainWindow.show()


class RegWindow(QtWidgets.QMainWindow, regDesign.Ui_RegWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icons/users.ico"))
        self.bttnReg.clicked.connect(self.reg)

    def reg(self):
        """Replace this func for insertData in database class."""
        try:
            db.cur.execute(f"insert into user(login, password) "
                           f"values('{self.LineEditLogin.text()}','{self.LineEditPassword.text()}')")
            db.conn.commit()
            self.messageBox(self.LineEditLogin.text())
            self.close()
            log.info("Successful registration")
        except sqlite3.Error as e:
            print(e)
            log.error(e)

    def messageBox(self, user):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(f"{user}, вы успешно зарегистрировались в АРМ!")
        msg.setWindowTitle("Успешная регистрация")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        retval = msg.exec()


def checkUser():
    """Replace this func for somthing in database class."""
    global db
    db = database.Database()
    try:
        db.cur.execute("SELECT * FROM 'user'")
        if db.cur.fetchone():
            log.info("User exists")
            return True
        else:
            return False
    except sqlite3.Error as e:
        log.error(e)
        return False


def main():
    global mainWindow
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    if checkUser():
        logWindow = LogInWindow()
        logWindow.show()
        app.exec()
    else:
        regWindow = RegWindow()
        regWindow.show()
        app.exec()


if __name__ == '__main__':
    main()
