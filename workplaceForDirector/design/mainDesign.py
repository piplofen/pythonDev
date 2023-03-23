# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(934, 610)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(50, 350))
        self.frame.setMaximumSize(QtCore.QSize(50, 10000000))
        self.frame.setStyleSheet("QFrame{\n"
"background: #FFA573;\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"border-radius: 10px;\n"
"margin-left: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(85, 170, 127, 105);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/customers.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/storage.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/statistic.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/jil.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/obj.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icons/syroi.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_8.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../icons/debtors.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_7.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../icons/requests.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_9.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../icons/client.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_10.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../icons/search.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_10.setIcon(icon9)
        self.pushButton_10.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.frame)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(500, 350))
        self.stackedWidget.setStyleSheet("QStackedWidget{\n"
"background-color: rgb(85, 170, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgba(255, 170, 255, 150);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: transparent;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(85, 170, 127, 155);\n"
"border-radius: 10px;\n"
"margin: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(85, 170, 127, 205);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Droid Serif")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.page)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.bttnLog = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Droid Serif")
        font.setPointSize(14)
        font.setItalic(False)
        self.bttnLog.setFont(font)
        self.bttnLog.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../icons/del.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnLog.setIcon(icon10)
        self.bttnLog.setIconSize(QtCore.QSize(24, 24))
        self.bttnLog.setObjectName("bttnLog")
        self.horizontalLayout_3.addWidget(self.bttnLog)
        self.bttnLog_2 = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Droid Serif")
        font.setPointSize(14)
        font.setItalic(False)
        self.bttnLog_2.setFont(font)
        self.bttnLog_2.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../icons/change.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnLog_2.setIcon(icon11)
        self.bttnLog_2.setIconSize(QtCore.QSize(24, 24))
        self.bttnLog_2.setObjectName("bttnLog_2")
        self.horizontalLayout_3.addWidget(self.bttnLog_2)
        self.bttnLog_3 = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Droid Serif")
        font.setPointSize(14)
        font.setItalic(False)
        self.bttnLog_3.setFont(font)
        self.bttnLog_3.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../icons/add.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnLog_3.setIcon(icon12)
        self.bttnLog_3.setIconSize(QtCore.QSize(24, 24))
        self.bttnLog_3.setObjectName("bttnLog_3")
        self.horizontalLayout_3.addWidget(self.bttnLog_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Жильцы дома "))
