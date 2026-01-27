import json
import os
import re
from difflib import SequenceMatcher

EPISODES_DIR = 'episodes'
JSON_PATH = 'podcast-episodes-full.json'

def clean_text(text):
    if not text: return ""
    # Normalize: lowercase, remove non-alphanumeric, remove "episode X", "ep X"
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    # Remove common prefixes/suffixes to focus on the core topic/guest
    text = re.sub(r'\bep\s*\d+\b', '', text)
    text = re.sub(r'\bepisode\s*\d+\b', '', text)
    text = re.sub(r'\bthe wall street coach\b', '', text)
    text = re.sub(r'\bpodcast\b', '', text)
    return " ".join(text.split())

def get_file_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Priority 1: H1 tag
            match = re.search(r'<h1.*?>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
            # Priority 2: Title tag
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).split('-')[0].strip()
    except:
        pass
    return ""

def similar(a, b):
    # Ratio of similarity
    return SequenceMatcher(None, a, b).ratio()

def main():
    print("Scanning HTML files...")
    # 1. Index all HTML files by their extracted Titles
    file_map = [] # List of {'filename': ..., 'raw_title': ..., 'clean_title': ...}
    
    files = os.listdir(EPISODES_DIR)
    for f in files:
        if not f.endswith(".html"): continue
        path = os.path.join(EPISODES_DIR, f)
        title = get_file_title(path)
        if title:
            file_map.append({
                'filename': f,
                'raw_title': title,
                'clean_title': clean_text(title)
            })
            
    print(f"Indexed {len(file_map)} files.")

    # 2. Iterate JSON and find best match
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)
        
    updated_count = 0
    
    for entry in data:
        ep_num = entry.get('ep')
        json_title = entry.get('title', '')
        # json_desc = entry.get('description', '')
        
        clean_json_title = clean_text(json_title)
        
        best_match = None
        best_score = 0
        
        # Try to find best match in file_map
        for fmeta in file_map:
            # Score based on title similarity
            score = similar(clean_json_title, fmeta['clean_title'])
            
            # Boost if specific unique words match? (like simple "guest name" check)
            # This helps if titles are phrased very differently
            
            if score > best_score:
                best_score = score
                best_match = fmeta
                
        # Must have a reasonable threshold
        if best_match:
            # print(f"Ep {ep_num}: '{json_title}' \n   -> '{best_match['raw_title']}' ({best_score:.2f}) [{best_match['filename']}]")
            
            # Auto-accept if score is high enough
            if best_score > 0.4: # 40% similarity is usually enough for "guest name + topic" overlap
                entry['link'] = f'/episodes/{best_match["filename"]}'
                updated_count += 1
            else:
                # If score is low, maybe title is missing guest name but it's in filename?
                # Check normalized filename against title
                fn_clean = clean_text(best_match['filename'].replace('.html', '').replace('-', ' '))
                score_fn = similar(clean_json_title, fn_clean)
                
                if score_fn > 0.4:
                     entry['link'] = f'/episodes/{best_match["filename"]}'
                     updated_count += 1
                     # print(f"   (Matched via Filename: {score_fn:.2f})")
                else:
                     print(f"LOW CONFIDENCE Ep {ep_num}: {json_title} vs {best_match['raw_title']} ({best_score})")

    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"Updated {updated_count} episodes.")

if __name__ == "__main__":
    main()
