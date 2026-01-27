import os
import re
import json

EPISODES_DIR = 'episodes'
THEME_ASSET_PATH = '/wp-content/themes/twsc-theme/assets'
SITE_URL = ''  # Relative paths from root

def update_html_files():
    episode_map = {} # ep_number -> filename

    if not os.path.exists(EPISODES_DIR):
        print("Episodes directory not found.")
        return

    files = os.listdir(EPISODES_DIR)
    
    for filename in files:
        if not filename.endswith('.html'):
            continue
            
        filepath = os.path.join(EPISODES_DIR, filename)
        
        # Extract episode number for mapping
        # Format: ep-001-... or ep-110-...
        match = re.match(r'ep-(\d+)-', filename)
        if match:
            ep_num = int(match.group(1))
            episode_map[ep_num] = filename

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Fix Navigation Links
        content = content.replace('href="../index.html"', 'href="/"')
        content = content.replace('href="../tpi.html"', 'href="/assessment"')
        content = content.replace('href="../coaching.html"', 'href="/coaching"')
        content = content.replace('href="../about.html"', 'href="/about"')
        content = content.replace('href="../podcast.html"', 'href="/podcast"')
        content = content.replace('href="../resources.html"', 'href="/resources"')
        
        # 2. Fix Asset Paths (CSS, JS)
        # Note: In the source they are "../styles.css", in WP they are inside assets/css
        content = content.replace('href="../styles.css?v=2"', f'href="{THEME_ASSET_PATH}/css/styles.css?v=2"')
        content = content.replace('href="../styles.css"', f'href="{THEME_ASSET_PATH}/css/styles.css"')
        content = content.replace('href="../styles-enhanced.css"', f'href="{THEME_ASSET_PATH}/css/styles.css"') # Map both to main styles or specific if needed
        
        content = content.replace('src="../script.js"', f'src="{THEME_ASSET_PATH}/js/script.js"')

        # 3. Fix Images
        # Source: src="../TWSCsite/Images/..."
        # Target: src="/wp-content/themes/twsc-theme/assets/images/..."
        content = content.replace('src="../TWSCsite/Images/', f'src="{THEME_ASSET_PATH}/images/')
        content = content.replace('src="TWSCsite/Images/', f'src="{THEME_ASSET_PATH}/images/') # Just in case

        # 4. Fix Back Link just in case
        content = content.replace('href="../podcast.html"', 'href="/podcast"')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    return episode_map

def update_json_links(episode_map):
    json_path = 'podcast-episodes-full.json'
    if not os.path.exists(json_path):
        print("JSON file not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_count = 0
    for episode in data:
        ep_num = episode.get('ep')
        if ep_num in episode_map:
            # Update link to point to the static HTML file
            # content will be at /episodes/filename.html
            episode['link'] = f'/episodes/{episode_map[ep_num]}'
            updated_count += 1
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Updated {updated_count} episodes in JSON.")

if __name__ == "__main__":
    print("Starting batch update...")
    feature_map = update_html_files()
    if feature_map:
        update_json_links(feature_map)
    print("Done.")
