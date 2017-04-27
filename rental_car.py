# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 20:56:14 2017

@author: EliteBook
"""

# Define a class for a car

class Car(object):
    # Implementation follows
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__daysrented = 0
        
    def setColour(self, value):
        self.__colour = value
        
    def setMake(self, value):
        self.__make = value
        
    def setDaysRented(self, days):
        self.__daysrented = days
        
    def getColour(self):
        return self.__colour
    
    def getMake(self):
        return self.__make
    
    def getDaysRented(self):
        return self.__daysrented
    
    
        
    
        
        
class PetrolCar(Car):
    def __init__(self):
        self.__AmountCarStock = 20
        
    def getAmountCarStock(self):
        return self.__AmountCarStock
    
    def setAmountCarStock(self, value):
        self.__AmountCarStock = value
        

        
class DieselCar(Car):
    def __init__(self):
        self.__AmountCarStock = 8
        
    def getAmountCarStock(self):
        return self.__AmountCarStock
    
    def setAmountCarStock(self, value):
        self.__AmountCarStock = value
        
class ElectricCar(Car):
    def __init__(self):
        self.__AmountCarStock = 4
        
    def getAmountCarStock(self):
        return self.__AmountCarStock
    
    def setAmountCarStock(self, value):
        self.__AmountCarStock = value
        
class HybridCar(Car):
    def __init__(self):
        self.__AmountCarStock = 8
        
    def getAmountCarStock(self):
        return self.__AmountCarStock
    
    def setAmountCarStock(self, value):
        self.__AmountCarStock = value
        
