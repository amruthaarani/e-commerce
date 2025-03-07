import os
import requests

# Define the images and their corresponding Unsplash image URLs
IMAGES = {
    'fashion-store': 'https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?auto=format&fit=crop&w=1200&q=80',
    'fashion-collection': 'https://images.unsplash.com/photo-1558769132-cb1aea458c5e?auto=format&fit=crop&w=1200&q=80'
}

def download_image(url, filename):
    """Download an image from a URL and save it to the specified filename."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

def main():
    # Create the about directory if it doesn't exist
    about_dir = os.path.join('static', 'images', 'about')
    os.makedirs(about_dir, exist_ok=True)
    
    # Download each image
    for image_name, url in IMAGES.items():
        filename = os.path.join(about_dir, f"{image_name}.jpg")
        download_image(url, filename)

if __name__ == "__main__":
    main() 