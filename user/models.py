from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    This Model will store user details.
    """
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                  "allowed."),
    )
    GENDER_CHOICES = (
        ('m', "Male"),
        ('f', "Female"),
        ('o', "Other")
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    profile_image = models.ImageField(upload_to="user_images/", default='user_images/default.jpg')
    phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True)

    class Meta:
        ordering = ['id']
