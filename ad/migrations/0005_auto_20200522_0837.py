# Generated by Django 2.2.10 on 2020-05-22 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0004_auto_20200522_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]