from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from users import views as user_views
urlpatterns = [ 
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('register/', user_views.register, name='register'),
    path('about/', views.about, name='about'),
    
]    