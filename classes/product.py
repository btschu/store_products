class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased==False:
            self.price=round(self.price*(1-percent_change),2)
        else:
            self.price=round(self.price*(1+percent_change),2)
        return self
    def print_info(self):
        print(f"Name of Product: {self.name}\n Category: {self.category}\n Price: {self.price}")
        return self