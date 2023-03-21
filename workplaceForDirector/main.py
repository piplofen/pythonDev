import utils as u
import logging as log
import sys

from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from design import logInDesign
from design import regDesign

u.logStart("log/log.log")


class LogInWindow(QtWidgets.QMainWindow, logInDesign.Ui_LogInWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icons/log-in.ico"))
        self.bttnExit.clicked.connect(self.close)


class RegWindow(QtWidgets.QMainWindow, regDesign.Ui_RegWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icons/users.ico"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    logWindow = LogInWindow()
    regWindow = RegWindow()
    logWindow.show()
    app.exec()


if __name__ == '__main__':
    main()
