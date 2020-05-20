# Generated by Django 3.0.4 on 2020-05-20 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_transactions_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toppings',
            name='pizza',
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='pizzas', to='orders.Toppings'),
        ),
    ]
