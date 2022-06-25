from django.urls import path
from . import views

app_name = 'tag'
urlpatterns = [
    path('', views.TagListView.as_view(), name='index'),
    path('<int:pk>/', views.TagDetailView.as_view(), name='detail'),
    path('new/', views.TagCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', views.TagUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.TagDeleteView.as_view(), name='delete'),
]
