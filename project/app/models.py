from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews/')
    review_text = models.TextField()

    def __str__(self):
        return self.product_name

# Create your models here.
