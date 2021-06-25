from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.buy_cart, name='buy'),
]