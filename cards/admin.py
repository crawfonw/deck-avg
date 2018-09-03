from django.contrib import admin

from .models import Archetype, Card, Deck

# Register your models here.
admin.site.register(Archetype)
admin.site.register(Card)
admin.site.register(Deck)
