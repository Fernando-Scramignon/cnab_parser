from django.db import models
from uuid import uuid4
from transaction_types.models import TransactionType


class Transaction(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    date = models.DateField(max_length=8)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    shop_owner = models.CharField(max_length=14)
    shop_name = models.CharField(max_length=19)

    type = models.ForeignKey(
        TransactionType, on_delete=models.CASCADE, related_name="transactions"
    )
