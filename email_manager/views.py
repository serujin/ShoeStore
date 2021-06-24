from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from xlsx_manager import views as xlsx_views

def send_email(request):
    email = EmailMessage(
        subject = 'Pedido de tienda online',
        body = 'Pedido realizado por ' + request.user.username + ', se adjunta un fichero excel con los detalles del pedido:',
        from_email = 'noreply@gmail.com',
        to = ['sergio.munoz.lillo@gmail.com', 'zapatos.bernini.onlineshop@gmail.com']
    )
    products = ['Patata', 'Chorizo', 'Limón']
    prices = ['20.20€', '10.99€', '5.99€']
    email.attach('shoes_order.xlsx', xlsx_views.generate_excel_from_values(products, prices).getvalue() , 'application/vnd.ms-excel')
    email.send()
    return redirect('home')