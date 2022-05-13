from django import forms
from publication_app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public', 'image']
        widget = {
            'title': forms.TextInput(),
            'text': forms.TextInput(),
            'is_public': forms.Textarea(),
            'image': forms.ImageField(),
        }