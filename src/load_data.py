from PIL import Image
import matplotlib.pyplot as plt
import tifffile as tiff
import cv2

import numpy as np
import os
import random

import const_ as cst

#"dataset"


######## List images grouped by class
cll_folder= "CLL"
fl_folder= "FL"
mcl_folder= "MCL"


lst_CLL_images=os.listdir(os.path.join(cst.data_dir,cll_folder))
lst_FL_images=os.listdir(os.path.join(cst.data_dir,fl_folder))
lst_MCL_images=os.listdir(os.path.join(cst.data_dir,mcl_folder))
lst_folder=[os.path.join(cst.data_dir, cll_folder),os.path.join(cst.data_dir, fl_folder),os.path.join(cst.data_dir, mcl_folder)]


lst_images=[lst_CLL_images,lst_FL_images,lst_MCL_images]


def Open_image(str_filePath): # output np.array
    if str_filePath[-3:]=="tif":
      imOut=tiff.imread(str_filePath)
    elif  (str_filePath[-4:]=="jpeg" or str_filePath[-3:]=="jpg"):
      image = Image.open(str_filePath)
      imOut = np.asarray(image)
    return imOut



bln_saveDataSet = False
str_dirSaveDataset ="Dataset"
#os.mkdir(os.path.join('/content/drive/MyDrive/HDA',str_dirSaveDataset))
int_trasf = 0 # No img trasformation[0], HE deconvolution [1], standardization [2]
bln_fromFile = False
str_forcedType = ""#"jpeg" #default ""

list_dataset0 = ""
list_dataset1 = ""
list_dataset2 = ""


cll_test_items=int((len(lst_images[0])+1)*cst.RATIO_TEST)
fl_test_items =int((len(lst_images[1])+1)*cst.RATIO_TEST)
mcl_test_items=int((len(lst_images[2])+1)*cst.RATIO_TEST)

print("Test set cardinality:  CLL {}, FL {}, MCL {}".format(cll_test_items,fl_test_items,mcl_test_items))

# qTest Training DataSet Splitting
random.shuffle(lst_images[0])
random.shuffle(lst_images[1])
random.shuffle(lst_images[2])

lst_images_test=[lst_images[0][:cll_test_items],lst_images[1][:fl_test_items],lst_images[2][:mcl_test_items]]
lst_images_train=[lst_images[0][cll_test_items:],lst_images[1][fl_test_items:],lst_images[2][mcl_test_items:]]# from Here i will select the 15% validation set 

train_ds = {cll_folder:[],fl_folder:[],mcl_folder:[]}
test_ds  = {cll_folder:[],fl_folder:[],mcl_folder:[]}



