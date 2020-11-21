from django.db import models
from django.db.models.deletion import CASCADE

class Game(models.Model):
    title = models.CharField(max_length=75)
    maker = models.CharField(max_length=50)
    skill_level = models.IntegerField()
    gamer = models.ForeignKey("Gamer",
        on_delete=CASCADE,
        related_name="games",
        related_query_name="game"
    )
    game_type = models.ForeignKey("GameType",
        on_delete=CASCADE,
        related_name="games",
        related_query_name="game"
    )
    number_of_players = models.IntegerField()
