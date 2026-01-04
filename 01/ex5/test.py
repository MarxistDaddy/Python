#learning about inhertance!

# see this example: a flower, tree, vegetable are all plants.
#they share common traits:  name, height, age
#but each unique behavrio.

#==> instead of writing the same code 3 times, we:
# put shared logic in one parent class@
# then we specialized plants inherit from it

#this is how to avoid duplicates, bugs and messy code!

#core concepts that i must learn here:

# 1 inheritance: a child class automatically gets everything from the parent class
# plant [parent] --> {flower}, {tree}, {vegetable} these 3 are plants
#  a chile class will receive everything that a parent has!
##super() isnt for overwriting the parenet object, but rather for reusing the parents object

#its basically tellling the parent class to handdle its part of initializing!
#Call the parent class’s version of this method

#	so bascially inheritance is baout creating a parent class
#       that contains all the objects that will be reused later on
#	python is oop, so this means that we create classes to work on everything
#	a child class is bout borrowing parent's class objects!


#super()

#class Plant:
#    def __init__(self, name, height, age):
#        self.name = name
#        self.height = height
#        self.age = age

# --> so this a parent class!


#class Flower(Plant):
#    def __init__(self, name, height, age, color):
#        self.name = name
#        self.height = height
#        self.age = age
#        self.color = color

# --> now this is a child class!

# ----> Flower basically replacted the parent class Plant behavior!
# ----> we basically just write another version of Plant class1
# ----> if Plant changes, Flower breaks!

#so instead of duplicating the code, we rely on parent class to initiate our child class, since they share the same behavior!

#class Flower(Plant):
#    def __init__(self, name, height, age, color):
#        super().__init__(name, height, age)
#        self.color = color

# --> what the fuck is this??
# how does suprt work here?


# parent behavior runs first
# child adds extra behvior!

# so basically:
# super is like: do what my paret class does, then add exra behavior!

# when we call:
# class child:
#     def __init__(self, name, ehight, age, color) ||child own behavior | shares some of parents: name, height, age. but color is unique
#         super().__init_(name, height, age) ||-> borrow|inherant parent behavior
#              self.color = color

#so super() is basically calling parents behavior to implement it here!

# so inside flower class!
# suport().__init__(name, height, age)
# call the parent class() version of _init_
# but pass it the same object (self)

# Plant.__init__(self, name, height, age)
# self here is still a flower object
# the parent doesnt create a new object
# it initiliaze the same object


#Blueprints	||--> of classes

#Namespaces	||--> whats this?

#Behavior containers	||--> inharitaing a behavior!

# ❌ “Classes are allocated in memory when they are called”
# ✅ Objects (instances) are allocated in memory when the class is called

# What’s happening is object creation, not class creation.


What a class actually is in Python

In Python:

A class itself is an object
It is created once, when the file is executed
It lives in memory whether or not you create instances

Example:

class Plant:
    pass


The moment Python reads this:

A Plant class object is created
Stored in memory
Bound to the name Plant
Even if you never do Plant(), the class still exists.
What happens when you write Flower(...)

This does two distinct steps:

1️⃣ Memory allocation (object creation)

Python:

Allocates memory for a new object

The object’s type is Flower

This is done by __new__ (advanced detail) #__new__

At this moment:

No attributes yet

Object exists










































