import os

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from account.models import Profile, User
from orders.forms import OrderForm
from orders.models import Order
from orders_test import settings


@login_required
def index(request):
    """Список заказов."""
    template = 'orders/index.html'
    user = request.user
    if user.profile.is_manage:
        orders = Order.objects.all()
    else:
        orders = user.orders.all()

    context = {
        'orders': orders,
    }
    return render(request, template, context)


@login_required
def order_create(request):
    """Создание заказа."""
    template = 'orders/order_create.html'
    if not request.user.profile.is_customer:
        return redirect('orders:orders_list')
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('orders:orders_list')
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, template, context)


@login_required
def order_detail(request, order_id):
    """Просмотр заказа."""
    template = 'orders/order_detail.html'
    order = get_object_or_404(Order, pk=order_id)
    context = {'order': order}
    return render(request, template, context)


@login_required
def order_completed(request, order_id):
    """Выполнить заказ."""
    order = get_object_or_404(Order, pk=order_id)
    order.status = Order.ChoicesStatus.COMPLETED_ORD
    order.save()
    return redirect('orders:orders_list')


@login_required
def order_rejected(request, order_id):
    """Отклонить заказ."""
    order = get_object_or_404(Order, pk=order_id)
    order.status = Order.ChoicesStatus.REJECTED_ORD
    order.save()
    return redirect('orders:orders_list')


@login_required
def download(request, order_id=None, path=''):
    """Скачать документ приложенный к заказу."""
    file_path = os.path.join(settings.MEDIA_ROOT, 'docs/' + path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/vnd.ms-excel"
            )
            response['Content-Disposition'] = (
                    'inline; filename=' + os.path.basename(file_path)
            )
            return response
    raise Http404


@login_required
def orders_statistic(request):
    """Статистика по заказам."""
    template = 'orders/statistic.html'
    orders_count = Order.objects.count()
    status_count = Order.objects.values('status').annotate(
        total=Count('status')
    ).order_by()

    context = {
        'orders_count': orders_count,
        'status_count': status_count
    }
    return render(request, template, context)
