#!/usr/bin/python3.10

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):	# --> why do we pass self
        print("Rose is blooming beautifully!")


rose = Flower("rose", 25, 30, "red color")

print(f"name = {rose.name}\nheight = {rose.height}\nage = {rose.age}\ncolor = {rose.color}")

rose.bloom() # if we dont pass self, we get this error! understand it!

#rose.bloom()
#TypeError: Flower.bloom() takes 0 positional arguments but 1 was given
#why does it need the argument self!
