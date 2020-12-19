from django.db import models

# Create your models here.
class sfrom(models.Model):
    na=models.CharField(max_length=10,default='')
    em=models.CharField(max_length=10,default='')
    def __str__(self):
        return self.na