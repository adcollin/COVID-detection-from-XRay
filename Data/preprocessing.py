# Imports
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from skimage.transform import resize
from pathlib import Path
import os
import matplotlib.image as mpimg

#Databases pre-processing
def data_load(input_path, img_size, save_path):
    """Function to load the images and convert them to numpy arrays"""
    # Load data
    df_train_img = list(Path(input_path).glob("*.png"))
    if len(df_train_img) == 0:
        df_train_img = list(Path(input_path).glob("*.jpg"))
    print("Number of images retrieved",len(df_train_img))
    df_train_np = {}
    
    # Resize data
    for i, img_name in enumerate(df_train_img):
        try:
            temp_image = mpimg.imread(img_name)
            img_resize = resize(temp_image, (img_size, img_size, 1), anti_aliasing=True)
            df_train_np[img_name] = img_resize
        except:
            continue

    #print("Image dimension after resizing (height, width, channel): ",list(df_train_np.values())[0].shape)

    # Save data
    np.save(save_path, df_train_np, allow_pickle=True, fix_imports=False)

if __name__ == "__main__":
    img_size = 224
    input_path="/mnt/f/Users/adele/WSL/Harvard/COMPSCI/Project/Brixia/dicom/dicom_png"
    output_path = "/mnt/f/Users/adele/WSL/Harvard/COMPSCI/Project/images_to_git/Brixia"
    data_load(input_path, img_size, output_path)
    print("Brixia data loaded")

    input_path="/mnt/f/Users/adele/WSL/Harvard/COMPSCI/Project/COVIDGR_1.0/N"
    output_path = "/mnt/f/Users/adele/WSL/Harvard/COMPSCI/Project/images_to_git/COVIDGR_1.0/N"
    data_load(input_path, img_size, output_path)
    print("COVIDGR N data loaded")

    input_path="/mnt/f/Users/adele/WSL/Harvard/COMPSCI/Project/COVIDGR_1.0/P"
    output_path = "/mnt/f/Users/adele/WSL/Harvard/COMPSCI/Project/images_to_git/COVIDGR_1.0/P"
    data_load(input_path, img_size, output_path)
    print("COVIDGR P data loaded")

    input_path="/mnt/f/Users/adele/WSL/Harvard/COMPSCI/Project/NIHCXR/images/images_001/images"
    output_path = "/mnt/f/Users/adele/WSL/Harvard/COMPSCI/Project/images_to_git/NIHCXR"
    data_load(input_path, img_size, output_path)
    print("NIHCXR 1 data loaded")

    input_path="/mnt/f/Users/adele/WSL/Harvard/COMPSCI/Project/NIHCXR/images/images_002/images"
    output_path = "/mnt/f/Users/adele/WSL/Harvard/COMPSCI/Project/images_to_git/NIHCXR"
    data_load(input_path, img_size, output_path)
    print("NIHCXR 2 data loaded")
