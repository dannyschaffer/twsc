#!/usr/bin/env python3
"""
Audit podcast episode HTML files against YouTube channel data.
Checks for:
1. Episodes missing YouTube video embeds
2. Episodes with wrong YouTube video IDs
3. Episodes that should have video but don't
"""

import json
import os
import re
from pathlib import Path

# Paths
EPISODES_DIR = Path("/Users/dannyschaffer/Local Sites/twsc/app/public/episodes")
YOUTUBE_DATA = Path("/Users/dannyschaffer/Desktop/Heynow/Clients/The Wall Street Coach/Nov 2025 Site/Antigravity/dataset_youtube-full-channel-transcripts-extractor_2025-11-22_08-07-57-187 (1).json")
PODCAST_JSON = Path("/Users/dannyschaffer/Local Sites/twsc/app/public/wp-content/themes/twsc-theme/podcast-episodes-full.json")

def load_youtube_data():
    """Load the YouTube channel data."""
    with open(YOUTUBE_DATA, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_podcast_json():
    """Load the podcast episodes JSON."""
    with open(PODCAST_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_video_id_from_html(html_content):
    """Extract YouTube video ID from HTML content."""
    # Look for YouTube embed URLs
    patterns = [
        r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
        r'youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})',
        r'youtu\.be/([a-zA-Z0-9_-]{11})'
    ]
    for pattern in patterns:
        match = re.search(pattern, html_content)
        if match:
            return match.group(1)
    return None

def extract_title_from_html(html_content):
    """Extract title from HTML h1 tag."""
    match = re.search(r'<h1[^>]*>([^<]+)</h1>', html_content)
    if match:
        return match.group(1).strip()
    return None

def normalize_title(title):
    """Normalize title for comparison."""
    if not title:
        return ""
    # Remove episode prefix, common words, and normalize
    title = re.sub(r'^EP\s*\d+:\s*', '', title, flags=re.IGNORECASE)
    title = re.sub(r'^Episode\s*\d+:\s*', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*-\s*The Wall Street Coach.*$', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*\|.*$', '', title)
    return title.lower().strip()

def find_matching_youtube_video(episode_title, youtube_data):
    """Find matching YouTube video for a given episode title."""
    norm_episode = normalize_title(episode_title)
    
    for video in youtube_data:
        norm_video = normalize_title(video.get('title', ''))
        
        # Exact match
        if norm_episode == norm_video:
            return video
        
        # One contains the other
        if norm_episode and norm_video:
            if norm_episode in norm_video or norm_video in norm_episode:
                return video
            
            # Check if most words match
            episode_words = set(norm_episode.split())
            video_words = set(norm_video.split())
            common_words = episode_words & video_words
            if len(common_words) >= min(len(episode_words), len(video_words)) * 0.6:
                return video
    
    return None

def audit_episodes():
    """Audit all episode HTML files."""
    youtube_data = load_youtube_data()
    
    results = {
        'missing_video': [],
        'wrong_video': [],
        'correct': [],
        'no_match_in_youtube': []
    }
    
    for html_file in sorted(EPISODES_DIR.glob('*.html')):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            title = extract_title_from_html(content)
            current_video_id = extract_video_id_from_html(content)
            
            # Find matching YouTube video
            matching_video = find_matching_youtube_video(title, youtube_data)
            
            if not matching_video:
                results['no_match_in_youtube'].append({
                    'file': html_file.name,
                    'title': title,
                    'has_video': current_video_id is not None,
                    'current_video_id': current_video_id
                })
            elif not current_video_id:
                # Has a matching YouTube video but no embed
                results['missing_video'].append({
                    'file': html_file.name,
                    'title': title,
                    'expected_video_id': matching_video.get('videoId'),
                    'youtube_title': matching_video.get('title')
                })
            elif current_video_id != matching_video.get('videoId'):
                # Has wrong video ID
                results['wrong_video'].append({
                    'file': html_file.name,
                    'title': title,
                    'current_video_id': current_video_id,
                    'expected_video_id': matching_video.get('videoId'),
                    'youtube_title': matching_video.get('title')
                })
            else:
                results['correct'].append({
                    'file': html_file.name,
                    'title': title,
                    'video_id': current_video_id
                })
        except Exception as e:
            print(f"Error processing {html_file.name}: {e}")
    
    return results

def main():
    print("Auditing podcast episode HTML files...")
    print("=" * 80)
    
    results = audit_episodes()
    
    print(f"\n📊 SUMMARY")
    print(f"   Correct videos: {len(results['correct'])}")
    print(f"   Missing videos: {len(results['missing_video'])}")
    print(f"   Wrong videos: {len(results['wrong_video'])}")
    print(f"   No YouTube match: {len(results['no_match_in_youtube'])}")
    
    if results['missing_video']:
        print(f"\n🔴 EPISODES MISSING YOUTUBE VIDEO ({len(results['missing_video'])}):")
        print("-" * 80)
        for item in results['missing_video'][:10]:  # Show first 10
            print(f"  File: {item['file']}")
            print(f"    Title: {item['title']}")
            print(f"    Expected Video: {item['expected_video_id']}")
            print(f"    YouTube Title: {item['youtube_title']}")
            print()
    
    if results['wrong_video']:
        print(f"\n🟠 EPISODES WITH WRONG VIDEO ID ({len(results['wrong_video'])}):")
        print("-" * 80)
        for item in results['wrong_video'][:10]:  # Show first 10
            print(f"  File: {item['file']}")
            print(f"    Title: {item['title']}")
            print(f"    Current Video: {item['current_video_id']}")
            print(f"    Expected Video: {item['expected_video_id']}")
            print(f"    YouTube Title: {item['youtube_title']}")
            print()
    
    # Save full results to JSON for further processing
    output_file = EPISODES_DIR.parent / 'episode_audit_results.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"\nFull results saved to: {output_file}")

if __name__ == '__main__':
    main()
