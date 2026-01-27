#!/usr/bin/env python3
"""
Fix episodes that are missing YouTube video embeds.
Adds the correct video section to HTML files that should have videos.
"""

import json
import re
from pathlib import Path

# Load the audit results
EPISODES_DIR = Path("/Users/dannyschaffer/Local Sites/twsc/app/public/episodes")
AUDIT_RESULTS = Path("/Users/dannyschaffer/Local Sites/twsc/app/public/episode_audit_results.json")

# Video section template
VIDEO_SECTION_TEMPLATE = '''
    <section class="video-section">
        <div class="video-container">
            <div class="video-wrapper">
                <iframe src="https://www.youtube.com/embed/{video_id}" title="{title}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            </div>
        </div>
    </section>
'''

def fix_missing_videos():
    """Add YouTube video embeds to episodes that are missing them."""
    
    with open(AUDIT_RESULTS, 'r', encoding='utf-8') as f:
        results = json.load(f)
    
    missing_videos = results.get('missing_video', [])
    
    if not missing_videos:
        print("No episodes missing videos!")
        return
    
    print(f"Fixing {len(missing_videos)} episodes missing YouTube videos...")
    
    for item in missing_videos:
        file_path = EPISODES_DIR / item['file']
        video_id = item['expected_video_id']
        title = item['title']
        
        if not file_path.exists():
            print(f"  ❌ File not found: {file_path}")
            continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if video section already exists
        if 'class="video-section"' in content or 'youtube.com/embed' in content:
            print(f"  ⏭️ Video already exists: {item['file']}")
            continue
        
        # Create video section HTML
        video_section = VIDEO_SECTION_TEMPLATE.format(
            video_id=video_id,
            title=title.replace('"', '&quot;')
        )
        
        # Find the best place to insert the video section
        # Option 1: After </section> that contains episode-hero
        # Option 2: Before <section class="audio-section">
        # Option 3: Before <section class="episode-content">
        
        if '<section class="audio-section">' in content:
            # Insert before audio section
            new_content = content.replace(
                '<section class="audio-section">',
                video_section + '\n    <section class="audio-section">'
            )
        elif '<section class="episode-content">' in content:
            # Insert before content section
            new_content = content.replace(
                '<section class="episode-content">',
                video_section + '\n    <section class="episode-content">'
            )
        elif '</section>' in content:
            # Find the hero section end and insert after
            # Look for the first </section> after "episode-hero"
            hero_match = re.search(r'(class="episode-hero".*?</section>)', content, re.DOTALL)
            if hero_match:
                hero_end = hero_match.end()
                new_content = content[:hero_end] + video_section + content[hero_end:]
            else:
                print(f"  ❌ Could not find insertion point: {item['file']}")
                continue
        else:
            print(f"  ❌ Could not find insertion point: {item['file']}")
            continue
        
        # Write the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ Fixed: {item['file']} (added video {video_id})")

def main():
    print("=" * 80)
    print("FIXING MISSING YOUTUBE VIDEO EMBEDS")
    print("=" * 80)
    
    fix_missing_videos()
    
    print("\n✅ Done!")

if __name__ == '__main__':
    main()
