import shutil
import os

EPISODES_DIR = "/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity/episodes"
OUTPUT_DIR = "/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity"
ZIP_NAME = "fixed_episodes"

def zip_episodes():
    print("Zipping fixed episodes...")
    zip_path = os.path.join(OUTPUT_DIR, ZIP_NAME)
    shutil.make_archive(zip_path, 'zip', root_dir=EPISODES_DIR)
    print(f"Created {zip_path}.zip")

if __name__ == "__main__":
    zip_episodes()
