from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserStatus(models.Model):
    status = (
        ('Normal', u'Normal'),
        ('VIP', u'VIP')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_status', verbose_name='User')
    status = models.CharField(choices=status, default='Normal', max_length=100, verbose_name='Account status')
    valid_date = models.DateTimeField(verbose_name='Valid date', null=True, blank=True, )
    level = models.IntegerField(default=0, verbose_name='VIP level')
    exp = models.IntegerField(default=0, verbose_name='user exp')
    bookshelf_coin = models.FloatField(default=0.0, verbose_name='Bookshelf coin')
    month_ticket = models.IntegerField(default=0, verbose_name='Monthly ticket')


class VipCombo(models.Model):
    combo_name = models.CharField(max_length=200, verbose_name='Vip combo', unique=True)
    description = models.TextField(verbose_name='Combo description', max_length=10000)
    price = models.FloatField(default=0.0, verbose_name='price')
    discount = models.DecimalField(decimal_places=2, max_digits=10, default=0.0, )
    length = models.IntegerField(default=0, verbose_name='Length')


class Payment(models.Model):
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "Success"),
        ("TRADE_CLOSED", "Over time"),
        ("WAIT_BUYER_PAY", "Trade create"),
        ("TRADE_FINISHED", "Trade close"),
        ("paying", "Wait for payment"),
    )

    user = models.ForeignKey(User, verbose_name='User', related_name='order', on_delete=models.CASCADE)
    goods = models.ForeignKey(VipCombo, verbose_name='Combo', related_name='order_goods', on_delete=models.CASCADE)
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="order number")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"trade number")
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="order status")
    order_mount = models.FloatField(default=0.0, verbose_name="order amount")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="payment time")

    # user information

    add_time = models.DateTimeField(auto_now_add=True, verbose_name="Added time")
