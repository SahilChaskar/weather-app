from django.contrib.auth.models import User
from django.db import models


class Owner(User):
    """Inherited Model definition for Owners"""

    orderList = models.TextField(default="")


class Location(models.Model):
    """Model definition for Locations (like city or town)"""

    locID = models.IntegerField(primary_key=True)
    name = models.TextField()
    temperature = models.TextField()
    description = models.TextField()
    icon = models.TextField()
    country = models.TextField(default='India')
    humidity = models.TextField(default='50')

    # a Many-to-One relationship with User Model
    owner = models.ForeignKey(Owner, blank=False, null=False, on_delete=models.CASCADE, related_name="owner")

    class Meta:
        # User can not request weather information for same location more than once
        unique_together = (("name", "owner"),)

    def __str__(self):
        return ' '.join(["Location name:", self.name, ", Belongs to:", str(self.owner.username)])

# models.py

class WeatherAlert(models.Model):
    user = models.ForeignKey(Owner, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)  # e.g., "Rain", "Snow", "Thunderstorm", etc.

    class Meta:
        unique_together = (("user", "location", "condition"),)
