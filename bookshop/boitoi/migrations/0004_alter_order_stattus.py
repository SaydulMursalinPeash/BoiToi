# Generated by Django 3.2.5 on 2021-08-03 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boitoi', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stattus',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delevered', 'Delevered'), ('On the way', 'On the way')], default='Pending', max_length=50, null=True),
        ),
    ]