class Car:
    def __init__(self,seat,gear,maxspeed):
        self.seat = seat
        self.gear = gear
        self.maxspeed = maxspeed

    def speed(self):
        print("speed is increasing")

    def apply_break(self):
        print("break is increasing")

class Hyndai:
    def __init__(self,milage):
        self.milage = milage

    def speed(self):
        print("speed is increasing")

class Harrier(Car):
    def __init__(self):
        pass

class Verna(Car,Hyndai):
    def __init__(self, seat, gear, maxspeed,milage):
        Car.__init__(self,seat, gear, maxspeed)
        Hyndai.__init__(self,milage)

def main():
    Obj = Verna(4,5,6,7)
    Obj.speed()
    Obj.apply_break()
    print(Obj.seat)
    print(Obj.gear)
    print(Obj.maxspeed)
    print(Obj.milage)

if __name__=='__main__':
    main()