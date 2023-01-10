from calendar import c
from email import message
from functools import total_ordering
from heapq import merge
import random
import pandas as pd
import numpy as np
import smtplib

# SUKESH

print("Group members")
print()
print("Sukesh Shetty")
print()
print("Roshan Bharti")
print()
print("Ankit Varma")
print()
print("Salim Shaikh")
print()
print()  # add project description
print("*"*5 + "#"*5 + "ATR CAFE" + "#"*5 + "*"*5)  # Cafe Name
name = 0
address = 0
phone = 0
email = 0
#food_list_csv = {"chicken 69":[180], "chicken biryani":[160], "pav bhaji":[60], "fried rice":[120], "dal makhani":[100], "coffee":[30], "tea":[30], "chicken tandoori": [300], "shawarma":[90], "egg roll":[70], "coke":[40], "egg omelette":[35], "naan roti":[40], "samosa":[20], "bhaji":[20], "lacha paratha":[50], "jeera rice":[80], "cookies":[20], "lassi":[45], "plain naan":[40], "butter chicken":[280], "sprite":[45], "pizza":[120], "grilled sandwich":[60], "pasta":[80], "cheese maggi":[60], "burger":[80], "french fries":[50], "hot dog":[70], "dosa":[40], "uttapam":[50], "idli":[40], "vada":[40], "paneer tikka":[100], "paneer chilli":[120], "chicken chilli":[160], "matar paneer":[130]} # Cafe food list
#food_list_dataframe = pd.DataFrame(food_list_csv) #this line will convert the dictionary to dataframe
#food_list_dataframe = food_list_dataframe.T  #this ;ine will transpose the dataframe
#print(food_list_dataframe)
#food_list_dataframe.to_csv(r"C:\Users\sukes\Desktop\assignment\food_list_csv.csv") # this will save the dataframe into the csv file on the desired location 
menu = pd.read_csv(r"C:\Users\sukes\Desktop\assignment\food_list_csv.csv") # this line will store the data in the menu variable from the csv file as a dataframe
food_list ={} # this is the empty dictionary where the food list will be saved
for i,j in zip(menu['Unnamed: 0'], menu['0']): #this will bring the items from the dataframe
    food_list[i]=j # this will convert the values from the dataframe to dictionary key and value pair



