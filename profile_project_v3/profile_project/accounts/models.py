from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    bio = models.TextField()
    avatar = models.ImageField(upload_to='/images')

    def __str__(self):
        return self.first_name
