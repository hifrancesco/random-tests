# # ### slice a list ###
# # saudi_cities_1 = ["Riyadh", "Jeddah", "Mecca", "Medina", "Dammam", "Taif", "Buraidah", "Khobar", "Tabuk", "Al Jubail"]
# # print(saudi_cities_1[2:5])

# # ### slice a tuple ###
# # saudi_cities_2 = ("Abha", "Al Hofuf", "Khamis Mushait", "Najran", "Yanbu", "Hail", "Arar", "Al-Kharj", "Al Bahah", "Al-Qatif")
# # print(saudi_cities_2[5::-5])

# # ### slice a string ###
# # word = "supercalifragilisticexpialidocious"
# # print(word[-10::-1])



# # # Step size
# # lst = [0, 1, 2, 3, 4, 5]
# # print(lst[1:6:2]) # Output: [1, 3, 5]

# # # Reverse a sequence
# # s = "hello world"
# # print(s[::-1])    # Output: "dlrow olleh"


# # ### basic slicing ###
# # american_cities = ("New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio")
# # american_sliced = american_cities[1:4]
# # print(american_sliced)

# # ### extended slicing ###
# # canadian_cities = ["Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Quebec City"]
# # canadian_sliced = canadian_cities[1:6:2]
# # print(canadian_sliced)

# # ### negative indexing ###
# # mexican_cities = ["Mexico City", "Guadalajara", "Monterrey", "Puebla", "Tijuana", "Ciudad Juarez", "Leon"]
# # mexican_sliced = mexican_cities[-2:]
# # print(mexican_sliced)

# # ### omitting indices ###
# # cuban_cities = ["Havana", "Santiago de Cuba", "Camagüey", "Holguín", "Santa Clara", "Guantánamo", "Pinar del Río"]
# # cuban_sliced = cuban_cities[::2]
# # print(cuban_sliced)

# import unittest
# from unittest.mock import patch
# from my_module import get_user_data

# class TestGetUserData(unittest.TestCase):

#     @patch("my_module.requests.get")
#     def test_get_user_data(self, mock_get):
#         mock_response = {"id": 123, "name": "Alice"}
#         mock_get.return_value.status_code = 200
#         mock_get.return_value.json.return_value = mock_response

#         user_data = get_user_data(123)

#         self.assertEqual(user_data, mock_response)
        



# ### string methods ###
# string = "hELLO wORLD"
# capitalized = string.capitalize()
# casefolded = string.casefold()

# print(capitalized)
# print(casefolded)

# ### string methods ###
# string = "Hello World!"
# centered = string.center(20, "*")
# counted = string.count("o")

# print(centered)
# print(counted)


# ### string methods ###
# string = "  Hello World!   "
# stripped = string.strip()
# replaced = string.replace("World", "Universe")
# splitted = string.split(" ")
# joined = "-".join(splitted)
# uppercased = string.upper()

# print(stripped) 
# print(replaced)
# print(splitted) 
# print(joined)      
# print(uppercased) 


# ### slice a list ###
# # saudi_cities_1 = ["Riyadh", "Jeddah", "Mecca", "Medina", "Dammam", "Taif", "Buraidah", "Khobar", "Tabuk", "Al Jubail"]
# # print(saudi_cities_1[2:5])

# # ### slice a tuple ###
# # saudi_cities_2 = ("Abha", "Al Hofuf", "Khamis Mushait", "Najran", "Yanbu", "Hail", "Arar", "Al-Kharj", "Al Bahah", "Al-Qatif")
# # print(saudi_cities_2[5::-5])

# # ### slice a string ###
# # word = "supercalifragilisticexpialidocious"
# # print(word[-10::-1])



# # # Step size
# # lst = [0, 1, 2, 3, 4, 5]
# # print(lst[1:6:2]) # Output: [1, 3, 5]

# # # Reverse a sequence
# # s = "hello world"
# # print(s[::-1])    # Output: "dlrow olleh"


# # ### basic slicing ###
# # american_cities = ("New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio")
# # american_sliced = american_cities[1:4]
# # print(american_sliced)

# # ### extended slicing ###
# # canadian_cities = ["Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Quebec City"]
# # canadian_sliced = canadian_cities[1:6:2]
# # print(canadian_sliced)

# # ### negative indexing ###
# # mexican_cities = ["Mexico City", "Guadalajara", "Monterrey", "Puebla", "Tijuana", "Ciudad Juarez", "Leon"]
# # mexican_sliced = mexican_cities[-2:]
# # print(mexican_sliced)

# # ### omitting indices ###
# # cuban_cities = ["Havana", "Santiago de Cuba", "Camagüey", "Holguín", "Santa Clara", "Guantánamo", "Pinar del Río"]
# # cuban_sliced = cuban_cities[::2]
# # print(cuban_sliced)

# import unittest
# from unittest.mock import patch
# from my_module import get_user_data

# class TestGetUserData(unittest.TestCase):

#     @patch("my_module.requests.get")
#     def test_get_user_data(self, mock_get):
#         mock_response = {"id": 123, "name": "Alice"}
#         mock_get.return_value.status_code = 200
#         mock_get.return_value.json.return_value = mock_response

#         user_data = get_user_data(123)

#         self.assertEqual(user_data, mock_response)
        



# ### string methods ###
# string = "hELLO wORLD"
# capitalized = string.capitalize()
# casefolded = string.casefold()

# print(capitalized)
# print(casefolded)

# ### string methods ###
# string = "Hello World!"
# centered = string.center(20, "*")
# counted = string.count("o")

# print(centered)
# print(counted)


# ### string methods ###
# string = "  Hello World!   "
# stripped = string.strip()
# replaced = string.replace("World", "Universe")
# splitted = string.split(" ")
# joined = "-".join(splitted)
# uppercased = string.upper()

# print(stripped) 
# print(replaced)
# print(splitted) 
# print(joined)      
# print(uppercased) 


import datetime

today = datetime.datetime.today()
weekday = today.strftime("%A")

if weekday == "Monday":
    print("It's Monday! You should go to the gym.")
else:
    print(f"It's {weekday}, you don't need to go to the gym today.")


"""

   _____ _                 _ ______                                       
  / ____| |               | |  ____|                                      
 | |    | | ___  _   _  __| | |__ _ __ __ _ _ __   ___ ___  ___  ___ ___  
 | |    | |/ _ \| | | |/ _` |  __| '__/ _` | '_ \ / __/ _ \/ __|/ __/ _ \ 
 | |____| | (_) | |_| | (_| | |  | | | (_| | | | | (_|  __/\__ \ (_| (_) |
  \_____|_|\___/ \__,_|\__,_|_|  |_|  \__,_|_| |_|\___\___||___/\___\___/ 


"""