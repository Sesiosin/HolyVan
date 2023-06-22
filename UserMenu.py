

from PyQt5 import QtCore, QtGui, QtWidgets
import User
import pymysql

import getDepositMenu
import setDepositMenu
import changePassword

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 315)
        self.userWindow=MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 30, 226, 203))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(2, 2, 2, -1)
        self.gridLayout.setSpacing(60)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.user=User.User("123456","123456")
        self.retranslateUi(MainWindow)
        self.pushButton_5.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mysqlConnect=None
        self.pushButton.clicked.connect(self.queryDeposit)
        self.pushButton_2.clicked.connect(self.getDeposit)

        self.getDepositUi=getDepositMenu.Ui_MainWindow()
        self.getDepositMenu=QtWidgets.QMainWindow()
        self.getDepositUi.setupUi(self.getDepositMenu)

        self.setDepositUi = setDepositMenu.Ui_MainWindow()
        self.setDepositMenu = QtWidgets.QMainWindow()
        self.setDepositUi.setupUi(self.setDepositMenu)

        self.pushButton_3.clicked.connect(self.setDeposit)
        self.pushButton_4.clicked.connect(self.changePassword)

        self.changePassUi = changePassword.Ui_MainWindow()
        self.changePassMenu = QtWidgets.QMainWindow()
        self.changePassUi.setupUi(self.changePassMenu)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户界面"))
        self.pushButton.setText("查询余额")
        self.pushButton_3.setText(_translate("MainWindow", "存款"))
        self.pushButton_4.setText(_translate("MainWindow", "修改密码"))
        self.pushButton_5.setText(_translate("MainWindow", "退出"))
        self.pushButton_2.setText(_translate("MainWindow", "取款"))

    def queryDeposit(self):
        cursor=self.mysqlConnect.cursor()
        # sql='select deposit from user where username="{self.user.username}" and password="{self.user.password}"'
        sql=f'select deposit from user where username="{self.user.username}"'
        cursor.execute(sql)
        deposit=cursor.fetchone()

        if deposit is not None:
            QtWidgets.QMessageBox.information(self.widget,
                                              "余额查询",
                                              f"当前余额{deposit[0]}元")

        else:
            QtWidgets.QMessageBox.warning(self.widget,
                                          "error",
                                          "No deposit")

    def getDeposit(self):
        self.getDepositUi.user=self.user
        self.getDepositUi.mysqlConnect=self.mysqlConnect
        self.getDepositMenu.show()


    def setDeposit(self):
        self.setDepositUi.user=self.user
        self.setDepositUi.mysqlConnect=self.mysqlConnect
        self.setDepositMenu.show()

    def changePassword(self):
        self.changePassUi.user = self.user
        self.changePassUi.mysqlConnect = self.mysqlConnect
        self.changePassMenu.show()
        self.changePassUi.loginMenu=self.loginMenu
        self.changePassUi.userWindow=self.userWindow


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_MainWindow()  # 创建PyQt设计器的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程