class Store():
    def __init__(self,name):
        self.name= name
        self.product_list = []

    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self

    def sell_product(self, id):
        self.product_list.pop(id)
        return self

    def inflation(self, percent_increase):
        for product in self.product_list:
            product.update_price(percent_increase, True)
        

    # def set_clearance(self, category, percent_discount): 
    #     self.product.update_price(percent_discount, "isnt_increased")


class Product():
    def __init__(self,name, price, category):
        self.product_name= name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += (percent_change*100)
            return self
            
        elif  is_increased == False:
            self.price -= (percent_change*100)
            return self

    def print_info(self):
        print(self.product_name)
        print(self.price)
        print(self.category)

store1 = Store('jason')
bigmac = Product('bigamc',10,'food')
spciyChicken = Product('spicyChiken',10,'food')
phone = Product('iphone',100,'hardware')

a = store1.add_product(bigmac).add_product(spciyChicken).add_product(phone)
store1.inflation(50)

print(store1.product_list[0].price)



# Let's give some methods to our Product class:
# update_price(self, percent_change, is_increased) - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.

# print_info(self) - print the name of the product, its category, and its price.
               

# add_product(self, new_product) - takes a product and adds it to the store
# sell_product(self, id) - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.

# inflation(self, percent_increase) - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)

# set_clearance(self, category, percent_discount) - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)
     
