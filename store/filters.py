import django_filters
from store.models import Store


class StoreFilter(django_filters.FilterSet):
    """
    This is filter class for store model.
    """

    def __init__(self, *args, **kwargs):
        super(StoreFilter, self).__init__(*args, **kwargs)
        for field in self.filters:
            self.filters[field].field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Store
        fields = ['name', 'category']
