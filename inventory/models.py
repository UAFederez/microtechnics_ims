from django.db import models
import uuid

# Create your models here.

class CategoryOptions():
    CATEGORY_USER_ADDED = 0
    CATEGORY_HARD_CODED = 1
    CATEGORY_GENERAL    = 2

    CATEGORY_CHOICES = (
        (CATEGORY_USER_ADDED, 'User-Added'),
        (CATEGORY_HARD_CODED, 'Hard-Coded'),
        (CATEGORY_GENERAL,    'General'),
    )

class Category(models.Model):
    cat_id = models.CharField(max_length  = 10,
                              primary_key = True,
                              unique      = True,
                              default     = uuid.uuid4)
    name   = models.CharField(max_length = 20)
    option = models.IntegerField(choices = CategoryOptions.CATEGORY_CHOICES)

class Item(models.Model):
    itemCode    = models.CharField(max_length  = 10, 
                                   primary_key = True,
                                   unique      = True,
                                   default     = uuid.uuid4)
    name        = models.CharField(max_length = 20)
    price       = models.DecimalField(max_digits     = 16, 
                                      decimal_places = 2)
    quantity    = models.IntegerField(default = 0)
    category    = models.ForeignKey(Category,
                                    on_delete = models.SET_NULL,
                                    null      = True)
    maxQuantity = models.IntegerField(default = 0)
    description = models.CharField(max_length = 50)
