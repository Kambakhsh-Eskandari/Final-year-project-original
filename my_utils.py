import cv2 
import numpy as np


def log_img(image):
    # Apply log transformation method
    img = image.copy()
    log_image =  (np.log(img + 1)) / np.log(1 + np.max(img))




    # Specify the data type so that
    # float value will be converted to int
    # log_image= np.array(log_image, dtype = np.uint8)

    for x in range(log_image.shape[0]):
        for y in range(log_image.shape[1]):
            if log_image[x][y] < 0:
                log_image[x][y] = 0
            # elif log_image[x][y] > 255:
            #     log_image[x][y] = 255
    
    
    return log_image
    
                
def normalize_image(image):
    
    img = image.copy()

    log_image = log_img(img)


    log_image_n =  (log_image - np.min(log_image)) / (np.max(log_image) - np.min(log_image))

    # for x in range(log_image_n.shape[0]):
    #     for y in range(log_image_n.shape[1]):
    #         if log_image_n[x][y] < 0:
    #             log_image_n[x][y] = 255


    # log_image_n = np.rint(log_image_n).astype(np.uint8)
    
    
    return log_image_n