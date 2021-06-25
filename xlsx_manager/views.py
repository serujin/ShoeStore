from django.shortcuts import render
import xlsxwriter
import pandas
from io import BytesIO
from decimal import Decimal

def generate_excel_from_values(request):
    products = request.session['products']
    quantities = request.session['quantities']
    prices = request.session['prices']
    total = request.session['total']
    buffer = BytesIO()
    total_col = ['' for n in range(len(products))]
    total_col[0] = total
    data = pandas.DataFrame({'Products': products, 'Units': quantities,'Prices': prices, 'Total': total_col})
    writer = pandas.ExcelWriter(buffer, engine='xlsxwriter')
    data.to_excel(writer, sheet_name='Products', index=False)
    workbook = writer.book
    worksheet = writer.sheets['Products']
    center = workbook.add_format({'align': 'center'})
    worksheet.set_column('A:A', 30)
    worksheet.set_column('B:D', 15, center)
    writer.save()
    return buffer
