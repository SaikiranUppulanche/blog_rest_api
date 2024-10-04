from django.urls import path
from .views import RegisterView, BlogPostListCreateView, BlogPostDetailView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('blogs/', BlogPostListCreateView.as_view(), name='blogs-list-create'),
    path('blogs/<int:pk>/', BlogPostDetailView.as_view(), name='blog-detail'),
]
