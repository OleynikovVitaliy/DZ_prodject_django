from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ProductView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'shop'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ProductView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view, name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]