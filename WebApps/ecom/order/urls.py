from django.urls import path
from . import views
urlpatterns = [
    path('', views.order_list),
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/edit/<int:order_id>', views.order_edit, name='order_edit'),
    path('orders/delete/<int:order_id>', views.order_delete, name='order_delete'),
]