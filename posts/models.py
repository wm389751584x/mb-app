"""This module does blah blah."""

from django.db import models

# Create your models here.

class Post(models.Model):
    """This class does blah blah."""
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
