from fpdf import FPDF

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
        
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        
        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=88, txt='Flatmates Bill', border=1, align='C', ln=1)
        
        # Insert period label and value
        pdf.cell(w=100, h=40, txt='Period:', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)
        
        # Insert name and due amount of first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=1, ln=1)
        
        # Insert name and due amount of second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=1, ln=1)
        
        pdf.output(self.filename)
        
    
thebill = Bill(amount=120, period="March 2023")
john = Flatmate(name="john", days_in_house=20)
marry = Flatmate(name="marry", days_in_house=25)

print("John pays: ", john.pays(bill=thebill, flatmate2=marry))
print("Marry pays: ", marry.pays(bill=thebill, flatmate2=john))

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=thebill)



