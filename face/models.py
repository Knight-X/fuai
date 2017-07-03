# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FaceFeature(models.Model):
    person_id = models.IntegerField()
    feature = models.CharField(max_length= 1000000)
