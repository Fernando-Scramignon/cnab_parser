from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import TransactionType


from .serializers import TransactionTypeSerializer


class TransactionTypeView(ListAPIView):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer


class TransactionTypeDetailView(RetrieveAPIView):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
