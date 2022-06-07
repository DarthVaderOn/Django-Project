from django import forms
from publication_app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public','tag']
        widget = {
            'title': forms.TextInput(),
            'text': forms.TextInput(),
            'is_public': forms.BooleanField(initial=True),
        }


class AddImagePost(PostForm):
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'multiple': True})
    )


    class Meta(PostForm.Meta):
        fields = PostForm.Meta.fields + ["image", ]