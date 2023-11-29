import os
import webbrowser 
from fpdf import FPDF

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
        
        # Getting the current working directory
        current_directory = os.path.dirname(os.path.realpath(__file__))

        # Adjusting the path to the image file
        image_path = os.path.join(current_directory, "img", "house.png")
        
        # Add icon
        pdf.image(image_path, w=30, h=30)
        
        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=88, txt='Flatmates Bill', border=0, align='C', ln=1)
        
        # Insert period label and value
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        
        # Insert name and due amount of first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)
        
        # Insert name and due amount of second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)
        
        # Create a directory if it doesn't exist
        output_directory = os.path.join(current_directory, 'bills')
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Define the complete path for the output file
        output_path = os.path.join(output_directory, self.filename)
        
        pdf.output(output_path)
        webbrowser.open(output_path)