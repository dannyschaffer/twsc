import os

# Directories to process
DIRS = [
    "/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity/episodes",
    "/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity/episodes_clean",
    "/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity/episodes_rebuilt",
    "/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity/wordpress-theme" # Check theme files just in case
]

def fix_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Fix Podcast Links
        # Replace href="/podcast" with href="/podcasts"
        # We look for quote boundaries to avoid breaking partial matches if any exist
        content = content.replace('href="/podcast"', 'href="/podcasts"')
        content = content.replace("href='/podcast'", "href='/podcasts'")
        
        # 2. Fix Resources Links and Text
        content = content.replace('href="/resources"', 'href="/tools"')
        content = content.replace("href='/resources'", "href='/tools'")
        content = content.replace('>Resources<', '>Tools<')
        
        if content != original_content:
            print(f"Fixed: {filepath}")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    print("Starting bulk link fix...")
    count = 0
    for directory in DIRS:
        if not os.path.exists(directory):
            print(f"Skipping missing directory: {directory}")
            continue
            
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.html') or file.endswith('.php'):
                    filepath = os.path.join(root, file)
                    if fix_file(filepath):
                        count += 1
    
    print(f"Finished. Updated {count} files.")

if __name__ == "__main__":
    main()
