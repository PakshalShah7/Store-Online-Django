from django import forms
from category.models import Category


class CategoryForm(forms.ModelForm):
    """
    This is form class for category model.
    """

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = '__all__'
