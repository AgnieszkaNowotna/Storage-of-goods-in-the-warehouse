import logging
from enum import IntEnum
logging.basicConfig(level = logging.DEBUG)

Choice_List = IntEnum('Choice_List', 'exit show add sell sold cost income')

items = [
    {'name':'Potatoes','quantity': 200, 'unit':'kg', 'unit_price': 1.50},
    {'name':'Tomatoes','quantity': 150, 'unit':'kg', 'unit_price': 7.75},
    {'name':'Apples','quantity': 250, 'unit':'kg', 'unit_price': 2.50},
    {'name':'Zucchinis','quantity': 100, 'unit':'pcs', 'unit_price': 3.50}]
sold_items = []

def get_items(list_name):
    key_list = ["Name","Quantity","Unit","Unit Price (PLN)"]
    print (f'%-15s %-15s %-15s %-15s'% (key_list[0], key_list[1], key_list[2], key_list[3]))
    for position in list_name:
        value_list = []
        for key,value in position.items():
            value_list.append(value)
        print(f'%-15s %-15s %-15s %-15s'% (value_list[0], value_list[1], value_list[2], value_list[3]))

def insert_new_product():
    k = 1
    while k > 0:
        name = input("What is the name of a new product?: ")
        try:
            name = int(name)
            logging.info(f"Insert value isn't a word")
        except ValueError:
            name = name.capitalize()
            k -= k
    k = 1
    while k > 0:
        quantity = input("How much of new product is added?: ")
        try:
            quantity = int(quantity)
            k -= k
        except ValueError:
            logging.info(f"Insert value isn't a number")
    k = 1
    while k > 0:
        unit_name = input("What is the unit of new product?: ")
        try:
            unit_name = int(unit_name)
            logging.info(f"Insert value isn't a word")
        except ValueError:
            unit_name = unit_name.lower()
            k -= k
    k = 1
    while k > 0:
        unit_price = input("What is the price for one unit of product in PLN?:")
        try:
            unit_price = float(unit_price)
            k -= k
        except ValueError:
            logging.info(f"Insert value isn't a number")
    return(name, quantity, unit_name, unit_price)
    
def add_item(name, unit_name, quantity, unit_price):
    new_product = dict()
    new_product['name'] = name
    new_product['quantity'] = quantity
    new_product['unit'] = unit_name
    new_product['unit_price'] = unit_price
    return new_product

def sell_item(name, quantity):
    for position in items:
        if position['name'] == name:
            position['quantity'] -= quantity
            sold_items.append({'name':name,'quantity': quantity, 'unit':position['unit'], 'unit_price': position['unit_price']})
        else:
            pass

def get_value(list_name):
    total_value= [position['quantity']*position['unit_price']for position in list_name]
    return sum(total_value)

def check_name():
    j = 1
    while j > 0:
        name = (input("What is the name of a sold product?: ")).capitalize()
        names = []
        for position in items:
            names.append(position['name'])
        try:
            names.index(name)
            j -= j
        except ValueError:
            logging.info("There's no product with given name")
    return name

def check_quantity(name):
    j = 1
    while j > 0:
        quantity = int(input("How much did sell?: ")) 
        for position in items:
            if position['name'] == name:
                if position['quantity'] < quantity:
                    logging.info("There's not enough amount of product to sell")
                else:
                    j -= j
    return quantity

i = 1 
while i > 0:
    choice = (input('''What would you like to do ?
1 - Escape from the program
2 - Show products
3 - Add new product
4 - Sell product
5 - Show sold products
6 - Show value of owned products
7 - Show income
'''))

    if (choice.isdigit() == False):
        logging.info(f'Wrong value is given')
    else:
        if int(choice) > 8:
            logging.info(f'Wrong value is given')
        else:
            choice = int(choice)

    if choice == Choice_List.exit:
        print ("Bye Bye!")
        i -= i
        exit()

    if choice == Choice_List.show:
        get_items(items)

    if choice == Choice_List.add:
        if __name__ == "__main__":
            product = insert_new_product()
            name = product[0]
            quantity = product[1]
            unit_name = product[2]
            unit_price = product[3]
            items.append(add_item(name, unit_name, quantity, unit_price))

    if choice == Choice_List.sell:
        if __name__ == "__main__":
            name = check_name()
            quantity = check_quantity(name)   
            sell_item(name, quantity)
            get_items(items)

    if choice == Choice_List.sold:
        get_items(sold_items)

    if choice == Choice_List.cost:
        logging.info(f"Total value of stored products is: {get_value(items)}")
        
    if choice == Choice_List.income:
        logging.info(f"Total income from sold products is: {get_value(sold_items)}")