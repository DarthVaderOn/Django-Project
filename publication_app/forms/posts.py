from django import forms
from publication_app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public', 'image']
        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'is_public': forms.Textarea(attrs={'class': 'form-control'}),
        }


