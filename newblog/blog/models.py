from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200,blank=True,null=True)
    text = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title