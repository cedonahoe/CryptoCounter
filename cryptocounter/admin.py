from django.contrib import admin

from .models import Coin, Ico, Price

# Register your models here.
admin.site.register(Coin)
admin.site.register(Ico)
admin.site.register(Price)
