# Django Models Template - customize for your project

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    status = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['phone']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    total_cents = models.BigIntegerField()
    status = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'orders'
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['status']),
        ]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_id = models.BigIntegerField()
    quantity = models.IntegerField(default=1)
    price_cents = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_items'
        indexes = [
            models.Index(fields=['order']),
        ]
