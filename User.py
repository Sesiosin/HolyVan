import UserMenu


class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def setDeposit(self,deposit):
        self.deposit=deposit
