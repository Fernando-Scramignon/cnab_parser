from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

        extra_kwargs = {"id": {"read_only": True}}


class TransactionShopSerializer(serializers.Serializer):
    shop_name = serializers.CharField(max_length=19)
    total_value = serializers.DecimalField(max_digits=10, decimal_places=2)
