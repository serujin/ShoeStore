from django.shortcuts import render
import xlsxwriter
import pandas
from io import BytesIO
from decimal import Decimal

def generate_excel_from_values(request):
    products = request.POST['products[]']
    prices = request.POST['prices[]']
    buffer = BytesIO()
    total = 0
    for price in prices:
        total += round(float(price[:-1]), 2)
    total_col = ['' for n in range(len(product_prices))]
    total_col[0] = str(round(total, 2)) + '€'
    data = pandas.DataFrame({'Products': products, 'Prices': prices, 'Total': total_col})
    writer = pandas.ExcelWriter(buffer, engine='xlsxwriter')
    data.to_excel(writer, sheet_name='Products', index=False)
    writer.save()
    return buffer
