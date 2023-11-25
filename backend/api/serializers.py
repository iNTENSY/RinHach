from rest_framework import serializers

from api.models import Transactions


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        exclude = ('id', 'is_denied')
