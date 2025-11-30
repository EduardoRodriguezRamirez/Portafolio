from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2),
    path('projects/<int:id>', views.index),
    path('about/', views.about),
    path('hello/<int:id>', views.hello),
    path('tasks/<int:id>', views.tasks),
]