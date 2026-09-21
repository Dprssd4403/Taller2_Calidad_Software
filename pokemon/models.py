from django.db import models

class Pokemon(models.Model):
    poke_id = models.IntegerField(unique=True, help_text="ID oficial de la PokéAPI")
    name = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=5, decimal_places=2, help_text="Altura en metros")
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso en kg")
    sprite_url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.poke_id} - {self.name.capitalize()}"

    class Meta:
        ordering = ['poke_id']