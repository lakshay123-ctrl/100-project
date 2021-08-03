class Bank(object):
   def __init__ (self,name,location,security,holidaysinweek):
        self.name = name
        self.location = location
        self.security = security
        self.holidaysinweek = holidaysinweek
   
   def withdrawcash(self):
       print("amount debited")
   def depositcash(self):
       print("amount credited")
   def issuecard(self):
       print("card has been issued")
   def loan(self):
       print("loan approved")  

bank = Bank("greeneryBank","UP","Proper","2")
print(bank.name)

bank.depositcash()
