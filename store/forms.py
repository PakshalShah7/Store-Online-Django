from django import forms
from django.forms import inlineformset_factory
from store.models import Image, Hour, Store


class ImageForm(forms.ModelForm):
    """
    This is form class for image model.
    """

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Image
        fields = ['image']


class HourForm(forms.ModelForm):
    """
    This is form class for hour model.
    """

    def __init__(self, *args, **kwargs):
        super(HourForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Hour
        fields = ['day', 'duration']


class StoreForm(forms.ModelForm):
    """
    This is form class for store model.
    """

    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Store
        fields = ['name', 'description', 'category', 'cover_image', 'address', 'phone_number',
                  'website', 'status', 'image']


HourFormset = inlineformset_factory(Store, Hour, form=HourForm, extra=1)
