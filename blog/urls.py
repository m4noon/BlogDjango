from django.urls import path
from . import views



app_name = 'post'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('new/', views.PostCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]
