from flask import flash
import csv

class Product:
    def __init__(self, name, quantity, unit, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.unit_price = unit_price
    
ITEMS = {}

def all_items():
    return ITEMS

def load_values(items_dict = ITEMS, file_name = "storage.csv"):
    with open(file_name, newline ='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = Product(name = row["Name"], quantity = int(row["Quantity"]), unit = row["Unit"],unit_price = float(row["Unit Price (PLN)"]))
            items_dict[row["Name"]] = item
    return items_dict

def add_product(data, items_dict = ITEMS):
    data.pop('csrf_token')
    product = data['name']
    if check_if_avaliable(data['name']) == False:
        item = Product(name = data['name'],quantity = data['quantity'],unit = data['unit'], unit_price = data['unit_price'])
        items_dict[data['name']] = item
        flash('New product has been added')
    else:
        if (ITEMS[product].name == data["name"] and ITEMS[product].unit == data["unit"] and ITEMS[product].unit_price == data["unit_price"]):
            ITEMS[product].quantity += data["quantity"]
            flash(f'Amount of {product} has been updated')
        else:
            item = Product(name = data['name'],quantity = data['quantity'],unit = data['unit'], unit_price = data['unit_price'])
            items_dict[data['name']] = item
            flash('New product has been added')
    return items_dict

def check_if_avaliable(item):
    for key in ITEMS.keys():
        if key == item:
            return True
        else:
            False

def save_list(items_dict = ITEMS, file_name = "storage.csv"):
    with open(file_name,'w',newline='') as csvfile:
        fieldnames = ["Name","Quantity","Unit","Unit Price (PLN)"]
        thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
        thewriter.writeheader()
        for item in items_dict.items():
            thewriter.writerow({"Name":item[1].name, "Quantity":item[1].quantity, "Unit":item[1].unit, "Unit Price (PLN)":item[1].unit_price})

def sell_product(product, amount, items_dict = ITEMS):
    print(product)
    item_key = product.name
    sell_item = items_dict[item_key]
    sell_item.quantity -= amount
    items_dict[product] = sell_item
    return items_dict