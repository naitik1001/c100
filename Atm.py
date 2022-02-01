class Atm(object):
    def __init__(self,cashWithDrawl,balanceEnquiry):
        self.cashWithDrawl=cashWithDrawl
        self.balanceEnquiry=balanceEnquiry
    def start(self):
        print("Please swipe your card")
        print("your card number is 1234 5678 9012 ,your cvv is 192,your pin is ****")
        print("Thank you ,your bank balance will be displayed in 30 seconds")
    def accelerate(self):
        print("your bank balance is $3000")
    def stop(self):
        print("Thanks for visiting our atm")
card=Atm("Cash","balanceEnquiry")
print(card.start())
print(card.accelerate())
print(card.stop())

    