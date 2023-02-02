from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 10, 65, 190, 190)
        self.set_font("helvetica", "", 30)
        self.cell(0, 40, "CS50 Shirtificate", align="C")
        self.ln(20)

    def footer(self):
        self.set_font("helvetica", "",  20)
        self.set_text_color(255, 255,255)
        self.cell(0, 170, f"{Name} took CS50", align="C")

Name = input("Name: ")

pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")