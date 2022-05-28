from django import forms
from media_app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public',]
        widget = {
            'title': forms.TextInput(),
            'text': forms.TextInput(),
            'is_public': forms.Textarea(),
        }

class AddImagePost(PostForm):
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'multiple': 'multiple'})
    )

    class Meta(PostForm.Meta):
        fields = PostForm.Meta.fields + ["image", ]