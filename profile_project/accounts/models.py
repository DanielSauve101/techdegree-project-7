from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    bio = models.TextField()
    avatar = models.ImageField(default='images/default.jpg', upload_to='images/')

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('accounts:view_profile', kwargs={'pk': self.user.pk})
