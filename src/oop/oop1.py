# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# This is the base class
class Vehicle:
    def __init__(self):

class GroundVehicle(Vehicle):
    super().__init__(self):

class FlightVehicle(Vehicle):
    super().__init__(self):

class Airplane(FlightVehicle):
    super().__init__(self)

class Starship(FlightVehicle):
    super().__init__(self)

class Car(GroundVehicle):
    super().__init__(self):

class Motorcycle(GroundVehicle):
    super().__init__(self):



