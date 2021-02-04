from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('add-post/', views.PostCreateView.as_view()),
    path('edit-post/<int:pk>/', views.PostEditView.as_view()),
    path('delete-post/<int:pk>/', views.PostDeleteView.as_view()),
    path('posts/<int:pk>/', views.add_comment),
    path('like-add/', views.add_like),
]
