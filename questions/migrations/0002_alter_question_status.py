# Generated by Django 3.2 on 2022-05-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
