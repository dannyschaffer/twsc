import shutil
import os

# Paths
THEME_DIR = "/Users/dannyschaffer/Local Sites/twsc/app/public/wp-content/themes"
OUTPUT_DIR = "/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity"

def build_zip():
    print("Updating Theme Zip (v55 - Automated Safety Nets)...")
    theme_zip_path = os.path.join(OUTPUT_DIR, "twsc-theme")
    shutil.make_archive(theme_zip_path, 'zip', root_dir=THEME_DIR, base_dir="twsc-theme")
    print(f"Updated {theme_zip_path}.zip")

if __name__ == "__main__":
    build_zip()
