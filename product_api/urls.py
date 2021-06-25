from django.conf.urls import url
from . import views

urlpatterns = [
    url('all/', views.get_all_products, name='all_products'),
    url(r'^$', views.get_all_products, name='all_products'),
    url(r'^name/(?P<name>\w+)$', views.get_product_by_name, name='product_name_filter'),
    url(r'^pk/(?P<pk>\d+)$', views.get_product_by_pk, name='product_pk_filter'),
    url(r'^price/(?P<price>\d+)$', views.get_product_by_price, name='product_price_filter'),
    url(r'^price/(?P<price>\d+\.\d{1})$', views.get_product_by_price, name='product_price_filter'),
    url(r'^price/(?P<price>\d+\.\d{2})$', views.get_product_by_price, name='product_price_filter'),
    url(r'^price/(?P<price>\d+\,\d{1})$', views.get_product_by_price, name='product_price_filter'),
    url(r'^price/(?P<price>\d+\,\d{2})$', views.get_product_by_price, name='product_price_filter')
]