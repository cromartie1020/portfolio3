from django.urls import path
from . import views

urlpatterns=[
    path('',views.ContactFormView,name='contact'),
    path('list/',views.ContactList,name='contact_list'),
]