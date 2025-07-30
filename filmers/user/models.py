from django.db import models
from django.contrib.auth.models import User

class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    

class SuperUser(BaseUser):
    def __str__(self):
        return self.user.username
    
class RegularUser(BaseUser):

    def __str__(self):
        return self.user.username
