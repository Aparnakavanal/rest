# Generated by Django 3.2 on 2021-09-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0002_remove_orders_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('phonenumber', models.IntegerField()),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
    ]
