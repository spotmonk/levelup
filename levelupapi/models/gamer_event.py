from django.db import models
from django.db.models.deletion import CASCADE

class GamerEvent(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=CASCADE, related_name="registrations")
    event = models.ForeignKey("Event", on_delete=CASCADE, related_name="registrations")
