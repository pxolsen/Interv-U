from django.db import models

class Question(models.Model):
    text = models.CharField()
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}: {self.text}"