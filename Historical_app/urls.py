from django.urls import path
from .import views
urlpatterns = [
     path('historical', views.historical, name="historical"),
     path('Place_details/<int:pk>', views.place_details, name='place_details')
]
