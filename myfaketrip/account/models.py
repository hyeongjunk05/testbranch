from django.db import models

# Create your models here.

class Account(models.Model):

    user_name = models.CharField(max_length = 50) 
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)
    created_at = models.DateTimeField(max_length = 20)
    updated_at = models.DateTimeField(max_length = 20)

    class Meta:
        db_table = 'account'