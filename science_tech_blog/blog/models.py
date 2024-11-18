from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# contact form model
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name or 'Anonymous' and self.email}"
