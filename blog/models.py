# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 20)
    time_stamp = models.DateField()
    content = models.CharField(max_length = 2000)
    author = models.CharField(max_length = 20)