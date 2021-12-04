from classes.product import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.list_of_products = []

    def add_product(self, new_product):
        self.list_of_products.append(new_product)
        return self
    def sell_product(self, id):
        for i in range(len(self.list_of_products)):
            if self.list_of_products[i].id==id:
                soldItem=self.list_of_products.pop(i)
                soldItem.print_info()
                return self
        return self
    def inflation(self, percent_increase):
        for list_of_products in self.list_of_products:
            list_of_products.update_price(percent_increase, True)
        return self
    def set_clearance(self, category, percent_discount):
        for list_of_products in self.list_of_products:
            if list_of_products.category==category:
                list_of_products.update_price(percent_discount, False)
        return self

