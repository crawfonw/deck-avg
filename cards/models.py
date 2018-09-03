from django.contrib.postgres.fields import JSONField
from django.db import models

FORMATS = ('Legacy', 'Vintage', 'Modern', 'Standard', 'Commander', 'Limited', 'Pauper', 'Peasant', 'Block', 'Extended',
           'Highlander', 'Canadian Highlander', )

SUPPORTED_FORMATS = ('Legacy', 'Vintage', 'Modern', 'Standard', 'Pauper', )

# Create your models here.
class Archetype(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name

class Deck(models.Model):
    name = models.CharField(max_length=300)
    archetype = models.ForeignKey(Archetype, on_delete=models.SET_NULL, null=True)
    format = models.CharField(choices=((x.upper(), x) for x in SUPPORTED_FORMATS), max_length=50)

    included_cards = models.ManyToManyField(Card)

    maindeck = JSONField(null=True, blank=True)
    sideboard = JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print(self.maindeck.keys())
        print(type(self.maindeck.keys()))
        for card in tuple(self.maindeck.keys()) + tuple(self.sideboard.keys()):
            c = Card.objects.get_or_create(name=card)
            self.included_cards.add(c[0].pk)
        super(Deck, self).save(*args, **kwargs)
