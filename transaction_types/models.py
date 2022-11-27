from django.db import models


class NatureChoices(models.Choices):
    cash_income = "Entrada"
    cash_outflow = "Saída"


class SignalChoices(models.Choices):
    plus = "+"
    minus = "-"


class TransactionType(models.Model):
    type = models.AutoField(primary_key=True, editable=False)
    description = models.CharField(max_length=50)
    nature = models.CharField(
        max_length=7,
        choices=NatureChoices.choices,
        default=NatureChoices.cash_income,
    )
    signal = models.CharField(
        max_length=1, choices=SignalChoices.choices, default=SignalChoices.plus
    )
