# Generated by Django 3.2.5 on 2021-07-27 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('info', models.CharField(blank=True, max_length=2200, null=True)),
                ('photo', models.ImageField(blank=True, default='avatar.png', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('description', models.CharField(max_length=1500, null=True)),
                ('reating', models.FloatField(blank=True, default=0, null=True)),
                ('cover', models.ImageField(blank=True, default='defaultcover.jpg', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.author')),
            ],
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=60, null=True)),
                ('photo', models.ImageField(blank=True, default='avatar.png', null=True, upload_to='')),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(default=' ', max_length=300, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='icons/')),
            ],
        ),
        migrations.CreateModel(
            name='Paymethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('account', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('info', models.CharField(blank=True, max_length=800, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1200, null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.book')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_address', models.CharField(default=' ', max_length=300, null=True)),
                ('stattus', models.CharField(choices=[('Pending', 'Pending'), ('Delevered', 'Delevered'), ('On the way', 'On the Way')], default='Pending', max_length=50, null=True)),
                ('pay_stattus', models.CharField(choices=[('Paid', 'Paid'), ('Due', 'Due')], max_length=50, null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('estimated_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.customer')),
                ('pay_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.paymethod')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.book')),
            ],
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=1200, null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.review')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.book')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.customer')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boitoi.catagory'),
        ),
    ]
