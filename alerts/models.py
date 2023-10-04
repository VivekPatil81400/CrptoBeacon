from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Alert(models.Model):
    name = models.CharField(max_length=50)
    low_amount = models.FloatField(null=True)
    high_amount = models.FloatField(null=True)
    percentage_change = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name