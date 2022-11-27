from rest_framework import serializers
from .models import TransactionType


class TransactionSerializer(serializers.Serializer):
    class Meta:
        model = TransactionType
        fields = "__all__"
