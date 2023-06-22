
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pymysql
import UserMenu
import User

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 283)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("")
        self.loginMenu=MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(130, 60, 173, 94))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setText("username:")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("password:")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.verifyPassword)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.mysqlConnect=pymysql.connect(host='112.126.86.88',
                                          user='root',
                                          password='root',
                                          database='demo',
                                          charset='utf8')



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATM System"))
        self.pushButton.setText(_translate("MainWindow", "Login"))

    def verifyPassword(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        print(f"username:{username} password:{password}")
        mysqlCursor=self.mysqlConnect.cursor()
        sql=f'select * from user where username="{username}" and password="{password}"'
        mysqlCursor.execute(sql)

        if mysqlCursor.fetchone() is not None:
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.loginMenu.setVisible(False)

            self.userMenu = QtWidgets.QMainWindow()
            self.userMenuUi = UserMenu.Ui_MainWindow()
            self.userMenuUi.setupUi(self.userMenu)

            #传参
            self.userMenuUi.user = None
            self.userMenuUi.mysqlConnect = self.mysqlConnect
            self.userMenuUi.loginMenu = self.loginMenu
            self.userMenuUi.user = User.User(username, password)
            self.userMenu.show()


        else:
            QtWidgets.QMessageBox.information(self.widget,
                                              'Error',
                                                "Error Password or username")





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()   # 创建窗体对象
    ui = Ui_MainWindow()   # 创建PyQt设计器的窗体对象
    ui.setupUi(MainWindow)    # 调用PyQt窗体的方法对象进行初始化设置
    MainWindow.show()    # 显示窗体

    sys.exit(app.exec_())   # 程序关闭时退出进程
