# Generated by Django 3.2.5 on 2021-08-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boitoi', '0004_alter_order_stattus'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
