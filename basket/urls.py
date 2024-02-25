from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<lesson_id>/', views.add_to_basket, name='add_to_basket'),
    path('adjust/<lesson_id>/', views.adjust_basket, name='adjust_basket'),
    path(
        'remove/<lesson_id>/', views.remove_from_basket,
        name='remove_from_basket'
    ),
]
