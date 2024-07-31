import cv2
import os

def convert_to_bw(input_path, output_path):
    image = cv2.imread(input_path)
    gpu_image = cv2.cuda_GpuMat()
    gpu_image.upload(image)
    
    gpu_gray_image = cv2.cuda.cvtColor(gpu_image, cv2.COLOR_BGR2GRAY)
    gray_image = gpu_gray_image.download()
    
    cv2.imwrite(output_path, gray_image)
