import csv

ITEMS =[]

class Product:
    def __init__(self, name, unit, unit_price, quantity):
        self.name = name
        self.unit = unit
        self.unit_price=unit_price
        self.quantity = quantity

    def load_products(file_name = "storage.csv"):
        ITEMS.clear()
        with open(file_name , newline ='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = Product(name = row["Name"], quantity = int(row["Quantity"]), unit = row["Unit"], unit_price = float(row["Unit Price (PLN)"]))
                ITEMS.append(item)
        return ITEMS
    
    def add_product(self, data):
        data.pop('csrf_token')
        ITEMS.append(data)
        return ITEMS
    
    def save_list(self, file_name = "storage.csv"):
        with open(file_name,'w',newline='') as csvfile:
            fieldnames = ["Name","Quantity","Unit","Unit Price (PLN)"]
            thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
            thewriter.writeheader()
            for item in ITEMS:
                thewriter.writerow({"Name":item.name,"Quantity":item.quantity,"Unit":item.unit,"Unit Price (PLN)":item.unit_price})

product = Product