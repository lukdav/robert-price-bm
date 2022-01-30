from django import forms

from .models import Blog

from products.widgets import CustomClearableFileInput


class Blog(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'image', 'article',)

        image = forms.ImageField(label='Image', required=True, widget=CustomClearableFileInput)
    

    def __init__(self, *args, **kwargs):
        """
        Sets placeholders, removes auto labels, adds auto-focus and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'image': 'Image',
            'article': 'Article',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image':
                self.fields[field].widget.attrs['placeholder'] = (
                    placeholders[field])
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 blog-form-input'

