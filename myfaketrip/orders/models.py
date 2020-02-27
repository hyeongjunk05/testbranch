from django.db import models


class Orders(models.Model):

    order         = models.ForeignKey('MainTheme', on_delete = models.CASCADE)
    account       = models.ForeignKey('Account', on_delete = models.CASCADE)
    phone         = models.ForeignKey('Phone', on_delete=models.CASCADE)
    payment       = models.ForeignKey('Payment', on_delete = models.CASCADE)
    age           = models.ForeignKey('Age', on_delete = models.CASCADE)
    travel_object = models.ForeignKey('TravelObject', on_delete = models.CASCADE)
    updated_at    = models.DateTimeField(auto_now = True)
    created_at    = models.DateTimeField(auto_now_add = True)
    request       = models.CharField(max_length = 500)
    countries     = models.ForeignKey('Countries', on_delete = models.CASCADE)

    class Meta:
        db_table = 'orders'


class OrderNumbers(models.Model):

    number = models.CharField(max_length = 45)

    class Meta:
        db_table = 'order_numbers'


class Payments(models.Model):

    payment = models.CharField(max_length = 45)

    class Meta:
        db_table = 'payment'


class Age(models.Model):

    age = models.CharField(max_length = 10)

    class Meta:
        db_table = 'age'


class TravelObjects(models.Model):

    sub_title = models.CharField(max_length = 45)

    class Meta:
        db_table = 'travelobjects'