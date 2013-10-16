import time

class ProductInfo(object):
    def __init__(self, name='generic_product', price=100):
        self.name = name
        self.price = price
        self.stock = 0


    # Returns the amount of product's units availables
    def get_stock(self):
        return self.stock

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def set_price(self, new_price):
        self.name = new_price

    def set_stock(self, new_stock):
        self.stock = new_stock


if __name__ == "__main__":

    #Item generation
    product = ProductInfo('temp_sensor', 47)
    product.set_stock(8)
    print "Product name: ", product.get_name()
    print "Product price: ", product.get_price()
    print "Product stock: ", product.get_stock()

    # We generate an infinite loop to let the program poll over and over again
    while True:
        time.sleep(1)
        stock = product.get_stock()
        if stock > 0:
            product.set_stock(stock - 1)
            print product.get_stock()
        else:
            print "Alert! no stock available"
            #break




