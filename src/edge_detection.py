import cv2
import os

def edge_detection(input_path, output_path):
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    gpu_image = cv2.cuda_GpuMat()
    gpu_image.upload(image)
    
    gpu_edges = cv2.cuda.createCannyEdgeDetector(100, 200)
    edges = gpu_edges.detect(gpu_image)
    
    result = edges.download()
    cv2.imwrite(output_path, result)
