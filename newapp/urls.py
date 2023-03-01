from django.urls import path
from . import views

urlpatterns = [
    
    path('posts/<int:pk>/',views.getPosts),
    path('posts',views.getPosts),
    path('post-create',views.postCreate),
    path('post-updata/<int:pk>',views.postUpdata),
    path('post-delete/<int:pk>',views.postDelete),
]
