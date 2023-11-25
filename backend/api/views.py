from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from api.models import Transactions
from api.serializers import TransactionSerializer


class TransactionViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    @action(methods=['post'], detail=True, url_path='')
    def approved(self, *args, **kwargs):
        pass