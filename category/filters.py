import django_filters
from category.models import Category


class CategoryFilter(django_filters.FilterSet):
    """
    This is filter class for category model.
    """
    name = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all())

    def __init__(self, *args, **kwargs):
        super(CategoryFilter, self).__init__(*args, **kwargs)
        for field in self.filters:
            self.filters[field].field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = ['name', 'parent']
