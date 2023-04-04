import numpy as np
import cv2

import const_ as cst




#return list of patches, each item is a list with coordinate,
        #selected/not selected, classification
def patches_maker(inpt_image,inpt_PatchSize):
    
    lst_output=[]
    
    if not (type(inpt_PatchSize) is tuple):
        print("Insert Patch Size as a tuple")
        return 0
    
    if type(inpt_image) == tuple:
        img_shape=inpt_image
        
    else:
        img_shape = inpt_image.shape
    #print(img_shape)
    
    int_nRow =int((img_shape[1]-2*cst.Y_EDGE)/inpt_PatchSize[1])
    int_nCol =int((img_shape[0]-2*cst.X_EDGE)/inpt_PatchSize[0])
    
    while (img_shape[1] - int_nRow*(inpt_PatchSize[1]+1))<=0:#CORRETTO minore e uguale non solo minore
        int_nRow-=1#CORRETTO prima era =-1 ... un assegnazione
    while (img_shape[0] - int_nCol*(inpt_PatchSize[0]+1))<=0:#CORRETTO minore e uguale non solo minore
        int_nCol-=1#CORRETTO prima era =-1 ... un assegnazione
        
    row_count = 0
    col_count = 0
    x_start=0
    y_start=0
    
    for i  in range(0, int_nRow*int_nCol):
        if col_count==int_nCol:
            col_count=0
            row_count+=1
            
            
        x_start=cst.X_EDGE+col_count*(inpt_PatchSize[0])
        y_start=cst.Y_EDGE+row_count*(inpt_PatchSize[1])
        #print("xstart: %d-----ystart: %d "%(x_start,y_start))
        lst_output.append([row_count,col_count,x_start,x_start+inpt_PatchSize[0],y_start,y_start+inpt_PatchSize[1],0,0]) 
        #x_left,x_right,y_top,y_bottom,notSelected[=0]/selected[=1],class[CLL=1,FL=2,MCL=3,nn=0]
        col_count+=1
    return lst_output


# this function show the input image divide in patches
    #with different color based on selection status and classification
def img_patched(inpt_image, inpt_list):
    
    out_image= np.copy(inpt_image)
    list_coloredPatch= []
    set_color=(0,0,0)
    
    for item in inpt_list:
        
        if item[6]==0:
            cv2.rectangle(out_image,(item[2],item[4]),(item[3],item[5]),cst.clr_array[0],8)
        else:
            list_coloredPatch.append(item)
            
                
    for item in list_coloredPatch:
        set_color=cst.clr_array[item[7]+1]
        #cv2.putText(out_image,"%d,%d"%(item[0],item[1]),(item[5],item[2]),font,1,(255,255,255))
        cv2.rectangle(out_image,(item[2],item[4]),(item[3],item[5]),set_color,8)
        
        
    plt.imshow(out_image)