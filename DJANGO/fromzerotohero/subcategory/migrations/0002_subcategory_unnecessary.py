# Generated by Django 2.2.6 on 2019-12-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='unnecessary',
            field=models.CharField(default='a', max_length=2),
        ),
    ]
