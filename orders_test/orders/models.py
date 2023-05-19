from django.db import models

from account.models import User


class Order(models.Model):
    """Модель заказа."""

    class ChoicesStatus(models.TextChoices):
        NEW_ORD = ('new', 'Новый')
        COMPLETED_ORD = ('completed', 'Выполнен')
        REJECTED_ORD = ('rejected', 'Отклонен')

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Заказчик',
    )
    text = models.TextField()
    file = models.FileField(
        upload_to='docs/',
        verbose_name='Документ',
    )
    status = models.CharField(
        max_length=15,
        choices=ChoicesStatus.choices,
        default=ChoicesStatus.NEW_ORD,
        verbose_name='Статус заказа'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-id']

    def __str__(self):
        return self.text[:30]
