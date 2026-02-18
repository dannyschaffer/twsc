import os
import requests

# Mapping of Name -> URL (from browser agent)
images = {
    "thuan-pham.png": "https://thewallstreetcoach.com/wp-content/uploads/2022/10/Testimonial-ThuanPham-1.png",
    "andres-armienta.png": "https://thewallstreetcoach.com/wp-content/uploads/2023/09/Andres-Armienta.png",
    "tom-burnett.png": "https://thewallstreetcoach.com/wp-content/uploads/2024/09/Tom-Burnett.png",
    "brian-shannon.png": "https://thewallstreetcoach.com/wp-content/uploads/2023/11/Brian-Shannon.png",
    "gregg-sciabica.png": "https://thewallstreetcoach.com/wp-content/uploads/2023/10/Gregg-Sciabica.png",
    "howard-lindzon.jpg": "https://thewallstreetcoach.com/wp-content/uploads/2021/02/TestimonialHowardLindzon-150x150.jpg",
    "benito-segovia.jpg": "https://thewallstreetcoach.com/wp-content/uploads/2023/03/Benito-Headshot-2018-bwSM.jpg",
    "brian-lee.jpg": "https://thewallstreetcoach.com/wp-content/uploads/2023/03/TestimonialBrianLeeCrop.jpg",
    "matthew-monaco.jpg": "https://thewallstreetcoach.com/wp-content/uploads/2021/02/TestiMatthewMonacoBWCrop.jpg",
    "tim-bohen.png": "https://thewallstreetcoach.com/wp-content/uploads/2023/03/TimBohenOrigCrop.png"
}

OUTPUT_DIR = "/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity/wordpress-theme/assets/images/testimonials"

def download_images():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    for filename, url in images.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        print(f"Downloading {filename}...")
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"Saved {filename}")
            else:
                print(f"Failed to download {url}: Status {response.status_code}")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    download_images()
