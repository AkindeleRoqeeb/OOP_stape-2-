class item:
    def __init__(self, name):
        # print('A life of creativity is the best')
############################################################################################################################
        print(f'our first product is: {name}')
    def calculate_total_price(self, x, y):
        return x * y


item1 = item('laptop')
item1.name = 'laptop'
item1.location = 'Nigeria'
item1.price = 300
item1.quality = 3
item1.quantity = 200

item2 = item('phone')
item2.name = 'phone'
item2.price = 300
item2.quality = 634
item2.quantity = 532
item2.location = 'Nigeria'

########################################################################################### OR ###############################

class item:
    def __init__(self, name, price, quantity, quality):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.quality = quality
    # def calculate_total_price(self, x, y):
    #     return x * y


item1 = item('laptop', 300, 3, 200)

item2 = item('phone', 320, 43, 23)

print(item1.name)
print(item2.name)

print(item1.price)
print(item2.price)

print(item1.quantity)
print(item2.quantity)

print(item1.quality)
print(item2.quality)

####################################################### if dont know the value of any parameter then set it to Zero ##################

class item:
    def __init__(self, name, price, quantity, quality=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.quality = quality
    # def calculate_total_price(self, x, y):
    #     return x * y


item1 = item('laptop', 300, 3)

item2 = item('phone', 320, 43)

print(item1.name)
print(item2.name)

print(item1.price)
print(item2.price)

print(item1.quantity)
print(item2.quantity)

print(item1.quality)
print(item2.quality)


###################################################################################################################################

class item:
    def __init__(self, name, price, quantity, quality=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.quality = quality
    def calculate_total_price(self):
        return self.price * self.quality


item1 = item('laptop', 300, 3, 2)
item2 = item('phone', 100, 43, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

######################################################## This is wronge if you want to calculate ##############################################################################

class item:
    def __init__(self, name, price, quantity, quality=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.quality = quality
    def calculate_total_price(self):
        return self.price * self.quality

########################################################### notice the int that is use as str ##########################
item1 = item('laptop', "300", 3, 2)
item2 = item('phone', "100", 43, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
