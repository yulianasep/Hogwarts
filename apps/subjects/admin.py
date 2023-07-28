from django.contrib import admin

# Register your models here.
from .models import Spell, Subject


admin.site.register(Spell)
admin.site.register(Subject)
