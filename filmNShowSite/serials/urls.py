from django.urls import path
from . import views

urlpatterns = [
    path('', views.SerialsView.as_view()),
    path('add-serial/', views.SerialCreateView.as_view()),
]