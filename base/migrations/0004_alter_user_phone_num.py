# Generated by Django 4.2.4 on 2023-08-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.CharField(max_length=15),
        ),
    ]