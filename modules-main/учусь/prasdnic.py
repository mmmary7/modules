from fpdf import *

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.image('b_day.jpg', h=297, w=210, x=0, y=0)
