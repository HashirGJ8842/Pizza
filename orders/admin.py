from django.contrib import admin
from . import models

admin.site.register(models.Pizza)
admin.site.register(models.SaladsPasta)
admin.site.register(models.SubsPlatters)
admin.site.register(models.Toppings)
admin.site.register(models.FinalPizza)
admin.site.register(models.FinalToppings)
admin.site.register(models.FinalSubs)
admin.site.register(models.FinalSalads)
admin.site.register(models.Receipt) 
