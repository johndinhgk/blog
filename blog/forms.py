from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        self.author = kwargs.pop('author',None)
        self.post = kwargs.pop('post',None)
        super().__init__(*args,**kwargs)
    def save(self, commit=False):
        Comment = super().save(commit=False)
        Comment.author = self.author
        Comment.post = self.post
        Comment.save()
    class Meta:
        model = Comment
        fields = ["body"]