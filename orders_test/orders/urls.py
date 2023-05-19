from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.index, name='orders_list'),
    path('order_create/', views.order_create, name='order_create'),
    path(
        'order_detail/<int:order_id>/',
        views.order_detail,
        name='order_detail'
    ),
    path(
        'order_detail/<int:order_id>/docs/<str:path>',
        views.download,
        name='fdownload'
    ),
    path(
        'order_completed/<int:order_id>/',
        views.order_completed,
        name='order_completed'
    ),
    path(
        'order_rejected/<int:order_id>/',
        views.order_rejected,
        name='order_rejected'
    ),
    path('docs/<str:path>/', views.download, name='download'),
    path('orders_statistic/', views.orders_statistic, name='orders_statistic')
]
