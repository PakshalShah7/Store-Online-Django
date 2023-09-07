import django_filters
from .models import User


class UserFilter(django_filters.FilterSet):
    """
    This is filter class for user model.
    """

    def __init__(self, *args, **kwargs):
        super(UserFilter, self).__init__(*args, **kwargs)
        for field in self.filters:
            self.filters[field].field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['is_superuser', 'is_staff', 'is_active']
