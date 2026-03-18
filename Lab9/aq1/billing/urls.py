from django.urls import path

from .views import bill_view, order_view

urlpatterns = [
    path('', order_view, name='order'),
    path('bill/', bill_view, name='bill'),
]
