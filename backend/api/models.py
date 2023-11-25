from django.db import models


CHOICES = (
    ('suspect', 'Сомнительный'),
    ('approved', 'Одобренный'),
)

class Transactions(models.Model):
    step = models.PositiveIntegerField()
    customer = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=255)
    zipcodeOri = models.CharField(max_length=255)
    merchant = models.PositiveIntegerField()
    zipMerchant = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    fraud = models.CharField(
        verbose_name='Статус',
        choices=CHOICES,
        default=CHOICES[0],
        max_length=20
    )
    is_denied = models.BooleanField(default=False)

    class Meta:
        verbose_name = '"Транзакция"'
        verbose_name_plural = 'Транзакции'

    def __str__(self) -> str:
        return f'Транзакция {self.id} от {self.customer}'
