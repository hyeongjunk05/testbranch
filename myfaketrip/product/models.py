from django.db import models


class Product(models.Model):

    main_theme     = models.ForeignKey('MainTheme', on_delete = models.CASCADE)
    sub_theme      = models.ForeignKey('SubTheme', on_delete = models.CASCADE)
    cities         = models.ForeignKey('Cities', on_delete = models.CASCADE)
    guides         = models.ForeignKey('Guides', on_delete = models.CASCADE)
    group          = models.CharField(max_length = 50)
    duration       = models.CharField(max_length = 50)
    language       = models.CharField(max_length = 50)
    transportation = models.CharField(max_length = 50)
    description    = models.CharField(max_length = 5000)
    amenities      = models.CharField(max_length = 50)
    refund_policy  = models.CharField(max_length = 5000)
    meeting_time   = models.CharField(max_length = 30)
    address        = models.CharField(max_length = 50)
    latitude       = models.DecimalField(max_digits = 3, decimal_places = 10)
    longitude      = models.DecimalField(max_digits = 3, decimal_places = 10)
    guide_info     = models.CharField(max_length = 50)

    class Meta:
        db_table = 'product'


class MainTheme(models.Model):
    
    main_theme_name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'main_theme'

class SubTheme(models.Model):

    theme_names   = models.ForeignKey('ThemeName', on_delete = models.CASCADE)
    tour_products = models.ForeignKey(Product, on_delete = models.CASCADE)
    name          = models.CharField(max_length = 45)


class Images(models.Model):
    
    tour_products = models.ForeignKey(Product, on_delete = models.CASCADE)
    product_img   = models.CharField(max_length = 2000)

    class Meta:
        db_table = 'images'


class Prices(models.Model):

    tour_products    = models.ForeignKey(Product, on_delete = models.CASCADE)
    origin_price     = models.IntegerField()
    discounted_price = models.IntegerField()
    discount_percent = models.IntegerField()
    date             = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'prices'


class Courses(models.Model):

    tour_products = models.ForeignKey(Product, on_delete = models.CASCADE)
    intro         = models.CharField(max_length = 45)
    img           = models.CharField(max_length = 45)

    class Meta:
        db_table = 'courses'


class Guides(models.Model):

    name    = models.CharField(max_length = 45)
    profile = models.CharField(max_length = 45)
    img     = models.CharField(max_length = 45)

    class Meta:
        db_table = 'guides'


class Cities(models.Model):

    name      = models.CharField(max_length = 45)
    countries = models.ForeignKey('Countries', on_delete = models.CASCADE)

    class Meta:
        db_table = 'countries'


class Countries(models.Model):

    country_name   = models.CharField(max_length = 45)
    country_number = models.IntegerField()

    class Meta:
        db_table = 'countries'


class Reviews(models.Model):

    tour_products  = models.ForeignKey('Product', on_delete = models.CASCADE)
    accounts       = models.ForeignKey('Accounts', on_delete = models.CASCADE)
    age            = models.ForeignKey('Age', on_delete = models.CASCADE)
    travel_objects = models.ForeignKey('TravelObjects', on_delete = models.CASCADE)
    grade          = models.DecimalField(max_digits = 2, decimal_places = 1)
    review         = models.CharField(max_length = 2000)
    created_at     = models.DateTimeField(auto_now_add = True)
    updated_at     = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'review'