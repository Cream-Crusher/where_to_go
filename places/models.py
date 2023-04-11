from django.db import models
from django.urls import reverse


class PlaceQuerySet(models.QuerySet):

    def loading_db_queries(self):

        return self.prefetch_related('images')


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    low = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    objects = PlaceQuerySet.as_manager()

    def __str__(self):

        return self.title


class Image(models.Model):
    img = models.ImageField('Картинка', upload_to='media', blank=True, unique=True)

    post = models.ForeignKey(
        'Place',
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='Картинка, к месту')

    def __str__(self):

        return str(self.img)

    def get_absolute_url(self):

        return reverse('tag_title', args={'slug': self.slug})
