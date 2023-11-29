from flat import Bill, Flatmate
from report import PdfReport
        
amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period (December 2020): ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period: "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period: "))
    
thebill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(thebill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(thebill, flatmate1))

pdf_report = PdfReport(filename=f"{thebill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=thebill)