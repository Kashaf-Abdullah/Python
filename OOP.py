#CREATING PHONE CLASS
class Phone:
    def make_calls(self):
        print("Making phone calls")
    def playGrames(self):
        print("playing games") 

#INSTANTIATING THE p1 OBJECT
p1=Phone()    

#INVOKING METHODS THROUGH OBJECT
p1.make_calls()
p1.playGrames()






#ADDING PARAMETRS TO THE CLASS
class Phone:
    def set_color(self,color):
        self.color=color;


    def set_cost(self,cost):
        self.cost=cost;

    def show_color(self):
        return self.color;    


    def show_cost(self):
        return self.cost;    
           
    def make_calls(self):
        print("making phone caalls")       

    def play_games(self):
        print("playing games")    

p1=Phone()    

p1.set_color('blue')
p1.set_cost(4000)
print(p1.show_color())
print(p1.show_cost())
p1.play_games()
p1.make_calls()



#CREATING A CLASS WITH CONSTRUCTOR
class Employee:
    def _init_(self,name,age,salary,gender):   #int method acts as the constructor
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
        

        def employee_details(self):
            print("Name of employee is",self.name)
            print("Age of employee is",self.age)
            print("Salary of employee is",self.salary)
            print("gender of emplyee is ",self.gender)

            e1=Employee('Julie',23,4555,'Female')
            e1.show_details()