from django.db import models

# Create your models here.


class Dolist(models.Model):
    work = models.CharField(max_length=1000)

    def __str__(self):
        return self.work
