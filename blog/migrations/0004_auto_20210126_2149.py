# Generated by Django 3.1.4 on 2021-01-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210126_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(max_length=400),
        ),
    ]
