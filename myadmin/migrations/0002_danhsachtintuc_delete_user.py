# Generated by Django 4.0 on 2022-07-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='danhsachtintuc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('mieuta', models.CharField(blank=True, max_length=255, null=True)),
                ('ngaytao', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
