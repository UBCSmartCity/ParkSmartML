from ultralytics import YOLO
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
import cv2
import argparse

def process_image(image_num, model="yolo11n-obb.pt", model_dir='./model', data_dir='./data', result_dir='./result'):
    image_path = os.path.join(data_dir, f"{image_num}.jpg")
    
    # Check if the image exists
    if not os.path.exists(image_path):
        print(f"Error: Image {image_num} not found at {image_path}")
        print("Please run the download script first or specify a valid image number.")
        return False
    
    os.makedirs(result_dir, exist_ok=True)
    
    print(f"Loading image from {image_path}...")
    img = Image.open(image_path)
    img = np.array(img)
    
    model_path = os.path.join(model_dir, model)

    # Load the model
    model = YOLO(model_path)
    
    # Predict with the model
    results = model(img)
    
    # Get the output image with predictions
    for r in results:
        im_array = r.plot(line_width=1, conf=False)  # plot a BGR numpy array of predictions
        
        # Save the result image
        result_path = os.path.join(result_dir, f"result_{image_num}.jpg")
        cv2.imwrite(result_path, im_array)
        print(f"Result image saved to {result_path}")
        
        # Display the image
        plt.figure(figsize=(12, 8))
        plt.imshow(cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
        plt.title(f"Image {image_num}")
        plt.axis('off')
        plt.show()
    
    return True

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Process images with YOLO model')
    parser.add_argument('--image', type=int, default=1, help='Image number to process (default: 1)')
    parser.add_argument('--model', type=str, default="yolo11n-obb.pt", help='Path to YOLO model (default: yolo11n-obb.pt)')
    
    args = parser.parse_args()
    
    # Process the specified image
    process_image(image_num=args.image, model=args.model)
