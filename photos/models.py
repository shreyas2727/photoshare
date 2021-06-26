from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    description = models.TextField(null=False,blank=False)
    image = models.ImageField(upload_to='photos/',null=False,blank=False)

    def __str__(self):
        return self.description