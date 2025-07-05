from django.urls import path
from .views import index,about,services, faq,contact
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'), 
    path('faq/', faq, name='faq'),
    path('contact/', views.contact_view, name='contact'),

]
