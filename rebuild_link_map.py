import json
import re
import os
from difflib import SequenceMatcher

# Path Config
JSON_PATH = 'podcast-episodes-full.json'
EPISODES_DIR = 'episodes'

def clean_title(text):
    if not text: return ""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Remove common fillers
    removals = ['episode', 'ep', 'the wall street coach', 'podcast']
    for r in removals:
        text = text.replace(r, '')
    return " ".join(text.split())

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def extract_h1(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            match = re.search(r'<h1.*?>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
    except:
        pass
    return None

def rebuild_mapping():
    print("Indexing ALL HTML files...")
    
    # 1. Build a robust index of the files we ACTUALLY have
    file_index = []
    
    files = os.listdir(EPISODES_DIR)
    for f in files:
        if not f.endswith('.html'): continue
        
        path = os.path.join(EPISODES_DIR, f)
        h1_title = extract_h1(path)
        
        # Also clean the filename itself as a fallback title
        filename_clean = f.replace('.html', '').replace('-', ' ')
        
        file_index.append({
            'filename': f,
            'h1': h1_title,
            'clean_h1': clean_title(h1_title),
            'clean_filename': clean_title(filename_clean)
        })

    print(f"Indexed {len(file_index)} files.")
    
    # 2. Re-process the JSON
    with open(JSON_PATH, 'r') as f:
        json_data = json.load(f)
        
    matched_count = 0
    unmatched_count = 0
    
    for entry in json_data:
        ep_num = entry['ep']
        json_title = entry['title']
        clean_json_title = clean_title(json_title)
        
        # Strategy: Best Match via Score
        best_match = None
        best_score = 0.0
        match_type = "None"
        
        for file_meta in file_index:
            # Score 1: JSON Title vs HTML H1 (Strongest signal)
            score_h1 = similar(clean_json_title, file_meta['clean_h1'])
            
            if score_h1 > best_score:
                best_score = score_h1
                best_match = file_meta
                match_type = "H1 Title"
            
            # Score 2: Jason Shapiro specific (Hardcoded fixes for known issues)
            # If the user specifically mentioned Jason Shapiro -> ep 76
            # But the file might be named oddly.
            
        # Threshold enforcement
        # If we have a very high match, use it.
        # If match is weak, we check specific overrides or fail gracefully.
        
        if best_match and best_score > 0.45: # decent text match
             entry['link'] = f"/episodes/{best_match['filename']}"
             matched_count += 1
        else:
             # Fallback: Try to find "Guest Name" match if present
             guest_name = ""
             if "with" in json_title.lower():
                 guest_name = json_title.lower().split("with")[-1].strip()
             
             if guest_name and len(guest_name) > 4:
                 for file_meta in file_index:
                     if guest_name in file_meta['clean_h1'] or guest_name in file_meta['clean_filename']:
                         entry['link'] = f"/episodes/{file_meta['filename']}"
                         matched_count += 1
                         # print(f"Recovered Ep {ep_num} via Guest '{guest_name}' -> {file_meta['filename']}")
                         break
                 else:
                     unmatched_count += 1
                     # print(f"FAILED to match Ep {ep_num}: {json_title}")
             else:
                 unmatched_count += 1
                 # print(f"FAILED to match Ep {ep_num}: {json_title}")

    # 3. Output
    with open(JSON_PATH, 'w') as f:
        json.dump(json_data, f, indent=4)
        
    print(f"Rebuild Complete. Matched: {matched_count}, Failed/Unchanged: {unmatched_count}")

if __name__ == "__main__":
    rebuild_mapping()
