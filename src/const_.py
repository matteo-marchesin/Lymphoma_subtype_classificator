import os

#Dimensions
X_EDGE=5
Y_EDGE=5
PATCH_SIZE=(50,50)#(32,32)#
IMAGE_W=1388
IMAGE_H=1040

#Parameters
bln_notThree = False
if bln_notThree:
  INT_CHANNEL=2
else:
  INT_CHANNEL=3
  
  
#Colors
# define color patch
#(black  -> not selected)
#(yellow -> selected)
#(red    -> CLL assigned)
#(green  -> FL assigned)
#(blu    -> MCL assigned) 
clr_array=[(0,0,0),(255,255,0),(255,0,0),(0,255,0),(0,0,255)]


#load Dataset
wrk_dir = ""

data_dir = os.path.join(wrk_dir, "data")

#split ratio
RATIO_TRAIN=0.70
RATIO_TEST=0.15

RATIO_VALIDATION=0.15