#food = np.array(["chicken 69", "chicken biryani", "pav bhaji", "fried rice", "dal makhani", "coffee", "tea", "chicken tandoori", "shawarma", "egg roll", "coke", "egg omelette", "naan roti", "samosa", "bhaji", "lacha paratha", "jeera rice", "cookies", "lassi", "plain naan", "butter chicken", "sprite", "pizza", "grilled sandwich", "pasta", "cheese maggi", "burger", "french fries", "hot dog", "dosa", "uttapam", "idli", "vada", "paneer tikka", "paneer chilli", "chicken chilli", "matar paneer"]) # name of the food
#price = np.array([180, 160, 60, 120, 100, 30, 30, 300, 90, 70, 40, 35, 40, 20, 20, 50, 80, 20, 45, 40, 280, 45, 120, 60, 80, 60, 80, 50, 70, 40, 50, 40, 40, 100, 120, 160, 130]) #price of all the food in the list
#chicken_69 = np.array(["shawarma", "egg roll", "coke"]) # recommendation for chicken 69
#shawarma = np.array(["coke", "chicken 69", "egg roll"]) # recommendation for shawarma
#egg_roll = np.array(["shawarma", "coke", "chicken 69"]) # recommendation for egg roll
#coke = np.array( ["sprite", "lassi", "coffee"]) # recommendation for coke
#chicken_biryani = np.array(["egg omelette", "naan roti", "coke"]) # recommendation for chicken biryani
#egg_omelette = np.array(["naan roti", "coke", "chicken biryani"]) # recommendation for egg omelete
#naan_roti = np.array(["coke", "egg omelette", "chicken biryani"]) # recommendation for naan roti
#pav_bhaji = np.array(["fried rice", "samosa", "bhaji"]) # recommendation for pav bhaji
#fried_rice = np.array(["pav bhaji", "samosa", "bhaji"]) # recommendation for fried rice
#samosa = np.array(["bhaji", "fried rice", "pav bhaji"]) # recommendation for samosa
#bhaji = np.array(["samosa", "fried rice", "pav Bhaji"]) # recommendation for bhaji
#dal_makhani = np.array(["laccha paratha", "jeera rice", "naan roti"]) # recommendation for dal makhni
#lacha_paratha = np.array(["jeera rice", "naan roti", "dal makhani"]) # recommendation for lacha paratha
#jeera_rice = np.array(["naan roti", "dal makhani", "laccha Paratha"]) # recommendation for jeera rice
#coffee = np.array(["tea", "cookies", "lassi"]) # recommendation for coffee
#lassi = np.array(["cookies", "tea", "coffee"]) # recommendation for lassi
#tea = np.array(["lassi", "coffee", "cookies"]) # recommendation for tea
#cookies = np.array(["tea", "coffee", "lassi"]) # recommendation for cookies
#chicken_tandoori = np.array(["plain naan", "butter Chicken", "sprite"]) # recommendation for chicken tandoori
#plain_naan = np.array(["chicken Tandoori", "sprite", "butter chicken"]) # recommendation for plain naan
#butter_chicken = np.array(["sprite", "plain naan", "chicken tandoori"]) # recommendation for butter chicken
#pizza = np.array(["grilled sandwich", "pasta", "cheese maggi"]) # recommendation for pizza
#cheese_maggi = np.array(["grilled sandwich", "pasta", "pizza"]) # recommendation for cheese maggi
#grilled_sandwhich = np.array(["pasta", "cheese maggi", "pasta"]) # recommendation for grilled sandwich
#pasta = np.array(["grilled sandwich", "cheese maggi", "pizza"]) # recommendation for pasta
#burger = np.array(["french fries", "coke", "hot dog"]) # recommendation for burger
#hot_dog = np.array(["french fries", "coke", "burger"]) # recommendation for hot dog
#french_fries = np.array(["coke", "hot dog", "burger"]) # recommendation for french fries
#dosa = np.array(["uttapam", "idli", "vada"]) # recommendation for dosa
#vada = np.array(["uttapam", "idli", "dosa"]) # recommendation for vada
#uttapam = np.array(["idli", "vada", "dosa"]) # recommendation for uttapam
#idli = np.array(["uttapam", "vada", "dosa"]) # recommendation for idli
#paneer_tikka = np.array(["paneer chilli", "matar paneer", "chicken chilli"]) # recommendation for paneer tikka
#paneer_Chilli = np.array(["matar Paneer", "paneer chilli", "paneer tikka"]) # recommendation for paneer chilli
#matar_paneer = np.array(["chicken chilli", "paneer tikka", "paneer Chilli"]) # recommendation for matar panner
#chicken_chilli = np.array(["paneer chilli", "chicken chilli", "matar paneer"]) # recommendation for chicken chilli
#sprite = np.array(["coke", "lassi", "egg_roll"]) # recommendation for sprite
#food_suggestion_dataframe = pd.DataFrame([food, price, chicken_69, shawarma, egg_roll, coke, chicken_biryani, egg_omelette, naan_roti, pav_bhaji, fried_rice, samosa, bhaji, dal_makhani, lacha_paratha, jeera_rice, coffee, lassi, tea, cookies, chicken_tandoori, plain_naan, butter_chicken, pizza, cheese_maggi, grilled_sandwhich, pasta, burger, hot_dog, french_fries, dosa, vada, uttapam, idli, paneer_tikka, paneer_Chilli, matar_paneer, chicken_chilli, sprite]) # this line will convert all the array to dataframe
#food_suggestion_dataframe = food_suggestion_dataframe.T # this line will create a transpose of the dataframe
#food_suggestion_dataframe.columns = ["food", "price", "chicken 69", "shawarma", "egg roll", "coke", "chicken biryani", "egg omelette", "naan roti", "pav bhaji", "rfied rice", "samosa", "bhaji", "dal makhani", "lacha paratha", "jeera rice", "coffee", "lassi", "tea", "cookies", "chicken tandoori", "plain naan", "butter chicken", "pizza", "cheese maggi", "grilled sandwhich", "pasta", "burger", "hot dog", "french fries", "dosa", 'vada', "uttapam", "idli", "paneer tikka", "paneer Chilli", "matar paneer", "chicken chilli", "sprite"] # this line gives column name to the dataframe
#food_suggestion_dataframe.to_csv(r"C:\Users\sukes\Desktop\assignment\food_suggestion.csv") # this line will save the dataframe to csv file
food_suggestion_dataframe = pd.read_csv(r"C:\Users\sukes\Desktop\assignment\food_suggestion.csv") # this line will read the data from csv and save it in dataframe

