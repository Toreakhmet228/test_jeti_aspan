
from django.urls import path,include
from .views import  *
urlpatterns = [

    path('catalog/', ProductListView.as_view(), name='product_list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/', ProductSearchView.as_view(), name='product_search'),
    path('catalog/update/stocks', UpdateStocksView.as_view(), name='update_stock'),
]
