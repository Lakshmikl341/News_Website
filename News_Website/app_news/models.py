from django.db import models
Choices=[
    ("Select", "Select"),

    ("Entertinment",
     (
         ("Cinema", "Cinema"),
     ("Stories", "Stories"),
     ("Others", "Others"),
     )
     ),
    ("Business", "Business"),
    ("Sports", "Sports"),
    ("Education", "Education"),
    ("Careers",
      (
         ("IT jobs", "IT Jobs"),
         ("Non-IT jobs", "Non-IT Jobs"),
         ("Government jobs", "Government jobs"),
         ("Others", "Others"),
      )
    ),
    ("Hot News", "Hot News"),
]
# Create your models here.
class NewsModel(models.Model):
    news_type = models.CharField(max_length=50, choices=Choices, default="Select")
    news_headline = models.CharField(max_length=50)
    post_news_text = models.CharField(max_length=500)
    post_news_image = models.FileField(upload_to="app_news/static/Images",null=True, blank=True)
    def __str__(self):
        return self.news_type