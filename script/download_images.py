import os
import requests
import argparse

def download_images(image_urls, data_dir='./data'):
    # Create data directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)
    
    # Download each image
    for i, url in enumerate(image_urls, 1):
        image_path = os.path.join(data_dir, f"{i}.jpg")
        
        # Check if image already exists
        if os.path.exists(image_path):
            print(f"Image {i} already exists at {image_path}, skipping download.")
            continue
        
        # Download and save image
        try:
            print(f"Downloading image {i} to {image_path}...")
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for HTTP errors
            
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f"Image {i} downloaded successfully.")
        except Exception as e:
            print(f"Error downloading image {i}: {e}")

if __name__ == "__main__":
    # List of image URLs
    image_urls = [
        "https://www.neighbor.com/storage-blog/wp-content/uploads/2023/08/john-matychuk-yvfp5YHWGsc-unsplash-380x250.jpg",
    ]
    
    download_images(image_urls)
    print(f"Downloaded {len(image_urls)} images to /data directory.")
