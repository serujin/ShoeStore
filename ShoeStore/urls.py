"""ShoeStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import RedirectView
from client_manager import views as client_manager_views
from product_manager import views as product_manager_views
from email_manager import views as email_manager_views
from home import views as home_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/signin/')),
    url('signup/', client_manager_views.sign_up, name='sign_up'),
    url('signin/', client_manager_views.sign_in, name='sign_in'),
    url('logout/', client_manager_views.logout, name='logout'),
    url('home/', home_views.home, name='home'),
    url('buy/', product_manager_views.buy_cart, name='buy'),
    url('email/', email_manager_views.send_email, name='mail'),
    
]
