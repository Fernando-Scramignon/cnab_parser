from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)

from .models import Transaction
from .serializers import TransactionSerializer, TransactionShopSerializer

from django.db.models import Sum
import ipdb


class TransactionView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionAggregationView(ListAPIView):
    queryset = (
        Transaction.objects.values("shop_name")
        .order_by("shop_name")
        .annotate(total_value=Sum("value"))
    )
    serializer_class = TransactionShopSerializer
