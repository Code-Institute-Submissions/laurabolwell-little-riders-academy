from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_lessons, name='lessons'),
    path('<lesson_id>', views.lesson_details, name='lesson_details')
]
