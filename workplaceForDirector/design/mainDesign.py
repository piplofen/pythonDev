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
        self.bttnCustomers = QtWidgets.QPushButton(parent=self.frame)
        self.bttnCustomers.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/customers.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnCustomers.setIcon(icon)
        self.bttnCustomers.setIconSize(QtCore.QSize(24, 24))
        self.bttnCustomers.setObjectName("bttnCustomers")
        self.verticalLayout.addWidget(self.bttnCustomers)
        self.bttnStorage = QtWidgets.QPushButton(parent=self.frame)
        self.bttnStorage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/storage.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnStorage.setIcon(icon1)
        self.bttnStorage.setIconSize(QtCore.QSize(24, 24))
        self.bttnStorage.setObjectName("bttnStorage")
        self.verticalLayout.addWidget(self.bttnStorage)
        self.bttnStatic = QtWidgets.QPushButton(parent=self.frame)
        self.bttnStatic.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/statistic.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnStatic.setIcon(icon2)
        self.bttnStatic.setIconSize(QtCore.QSize(24, 24))
        self.bttnStatic.setObjectName("bttnStatic")
        self.verticalLayout.addWidget(self.bttnStatic)
        self.bttnJil = QtWidgets.QPushButton(parent=self.frame)
        self.bttnJil.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/jil.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnJil.setIcon(icon3)
        self.bttnJil.setIconSize(QtCore.QSize(24, 24))
        self.bttnJil.setObjectName("bttnJil")
        self.verticalLayout.addWidget(self.bttnJil)
        self.bttnObj = QtWidgets.QPushButton(parent=self.frame)
        self.bttnObj.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/obj.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnObj.setIcon(icon4)
        self.bttnObj.setIconSize(QtCore.QSize(24, 24))
        self.bttnObj.setObjectName("bttnObj")
        self.verticalLayout.addWidget(self.bttnObj)
        self.bttnSyroi = QtWidgets.QPushButton(parent=self.frame)
        self.bttnSyroi.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icons/syroi.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnSyroi.setIcon(icon5)
        self.bttnSyroi.setIconSize(QtCore.QSize(24, 24))
        self.bttnSyroi.setObjectName("bttnSyroi")
        self.verticalLayout.addWidget(self.bttnSyroi)
        self.bttnDebtors = QtWidgets.QPushButton(parent=self.frame)
        self.bttnDebtors.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../icons/debtors.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnDebtors.setIcon(icon6)
        self.bttnDebtors.setIconSize(QtCore.QSize(24, 24))
        self.bttnDebtors.setObjectName("bttnDebtors")
        self.verticalLayout.addWidget(self.bttnDebtors)
        self.bttnRequests = QtWidgets.QPushButton(parent=self.frame)
        self.bttnRequests.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../icons/requests.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnRequests.setIcon(icon7)
        self.bttnRequests.setIconSize(QtCore.QSize(24, 24))
        self.bttnRequests.setObjectName("bttnRequests")
        self.verticalLayout.addWidget(self.bttnRequests)
        self.bttnClient = QtWidgets.QPushButton(parent=self.frame)
        self.bttnClient.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../icons/client.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnClient.setIcon(icon8)
        self.bttnClient.setIconSize(QtCore.QSize(24, 24))
        self.bttnClient.setObjectName("bttnClient")
        self.verticalLayout.addWidget(self.bttnClient)
        self.bttnSearch = QtWidgets.QPushButton(parent=self.frame)
        self.bttnSearch.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../icons/search.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnSearch.setIcon(icon9)
        self.bttnSearch.setIconSize(QtCore.QSize(24, 24))
        self.bttnSearch.setObjectName("bttnSearch")
        self.verticalLayout.addWidget(self.bttnSearch)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.bttnExit = QtWidgets.QPushButton(parent=self.frame)
        self.bttnExit.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../icons/exit.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnExit.setIcon(icon10)
        self.bttnExit.setIconSize(QtCore.QSize(24, 24))
        self.bttnExit.setObjectName("bttnExit")
        self.verticalLayout.addWidget(self.bttnExit)
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
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.bttnDel = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Droid Serif")
        font.setPointSize(14)
        font.setItalic(False)
        self.bttnDel.setFont(font)
        self.bttnDel.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../icons/del.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnDel.setIcon(icon11)
        self.bttnDel.setIconSize(QtCore.QSize(24, 24))
        self.bttnDel.setObjectName("bttnDel")
        self.horizontalLayout_3.addWidget(self.bttnDel)
        self.bttnChange = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Droid Serif")
        font.setPointSize(14)
        font.setItalic(False)
        self.bttnChange.setFont(font)
        self.bttnChange.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../icons/change.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnChange.setIcon(icon12)
        self.bttnChange.setIconSize(QtCore.QSize(24, 24))
        self.bttnChange.setObjectName("bttnChange")
        self.horizontalLayout_3.addWidget(self.bttnChange)
        self.bttnAdd = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Droid Serif")
        font.setPointSize(14)
        font.setItalic(False)
        self.bttnAdd.setFont(font)
        self.bttnAdd.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../icons/add.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnAdd.setIcon(icon13)
        self.bttnAdd.setIconSize(QtCore.QSize(24, 24))
        self.bttnAdd.setObjectName("bttnAdd")
        self.horizontalLayout_3.addWidget(self.bttnAdd)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное окно"))
        self.label_3.setText(_translate("MainWindow", "Жильцы дома "))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
