from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('form/',form,name='form'),
    path('about/',about,name='about'),
    path('delete/<int:id>/',delete_data,name='delete_data'),
    path('search/',search_data,name='search'),
    path('update/<int:id>',update_data,name='update_data'),
]
