#!/usr/bin/python
class product:
    #name = Toothbrush(The product)
    amount = 1000 
    price1 = 10.00
    def __init__(self):`
        self.number = eval(input('How many items do you want to buy:', ))
    def __str__(self):
        return ('Your bill is ${}'.format(self.profit))
    def get_price(self):
        if self.number < 10:
           print('You will be charged the normal price of $10.00 per item')
        if self.number >= 10 and self.number < 100:
            print('you will be given a 10% discount')
        if self.number >= 100:
            print('you will be given a 20% discount')
    def make_purchase(self):
            if self.number < 10:
                self.price = self.number * self.price1
                return self.price
            elif self.number >= 10 and self.number < 100:
                self.price = (self.number * self.price1) - ((self.number * self.price1) *(10 / 100))
                return self.price
            elif self.number >= 100 and self.number <= 1000:
                self.price = (self.number * self.price1) - ((self.number * self.price1) *(20 / 100))
                return self.price
            else :
                 self.number > self.amount
                 
                 return ('The available stock is not up to that.')
        
obj = product()
obj.get_price()
print(obj.make_purchase())
