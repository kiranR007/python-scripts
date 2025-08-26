class Mobile:
    def __init__(self,brand,color,isjack):
        self.brand = brand
        self.color = color
        self.isJack = isjack

    def isCalling(self):
        print("phone ringing")

    def show_details(self):
        print("brand name {}".format(self.brand))
        print("color is {}".format(self.color))
        print("is Jack {}".format(self.isJack))

def main():
    obj = Mobile("redmi","black",True)
    # obj.brand = "smasung"
    # obj.color = "red"
    obj.show_details()
    obj.isCalling()

if __name__=='__main__':
    main()
