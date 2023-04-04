
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