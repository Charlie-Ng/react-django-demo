from django.urls import path

from . import views

urlpatterns = [
    path('user-item/', views.userItem.as_view()),
]
