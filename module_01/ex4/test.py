#!/usr/bin/python3.10

class ex:
    def __init__(self):
        self.public = "im public"
        self._protected = "im protected"
        self.__private = "im private" #we make it private by preceding with _ _

    def set(self, value):
        if value > 10:
            self.__private = value
            print("value set!")
        else:
            print("less than 10")
    
    def show(self):
        return self.__private #we can assign the value inside class!


one = ex()

#print(one.public)	#we can access this with no problem
#print(one._protected)   #we can access this with no problem only if we pass _object
#print(one.__private)	#we cant access this! error!
#print(one._ex__private)	#we now access this through name mangling!



one.set(20)
print(one.show())









#set the values of object according to ceretain criteria!
#encapsulation
#private vs __private
#accessing __private
#name mangeling vs getters?
#setters vs getters!
#...
#when can we access the object:
#self.p1 || self._p1 || self.__p2? differnce!
#setters dotn return the value, but you return a message that states whts going on
#getters return the value that we want to display!
#what are propertis advanced!
#notes about python, if we printing the returned value of a function that doesn return anything print(f.getters()) => getters() doesnt return anythign. so here we well get the value: ==> None

#if we try to print the value of private object thats not initiliazed, we will get the message: Im private!
