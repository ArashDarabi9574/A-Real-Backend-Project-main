from django.db import models


class State(models.Model):
    class Meta:
        verbose_name = "استان"
        verbose_name_plural = "استان ها"

    name = models.CharField(max_length=150, verbose_name='عنوان')
    slug = models.SlugField(unique=True, verbose_name='اسلاگ')

    def __str__(self):
        return self.name
