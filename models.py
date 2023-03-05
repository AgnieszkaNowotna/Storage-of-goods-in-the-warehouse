import csv

class Product:
    def __init__(self, name, unit, unit_price, quantity):
        self.name = name
        self.unit = unit
        self.unit_price=unit_price
        self.quantity = quantity

    def load_products(file_name = "storage.csv"):
        ITEMS = []
        with open(file_name , newline ='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = Product(name = row["Name"], quantity = int(row["Quantity"]), unit = row["Unit"], unit_price = float(row["Unit Price (PLN)"]))
                ITEMS.append(item)
        return ITEMS
    
product = Product