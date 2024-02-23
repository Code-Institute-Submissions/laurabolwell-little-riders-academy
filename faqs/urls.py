from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_faqs, name='faqs'),
    path('add/', views.add_question, name='add_question'),
    path('edit/<int:question_id>/', views.edit_question, name='edit_question'),
]
