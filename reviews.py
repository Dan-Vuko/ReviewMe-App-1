### PROGRAMMING ASSIGNMENT 1 - [REVIEWME!] ###

######                                    #     #
#     # ###### #    # # ###### #    #     ##   ## ######
#     # #      #    # # #      #    #     # # # # #
######  #####  #    # # #####  #    #     #  #  # #####
#   #   #      #    # # #      # ## #     #     # #
#    #  #       #  #  # #      ##  ##     #     # #
#     # ######   ##   # ###### #    #     #     # ######


# # - = - = - = - = - = - = # # - = - = - = - = - = - = # #
##################### FUNCTION CALLS ######################
# # - = - = - = - = - = - = # # - = - = - = - = - = - = # #

### Restaurant Name Function ### - [✓] Fully Functional
def restaurant_name():
    # collecting the restaurant(Input) as a variable: - This assigns variable "restaurant_name(input)"#
    return input("Please enter the name of the restaurant:\n")


### Critic Amount Function ### - [X] Almost Fully Functional
### BUG - When user inputs wrong value, it repeats but then returns a TypeError.
def critic_amount():
    # collecting the critic amount(Input) as a variable integers only allowed #
    # Once integer is entered, the loop will break, if non-integer entered, will display ValueError and ask for input again #
    while True:
        try:
            # variable = input
            crit_value = int(input("Please enter the number of critics:\n"))
            break
        except ValueError:
            print("Invalid number of critics. Please enter a number between 1 and 10.")
    # If the following is False, the program will move to the else statement #
    if crit_value >= 1 and crit_value <= 10:
        return crit_value
    else:
        print("Invalid number of critics. Please enter a number between 1 and 10.")
        critic_amount()


def input_helper(input_string):
    while True:
        input_value = input(input_string)

        if input_value.isdigit():
            if int(input_value) >= 1 and int(input_value) <= 5:
                return int(input_value)
            else:
                print("Invalid input. Please enter a number between 1 and 5, or N/A.")
                input_helper(input_string)
        elif input_value == "N/A":
            return None
        else:
            print("Invalid input. Please enter a number between 1 and 5, or N/A.")
            input_helper(input_string)


### Function that creates dictionary of critics & takes their inputs #### [✓] Fully Functional
def critic_dictionary(critic):
    # Creates empty dictionary #
    critic_dict = {}
    # Loops through dictionary, the variable critic will be looped through, starting at 1 and adding 1 to the loop until
    # the value of critic is equal to the value of critic_amount #
    for key in range(1, critic + 1):
        # Critic name will be generated as Critic + key amount in dictionary #
        critic_name = f"Critic {key}"
        # While Loop that collects the critic score(Input) as a variable for three inputs named: Food, Wine, Atmosphere.
        # Only allow integers between 1 and 5 or repeat user input #
        while True:
            try:
                # E.g. - Completed dictionary would look like {Critic 1 {'Food': 2, 'Wine': 3, 'Atmosphere': 5}} #
                # Calls input_helper function to validate input #
                critic_dict[critic_name] = {
                    "Food": input_helper(f"{critic_name} - Food Score: "),
                    "Wine": input_helper(f"{critic_name} - Wine Score: "),
                    "Atmosphere": input_helper(f"{critic_name} - Atmosphere Score: "),
                }
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
                # print("1234")
    # Return dictionary #
    return critic_dict


#### Function to calculate the average score for food per critic in total to two decimal points #
def food_average(critic_dict):
    # Initialize variable to 0 #
    food_sum = 0
    food_len = 0
    # Loop through dictionary #
    for key in critic_dict:
        # Add the value of the food score to the variable #
        if critic_dict[key]["Food"] != None:

            food_sum += critic_dict[key]["Food"]
            food_len += 1
    # Return the average of the food score #
    if food_len != 0:
        return round(food_sum / food_len, 2)
    else:
        return 0


#### Function to calculate the average score for wine per critic in total to two decimal points #
def wine_average(critic_dict):
    # Initialize variable to 0 #
    wine_sum = 0
    wine_len = 0
    # Loop through dictionary #
    for key in critic_dict:
        # Add the value of the wine score to the variable #
        if critic_dict[key]["Wine"] != None:
            wine_sum += critic_dict[key]["Wine"]
            wine_len += 1
    # Return the average of the wine score #
    if wine_len != 0:
        return round(wine_sum / wine_len, 2)
    else:
        return 0


