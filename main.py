#!/usr/bin/env python3
# -*- coding: utf-8 -*-

EXTERNAL_SOURCES: list[str] = [
    "Const.py",      # Constat values
    "load_data.py",          # load data img
     "patch_maker.py" # function to create patchees from image
]




#Import
import os
import time
import random
import sys
from copy import copy

sys.path.append("src/")
import Const
import load_data
import patch_maker


import pandas as pd
import numpy as np

from scipy import ndimage
import matplotlib.pyplot as plt


from PIL import Image
import tifffile as tiff
import cv2
import json

import pickle
import shutil
import argparse


#tensorflow
import tensorflow as tf
from tensorflow.keras import layers, Input
from tensorflow.keras.layers import Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D, Dropout
from tensorflow.keras.models import Model, load_model, Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from scipy.special import softmax

print("HDA Course aa 2022-2023 - Project C1 - Live Presentation ")


parser= argparse.ArgumentParser(description='Live presentation - Lymphoma Subtype Classificator')
parser.add_argument('-f', type=int,help="Create Folder")
parser.add_argument('-a', type=int,help="Automatic Validation all file")

args=parser.parse_args()
if args.f == None:
    bln_createFolder=False
else:
    if args.f==1:
        bln_createFolder=True
    else:
        bln_createFolder=False

if args.a == None:
    bln_auto=False
else:
    if args.a==1:
        bln_auto=True
    else:
        bln_auto=False


def class2indx(str_inpt):
    if str_inpt=="CLL":
        return 0
    elif str_inpt=="FL" or str_inpt=="FL_":
        return 1
    elif str_inpt=="MCL":
        return 2

def predict_class(inpt_model,inpt_img):
    out=inpt_model(inpt_img.reshape((1,50,50,3)),training=False)
    y_pred=tf.argmax(softmax(out,axis=1),axis=1)[0]
    #print(out)
    #if len(y_pred)!=1:
    #    y_pred=999
    #    print("ERROR: prediction output"+str(y_pred))
    
    return y_pred


def import_model(model_path):
    
    out_model=load_model(model_path)
    return out_model

X_EDGE=5
Y_EDGE=5
PATCH_SIZE=(50,50)
IMAGE_W=1388
IMAGE_H=1040
# define color patch
#(black  -> not classified)
#(red    -> CLL assigned)
#(green  -> FL assigned)
#(blu    -> MCL assigned)
clr_array=[(0,0,0),(0,0,255),(0,255,0),(255,0,0),(255,255,255)]
font = cv2.FONT_HERSHEY_SIMPLEX

if __name__ == "__main__":
    asyncio.run(main())
