import os
from src.edge_detection import edge_detection
from src.image_conversion import convert_to_bw


def process_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".tiff"):
            input_path = os.path.join(input_dir, filename)
            output_edge_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_edges.png")
            output_bw_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_bw.png")

            edge_detection(input_path, output_edge_path)
            convert_to_bw(input_path, output_bw_path)

if __name__ == "__main__":
    input_directory = "D:\\Compressed\\aerials\\aerials"
    output_directory = "output"
    process_images(input_directory, output_directory)
