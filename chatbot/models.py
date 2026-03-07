from django.db import models


class Feedback(models.Model):

    rating = models.IntegerField()

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}"