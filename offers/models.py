from django.db import models
from django.conf import settings

# Create your models here.

class Offer(models.Model):
    categories = [
        ('buy', 'купить',),
        ('sell', 'продать',)
    ]

    statuses = [
        ('active', 'активно',),
        ('closed', 'закрыто',)
    ]

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'
        ordering = ['id', 'title']

    title = models.CharField('название', max_length=150)
    description = models.CharField('описание', max_length=400, blank=True)
    category = models.CharField('категория', max_length=20, choices=categories, default='buy')
    status = models.CharField('статус', max_length=20, choices=statuses, default='active')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author', verbose_name='владелец')
    responders = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='откликнулись', related_name='responders', blank=True)
    selected_responder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='выбран', related_name='selected_responder', blank=True, null=True)
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)

    def __str__(self):
        return f'{self.title} | {self.author}'

class Photo(models.Model):
    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фотографии'

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    img = models.ImageField('фото', upload_to='offers/%Y/%m/')

    def __str__(self):
        return f'{self.img}'