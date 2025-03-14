from django.db import models

class Card(models.Model):
    player_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    card_brand = models.CharField(max_length=100)
    card_number = models.CharField(max_length=50)
    front_image = models.ImageField(upload_to='cards/front/')
    back_image = models.ImageField(upload_to='cards/back/')
    for_sale = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player_name} - {self.card_brand}"
