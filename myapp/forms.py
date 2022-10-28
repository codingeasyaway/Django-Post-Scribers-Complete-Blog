from django import forms
from .models import PostModel, Comments

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta:
        model = PostModel
        fields = ('title', 'content')
class PostModelUpdateFrom(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')
class CommentsFrom(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here..'}))
    class Meta:
        model = Comments
        fields = ('content',)
