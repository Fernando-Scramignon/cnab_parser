from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Transaction
from .serializers import (
    TransactionSerializer,
    TransactionDetailSerializer,
    TransactionShopSerializer,
)

from django.db.models import Sum


class TransactionView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailView(RetrieveUpdateDestroyAPIView):

    serializer_map = {
        "DELETE": TransactionDetailSerializer,
        "GET": TransactionDetailSerializer,
        "PATCH": TransactionSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_map.get(self.request.method, self.serializer_class)

    queryset = Transaction.objects.all()
    serializer_class = TransactionDetailSerializer


# returns the operations and balance of each shop
class TransactionAggregationView(APIView):
    # this is for the documentation (drf-spectacular)
    queryset = Transaction.objects
    serializer_class = TransactionShopSerializer

    transactions = Transaction.objects.all()

    shops = ()
    output = []

    for transaction in transactions:
        if transaction.shop_name in shops:
            continue
        total_amount = 0
        shops = (*shops, transaction.shop_name)

        transaction_dict = {}
        transaction_dict["shop_name"] = transaction.shop_name

        operations = transactions.filter(shop_name=transaction.shop_name)

        operations_cash_income = operations.filter(type__nature="Entrada").aggregate(
            Sum("value")
        )["value__sum"]

        if not operations_cash_income:
            operations_cash_income = 0

        operations_cash_outflow = operations.filter(type__nature="Saída").aggregate(
            Sum("value")
        )["value__sum"]

        if not operations_cash_outflow:
            operations_cash_outflow = 0

        transaction_dict["income"] = operations_cash_income
        transaction_dict["outflow"] = operations_cash_outflow
        transaction_dict["balance"] = operations_cash_income - operations_cash_outflow

        operations_serializer = TransactionDetailSerializer(operations, many=True)
        transaction_dict["operations"] = operations_serializer.data

        output.append(transaction_dict)

    def get(self, request):
        return Response(self.output)
