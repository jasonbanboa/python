from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        name = input("Name: ")
        self.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", x=0, y=60)
        self.set_font("Helvetica", size=50)
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        self.set_font("Helvetica", size=25)
        self.set_text_color(255,255,255)
        self.cell(-183, 240, f"{name} took CS50", align="C")


def main():
    pdf = PDF()
    pdf.add_page()
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

