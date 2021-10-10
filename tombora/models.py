from django.db import models


# Create your models here.

class Member(models.Model):
    registered_on = models.TimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    user_email = models.EmailField()
    password = models.CharField(max_length=100)
    retype_password = models.CharField(max_length=100)
    agreement = models.BooleanField(default=False)



    def __str__(self):
        return self.username

    memberAuth_objects = models.Manager()
