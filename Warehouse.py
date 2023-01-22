
from enum import IntEnum
Choice_List = IntEnum('Choice_List', 'exit show add')

items = [
    {'name':'Potatoes','quanitity': 200, 'unit':'kg', 'unit_price': 1.50},
    {'name':'Tomatoes','quanitity': 150, 'unit':'kg', 'unit_price': 7.75},
    {'name':'Apples','quanitity': 250, 'unit':'kg', 'unit_price': 2.50},
    {'name':'Zucchini','quanitity': 100, 'unit':'pcs', 'unit_price': 3.50}]

def get_items():
    key_list = ["Name","Quantity","Unit","Unit Price (PLN)"]
    print (f'%-15s %-15s %-15s %-15s'% (key_list[0], key_list[1], key_list[2], key_list[3]))
    for position in items:
        value_list = []
        for key,value in position.items():
            value_list.append(value)
        print(f'%-15s %-15s %-15s %-15s'% (value_list[0], value_list[1], value_list[2], value_list[3]))

def add_item(name, unit_name, quantity, unit_price):
    new_product = dict()
    new_product[name] = name
    new_product[quantity] = quantity
    new_product[unit_name] = unit_name
    new_product[unit_price] = unit_price
    return new_product

i = 1 
while i > 0:
    choice = int(input('''What would you like to do ?
1 - Escape from the program
2 - Show products
3 - Add new item
'''))
    if choice == Choice_List.exit:
        print ("Bye Bye!")
        i -= i
        exit()
    if choice == Choice_List.show:
        get_items()
    if choice == Choice_List.add:
        if __name__ == "__main__":
            name = input("What is the name of a new product?: ")
            quantity = input("How much of new product is added?: ")
            unit_name = input("What is the unit of new product?: ")
            unit_price = input("What is the price for one unit of product?:")
            items.append(add_item(name, unit_name, quantity, unit_price))

