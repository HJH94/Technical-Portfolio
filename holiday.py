import time
import os

def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        # Check if OS is Linux 
        os.system('clear')

clear_screen() # I found this clear_screen() online and wanted to add it into the programme to make the terminal look neater 

def flight_calc(flight_input): # I wanted to have this separate as a sub routine 
    return len(flight_input)*50 # used len to convert the city flight into a number to calculate a flight cost 

def num_nights(night_input): # creating the function 
    return night_input * 150 # multiplying the input by 150 to return a value 

def rental_days(rental_int): # creating the function 
    return rental_int * 80 # multiply input by 80 per day 

def holiday_cost(a, b, c): # used easy variables here 
    result = a+b+c # adding the variables together 
    return result # return the result 
        
print("Welcome to the HallComm Ltd Holiday Calculator!\n") # used my company name as an original touch to the programme
time.sleep(0.5) 
city_flight = input("Please enter the city you wish to fly to: \n") # asks user to input city, input as a string
time.sleep(0.5) 
clear_screen()
hotel_nights = int(input("Please enter the number of nights you wish to stay for: \n")) # integer input for number of nights 
time.sleep(0.5) 
clear_screen()
rental_time = int(input("Please enter the number of days you want to hire a car for (enter 0 if no car required): \n")) # integer input of rental car days 
time.sleep(0.1)
clear_screen()
print("Please wait while we calculate your holiday costs") # telling the user what the programme is doing 
time.sleep(2)


hotel_cost = num_nights(hotel_nights) # call the function to calculate hotel cost  

car_rental = rental_days(rental_time) # call the function to calculate rental cost

plane_cost = flight_calc(city_flight) # taking the city flight and making it a value 

total_price = holiday_cost(hotel_cost, car_rental, plane_cost) # call the function to add them together 

# holiday_cost = hotel_cost + car_rental + plane_cost # calculating the total holiday cost 

time.sleep(1.5)  # giving the user time to read  so the programme doesn't instantly return a value and cause doubt     clear_screen()
clear_screen()
print(f"\nYour custom package holiday to {city_flight} will cost: £{total_price} \n") # showing the user total holiday cost 
print(f"Cost Breakdown: \nHotel total: {hotel_nights} nights at £150 per night. \nCar rental total: £{car_rental} for {rental_time} days at £80 per day. \nCost of flights: £{plane_cost} \n")
print("Thank you for choosing HallComm Ltd for your holiday needs! \n") 
 