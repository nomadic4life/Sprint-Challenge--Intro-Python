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
# Put a comment noting which class is the base class.


class Vehicle:
    pass


class GroundVehicle(Vehicle):
    pass


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass


class FlightVehicle(Vehicle):
    pass


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass


# class Vehicle:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type


# class GroundVehicle(Vehicle):
#     def __init__(self, name):
#         Vehicle.__init__(self, name, "Ground Vehicle")


# class Car(GroundVehicle):
#     def __init__(self, name, model):
#         self.model = model
#         self.wheels = 4
#         GroundVehicle.__init__(self, name)

#     def __str__(self):
#         print(
#             f"Car name: {self.name} is model type: {self.model} of vehichle type: {self.type}.")


# class Motorcycle(GroundVehicle):
#     def __init__(self, name, model):
#         self.model = model
#         self.wheels = 2
#         GroundVehicle.__init__(self, name)

#     def __str__(self):
#         print(
#             f"Motorcycle name: {self.name} is model type: {self.model} of vehichle type: {self.type}, that has {self.wheels} number of wheels.")


# class FlightVehicle:
#     def __init__(self, name):
#         self.name = name
#         self.type = "Flight Vehicle"


# class Airplane(FlightVehicle):
#     def __init__(self, name):
#         self.model = "Airplane"
#         FlightVehicle.__init__(self, name)


# class Starship:
#     def __init__(self, name):
#         self.name = name
#         self.type = "Star Traveller"
