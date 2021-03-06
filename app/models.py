from django.db import models
from django.utils.timezone import datetime
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    phone=models.IntegerField()
    info=models.CharField(max_length=30)
    gender=models.CharField(max_length=10,choices=(
        ('male','M'),
        ('female','F')
    ))
    image=models.ImageField(upload_to='images/' , blank=True)
    date_added=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name
class Meta:
    ordering=['-id']      