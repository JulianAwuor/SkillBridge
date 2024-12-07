from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = [
        ('Mentor', 'Mentor'),
        ('Learner', 'Learner'),
    ]

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    about = models.TextField()
    experience = models.TextField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    specialty = models.CharField(max_length=50, blank=True, null=True)
    interest =  models.CharField(max_length=50, blank=True, null=True )
    phone =models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


