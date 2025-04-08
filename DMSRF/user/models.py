from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.


class User(models.Model):
    STATE_CHOICE = (
    ('Barisal', 'Barisal'),
    ('Chattogram', 'Chattogram'),
    ('Dhaka', 'Dhaka'),
    ('Khulna', 'Khulna'),
    ('Mymensingh', 'Mymensingh'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur'),
    ('Sylhet', 'Sylhet'),
)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user_name =  models.CharField(max_length=100)
    user_email =  models.EmailField(max_length=50)
    user_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    user_age = models.PositiveIntegerField()
    user_phone = models.CharField(max_length=15)
    user_state = models.CharField(choices=STATE_CHOICE, max_length=100)
    user_address = models.TextField()
    # user_profile_picture = models.ImageField(upload_to='profileimg', blank=True)
    # user_nid = models.FileField(upload_to= 'doc', blank= True)

    def __str__(self):
        return self.user_name
    
