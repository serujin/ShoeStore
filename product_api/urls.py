from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_all_products, name='all_products'),
    # url(r'^product/$')
]