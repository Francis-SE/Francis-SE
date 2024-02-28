
"""
    This is a holiday booking program that allows users to select their
    flight, hotel, and car rental options, and calculates the total cost
    of the holiday.

    - view and select flights
    - view and select hotel rooms
    - view and select rental car
    - view the total cost of holiday booking

"""
import os 

# Initialize selected options
selected_options = {
        "city_flight": {"option": "", "cost": 0},
        "room_type": {"option": "", "cost": 0},
        "num_nights": 0,
        "car_type": {"option": "", "cost": 0},
        "rental_days": 0,
    }

# Dictionaries to store cost of flights, rooms, and cars
city_flight_costs = {
        "Paris": 130,
        "Milan": 125,
        "Venice": 90,
        "Barcelona": 120,
        "Istanbul": 180
    }
room_prices = {"Standard": 100, "Deluxe": 150, "Suite": 200}
car_prices = {"Small": 16, "Medium": 22, "Large": 40}

# Function to clear the screen
def clear_scr():
    os.system('cls')

# Function to display current selected options
def currently_selected():
    print("\nCurrently selected:")
    print(f"City: {selected_options["city_flight"]["option"]}"
          f"\t\tCost: {selected_options["city_flight"]["cost"]}")
    print(f"Room Type: {selected_options["room_type"]["option"]}"
          f"\tCost: {selected_options["room_type"]["cost"]}")
    print(f"Car Type: {selected_options["car_type"]["option"]}"
          f"\tCost: {selected_options["car_type"]["cost"]}")
    
# Function to display selected options
def display_selected():
    print("Here is your Holiday Booking details:\n")
    print(f"City Flight: {selected_options["city_flight"]["option"]}"
           f"\tCost: {selected_options["city_flight"]["cost"]}")
    print(f"Room Type: {selected_options["room_type"]["option"]}"
           f"\tCost: {selected_options["room_type"]["cost"]}")
    print(f"Car Type: {selected_options["car_type"]["option"]}"
           f"\tCost: {selected_options["car_type"]["cost"]}")

# Function to calculate flight cost
def plane_cost(city_flight):
    cost = city_flight_costs.get(city_flight, 0)
    return cost, city_flight

# Function to calculate hotel cost
def hotel_cost(num_nights, room_type):
    cost = num_nights * room_prices.get(room_type, 0)
    return cost, room_type

# Function to calculate car rental cost
def car_rental(rental_days, car_type):
    cost = rental_days * car_prices.get(car_type, 0)
    return cost, car_type

# Function to get input
def get_input(prompt):
    user_input = input(prompt).capitalize()
    return user_input

# Function to get input with error handling
def get_second_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input! Please enter again.")
            
# Function to calculate total holiday cost
def holiday_cost(city_flight, num_nights, room_type, rental_days, car_type):
    total_cost = (hotel_cost(num_nights, room_type)[0] +
                plane_cost(city_flight)[0] + 
                car_rental(rental_days, car_type)[0])
    return total_cost

