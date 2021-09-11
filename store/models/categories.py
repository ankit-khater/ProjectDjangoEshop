
from django.db import models

class Categories(models.Model):

    # property of Category class

    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Categories.objects.all()