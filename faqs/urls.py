from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_faqs, name='faqs'),
    path('add/', views.add_question, name='add_question'),
]
