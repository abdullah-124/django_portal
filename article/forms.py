from django import forms
from .models import Article,Review

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['author']
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','comment']