from django.contrib import admin
from django.conf.urls import handler400, url, include

urlpatterns = [
    url(r'^', include('client_manager.urls')),
    url('home/', include('home.urls')),
    url('transaction/', include('order_manager.urls')),
    url('email/', include('email_manager.urls')),  
    url('api/', include('product_api.urls')), 
    url('admin/', admin.site.urls),
]