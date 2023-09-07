from django.core.validators import RegexValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel
from category.models import Category
from user.models import User
from django.utils.translation import gettext_lazy as _


class Image(TimeStampedModel):
    """
    This Model will store image details.
    """
    image = models.ImageField(upload_to='store_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')

    class Meta:
        ordering = ['id']


class Store(TimeStampedModel):
    """
    This Model will register Store details.
    """
    STATUS = (
        ('Active', "Active"),
        ('Inactive', "Inactive")
    )
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                  "allowed."),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    cover_image = models.ImageField(upload_to='cover_images/',
                                    default='cover_images/default_shop.jpg')
    address = models.TextField(max_length=300)
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    website = models.URLField(null=True, blank=True)
    image = models.ManyToManyField(Image, null=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Hour(models.Model):
    """
    This Model will store hour details.
    """
    DAY = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    )
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='stores', null=True)
    day = models.CharField(max_length=15, choices=DAY)
    duration = models.CharField(max_length=15,
                                help_text="Please write in this format, for example -> '9 am - 9:30 pm' or closed",
                                null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.day
