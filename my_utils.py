import cv2 
import numpy as np


def log_img(image):
    # Apply log transformation method
    c = 255 / np.log(1 + np.max(image))
    log_image = c * (np.log(image + 1))



    # Specify the data type so that
    # float value will be converted to int
    # log_image= np.array(log_image, dtype = np.uint8)

    for x in range(log_image.shape[0]):
        for y in range(log_image.shape[1]):
            if log_image[x][y] > 255:
                log_image[x][y] = 255
    
    return log_image
    
                
def normalize_image(image):
    
    log_image = log_img(image)
    
    log_image_n = (log_image - np.min(log_image)) / (np.max(log_image) - np.min(log_image))

    # log_image_n = np.rint(log_image_n).astype(np.uint8)
    
#     
    return log_image_n