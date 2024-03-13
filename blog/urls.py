from django.urls import path

from blog.views import BlogpostCreateView, BlogpostListView, BlogpostDetailView, BlogpostUpdateView, BlogpostDeleteView

app_name = 'blog'


urlpatterns = [
     path('', BlogpostListView.as_view(), name='blog_list'),
     path('view/<int:pk>/', BlogpostDetailView.as_view(), name='view'),
     path('create/', BlogpostCreateView.as_view(), name='create'),
     path('update/<int:pk>/', BlogpostUpdateView.as_view(), name='update'),
     path('delete/<int:pk>/', BlogpostDeleteView.as_view(), name='delete'),
]
