from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('orders.urls', namespace='orders')),
    path('account/', include('account.urls', namespace='account')),
    path('admin/', admin.site.urls),
]
