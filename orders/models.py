from django.db import models


class Pizza(models.Model):
    type = models.CharField(max_length=64)
    subtype = models.CharField(max_length=64)
    size = models.CharField(max_length=1, choices=[('L', 'Large'), ('S', "Small")])
    price = models.FloatField()

    def __repr__(self):
        return f'PIZZA, {self.type}, {self.subtype}, {self.size}'


class Toppings(models.Model):
    name = models.CharField(max_length=64)
    pizza = models.ManyToManyField(Pizza, blank=True, related_name='toppings')

    def __repr__(self):
        return f'Topping = {self.name}'


class SubsPlatters(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=1, choices=[('L', 'Large'), ('S', "Small")])
    price = models.FloatField()

    def __repr__(self):
        return f'Subs/Dinner Platter {self.name} {self.size} {self.price}'


class SaladsPasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __repr__(self):
        return f'Salads/Pasta {self.name} {self.price}'


class Transactions(models.Model):
    pizza = models.ManyToManyField(Pizza, blank=True, related_name='customers')
    salads_pasta = models.ManyToManyField(SaladsPasta, blank=True, related_name="customers")
    subs_platters = models.ManyToManyField(SubsPlatters, blank=True, related_name="customers")
    total_price = models.FloatField()

    def __repr__(self):
        return f'Pizza={self.pizza}, Salads & Pasta={self.salads_pasta}, Subs & Platters={self.subs_platters}, Expenditure={self.total_price}'