# Generated by Django 3.2.4 on 2021-08-13 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='Wallet.Product'),
        ),
        migrations.DeleteModel(
            name='Product_Cart',
        ),
    ]
