# Generated by Django 4.2.5 on 2024-03-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_order_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=40),
        ),
    ]