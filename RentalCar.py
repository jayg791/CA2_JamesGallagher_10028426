# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 18:46:46 2017

@author: EliteBook
"""

# RentalCar.py

## Define Car class
class Car(object):
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        
    def getColour(self):
        return self.__colour

    def setColour(self, colour):
        self.__colour = colour
        
    def getMake(self):
        return self.__make

    def setMake(self, make):
        self.__make = make
    
    def getMileage(self):
        return self.__mileage

    def setMileage(self, mileage):
        self.__mileage = mileage


## Create Petrol Car Object        
class PetrolCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.__NumberCylinders = 4

    def getNumberCylinders(self):
        return self.__NumberCylinders

    def setNumberCylinders(self, value):
        self.__NumberCylinders = value        
        
## Create Diesel Car Object        
class DieselCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.__NumberCylinders = 4

    def getNumberGlowPlugs(self):
        return self.__NumberCylinders

    def setNumberGlowPlugs(self, value):
        self.self.__NumberCylinders = value        

## Create Electric Car Object         
class ElectricCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value
        
## Create Hybrid Car Object 
class HybridCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = ''

    def getSecondFuelSource(self):
        return self.__numberFuelCells

    def setSecondFuelSource(self, value):
        self.__numberFuelCells = value