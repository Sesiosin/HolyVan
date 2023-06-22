from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(379, 260)
        self.changePassWindow=MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(110, 30, 175, 156))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 379, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.change)
        self.user=None

        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "修改密码"))
        self.label.setText(_translate("MainWindow", "原密码"))
        self.label_2.setText(_translate("MainWindow", "新密码"))
        self.label_3.setText(_translate("MainWindow", "确认新密码"))
        self.pushButton.setText(_translate("MainWindow", "修改"))

    def change(self):
        rawPass=self.lineEdit.text()
        newPass=self.lineEdit_2.text()
        newPass2=self.lineEdit_3.text() # 重复输入的新密码
        newPasslen=len(newPass)

        if newPasslen < 6:
            self.label_4.setText("新密码长度至少为6位")
            self.label_4.setStyleSheet("color:rgb(255,0,0)")

        else:
            totalEqual=True
            for i in range(0,newPasslen-1):
                if newPass[i] != newPass[i+1]:
                    totalEqual=False
                    break

            if totalEqual is True:
                self.label_4.setText("新密码各位不能完全相同")
                self.label_4.setStyleSheet("color:rgb(255,0,0)")

            else:
                if newPass != newPass2:
                    self.label_4.setText("新密码与重复新密码不相同")
                    self.label_4.setStyleSheet("color:rgb(255,0,0)")

                else:
                    if rawPass != self.user.password:
                        self.label_4.setText("原密码错误")
                        self.label_4.setStyleSheet("color:rgb(255,0,0)")

                    else:
                        cursor = self.mysqlConnect.cursor()
                        sql = f'update user set password="{newPass}" where username="{self.user.username}"'
                        cursor.execute(sql)
                        sql = f'select * from user where username="{self.user.username}"'
                        cursor.execute(sql)
                        test = cursor.fetchone()
                        print(test)
                        self.mysqlConnect.commit()
                        self.label_4.setText("密码修改成功")
                        self.label_4.setStyleSheet("color:rgb(0,0,0)")

                        self.userWindow.close()
                        self.loginMenu.setVisible(True)
                        self.changePassWindow.close()
