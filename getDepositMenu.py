from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.user=None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(295, 193)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 40, 173, 86))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 295, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.getDeposit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "取款"))
        self.label.setText(_translate("MainWindow", "输入取款数额"))
        self.pushButton.setText(_translate("MainWindow", "取款"))

    def getDeposit(self):
        num=self.lineEdit.text()
        num=int(num,base=10)

        if num%100!=0 or num>5000 or num<=0:
            self.label_2.setText("取款金额不正确")
            self.label_2.setStyleSheet("color:rgb(255,0,0)")


        else:
            cursor = self.mysqlConnect.cursor()
            sql = f'select deposit from user where username="{self.user.username}"'
            cursor.execute(sql)
            deposit=cursor.fetchone()[0]

            if num>deposit:
                self.label_2.setText("余额不足")
                self.label_2.setStyleSheet("color:rgb(255,0,0)")
            else:
                deposit=deposit-num
                sql=f'update user set deposit={deposit} where username="{self.user.username}"'
                cursor.execute(sql)
                sql=f'select * from user where username="{self.user.username}"'
                cursor.execute(sql)
                test=cursor.fetchone()
                print(test)
                self.mysqlConnect.commit()
                self.label_2.setText("取款成功")
                self.label_2.setStyleSheet("color:rgb(0,0,0)")

