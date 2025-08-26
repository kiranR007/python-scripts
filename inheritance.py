class Car:
    def __init__(self,gear,seat,maxspeed):
        self.gear = gear
        self.seat = seat
        self.maxspeed = maxspeed
    
    def speed(self):
        print("speed is increasing")

    def apply_break(self):
        print("break is increasing")

class Harrier(Car):
    def __init__(self,milage,gear,seat,maxspeed):
        super().__init__(gear,seat,maxspeed)
        self.milage = milage
        
    def race_mode(self):
        print("race mode on")

class Verna(Car):
    pass


def main():
    C1 = Car(1,4,180)
    H1 = Harrier(2,8,190)
    V1 = Verna(1,5,160)

    print(H1.apply_break())
    print(H1.speed())
    print(H1.race_mode())

    print(H1.gear)
    print(H1.seat)
    print(H1.maxspeed)


if __name__=='__main__':
    main()
