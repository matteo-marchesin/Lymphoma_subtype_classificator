# Lymphoma_subtype_classificator
Lymphoma Subtype Classificator using Simple CNN


Lymphoma is a cancer that develops in lymphocytes and can be classified in several subtypes that are known to have different prognoses and treatment. The different subtypes of lymphoma can be distinguished according to the distinct morfological pattern and cytologic layout even if, nowadays, this process is carry on by molecular and immunological techniques.
The input data consists of hematoxylin(H)-eosin(E) stained samples images organized by lymphoma subtypes. Specifically, there is a total of 374 images (size:1388x1040, RGB 24-bit) of which 133 coming from Chronic lymphocytic leukemia (CLL), 139 from follicular lymphoma samples (FL) and 122 from Mantle Cells Lymphoma (MCL) samples.

The **main_file** is a jupyter notebook containing the prepocessing steps and CNN definition&training; **live_classificator** is a python file that can be used to run the classificator on sample images using a *winner-take-all* strategy
