
# ---------------------------------
# Program by Artem Kotlyarov
# Version:           Date:
# 1.0                24.03.2018
# ----------------------------------


import json
import random
import datetime
import datetime
import uuid

menu = ['Burger and Cola', 'Pizza and Sprite', 'Hot-Dog end Cofee']
menu_list_01 = {
    '0': 'Burger and Cola',
    '1': 'Pizza and Sprite',
    '2': 'Hot-Dog end Cofee',
}

inputfile = "./persons.json"
enter_user = input(
    "Здравствуйте! Выберете режим работы программы, введите в консоль следующие варианты:\n\nAdmin\nUser\n\n")
if str(enter_user) == 'Admin':
    admin_menu = input(
        "В режимие раброты Admin вы можете увидить список заказов и меню. \nOrders - список заказов. \n Menu - возможность добавить новую позицию в меню, удалить или редактировать\n\nВведите следующий параметр:\n\nMenu\nOrders\n\n")
    if str(admin_menu) == 'Orders':
        myfile = open(inputfile, mode='r')
        print(myfile.read(), ', '.join(myfile))
    if str(admin_menu) == 'Menu':
        for key, value in menu_list_01.items():
            print(key + ":" + value)
        menu_option = input(
            "\nВведите один из вариантов редактирования меню:\n1.Добавить позицию.\n2.Удалить позицию\n3.Редактировать позицию\n")
        if int(menu_option) == 1:
            menu_opt0_01 = input(
                "Введите название позиции, желательно в формате предоставленном выше!\n\n")
            menu.append(menu_opt0_01)
            print(', '.join(menu))
            print("Позиция успешно добавлена!")
        else:
            print("Нет такого варианта !")
        if int(menu_option) == 2:
            menu_opt0_02 = input(
                "Ввведите номер позиции которую хотите удалить:\n\n")
            menu.pop(int(menu_opt0_02))
            print(', '.join(menu), "\n\n")
        if int(menu_option) == 3:
            menu_opt0_03 = input(
                "Введите номер позиции для редактирования!\n\n")
            menu_opt0_03_0 = input("Новое название для позиции:\n\n")
            menu[int(menu_opt0_03)] = str(menu_opt0_03_0)
            print(', '.join(menu))


if str(enter_user) == 'User':
    print("==========================================================================")
    name = input(
        "\nHello, you are greeted by the KFC international network, what is your name?\n\n")
    if str(name) == 'y':
        quit()
    age = input(name+", how old are you?\n\n")
    if str(age) == 'y':
        quit()
    if int(age) > 17:
        country = input(
            "Well, our service only works for autopeminors. We work with the countries of northern Europe:\n\n 1.Denmark,\n 2.Sweden,\n 3.Finland,\n 4.Norway, \n\nWhere are you?\n\n")
        if str(country) == 'y':
            quit()
        country_list = ['1', '2', '3', '4']
        if country in country_list:
            for key, value in menu_list_01.items():
                print(key + ":" + value)
            denmark_dialog_01 = input(
                "Here is your menu, сhoose a position from the list above:\n\n")
            if str(denmark_dialog_01) == 'y':
                quit()
            if int(denmark_dialog_01) == 0:
                print(menu[0])
            if int(denmark_dialog_01) == 1:
                print(menu[1])
            time = input(
                "Thank you for your choice, food delivery will be at 15:00, is it convenient for you at this time?")
            if str(time) == 'y':
                quit()
            if str(time) == "Yes":
                print("Application accepted, your order is processed by moderators :)")
                today = datetime.datetime.today()
                print(today.strftime("%m/%d/%Y"))
            if str(time) == "No":
                kfc_order = input(
                    "Then let's come up with a convenient delivery time for you:\n\n")
            print("The application is accepted, your order will be delivered to " +
                  (kfc_order)+". Thank you, your KFC!")

            def kfc_test():
                json_list = {
                    'Name': name,
                    'Age': age,
                    'Country': country,
                    'Menu': denmark_dialog_01,
                    'Time order': kfc_order,
                    'ID': str(uuid.uuid1()),
                }
                return json_list

            def write_json(person_dict):
                try:
                    data = json.load(open('persons.json'))
                except:
                    data = []
                data.append(person_dict)
                with open('persons.json', 'w') as file:
                    json.dump(data, file, indent=2, ensure_ascii=False)

            def main():
                persons = {}
                write_json(kfc_test())
            if __name__ == '__main__':
                main()
        else:
            print("Our system does not work with this country")
    else:
        print("Sorry, you have not reached adulthood, you are not available for the service function. Run to your mother!")

input("\n\n Click Enter to exit!")