#### Function to calculate the average score for atmosphere per critic in total to two decimal points #
def atmosphere_average(critic_dict):
    # Initialize variable to 0 #
    atmosphere_sum = 0
    atmosphere_len = 0

    # Loop through dictionary #
    for key in critic_dict:
        # Add the value of the atmosphere score to the variable #
        if critic_dict[key]["Atmosphere"] != None:
            atmosphere_sum += critic_dict[key]["Atmosphere"]
            atmosphere_len += 1
    # Return the average of the atmosphere score #
    # return round(atmosphere_average / atmosphere_len, 2)
    if atmosphere_len != 0:
        return round(atmosphere_sum / atmosphere_len, 2)
    else:
        return 0


### Print only the lowest minimum and highest maximum inputs for food given by critics ### [✓] Fully Functional
def food_min_max(critic_dict):
    # Create empty dictionary #
    food_min_max = {}
    # Loop through dictionary #
    for key in critic_dict:
        # Add values #
        if critic_dict[key]["Food"] != None:
            food_min_max[key] = critic_dict[key]["Food"]
    # Return dictionary #
    if len(food_min_max.values()) == 0:
        return (0, 0)
    else:
        return min(food_min_max.values()), max(food_min_max.values())


### Print only the lowest minimum and highest maximum inputs for wine given by critics ### [✓] Fully Functional
def wine_min_max(critic_dict):
    # Create empty dictionary #
    wine_min_max = {}
    # Loop through dictionary #
    for key in critic_dict:
        # Add values #
        if critic_dict[key]["Wine"] != None:
            wine_min_max[key] = critic_dict[key]["Wine"]
    # Return dictionary #
    if len(wine_min_max.values()) == 0:
        return (0, 0)
    else:
        return min(wine_min_max.values()), max(wine_min_max.values())


### Print only the lowest minimum and highest maximum inputs for atmosphere given by critics ### [✓] Fully Functional
def atmosphere_min_max(critic_dict):
    # Create empty dictionary #
    atmosphere_min_max = {}
    # Loop through dictionary #
    for key in critic_dict:
        # Add values #
        if critic_dict[key]["Atmosphere"] != None:
            atmosphere_min_max[key] = critic_dict[key]["Atmosphere"]
    # Return dictionary #
    if len(atmosphere_min_max.values()) == 0:
        return (0, 0)
    else:
        return min(atmosphere_min_max.values()), max(atmosphere_min_max.values())


# # - = - = - = - = - = - = # # - = - = - = - = - = - = # #
##################### PROGRAM START!!! ####################
# # - = - = - = - = - = - = # # - = - = - = - = - = - = # #


### Call the restaurant_name function ### [✓] Fully Functional
restaurant = restaurant_name()
### Call the critic_amount function ###
print(f"Please set the number of critics for {restaurant} (maximum 10)")
critic = critic_amount()

### Call the critic_dictionary function ###
# Enters the variable critic amount from critic_amount function (critic) into the dictionary function #
print(
    "Please enter the scores below. If not assessed, please enter NA, otherwise enter a number between 1 and 5."
)
critic_amount = critic_dictionary(critic)

### Call the food_average function ### [✓] Fully Functional
print("\nFood Scores:")
### Food Average
print(f"Average: {food_average(critic_amount)}")
### Food Minimum & Maximum
print(f"Minimum: {food_min_max(critic_amount)[0]}"), print(
    f"Maximum: {food_min_max(critic_amount)[1]}"
)

### Call the wine_average function ### [✓] Fully Functional
print("\nWine Scores:")
### Wine Average
print(f"Average: {wine_average(critic_amount)}")
### Wine Minimum & Maximum
print(f"Minimum: {wine_min_max(critic_amount)[0]}"), print(
    f"Maximum: {wine_min_max(critic_amount)[1]}"
)

### Call the atmosphere_average function ### [✓] Fully Functional
print("\nAtmosphere Scores:")
### Atmosphere Average
print(f"Average: {atmosphere_average(critic_amount)}")
### Atmosphere Minimum & Maximum
print(f"Minimum: {atmosphere_min_max(critic_amount)[0]}"), print(
    f"Maximum: {atmosphere_min_max(critic_amount)[1]}"
)
# # - = - = - = - = - = - = # # - = - = - = - = - = - = # #
