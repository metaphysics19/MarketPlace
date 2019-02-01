from django.urls import path
from .views import PostListView, ProductsCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('product/<int:pk>/', views.products_detail, name='products_detail'),  # εμφανίζει το product_detail.html
    path('product/new/', ProductsCreateView.as_view(), name='product-create')

]
