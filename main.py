from classes.store import Store
from classes.product import Product

# Store Name
Target = Store("Target")

# Products
iPad = Product("iPad", 699.99, "Technology")
Bike = Product("Bike", 109.99, "Sporting Goods")
Diapers = Product("Diapers", 19.99, "Baby Items")
Shirt = Product("Shirt", 12.95, "Clothing")

# running functions
Target.add_product(iPad).add_product(Bike).add_product(Diapers).add_product(Shirt)
for product in Target.list_of_products:
    product.print_info()
Target.inflation(.25)
for product in Target.list_of_products:
    product.print_info()
iPad.update_price(.50, False)
for product in Target.list_of_products:
    product.print_info()
Target.set_clearance("Baby Items", .5)
for product in Target.list_of_products:
    product.print_info()
Target.sell_product()
for product in Target.list_of_products:
    product.print_info()