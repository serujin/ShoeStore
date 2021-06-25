from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/signin/')),
    url('signup/', views.sign_up, name='sign_up'),
    url('signin/', views.sign_in, name='sign_in'),
    url('logout/', views.logout, name='logout'),
]