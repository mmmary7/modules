# a = open('text2.txt', 'w', encoding='utf-8')
from fpdf import FPDF
pdf_file = FPDF('P', 'cm', (10, 15))
pdf_file.add_page()
pdf_file.set_font('arial', size=16)
pdf_file.set_text_color(25, 30, 200)
pdf_file.set_fill_color(0, 255, 0)
pdf_file.set_draw_color(255, 0, 0)
pdf_file.cell(8, 5, txt='Welcome!', align='C', border=1, fill=True)
pdf_file.image('zmeika.jpg', h=0, w=5, x=2.5, y=8)

pdf_file.output('my_pdf.pdf')


