# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 18:45:59 2017

@author: EliteBook
"""

# Aungier_Car_Rental.py



from RentalCar import Car, PetrolCar, DieselCar, ElectricCar, HybridCar


class Dealership(object):

    def __init__(self):
        self.petrol_cars = []
        self.diesel_cars = []
        self.electric_cars = []
        self.hybrid_cars = []
        
    
    def create_current_stock(self):
        for i in range(20):
           self.petrol_cars.append(PetrolCar())
        for i in range(8):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
           self.electric_cars.append(ElectricCar())
        for i in range(8):
           self.hybrid_cars.append(HybridCar())

    
    def stock_count(self):
        print "\nPetrol cars in stock {}".format(len(self.petrol_cars))
        print "Diesel cars in stock {}".format(len(self.diesel_cars))
        print "Hybrid cars in stock {}".format(len(self.hybrid_cars))
        print "Electric cars in stock {}\n".format(len(self.electric_cars))
        
        
   
    def rent(self, car_list, required):
        if len(car_list) < required:
            return '\nThere are not enough cars in stock to fulfil rental\n{}' .format(self.stock_count())
            
        else:
            count = 0
            while count < required:
                car_list.pop()
                count += 1
                
            return 'You have successfully rented {} cars\n' .format(required)
        
    
    def restock(self, car_list, returned, Car):
        for i in range(returned):
            car_list.append(Car())
        return 'You have successfully returned {} cars' .format(returned)    
       
        
     
    def select_car_type(self):
        while True:
            car_type = str.lower(raw_input("Please type\n'p' for a Petrol Car\n'd' for a Diesel Car\n'e' for an Electric Car\n'h' for a Hybrid Car:\n'n' for None and to exit\n> "))
            if car_type == 'n':
                print 'Goodbye'
                quit()
            if car_type == 'p' or car_type == 'd' or car_type == 'e' or car_type == 'h':
                return car_type
                break
            else:
                print "Please Enter a Valid Selection"
                continue
            
    
    def get_quantity(self):
        while True:    
            quantity = raw_input('How many cars would you like to rent?\n> ')
            try:
                quantity = int(quantity)
                return quantity
            except:
                print "Please Enter a Valid Selection"
                continue
    
        
if __name__ == '__main__': 
    
    
    Aungier_Car_Rental = Dealership()  

    Aungier_Car_Rental.create_current_stock()
    
    print 'Welcome to Aungier Car Rental\n'
    print Aungier_Car_Rental.stock_count()
    
    
    while True:
        mode = raw_input("Would you like to rent or return a car?\n\nPlease type '1' to rent or '2' to return\nType 'q' to quit> ")
        if mode == 'q':
            print 'Goodbye'
            quit()
        
        
        if mode == '1':
            while True:
                print 'What type of car would you like?\n'
                
                car_type = Aungier_Car_Rental.select_car_type()
                
                required = Aungier_Car_Rental.get_quantity()
                                
                if car_type == 'p':
                    print Aungier_Car_Rental.rent(Aungier_Car_Rental.petrol_cars, required)
                    break
                if car_type == 'd':
                    print Aungier_Car_Rental.rent(Aungier_Car_Rental.diesel_cars, required)
                    break
                if car_type == 'e':
                    print Aungier_Car_Rental.rent(Aungier_Car_Rental.electric_cars, required)
                    break
                if car_type == 'h':
                    print Aungier_Car_Rental.rent(Aungier_Car_Rental.hybrid_cars, required)
                    break
                   
        
        
        elif mode == '2':  
            while True:
                print 'What type of car are you returning?\n'
                
                car_type = Aungier_Car_Rental.select_car_type()
                
                returned = Aungier_Car_Rental.get_quantity()
                
                if car_type == 'p':
                    if (len(Aungier_Car_Rental.petrol_cars) + returned) > 24:
                        print 'Please check type and quantity: exceeds max stock'
                        continue
                    print Aungier_Car_Rental.restock(Aungier_Car_Rental.petrol_cars, returned, PetrolCar)
                    break
                if car_type == 'd':
                    if (len(Aungier_Car_Rental.diesel_cars) + returned) > 12:
                        print 'Please check type and quantity: exceeds max stock'
                        continue
                    print Aungier_Car_Rental.restock(Aungier_Car_Rental.diesel_cars, returned, DieselCar)
                    break
                if car_type == 'e':
                    if (len(Aungier_Car_Rental.electric_cars) + returned) > 4:
                        print 'Please check type and quantity: exceeds max stock'
                        continue
                    print Aungier_Car_Rental.restock(Aungier_Car_Rental.electric_cars, returned, ElectricCar)
                    break
                if car_type == 'h':
                    if (len(Aungier_Car_Rental.hybrid_cars) + returned) > 4:
                        print 'Please check type and quantity: exceeds max stock'
                        continue
                    print Aungier_Car_Rental.restock(Aungier_Car_Rental.hybrid_cars, returned, HybridCar)
                    break
                
                    
        else:
            print 'You must select either 1, 2 or q'
            continue