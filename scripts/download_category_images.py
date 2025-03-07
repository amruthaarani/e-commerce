import os
import requests

# Dictionary mapping image names to their Unsplash URLs
IMAGES = {
    'men-shirts.jpg': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf',
    'women-dresses.jpg': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8',
    'kids-wear.jpg': 'https://images.unsplash.com/photo-1622290291468-a28f7a7dc6a8',
    'accessories.jpg': 'https://images.unsplash.com/photo-1601121141461-9d6647bca1ed'
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
    # Create the static/images directory if it doesn't exist
    os.makedirs('static', exist_ok=True)
    
    # Download each image
    for image_name, url in IMAGES.items():
        filepath = os.path.join('static', image_name)
        download_image(url, filepath)

if __name__ == '__main__':
    main() 