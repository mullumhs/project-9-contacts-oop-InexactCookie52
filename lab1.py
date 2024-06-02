"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and manipulate Car objects in Python to understand 
  basic concepts of Object-Oriented Programming.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.is_engine_on = False
        self.odomiter = 0
    def start_engine(self):
        self.is_engine_on = True
        print(f"The engine of the {self.color} {self.brand} is now on.")

    def stop_engine(self):
        self.is_engine_on = False
        print(f"The engine of the {self.color} {self.brand} is now off.")


# Add another property to the Car class called "odometer".
# This property should be initialised to 0.



# Create two Car objects. One should be a red Toyota and the other a blue Ford.
toyota = Car("red", "toyota")
ford = Car("blue", "ford")

# Start the engine of the red Toyota.
toyota.start_engine()


# Create a method called "drive" that takes a distance as a parameter.
# The car can only be driven if the engine is on.
drive_distance = int(input("how far do you want to drive? "))
if toyota.is_engine_on:
    toyota.odomiter += drive_distance

# Attempt to drive both cars 100Km.
drive_distance2 = int(input("how far do you want to drive car 2? "))
if ford.is_engine_on:
    ford.odomiter += drive_distance2
else:
    print("Car is off")

# Print the brand, odometer and colour of both cars.
print(toyota.brand, toyota.color, toyota.odomiter)
print(ford.brand, ford.color, ford.odomiter)