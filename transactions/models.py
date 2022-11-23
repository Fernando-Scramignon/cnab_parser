from django.db import models
from uuid import uuid4


class Transaction(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    type = models.CharField(max_length=1)
    date = models.DateField(max_length=8)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    shop_owner = models.CharField(max_length=14)
    shop_name = models.CharField(max_length=19)
