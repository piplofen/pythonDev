import utils as u
import logging as log
import sys

from PyQt6 import QtWidgets
from design import logInDesign

u.logStart("log/log.log")


class MainWindow(QtWidgets.QMainWindow, logInDesign.Ui_LogUpWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
