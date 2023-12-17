from rest_framework import viewsets, mixins

from api.models import Transactions
from api.serializers import TransactionSerializer


class TransactionViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
