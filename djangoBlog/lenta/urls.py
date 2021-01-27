from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_lenta),
    path('like-add/', views.add_like),
    path('comment-add/', views.add_comment),
    path('add-post/', views.add_post),
    path('delete-post/<int:id>/', views.delete_post)
]
