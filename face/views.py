# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import numpy as np
import face_feat as ff
import json
from face.models import FaceFeature

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST' and request.FILES['img']:
        pid = request.POST.get('person')
        img = request.FILES['img']
        handle_uploaded_file(img)
        infos = ff.face_info()
        for info in infos:
            face = FaceFeature(
                person_id = pid,
                feature = json.dumps(info.tolist()),
            )
            face.save()
    return render(request, 'face/upload.html')

def handle_uploaded_file(f):
    with open('./tmp.jpg', 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)
