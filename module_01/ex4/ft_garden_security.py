#!/usr/bin/python3.10

#==> can we call funtions anywhere?? isnt against how interpreter works!
class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)
        print(self.get_height())
        print(self.get_age())

    def set_height(self, height):
        if height < 0:
            print("invalid height!")
        else:
            self.__height = height

    def set_age(self, age):
        if age < 0:
           print("invalid age!")
        else:
           self.__age = age

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

obj = SecurePlant("rose", 1, 3)



#when i try to create a new class! i can pass arguments direclty to it! 
# this measn that i can also pass arguments/values of the private objects directly

#but: the assinging of privarte objects is done through setters abd getters
#so i can call these 2 functions to assign the objects directly!
#but when i call these functions, getters(height), setter(heigth)
#i cant use them directly like get(heigth | set(heigt))
#i need to use self with them: self.get(height | self.et(height))
#inside these function i have the self.object == value pass as argument!

