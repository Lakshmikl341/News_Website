# Generated by Django 3.1.2 on 2020-10-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='news_headline',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
