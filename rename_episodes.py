import json
import os
import re
import shutil

# Configuration
EPISODES_DIR = 'episodes'
JSON_PATH = 'podcast-episodes-full.json'
NEW_EPISODES_DIR = 'episodes_clean'

def sanitize_filename_title(title):
    # Convert "EP 110: Title" -> "ep-110-title"
    # Basic slugification
    clean = title.lower()
    clean = re.sub(r'[^a-z0-9\s-]', '', clean)
    clean = re.sub(r'\s+', '-', clean)
    return clean

def rename_files():
    # 1. Load the valid map
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)
        
    # 2. Prepare new directory
    if not os.path.exists(NEW_EPISODES_DIR):
        os.makedirs(NEW_EPISODES_DIR)
        
    updated_count = 0
    
    for entry in data:
        current_link = entry.get('link', '')
        if not current_link.startswith('/episodes/'):
            continue
            
        old_filename = current_link.replace('/episodes/', '')
        old_path = os.path.join(EPISODES_DIR, old_filename)
        
        if os.path.exists(old_path):
            # Create NEW clean filename based on the REAL Episode Number
            ep_num = entry['ep']
            # We want: ep-110-market-wizards-secrets-revealed.html
            
            # Extract basic title slug from the JSON title
            # Remove "EP 110: " prefix if present in title string to avoid double numbering
            raw_title = entry['title']
            clean_title_text = re.sub(r'^ep\s*\d+[:\s-]*', '', raw_title, flags=re.IGNORECASE)
            title_slug = sanitize_filename_title(clean_title_text)
            
            # Limit slug length to avoid crazy long filenames
            if len(title_slug) > 50:
                title_slug = "-".join(title_slug[:50].split('-')[:-1]) # clean cut at word bound
            
            new_filename = f"ep-{ep_num:03d}-{title_slug}.html"
            new_path = os.path.join(NEW_EPISODES_DIR, new_filename)
            
            # Copy file to new location with new name
            shutil.copy2(old_path, new_path)
            
            # Update JSON to point to new clean filename
            entry['link'] = f"/episodes/{new_filename}"
            updated_count += 1
            
            # Optional: Fix any internal canonical links/og:urls inside the HTML?
            # Ideally yes, but file rename is the main request.
            
    # 3. Save updated JSON
    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"Renamed and relocated {updated_count} episodes to '{NEW_EPISODES_DIR}'.")

if __name__ == "__main__":
    rename_files()
