from django.urls import path
from . import views

urlpatterns = [
    path('', views.leave_testimonial, name='leave_testimonial')
]
