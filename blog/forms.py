from django import forms
from blog.models import Post, RecruitmentPost

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'body')

        widgets = {
            'body':forms.Textarea(attrs={'class':'editable postcontent'})  
        }

class RecruitmentPostForm(forms.ModelForm):
    class Meta():
        model = RecruitmentPost
        fields = ('title', 'body')

        widgets = {
            'body':forms.Textarea(attrs={'class':'editable postcontent'})  
        }