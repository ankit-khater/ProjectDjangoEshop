from django.db import models
from .categories import Categories

class Product(models.Model):

    # property of products

    name=models.CharField(max_length=50)

    price=models.IntegerField(default=0)

    category=models.ForeignKey(Categories,on_delete=models.CASCADE,default=1)

    description=models.CharField(max_length=200,default='',null=True,blank=True)

    image=models.ImageField(upload_to='uploads/products/')


    #method which return all objects of Product class
    @staticmethod
    def get_all_product():

        return Product.objects.all()

    @staticmethod
    def get_all_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_product()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)