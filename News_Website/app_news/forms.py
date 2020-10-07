from django import forms
from app_news.models import NewsModel


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ['news_type',"news_headline", "post_news_text","post_news_image"]