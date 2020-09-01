from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()


class Post(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
