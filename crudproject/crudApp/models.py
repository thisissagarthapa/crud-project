from django.db import models
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()
    isDelete=models.BooleanField(default=False)
    