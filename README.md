# Lymphoma Subtype Histopathology Classificator (CNN based)

## Overview
Lymphoma is a type of cancer that originates in lymphocytes and encompasses several subtypes, each characterized by distinct prognoses and treatment approaches. These subtypes can traditionally be distinguished based on their specific morphological patterns and cytological features, although modern classification increasingly relies on molecular and immunological techniques.


## Dataset Description
The dataset used in this study comprises [hematoxylin and eosin (H&E)](https://en.wikipedia.org/wiki/H%26E_stain) stained histopathological images categorized by lymphoma subtype.  
It includes a total of **374 RGB images** (size: **1388 × 1040 pixels**), distributed as follows:

| Lymphoma Subtype | Acronym | Number of Images |
|------------------|----------|------------------|
| Chronic Lymphocytic Leukemia | CLL | 133 |
| Follicular Lymphoma | FL | 139 |
| Mantle Cell Lymphoma | MCL | 122 |
| **Total** | — | **374** |


On Kaggle you can find the data-set to [download](https://www.kaggle.com/datasets/andrewmvd/malignant-lymphoma-classification?select=MCL).


## Project Files Description

###  main_file.ipynb
The `main_file.ipynb` notebook includes all **data preprocessing steps**, the **CNN model definition**, and the **training process**.  
It can be executed step-by-step to reproduce the model training workflow and visualize performance metrics such as accuracy and loss.

### live_classificator.py
The `live_classificator.py` script allows users to **run the trained classifier on sample images**.  
It applies a **winner-take-all** decision strategy to assign each input image to the most likely lymphoma subtype.





The **main_file** is a jupyter notebook containing the prepocessing steps and CNN definition&training; **live_classificator** is a python file that can be used to run the classificator on sample images using a *winner-take-all* strategy
