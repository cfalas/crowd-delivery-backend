# Generated by Django 3.0.4 on 2020-04-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20200404_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ProductWeight',
            field=models.IntegerField(default=1),
        ),
    ]
