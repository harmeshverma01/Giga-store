from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="Product")
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cover_image = models.ImageField()
    status = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return self .name

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ProductImages")
    Image = models.ImageField()

    def __str__(self):
        return str(self.product)       