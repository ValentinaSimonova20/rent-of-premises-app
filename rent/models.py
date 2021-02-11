from django.db import models
from django.contrib.auth.models import User


class Premises(models.Model):
    areaName = models.CharField(verbose_name='Название площади',
                                max_length=30)

    describe = models.TextField(verbose_name='Описание площади',
                                blank=True)

    area = models.FloatField(verbose_name='Площадь помещения',
                             blank=False)

    floor = models.IntegerField(verbose_name='Этаж', blank=False)

    price = models.FloatField(verbose_name="Цена/месяц в руб.")

    photo = models.ImageField(verbose_name='Изображения',
                              upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

    def __str__(self):
        return self.areaName


class Applications(models.Model):
    client = models.ForeignKey(User, verbose_name='Клиент', on_delete=models.PROTECT, null=False)

    premises = models.ForeignKey('Premises', verbose_name='Помещение', on_delete=models.PROTECT, null=False)

    additionalInfo = models.TextField(verbose_name='Дополнительная информация', blank=True)

    created_at = models.DateTimeField(verbose_name='Дата подачи заявки',
                                      auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['created_at']


