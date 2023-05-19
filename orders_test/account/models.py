from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
    )
    is_customer = models.BooleanField(
        default=True,
        verbose_name='Заказчик',
    )
    is_manage = models.BooleanField(
        default=False,
        verbose_name='Исполнитель',
    )

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.username
