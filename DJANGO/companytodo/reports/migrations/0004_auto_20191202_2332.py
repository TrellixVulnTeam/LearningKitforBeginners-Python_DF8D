# Generated by Django 2.2.7 on 2019-12-02 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_problemreported'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problemreported',
            options={'verbose_name': 'Problem Reported', 'verbose_name_plural': 'Problems Reported'},
        ),
    ]
