from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_details = models.TextField()
    post_posted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    post_updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.post_title
