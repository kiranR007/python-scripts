class Acount:
    __amount = 0
    def deposite(self,add):
        self.__amount += add

    def debit(self,sub):
        self.__amount -= sub

    def PrintAmount(self):
        print("amount is ",self.__amount)

b1 = Acount()
b1.deposite(1000)
b1.deposite(2000)
b1.deposite(3000)
b1.debit(1000)
b1.PrintAmount()
