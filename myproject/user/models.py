from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class Post(models.Model):
    user = models.CharField(max_length=20)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

