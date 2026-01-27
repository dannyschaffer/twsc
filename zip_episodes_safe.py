import shutil
import os

ANTIGRAVITY_DIR = "/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity"
OUTPUT_DIR = ANTIGRAVITY_DIR
ZIP_NAME = "fixed_episodes"

def zip_episodes():
    print("Zipping fixed episodes (with folder structure)...")
    zip_path = os.path.join(OUTPUT_DIR, ZIP_NAME)
    # This creates a zip containing 'episodes/file.html' instead of just 'file.html'
    shutil.make_archive(zip_path, 'zip', root_dir=ANTIGRAVITY_DIR, base_dir='episodes')
    print(f"Created {zip_path}.zip")

if __name__ == "__main__":
    zip_episodes()
