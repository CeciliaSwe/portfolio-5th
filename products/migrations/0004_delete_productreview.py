# Generated by Django 3.2 on 2022-05-19 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productreview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductReview',
        ),
    ]