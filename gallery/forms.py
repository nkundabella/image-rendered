from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    """
    A ModelForm that allows users to upload a new Photo directly into the database.
    Django automatically validates the file format using Pillow for ImageField.
    """
    class Meta:
        model = Photo
        fields = ['title', 'caption', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Sunset over the Lake',
                'required': True,
            }),
            'caption': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 3,
                'placeholder': 'Add a short caption or story about this photo...',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-file-input',
                'accept': 'image/*',
                'required': True,
                'id': 'image-file-input',
            }),
        }
