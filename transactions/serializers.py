from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Transaction

from transaction_types.serializers import TransactionTypeSerializer


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

        extra_kwargs = {"id": {"read_only": True}}


class TransactionDetailSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

    type = TransactionTypeSerializer()


class TransactionShopSerializer(serializers.Serializer):
    shop_name = serializers.CharField(max_length=19)
    income = serializers.DecimalField(10, 2)
    outflow = serializers.DecimalField(10, 2)
    balance = serializers.DecimalField(10, 2)
    operations = TransactionSerializer(many=True)
