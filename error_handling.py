# Errors,Exceptions and saving JSON data
# What happen Behind the scene
# 1.the users enters a city or name in the browser
# 2.The apps sent a request to the weather API(open-weather-map)
# 3.the API response the data in json format
# 4.java-scrips read the json and display the whether on the page
#
# Other real time use-case
# 1.chat app--> send and receive message
# 2.stock-tracker-->to know real time prices of stock
# 3.online-shopping--> card-updating,product info
# 4.food delivery--> order tracking

# type-error str+int adding together this error occurs
# file not found error
# try something that might cause an exception
# except do if there was an exception
# else do if there was no exception
# finally do this no matter what happens
# Raise to rise our own exception

try:
    file = open("text.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("text.txt", "w")
    file.write("OOPS no file in that directory")
except KeyError as message:
    print(f"This key {message} does not exist")
else:
    inside_the_file =file.read()
    print(inside_the_file)
finally: # this line of code will not execute other line of our program
    # file.close()
    raise TypeError("file was closed no matter what happen it will run ")

try:
    print("str" + 12)
except TypeError:
    print("we unable to add str + int together")

try:
    print(0/12)
    dict = {"any_key": "any_value"}
    print(dict["key"])
except ZeroDivisionError:
    print("0 can't divide by any number")
except KeyError as error_name:
    print(f"The key {error_name} does not exist")

try:
    a = 12, print(b)
except NameError:
    print("variable name was differ so it's called name-error")

try:
     index = ["hi", 12, True]
     print(index[3])
except IndexError:
     print("Index Error")
