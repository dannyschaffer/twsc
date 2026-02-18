import shutil
import os

# Paths
SOURCE_DIR = "/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity/wordpress-theme"
OUTPUT_DIR = "/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity"
TEMP_DIR = os.path.join(OUTPUT_DIR, "temp_build")
THEME_NAME = "twsc-theme"

def build_zip():
    print("Building Theme Zip v62 (Redirects & Results)...")
    
    # Clean up temp if exists
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    
    # Create temp structure
    target_folder = os.path.join(TEMP_DIR, THEME_NAME)
    os.makedirs(target_folder)
    
    # Copy files
    print(f"Copying files from {SOURCE_DIR} to {target_folder}...")
    shutil.copytree(SOURCE_DIR, target_folder, dirs_exist_ok=True)
    
    # Zip
    zip_path = os.path.join(OUTPUT_DIR, "twsc-theme")
    print(f"Creating zip {zip_path}.zip...")
    shutil.make_archive(zip_path, 'zip', root_dir=TEMP_DIR, base_dir=THEME_NAME)
    
    # Cleanup
    shutil.rmtree(TEMP_DIR)
    print("Done.")

if __name__ == "__main__":
    build_zip()
