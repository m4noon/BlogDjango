from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all/', views.show_all_posts),
    path('<int:post_id>/', views.show_post)
]