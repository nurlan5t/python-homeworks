from django import forms

from .models import Post, Post_Comment

class CommentForm(forms.ModelForm):
    post = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                  disabled=True, required=False, queryset=Post.objects.all())

    class Meta:
        model = Post_Comment
        fields = [
            'post',
            'text',
        ]
        