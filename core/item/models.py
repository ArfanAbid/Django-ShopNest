from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    
    class Meta:
        ordering = ('name',)   #The tuple ('name',) indicates that the ordering should be based on the name field. If you want to specify descending order, you can use ('-name',).
        verbose_name_plural= 'Categories' # The verbose_name_plural attribute allows you to specify a human-readable name for the model when it appears in plural form, which can be useful for better presentation in the admin interface.
        
    def __str__(self):
        return self.name
    

class Item(models.Model):
    category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)    
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='item_image',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User,related_name='item',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name