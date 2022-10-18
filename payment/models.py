from django.db import models

class PaymentDetails(models.Model):
    payment_id = models.CharField(max_length=80, null=True)
    transaction_id = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.payment_id