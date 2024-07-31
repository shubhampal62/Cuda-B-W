import cv2
import numpy as np
import os

def load_image(image_path):
    return cv2.imread(image_path)

def save_image(image, save_path):
    cv2.imwrite(save_path, image)

def edge_detection(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 100, 200)
    return edges

def main():
    input_folder = '../../data/aerials/aerials'
    output_folder = 'bin/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = []
    for file in os.listdir(input_folder):
        if file.endswith('.tiff') or file.endswith('.png'):
            image_files.append(file)
    

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        save_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + '.png')

        print(f'Processing {image_path}...')
        image = load_image(image_path)
        edges = edge_detection(image)
        save_image(edges, save_path)
        print(f'Saved edge-detected image to {save_path}')

if __name__ == '__main__':
    main()
