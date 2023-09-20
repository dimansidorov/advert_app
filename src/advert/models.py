from django.db import models 
from django.core.validators import MinValueValidator 


class Category(models.Model): 
    name = models.CharField(max_length=50, null=False) 
    
    def __str__(self) -> str: 
        return self.name 
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    
class City(models.Model): 
    name = models.CharField(max_length=50, null=False) 
    
    def __str__(self) -> str: 
        return self.name 
    
    class Meta:
        verbose_name_plural = 'Cities'
    
    
class Advert(models.Model): 
    title = models.CharField(max_length=50, null=False) 
    description = models.TextField(blank=False, null=False) 
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=False) 
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False) 
    views = models.BigIntegerField(default=0, validators=[MinValueValidator(0)]) 
    
    def __str__(self) -> str: 
        return self.title