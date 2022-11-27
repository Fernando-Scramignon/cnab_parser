from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import TransactionType
from .serializers import TransactionSerializer


class TransactionTypeView(ListAPIView):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionSerializer
