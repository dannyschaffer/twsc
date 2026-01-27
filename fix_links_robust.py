import json
import re
import os
from difflib import SequenceMatcher

EPISODES_DIR = 'episodes'
JSON_PATH = 'podcast-episodes-full.json'

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def clean_title(text):
    if not text: return ""
    # Remove special chars and lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    # Remove common prefixes like 'ep', 'episode', etc.
    text = re.sub(r'\b(ep|episode)\s*\d+', '', text)
    return text.strip()

def get_html_title(filepath):
    """Refined extraction of title from HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Try to grab H1 as it's usually the main title
            match = re.search(r'<h1.*?>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
            # Fallback to <title> tag
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if match:
                title = match.group(1).split('-')[0].strip() # Remove " - The Wall Street Coach"
                return title
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return ""

def fix_links_robust():
    print("Loading data...")
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)
        
    files = [f for f in os.listdir(EPISODES_DIR) if f.endswith('.html')]
    
    # Pre-process file titles
    file_metadata = []
    print(f"Scanning {len(files)} HTML files...")
    for filename in files:
        path = os.path.join(EPISODES_DIR, filename)
        raw_title = get_html_title(path)
        
        # Also Extract episode number from filename if obvious
        # ep-110-... -> 110
        # ep-001-ep02-... -> 02 (priority)
        ep_num = None
        
        # Check for inner ep number: ep-069-ep-78-...
        inner_match = re.search(r'[-_](?:ep|episode)[-_]?(\d+)', filename, re.IGNORECASE)
        if inner_match:
            ep_num = int(inner_match.group(1))
        else:
             # Fallback to prefix
             prefix_match = re.match(r'ep-(\d+)-', filename)
             if prefix_match:
                 ep_num = int(prefix_match.group(1))

        file_metadata.append({
            'filename': filename,
            'raw_title': raw_title,
            'clean_title': clean_title(raw_title),
            'ep_num': ep_num
        })

    updated_count = 0
    
    print("Matching episodes...")
    for entry in data:
        json_ep = entry.get('ep')
        json_title = entry.get('title', '')
        clean_json_title = clean_title(json_title)
        
        best_match = None
        best_score = 0
        
        # Priority 1: Exact Episode Number Match (if filename has inner secondary number)
        # Note: We found that the inner number is usually the "real" one for migrated files
        candidate_by_num = [f for f in file_metadata if f['ep_num'] == json_ep]
        
        # If we have number matches, check titles to be sure (limit false positives)
        if candidate_by_num:
            # If multiple, pick best title match
            for cand in candidate_by_num:
                score = similar(clean_json_title, cand['clean_title'])
                if score > best_score:
                    best_score = score
                    best_match = cand
            
            # If the score is decent, take it. 
            # If score is low, it might be a wrong number extraction (e.g. ep-2023 for year vs ep number)
            if best_score > 0.3: 
                entry['link'] = f'/episodes/{best_match["filename"]}'
                updated_count += 1
                continue
        
        # Priority 2: Fuzzy Title Match
        # If no number match or low confidence, search all files by title
        for file_meta in file_metadata:
            score = similar(clean_json_title, file_meta['clean_title'])
            if score > best_score:
                best_score = score
                best_match = file_meta
        
        # Threshold for title match acceptance
        if best_match and best_score > 0.6: # 60% similarity
            entry['link'] = f'/episodes/{best_match["filename"]}'
            updated_count += 1
            # print(f"Matched Ep {json_ep}: '{json_title}' -> '{best_match['raw_title']}' ({best_score:.2f})")
        else:
            print(f"Could not reliably match Ep {json_ep}: {json_title}")

    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"Updated {updated_count} episodes with robust title matching.")

if __name__ == "__main__":
    fix_links_robust()
