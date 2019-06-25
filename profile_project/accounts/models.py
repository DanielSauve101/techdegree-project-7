from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    bio = models.TextField()
    avatar = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.first_name
