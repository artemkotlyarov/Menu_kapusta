
#---------------------------------
# Program by Artem Kotlyarov
# Version:           Date:
# 1.0                24.03.2018
#----------------------------------

#import sys
#sys.version_info
#(2, 6, 4, 'final', 0)
#if not sys.version_info[:2] == (2, 6):
 #       print "Error, I need python 2.6"
#else:
   #from my_module import twoPointSixCode
import sys
import re
import json

exit_01 = "You can press the Y key and exit the program of this service!\n\n"
print(exit_01)
print (sys.version)


name = input("\nHello, you are greeted by the KFC international network, what is your name?\n\n")
if str (name) == 'y':
        quit()
age = input(name+", how old are you?\n\n")
if str (age) == 'y':
        quit()





if int (age) > 17:
    country = input ("Well, our service only works for minors. We work with the countries of northern Europe:\n\n 1.Denmark,\n 2.Sweden,\n 3.Finland,\n 4.Norway, \n\nWhere are you?\n\n")
    if str (country) == 'y':
        quit()
    country_list = ['1', '2', '3', '4']
    if country in country_list:                
        menu = ['Kapusta s vodoy - 1$', 'Kapusta bez vodi - 0,36$', 'Voda bez kapusti - 0,75$']
        menu_list_01 = {
            '0': 'Kapusta s vodoy - 1$',
            '1': 'Kapusta bez vodi - 0,36$',
            '2': 'Voda bez kapusti - 0,75$', 
        }
        for key, value in menu_list_01.items():
                print(key + ":" + value)
                            
        #print(menu_list_01)
      
        denmark_dialog_01 = input("Here is your menu, сhoose a position from the list above:\n\n")
        if str (denmark_dialog_01) == 'y':
                quit()
        if int (denmark_dialog_01) == 0:
                print(menu[0])
        if int (denmark_dialog_01) == 1:
                print(menu[1])
        if int (denmark_dialog_01) == 2:
                print(menu[2])

        time = input ("Thank you for your choice, food delivery will be at 15:00, is it convenient for you at this time?")
        if str (time) == 'y':
                quit()
        if str (time) == "Yes":
                print("Application accepted, your order is processed by moderators :)")
        if str (time) == "No":
                kfc_order = input("Then let's come up with a convenient delivery time for you:\n\n")
                json_list = {
                'Name': name,
                'Age': age,
                'Country': country,
                'Menu': denmark_dialog_01,
                'Time order': kfc_order,
                }


                print("The application is accepted, your order will be delivered to "+(kfc_order)+". Thank you, your KFC!")
                
    else:
            print ("Our system does not work with this country")
else:
        print ("Sorry, you have not reached adulthood, you are not available for the service function. Run to your mother!")

filename = "menu_kfc.json"
#myfile = open(filename, mode ='w', encoding='utf-8')

with open(filename, "a") as myfile:
        json.dump (json_list, myfile)

input("\n\n Click Enter to exit!")
