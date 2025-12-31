#!/usr/bin/python3.10

class Plant:  #this is a class, just a template. nothing in memory yet!
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):	#this is now a method. to modify the attributes of class
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant): #child class (takes another class as argument)
    def __init__(self, name, height, color):     #child class own init
        super().__init__(name, height) #using super to inhirent parent init!
        self.color = color   #unique tributes to child class		|| configuration passed as argument
        self.blooming = False #another unite tribues to child class	|| state isnt passed as arguments

    def bloom(self): #method to modify tributes of child class
        self.blooming = True     #the tribues becomes now this!



class PrizeFlower(FloweringPlant): #another child class: c.c -> c -> p
    def __init__(self, name, height, color, prize_points): 
        super().__init__(name, height, color) #borrow name, height, color from c class: class in return will provide color, but will borrow name, height from p
        self.prize_points = prize_points








rose = Plant("rose", 20)
rose.grow()

print(f"{rose.name}, {rose.heigth}cm")


# super().__init__(self, name, heigth) -> super doesnt need self here, why?


#class FlowringPlant(Plant): #child class (takes another class as argument)
#      def __init__(self, name, height, color, booming):
#          super().__init__(name, heigth) #using super to inhirent parent init!
#          self.color = color   #unique tributes to child class
#          self.booming = False #another unite tribues to child class

# --> here! i passed booming to init, to intiliaze it! 
# state vs configuration:

# arguments that are passed to ini are of type configuration!, their value is decided by the called. here, we know the name, height and color!

#but we dont know of the plant is booming or not! so the caller cannot onfigure it

#its default value here would be Flase, its not booming. so init is the one thats responsible fore initliazing this type of attributes by giving default value

#when this is the case, its called state! when the user modifies the vallues its called configuration!

#Configuration	Provided at construction, external input

#State		Internal, mutable, changes over time

# ----> this is important:

#states change overtime  |  configuration cannot change overtime!

# find an exmaple! of how states are changable over time and configuration arent!
#configurtion is about setting its value to the arguments itself
#self.name = name

#state is about setting he value dirctly, and internally in the class
#self.name = "atlas"















