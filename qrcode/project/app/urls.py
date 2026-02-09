from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('qr-generator/',views.qr_generator,name='qr_generator'),
]