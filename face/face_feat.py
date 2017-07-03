import sys
import os
import dlib
import glob
from skimage import io
import numpy as np

def face_info():
    face_rec_model_path = "./dlib_face_recognition_resnet_model_v1.dat"
    predictor_path = "./shape_predictor_68_face_landmarks.dat"
    f = "./bill.jpg"


    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(predictor_path)
    facerec = dlib.face_recognition_model_v1(face_rec_model_path)

    img = io.imread(f)

    dets = detector(img, 1)
    result = []
    for k, d in enumerate(dets):
        shape = sp(img, d)
        face_descriptor = facerec.compute_face_descriptor(img, shape)
        result.append(np.array(face_descriptor))
    return result 

