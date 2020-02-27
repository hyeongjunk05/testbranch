from django.db import models


class Account(models.Model):

    social         = models.ForeignKey('SocialLogin', on_delete = models.CASCADE)
    username       = models.CharField(max_length = 50) 
    email          = models.EmailField(max_length = 50)
    password       = models.CharField(max_length = 50)
    created_at     = models.DateTimeField(auto_now_add = True)
    updated_at     = models.DateTimeField(auto_now = True)
    profile        = models.CharField(max_length = 50)
    phone          = models.IntegerField()
    refund_account = models.IntegerField()
    refund_bank    = models.CharField(max_length = 45)
    account_holder = models.CharField(max_length = 45)
    facebook       = models.CharField(max_length = 45)
    facebook_key   = models.CharField(max_length = 200)
    naver          = models.CharField(max_length = 45)
    naver_key      = models.CharField(max_length = 200)
    kakao          = models.CharField(max_length = 45)
    kakao_key      = models.CharField(max_length = 200)



    class Meta:
        db_table = 'accounts'

class SocialLogin(models.Model):

    name = CharField(max_length = 45)

    class Meta:
        db_table = 'social_login'