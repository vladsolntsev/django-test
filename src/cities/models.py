from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='description')
    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name