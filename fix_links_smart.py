import json
import re

# Correct mapping for problematic episodes
manual_mapping = {
    78: "ep-069-ep-78-the-big-short-legendary-investor-steven-eisman-talks-2.html",
    77: "ep-077-ep-79-mari-hincapie---on-a-mission-to-inspire-female-traders.html", # Wait, let's verify these based on title content if possible
    # Actually, the file names seem to have mixed episode numbers in them like "ep-069-ep-78..."
    # This suggests the auto-numbering in the filename might be the "index" and the "ep-XX" in the text is the real one.
}

def load_json():
    with open('podcast-episodes-full.json', 'r') as f:
        return json.load(f)

def clean_filename_ep_num(filename):
    # Extracts the "real" episode number if it exists in the title part of the filename
    # Example: "ep-069-ep-78-the-big-short..." -> 78
    # Example: "ep-001-ep02-practice..." -> 2
    
    # Try to find "ep-XX" or "episode-XX" pattern in the filename string *after* the initial numbering
    # The file format seems to be: ep-{INDEX}-{TITLE}.html
    
    # Let's look for patterns like "-ep-78-", "-episode-78-", "-ep78-"
    match = re.search(r'[-_](?:ep|episode)[-_]?(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def fix_json_links():
    import os
    
    # Load JSON
    data = load_json()
    
    # Get all HTML files
    episodes_dir = 'episodes'
    files = os.listdir(episodes_dir)
    html_files = [f for f in files if f.endswith('.html')]
    
    # Create a map of Real_Ep_Num -> Filename
    ep_map = {}
    
    for filename in html_files:
        # Strategy 1: Trust the manual override logic?
        # Strategy 2: Parse the filename.
        # file: ep-069-ep-78-the-big-short...
        
        # First, try to extract the explicit "ep-XX" from the title part
        derived_ep = clean_filename_ep_num(filename)
        
        if derived_ep:
            ep_map[derived_ep] = filename
            # print(f"Mapped Ep {derived_ep} to {filename}")
        else:
            # Fallback: The initial number might be the episode number for some?
            # file: ep-001-ep02... -> initial is 001, title says ep02.
            # file: ep-654-the-hidden-trap... -> initial is 654.
            
            match = re.match(r'ep-(\d+)-', filename)
            if match:
                index_num = int(match.group(1))
                # Store this as a fallback if we don't have a specific map yet
                if index_num not in ep_map:
                    ep_map[index_num] = filename

    # Apply updates
    updated_count = 0
    for episode in data:
        ep_num = episode.get('ep')
        
        # Override for specific known issue
        if ep_num == 78:
             # Look for the file that actually contains "steven-eisman"
             target_file = next((f for f in html_files if "steven-eisman" in f and "ep-78" in f), None)
             if not target_file:
                 # Try lazier match
                  target_file = next((f for f in html_files if "steven-eisman" in f), None)
             
             if target_file:
                 episode['link'] = f'/episodes/{target_file}'
                 updated_count += 1
                 continue

        if ep_num in ep_map:
            episode['link'] = f'/episodes/{ep_map[ep_num]}'
            updated_count += 1
        else:
             # Last resort fuzzy match by title?
             # Normalize title
             safe_title = re.sub(r'[^a-zA-Z0-9]', '', episode['title'].lower())
             for fname in html_files:
                 safe_fname = re.sub(r'[^a-zA-Z0-9]', '', fname.lower())
                 if safe_fname.endswith('html') and safe_title[:20] in safe_fname: # simple check
                      episode['link'] = f'/episodes/{fname}'
                      updated_count += 1
                      break

    with open('podcast-episodes-full.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"Refined {updated_count} links.")

if __name__ == "__main__":
    fix_json_links()
