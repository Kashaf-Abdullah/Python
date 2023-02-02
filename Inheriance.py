class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage;      
        self.cost=cost

    def show_details(self):
        print("I am a vehicle")
        print("Mileage of vehicle is ",self.mileage)
        print("Cost of vehicle is ",self.cost)

v=Vehicle(77,888)
v.show_details()


class Car(Vehicle):
    def _show_car_details(self):
       print("i am car")


       c1=Car()
       c1.show_details()
       c1._show_car_details()


