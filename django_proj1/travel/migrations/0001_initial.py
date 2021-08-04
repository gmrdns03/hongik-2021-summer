# Generated by Django 3.2.6 on 2021-08-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='메세지')),
                ('latitude', models.FloatField(verbose_name='위도')),
                ('longitude', models.FloatField(verbose_name='경도')),
            ],
        ),
    ]
