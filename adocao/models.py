from django.db import models


class Adocao(models.Model):
    valor = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    email = models.EmailField(null=False, blank=False, max_length=255)
    pet = models.ForeignKey(to="pet.Pet", null=False, on_delete=models.CASCADE)

