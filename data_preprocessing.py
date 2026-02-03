import cv2

def preprocess_image(img_path):
    img=cv2.imread(img_path)
    return img