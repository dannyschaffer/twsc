import json
import re
import os
from collections import Counter

EPISODES_DIR = 'episodes'
JSON_PATH = 'podcast-episodes-full.json'

def get_text_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read().lower()
    except:
        return ""

def extract_keywords(text):
    # simple extraction of words > 4 chars
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = [w for w in text.split() if len(w) > 4 and w.lower() not in ['episode', 'about', 'podcast', 'coach', 'trading', 'trader', 'market', 'street', 'wall', 'interview', 'discuss']]
    return set(words)

def fix_links_content():
    print("Loading file contents...")
    files_data = []
    for f in os.listdir(EPISODES_DIR):
        if not f.endswith('.html'): continue
        path = os.path.join(EPISODES_DIR, f)
        content = get_text_content(path)
        files_data.append({
            'filename': f,
            'content': content
        })
    
    with open(JSON_PATH, 'r') as f:
        json_data = json.load(f)
        
    updated = 0
    
    for entry in json_data:
        # Skip if already looks corrected (high number file) or we want to force re-check?
        # Let's force re-check for episodes that have specific guests or strong keywords
        
        ep_num = entry['ep']
        title = entry.get('title', '')
        desc = entry.get('description', '')
        
        # Keywords from Title + Description
        search_text = title + " " + desc
        keywords = extract_keywords(search_text)
        
        if not keywords: continue
        
        best_match = None
        best_score = 0
        
        for fdata in files_data:
            score = 0
            file_content = fdata['content']
            
            # Simple keyword matching
            for kw in keywords:
                if kw.lower() in file_content:
                    score += 1
            
            # Boost if filename number matches (only for high numbers?)
            # No, user said file numbering is messed up.
            
            # Normalize by content length? slightly.
            # But mostly we care about specific unique words (names).
            
            if score > best_score:
                best_score = score
                best_match = fdata
        
        # Threshold: Need at least 2 keywords or 30% of keywords matching
        if best_match and best_score >= max(2, len(keywords) * 0.4):
             # Only update if different or currently points to "clip" content
             curr_link = entry.get('link', '')
             if best_match['filename'] not in curr_link:
                 entry['link'] = f'/episodes/{best_match["filename"]}'
                 updated += 1
                 # print(f"Matched Ep {ep_num} ({title[:30]}...) -> {best_match['filename']} (Score: {best_score})")

    with open(JSON_PATH, 'w') as f:
        json.dump(json_data, f, indent=4)
        
    print(f"Content search updated {updated} links.")

if __name__ == "__main__":
    fix_links_content()
