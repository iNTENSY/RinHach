# Generated by Django 4.2.7 on 2023-11-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='customer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='gender',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='zipMerchant',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='zipcodeOri',
            field=models.CharField(max_length=255),
        ),
    ]
