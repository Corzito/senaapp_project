from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('', views.home, name='home'),
    path('aprendices/', views.aprendices, name='aprendices'),
]