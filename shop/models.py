from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


class Goods(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    image = models.ImageField()
    price = models.IntegerField(default=0)
    is_offer = models.BooleanField(default=False)
    date_pub = models.DateField(default=timezone.now())
    class Meta:
        ordering = ['date_pub']
    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'pk': self.id})