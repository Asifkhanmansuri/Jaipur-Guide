from django.urls import path
from .import views
urlpatterns = [
    path('home_page', views.home, name='home'),
    path('', views.home_page, name='home_page'),
    # path('login', views.login, name='login'),
    
   
]
