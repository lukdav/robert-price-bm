from django import forms

from .models import NewsPost

from products.widgets import CustomClearableFileInput


class NewsPostForm(forms.ModelForm):

    class Meta:
        model = NewsPost
        fields = (
            'title',
            'image',
            'content',
        )

    image = forms.ImageField(label='Image',
        required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Set placeholders, auto-focus to title and a class to the fields
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'image': 'Image',
            'content': 'Article Content',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image':
                self.fields[field].widget.attrs['placeholder'] = (
                    placeholders[field])
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 news-form-input'
