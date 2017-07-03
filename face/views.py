# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import numpy as np
import ff
import json
from face.models import FaceFeature

# Create your views here.

def index(request):
    jpg = Image.open('/code/face/p.png')
    x = ff.face_info()
    pid = 1
    for s in x:
        print s
        m = FaceFeature(
                person_id = pid,
                feature = json.dumps(s.tolist())
                )
    m.save()

    return HttpResponse("Hello world")
