from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductCreateView.as_view(), name='create_product'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]