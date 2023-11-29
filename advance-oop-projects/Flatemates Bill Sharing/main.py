class Bill:
    """
    Object that contains data about the bill
    such as total amount and period of the bill.
    """
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
        

class Flatmate():
    """
    Create a flatmate person who lives in the 
    flat and pays the share of the bill.
    """
    
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
    def pays(self, bill, flatmate2):
        weight = self.days_in_house / ( self.days_in_house + flatmate2.days_in_house ) 
        to_pay = bill.amount * weight
        return to_pay

class PdfReport():
    """
    Creates a pdf file that contains data about
    the flatmate such as their name, their due amound
    and the period of the bill
    """
    
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, flatmate1, flatmate2, bill):
        pass
        
    
thebill = Bill(amount=120, period="March 2023")
john = Flatmate(name="john", days_in_house=20)
marry = Flatmate(name="marry", days_in_house=25)

print(john.pays(bill=thebill, flatmate2=marry))
print(marry.pays(bill=thebill, flatmate2=john))



