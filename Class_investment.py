class Investment:
    def __init__(self, principal = 0, interest = 0):
        self.p = principal
        self.i = interest
    
    def __str__(self):
        return 'Investment value is: ${}, interest rate- {}%'.format(self.profit, self.n)
    def value_after(self, n = 0):
        self.n = n
        self.profit = pow(self.p * (1 + (self.i/100)), self.n)
        return self.profit
    
payment = Investment(10000, 7)
payment.value_after(7)
print(payment)


