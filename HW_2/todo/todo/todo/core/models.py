# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime 
from django.db import models

# Create your models here.

class todo(models.Model):
    
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __unicode__(self):
        return self.name

