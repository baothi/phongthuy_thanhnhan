# Generated by Django 4.0 on 2022-07-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_danhsachtintuc_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='danhsachtintuc',
            name='trangthai',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='danhsachtintuc',
            name='mieuta',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
    ]