# This loop controls the flow of the program
def main():
    while True:
        clear_scr()
        currently_selected()
        print()
        print('-'*35)
        title = "Holiday Booking"
        print((" "*(15-(len(title)//2))), title)
        print('-'*35)

        print("1. Flight")
        print("2. Hotel")
        print("3. Car Rentals")
        print("4. Display Total")
        print("5. Quit")
    
        choice = input("\nEnter an option (1-5): ")

        if choice == "1":
            if selected_options["city_flight"]["option"] == "":
                
                clear_scr()
                print("Below are the available flights:\n")
                print("\tCity \t\t Cost")

# Displays available flight option
                for pos, (key, value) in enumerate(city_flight_costs.items()):
                    print(str(pos + 1) + ". " + key + " " * (25 - len(key)) + f"£{value}")
                
                city_flight = get_input("\nType the city you will be flying to: ")
                while city_flight not in city_flight_costs:  # Validate city_flight input
                    print("Your choice is not in the list. Please select from the list.")
                    city_flight = get_input("\nType the city you will be flying to: ")

# This code calculates cost of the selected flight option and updates
# `selected_options` dictionary with the chosen flight option and its cost. It then
# prints a message confirming the selection and displaying the chosen flight option
# and its cost.
                city_flight_cost, city_flight_option = plane_cost(city_flight)
                selected_options["city_flight"]["option"] = city_flight_option
                selected_options["city_flight"]["cost"] = city_flight_cost
                print(f"\nYou have selected {selected_options["city_flight"]["option"]} with"
                    f" a cost of £{selected_options["city_flight"]["cost"]}")
                
                input("\nPress Enter to return to main menu.")
            else:
                clear_scr()
                print("You have already selected your flight.")
                cancel_choice = input("Do you want to cancel your selection and"
                                    " choose another? (yes/no): ")
                while cancel_choice not in ["yes", "no"]:
                    print("Invalid input!")
                    cancel_choice = input("Do you want to cancel your selection and"
                                    " choose another? (yes/no): ")

                if cancel_choice.lower() == "yes":
                    selected_options["city_flight"]["option"] = ""
                    selected_options["city_flight"]["cost"] = 0
                    print("Your previous selection has been canceled.")
                    input("\nPress Enter to return to the main menu.")
                else:
                    input("\nPress Enter to return to the main menu.")

        elif choice == "2":
            if selected_options["room_type"]["option"] == "":
                clear_scr()
                print("Below are the available hotel rooms:\n")
                print("\tAvailable Room \t Cost")

# Displays available flight option
                for pos, (key, value) in enumerate(room_prices.items()):
                    print(str(pos + 1) + ". " + key + " " * (28 - len(key)) + f"£{value}")
                
                room_type = get_input("\nType the room you want to stay: ")
                while room_type not in room_prices:  # Validate city_flight input
                    print("Your choice is not in the list. Please select from the list.")
                    room_type = get_input("\nType the room you want to stay: ")

                num_nights = get_second_input("Enter number of days you want to stay: ")

# This code calculates cost of the selected room option and updates
# `selected_options` dictionary with the chosen room option and its cost. It then
# prints a message confirming the selection and displaying the chosen room option
# and its cost.
                room_cost, room_type_option = hotel_cost(num_nights, room_type)
                selected_options["num_nights"] = num_nights
                selected_options["room_type"]["option"] = room_type_option
                selected_options["room_type"]["cost"] = room_cost
                print(f"\nYou have selected {selected_options['room_type']['option']} "
                    f"room with a total cost of £{selected_options['room_type']['cost']}"
                    f" for {num_nights} days.")
            
                input("\nPress Enter to return to main menu.")
            
            else:
                clear_scr()
                print("You have already selected your room.")
                cancel_choice = input("Do you want to cancel your selection and"
                                    " choose another? (yes/no): ")
                while cancel_choice not in ["yes", "no"]:
                    print("Invalid input!")
                    cancel_choice = input("Do you want to cancel your selection and"
                                    " choose another? (yes/no): ")
                if cancel_choice.lower() == "yes":
                    selected_options["room_type"]["option"] = ""
                    selected_options["room_type"]["cost"] = 0
                    print("Your previous selection has been canceled.")
                    input("\nPress Enter to return to the main menu.")
                else:
                    input("\nPress Enter to return to the main menu.")

        if choice == "3":
            if selected_options["car_type"]["option"] == "":
                clear_scr()
                print("Below are the available type of car to rent:\n")
                print("\tCar Type \t Cost")
# Displays available flight option
                for pos, (key, value) in enumerate(car_prices.items()):
                    print(str(pos + 1) + ". " + key + " " * (25 - len(key)) + f"£{value}")
                
                car_type = get_input("\nEnter the type of car you want to hire : ")
                while car_type not in car_prices:  # Validate city_flight input
                    print("Your choice is not in the list. Please select from the list.")
                    car_type = get_input("\nEnter the type of car you want to hire: ")

                rental_days = get_second_input("Enter the number of days for which you"
                                            " will be hiring a car: ")

# This code calculates cost of the selected car option and updates
# `selected_options` dictionary with the chosen car option and its cost. It then
# prints a message confirming the selection and displaying the chosen car option
# and its cost.
                car_cost, car_type_option = car_rental(rental_days, car_type)
                selected_options["rental_days"] = rental_days
                selected_options["car_type"]["option"] = car_type_option
                selected_options["car_type"]["cost"] = car_cost
                print(f"\nYou have selected {selected_options["car_type"]["option"]} "
                    f"type of car with a total cost of £{selected_options["car_type"]["cost"]}"
                    f" for {rental_days} days")

                input("\nPress Enter to return to main menu.")

            else:
                clear_scr()
                print("You have already selected your car.")
                cancel_choice = input("Do you want to cancel your selection and"
                                    " choose another? (yes/no): ")
                while cancel_choice not in ["yes", "no"]:
                    print("Invalid input!")
                    cancel_choice = input("Do you want to cancel your selection and"
                                    " choose another? (yes/no): ")
                if cancel_choice.lower() == "yes":
                    selected_options["car_type"]["option"] = ""
                    selected_options["car_type"]["cost"] = 0
                    print("Your previous selection has been canceled.")
                    input("\nPress Enter to return to the main menu.")
                else:
                    input("\nPress Enter to return to the main menu.")

        if choice == '4':
            clear_scr()
            print("Review and Confirm Booking\n")
            display_selected()
            total_cost = holiday_cost(selected_options["city_flight"]["option"], 
                                    selected_options["num_nights"], 
                                    selected_options["room_type"]["option"],
                                    selected_options["rental_days"], 
                                    selected_options["car_type"]["option"],)
            print(f"\nYour total Holiday cost is £{total_cost}")
            input("\nPress Enter to return to main menu.")
        
        elif choice == "5":
            clear_scr()
            print("Thank you for booking with us. Goodbye!")
            break

        
if __name__ == "__main__":
    main()