from django.urls import path
from . import views

urlpatterns = [
    
    path('post/<int:pk>',views.retrievePosts.as_view()),
    path('posts',views.listCreatePost.as_view()),
    path('<int:pk>/update',views.updatePost.as_view()),
    path('<int:pk>/delete',views.deletePost.as_view()),
]
