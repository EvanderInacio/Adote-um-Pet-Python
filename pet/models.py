from django.db import models


class Pet(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=255)
    historia = models.TextField(blank=False, null=False)
    foto = models.TextField(blank=False, null=False)