while True:
    print()
    print()
    print("Are you a customer or owner or exit:- ")
    print("press o for owner")
    print("press c for customer")
    print("press x to exit")
    owner_or_customer = input("enter the word here :-") # Here the user will enter weather he is the owner or the customer of the restruant
    if owner_or_customer == "c":
        loop_menu = 0  # loop created to show the menu list again
        while loop_menu == 0:
            print("welcome")
            print("what would you like to do")
            print()
            print("1. Enter your data")
            print()
            print("2. Place Order")
            print()
            print("3. Exit")
            print()
            print()
            task_of_customer = int(input("enter the no in front of what you want to do :- "))  # the user will enter what he would like to do from the menue above
            print()

            if task_of_customer == 1:
                loop_data_entry = 0 # loop to show the enter data list agsin till the user writes the correct details
                while loop_data_entry == 0:
                    name = input("enter your name :- ")  # User will enter his name
                    print()
                    address = input("enter address : ")  # User will enter his address
                    print()
                    phone = input("enter phone no :- ")  # User will enter his phone
                    print()
                    email = input("enter your email here :- ")
                    if len(phone) == 10:  # it is to check wether the lenght of the phone no is correct
                        if "@" in email and "." in email:
                            print("welcome", name, "hope you enjoy here")
                            print()
                            loop_data_entry = 2
                        else:
                            print("enter the correct email address")
                            print()
                    else:
                        print("the phone no you have entered is incorrect")
                        print()
                print()
                print()

            if task_of_customer == 2:
                if name != 0 and address != 0 and phone != 0:
                    print("*"*5 , "#"*5 , "MENU" , "#"*5 , "*"*5)
                    print()
                    for keys,values in food_list.items():# this line will store the key and values in the food list
                        print(keys,"",":","", values) #This line will print the key value paor of the dataframe
                        print()
                    
                    no_of_orders = int(input("Enter the no of dishes you want to order :- "))# here the user will enter the no of food he wants to order
                    print()
                    i = 0
                    food_ordered_total = {}  # this is the dictionary where all the food ordered will be stored
                    total_amount = 0 # this will store the total amount of the food purchased
                    while i < no_of_orders :
                        food_ordered_everytime = input("Enter the name of the food you want to eat :- ")# here the user will enter the name of the food he want to order
                        print()
                        no_of_dishes = int(input("Enter the no of plates of the dish you want to order :- "))# here the user will enter the no of plates of the dish he needs
                        print()
                        food_price = food_list[food_ordered_everytime]#here the program will store the price of the food from the food list
                        total_food_price = food_price * no_of_dishes # this variable will store the total price of the food 
                        food_ordered_total[food_ordered_everytime] = total_food_price # this line will store the food ordered and the total price into the food ordered total dictionary
                        total_amount += total_food_price # This line will calculate the total amount of the food ordered
                        i += 1
                    
                    print("your total bill for now is :-")
                    for keys,values in food_ordered_total.items():#this line will display the food ordered by the customer
                        print(keys,"",":","", values) # it will display the dictionary in key and value pair
                        print()

                    print("The total amount you have to pay is :- ", total_amount) # this will display the total amount of the food ordered including the food ordered and the suggestions accepted.
                    print()
                    food_suggestion_dataframe = pd.read_csv(r"C:\Users\sukes\Desktop\assignment\food_suggestion.csv") # this line will brinh the food suggestion from the csv in dataframe
                    i = 0
                    suggestion_dict = {} # here the suggestion of the food will be stored
                    while i < no_of_orders:
                        for keys,values in food_ordered_total.items():#this line will display the food ordered by the customer
                            food_suggestion_price = food_list[keys] # this line will bring the sduggested food price
                            suggestion_food = random.randint(0,2) # this line will generate random suggestion on for food
                            print("wolud like to add", food_suggestion_dataframe.iloc[suggestion_food][keys],":", food_suggestion_price) # this line will display the sugestion food and price
                            print()
                            suggestion_want_not = input("press y to add this to your bill :- ") #here the user will enter y to enter food from the suggestion to the bill
                            print()
                            food_suggestion_to_bill =  food_suggestion_dataframe.iloc[suggestion_food][keys]
                            if suggestion_want_not == 'y':
                                no_of_plates = int(input("enter the no of plates of the dish you would like :- ")) # if user wants to enter the food in menu the program will ask no of plates of the dishes he need
                                print()
                                print("The food has been added to the suggestion")
                                print()
                                total_suggestion_food_price = food_suggestion_price * no_of_plates # this will calculate totoal price of the food 
                                suggestion_dict[food_suggestion_to_bill] = total_suggestion_food_price
                            else :
                                print("Maybe next time")
                                print()
                            i += 1
                    food_ordered_total.update(suggestion_dict)
                    print("your total bill for now is :-")
                    print()
                    total_amount = 0
                    for keys,values in food_ordered_total.items():
                        total_amount += values
                        print(keys,"",":","", values)
                        print()
                    
                    Message_1 = "Thank You, We are glad that you chose ATR and provided us with the honour to serve you" # this is the message that will be present in the email
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login("invokerisback@gmail.com", "roshanbharti-1.")# this is the login credential of from which email the emails will be sent
                    server.sendmail("invokerisback@gmail.com",email, Message_1)
                    server.quit()

                    if total_amount < 500:# this line will check weather the total amount is less than 500
                        print("you will not get any discount")
                        print("The total amount you have to pay is :- ", total_amount)
                    if total_amount >500 and total_amount < 1000:# this line will check weather the total amount is greater than 500 and less than 1000
                        print("you will get 10 percent discount as your bill is greater than 500 rs")
                        greater_500 = total_amount - ((total_amount * 10)/100)
                        print("The total amount you have to pay is :- ", greater_500)
                    if total_amount >1000 and total_amount < 2000:# this line will check weather the total amount is greater than 1000 and less than 2000
                        print("you will get 30 percent discount as your bill is greater than 500 rs")
                        greater_1000 = total_amount - ((total_amount * 30)/100)
                        print("The total amount you have to pay is :- ", greater_1000)
                    if total_amount >2000:# this line will check weather the total amount is greater than 2000
                        print("you will get 50 percent discount as your bill is greater than 2000 rs")
                        greater_2000 = total_amount - ((total_amount * 50)/100)
                        print("The total amount you have to pay is :- ", greater_2000)
                    name = 0
                    address = 0
                    phone = 0
                    email = 0
                    print()


                    
                else:
                    print("Please first enter your details then order the food ")
                    print()
            
            if task_of_customer == 3:
                quit()

    if owner_or_customer == "o":
        loop_entry = 1
        while loop_entry == 1 : # loop to make user name and password come sgain and again
            print("welcome sir/ Mam")
            print()
            print("To confirm you are the owner please enter the following details")
            print()
            username = 0
            password = 0
            print("the username is owner")
            print()
            print("the password is 12345")
            print()
            username = input("enter your user name :- ") # this line will ask for username
            print()
            password = input("enter your password :- ") # this line will ask for password
            print()
            if username == "owner" and password == "12345": #this line will check weather the user has entered correct username and password
                print("Welcome the owner of ATR CAFE")
                print()
                loop_entry = 0
                print("What would you like to do :- ")
                print()
                print("1. Change the price of food")
                print()
                print("2.  Add food to the list")
                print()
                print("3. Delete food from the list")
                print()
                task_of_owner = int(input("enter the no in front of the task you want to do :- "))# here the user will enter what task he wants to do
                print()
                if task_of_owner == 1:

                     # SALIM

                    loop_price_change = 1
                    while loop_price_change == 1: 
                        print(food_list)
                        food_for_price_change = input("Enter the name of the food whose price you want to change :- ") # here the user will enter the name of the food whose price to be changed
                        if food_for_price_change in food_list: # this will check weather the food is in the food list
                            print("The current price of the food is :- ",food_list[food_for_price_change]) # this line will show the current food price
                            print()
                            food_new_price = int(input("Enter the new price of food :- ")) # the user will enter the new price for food
                            print()
                            food_list[food_for_price_change] = food_new_price # here the new price will be added to the foodlist
                            food_list_datframe = pd.DataFrame(food_list, index=[0]) # this line will create the dataframe of the food list
                            food_list_datframe = food_list_datframe.T # this line will transpose the food list dataframe
                            food_list_datframe.to_csv(r"C:\\Users\\sukes\\Desktop\\assignment\\food_list_csv.csv") #this will save the dataframe to csv
                            food_list_food_to_list = food_suggestion_dataframe["food"].to_list() # this will take the column food from the dataframe and turn it into list
                            index_of_food = food_list_food_to_list.index(food_for_price_change) # this will give the index of the food entered in the food for price change
                            food_suggestion_dataframe.at[index_of_food,"Price"] = food_new_price #this line will change the old food price with the new one
                            food_suggestion_dataframe.to_csv(r"C:\Users\sukes\Desktop\assignment\food_suggestion.csv") # this line will save the suggestion datafgrame to the csv file.
                            food_list_datframe = pd.DataFrame(food_list, index= [0]) # this will convert the variabel to the food list dataframe
                            food_list_datframe = food_list_datframe.T 
                            food_list_datframe.to_csv(r"C:\Users\sukes\Desktop\assignment\food_list_csv.csv")
                            loop_price_change = 2
                        else:
                            print("The food is not in food list")
                            loop_price_change = 2

                            #ANKIT

                if task_of_owner == 2:
                    loop_add_food = 1
                    while loop_add_food == 1:
                        food_to_add = input("enter the name of the food to be added :- ") # enter the nameo f the food to be added
                        print()
                        if food_to_add in food_list: # this will check weather food to add is present in food list 
                            print("Food is already present in the menu")
                            print()
                        else:
                            price_of_add_food = int(input("Enter the price for food :-")) # enter the price of the new food
                            print()
                            add_to_food_list = input("press y if you want to add food to the menu :- ")
                            print()
                            if add_to_food_list == "y":
                                print("Enter the suggestion for the food")
                                print()
                                suggestion_1 = input("Enter the first suggestion food :- ") # enter the first suggestion 
                                print()
                                if suggestion_1 in food_list:  # this will check weather food to add is present in food list 
                                    print()
                                    suggestion_2 = input("Enter the second suggestion food :- ") # enter the second suggestion 
                                    print()
                                    if suggestion_2 in food_list:  # this will check weather food to add is present in food list 
                                        print()
                                        suggestion_3 = input("Enter the third suggestion food :- ") # enter the third suggestion 
                                        print()
                                        if suggestion_3 in food_list:  # this will check weather food to add is present in food list 
                                            print()
                                            food_list[food_to_add] = price_of_add_food # this will add the new food to the foodlist
                                            suggestion_list = np.array([suggestion_1, suggestion_2, suggestion_3])  # this line will create an array of all the suggestion
                                            suggestion_dataframe = pd.DataFrame({food_to_add : [suggestion_1, suggestion_2, suggestion_3]})  # this line will create an dataframe of all the array of all the suggestion
                                            food_suggestion_dataframe = pd.concat([food_suggestion_dataframe, suggestion_dataframe], axis= 1) # this line will merge bvoth the dataframe
                                            food_suggestion_dataframe.to_csv(r"C:\Users\sukes\Desktop\assignment\food_suggestion.csv")
                                            food_list_datframe = pd.DataFrame(food_list, index= [0])
                                            food_list_datframe = food_list_datframe.T 
                                            food_list_datframe.to_csv(r"C:\Users\sukes\Desktop\assignment\food_list_csv.csv")
                                            loop_add_food = 2
                                        else:
                                            print("Please enter the suggested food to the list first")
                                            print()
                                    else:
                                        print("Please enter the suggested food to the list first")
                                        print()
                                else:
                                    print("Please enter the suggested food to the list first")
                                    print()
                            else:
                                print("Enter the details again")
                

                if task_of_owner == 3:
                    loop_delete_food = 1
                    if loop_delete_food == 1:
                        print(food_list)
                        food_to_delete = input("Enter the name of the food you want to delete :- ") # enter the name of the food you want to delete
                        if food_to_delete in food_list:
                            sure_to_delete = input("Enter y if you want to delete food :- ")
                            if sure_to_delete == 'y':
                                print("The food is deleted")
                                food_list.pop(food_to_delete) # this line will delete the food from the food list
                                food_suggestion_dataframe.drop(food_to_delete, axis=1, inplace=True) # this line will delete the column from the food suggestion dataframe
                                food_suggestion_dataframe.to_csv(r"C:\Users\sukes\Desktop\assignment\food_suggestion.csv")
                                food_list_datframe = pd.DataFrame(food_list, index= [0])
                                food_list_datframe = food_list_datframe.T 
                                food_list_datframe.to_csv(r"C:\Users\sukes\Desktop\assignment\food_list_csv.csv")
                                loop_delete_food = 2
                            else:
                                print("Enter the details again")
                        else:
                            print("The food is already not in food list")




            elif username == "owner" and password != "12345":# this will tell that user has entered wrong password
                print("Your password is wrong")
                print()
            elif username != "owner" and password == "12345":# this will tell that user has entered wrong username
                print("Your Username is wrong")
                print()

    if owner_or_customer == "x":
        quit()
