# Generated by Django 4.0 on 2022-07-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0004_baiviet'),
    ]

    operations = [
        migrations.AddField(
            model_name='baiviet',
            name='hinhanh',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
