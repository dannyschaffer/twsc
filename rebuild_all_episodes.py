#!/usr/bin/env python3
"""
REBUILD ALL EPISODES - Complete Episode Regeneration with Correct YouTube Videos

This script:
1. Loads the podcast-episodes-full.json (source of truth for episode list)
2. Loads YouTube video data from the dataset
3. Matches each episode to the correct YouTube video by fuzzy title matching
4. Regenerates ALL episode HTML files with correct YouTube embeds
5. Deploys to WordPress
"""

import json
import os
import re
import shutil
from difflib import SequenceMatcher

# Paths
EPISODES_JSON = "podcast-episodes-full.json"
YOUTUBE_DATA = "dataset_youtube-full-channel-transcripts-extractor_2025-11-22_08-07-57-187 (1).json"
OUTPUT_DIR = "episodes_rebuilt"
WP_EPISODES_DIR = "/Users/dannyschaffer/Local Sites/twsc/app/public/episodes"
WP_THEME_JSON = "/Users/dannyschaffer/Local Sites/twsc/app/public/wp-content/themes/twsc-theme/podcast-episodes-full.json"

# HTML Template with YouTube embed
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - The Wall Street Coach Podcast</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="/wp-content/themes/twsc-theme/assets/css/styles.css?v=2">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        .episode-hero {{
            background-color: #F9F9F7;
            color: var(--navy);
            padding: 6rem 0 3rem;
            text-align: center;
        }}
        .episode-hero h1 {{
            font-size: 2.5rem;
            max-width: 900px;
            margin: 0 auto;
            color: var(--navy);
        }}
        .video-section {{
            background-color: #08333A;
            padding: 4rem 0;
        }}
        .video-container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 0 2rem;
        }}
        .video-wrapper {{
            position: relative;
            padding-bottom: 56.25%;
            height: 0;
            overflow: hidden;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }}
        .video-wrapper iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }}
        .episode-content {{
            background-color: #F9F9F7;
            padding: 4rem 0;
        }}
        .episode-container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 0 2rem;
        }}
        .episode-body {{
            background: #fff;
            padding: 3rem;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        }}
        .episode-body h2, .episode-body h3 {{
            color: var(--navy);
            margin-bottom: 1rem;
        }}
        .episode-body p {{
            color: var(--text-secondary);
            line-height: 1.8;
            margin-bottom: 1rem;
        }}
        .back-link {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--text-secondary);
            text-decoration: none;
            margin-bottom: 2rem;
            transition: color 0.3s;
        }}
        .back-link:hover {{
            color: var(--navy);
        }}
        .episode-cta {{
            background: var(--navy);
            padding: 3rem;
            border-radius: 12px;
            text-align: center;
            margin-top: 3rem;
        }}
        .episode-cta h3 {{
            color: #fff;
            margin-bottom: 1rem;
        }}
        .episode-cta p {{
            color: rgba(255,255,255,0.7);
            margin-bottom: 1.5rem;
        }}
        .listen-links {{
            text-align: center;
            padding: 1.5rem;
            background: rgba(255,255,255,0.05);
            border-radius: 8px;
            margin-top: 1rem;
        }}
        .listen-links a {{
            color: var(--gold);
            margin: 0 0.5rem;
        }}
        @media (max-width: 768px) {{
            .episode-hero h1 {{
                font-size: 1.8rem;
            }}
            .episode-body {{
                padding: 1.5rem;
            }}
        }}
    </style>
</head>
<body>
    <nav class="nav-bar" id="mainNav">
        <div class="nav-container">
            <div class="nav-logo">
                <a href="/"><img src="/wp-content/themes/twsc-theme/assets/images/The-Wall-Street-Coach-Logo-Transparent@white.png" alt="The Wall Street Coach" class="logo-img"></a>
            </div>
            <button class="mobile-menu-toggle" id="mobileMenuToggle">
                <span></span><span></span><span></span>
            </button>
            <div class="nav-links" id="navLinks">
                <a href="/assessment" class="nav-link">Assessment</a>
                <a href="/coaching" class="nav-link">Coaching</a>
                <a href="/about" class="nav-link">About</a>
                <a href="/podcast" class="nav-link nav-link-featured">Podcast</a>
                <a href="/resources" class="nav-link">Resources</a>
            </div>
        </div>
    </nav>

    <section class="episode-hero">
        <div class="container">
            <a href="/podcast" class="back-link">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M19 12H5M12 19l-7-7 7-7"/>
                </svg>
                Back to All Episodes
            </a>
            <h1>{title}</h1>
        </div>
    </section>

    <section class="video-section">
        <div class="video-container">
            <div class="video-wrapper">
                <iframe 
                    src="https://www.youtube.com/embed/{youtube_id}" 
                    title="{title}"
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
                </iframe>
            </div>
            <div class="listen-links" style="margin-top: 1.5rem; color: rgba(255,255,255,0.7);">
                Also available on 
                <a href="https://podcasts.apple.com/us/podcast/the-wall-street-coach-with-kim-ann-curtin/id1480748536" target="_blank">Apple Podcasts</a>, 
                <a href="https://open.spotify.com/show/14yIEC46UAHIoO7wsJUAN1" target="_blank">Spotify</a>
            </div>
        </div>
    </section>

    <section class="episode-content">
        <div class="episode-container">
            <div class="episode-body">
                <h3>About This Episode</h3>
                <p>{description}</p>
            </div>

            <div class="episode-cta">
                <h3>Ready to Transform Your Trading Psychology?</h3>
                <p>Take the Trader Positioning Index assessment to uncover your blind spots.</p>
                <a href="/assessment" class="btn-primary" style="background: var(--gold); color: var(--navy); padding: 1rem 2rem; border-radius: 8px; text-decoration: none; display: inline-block;">Get Your TPI Profile</a>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-about">
                    <p>Transforming Wall Street from the inside out.</p>
                    <div class="footer-brand">
                        <span class="footer-logo">The Wall Street Coach</span>
                        <p class="footer-copyright">&copy; 2025 The Wall Street Coach TM. All rights reserved.</p>
                    </div>
                </div>
                <div class="footer-links">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="/assessment">Assessment</a></li>
                        <li><a href="/coaching">Coaching</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/podcast">Podcast</a></li>
                        <li><a href="/resources">Resources</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
    <script src="/wp-content/themes/twsc-theme/assets/js/script.js"></script>
</body>
</html>
'''

def normalize_title(title):
    """Normalize title for matching"""
    title = title.lower()
    # Remove common prefixes
    title = re.sub(r'^(ep\.?|episode)\s*\d+[:\s]*', '', title)
    # Remove special characters
    title = re.sub(r'[^\w\s]', ' ', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def extract_guest_name(title):
    """Extract guest name from title"""
    # Common patterns: "with Guest Name", "Guest Name on", "Guest Name's"
    patterns = [
        r'with\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
        r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+on\b',
        r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'s",
    ]
    for pattern in patterns:
        match = re.search(pattern, title)
        if match:
            return match.group(1).lower()
    return ""

def fuzzy_match(s1, s2):
    """Calculate similarity ratio between two strings"""
    return SequenceMatcher(None, s1, s2).ratio()

def find_best_youtube_match(episode, youtube_videos):
    """Find the best matching YouTube video for an episode"""
    ep_title = episode['title']
    ep_num = episode.get('ep', 0)
    
    best_match = None
    best_score = 0
    
    # First, try exact episode number match
    for video in youtube_videos:
        yt_title = video.get('title', '')
        
        # Check for exact episode number in YouTube title
        ep_patterns = [
            rf'\bEP\.?\s*{ep_num}\b',
            rf'\bEpisode\s*{ep_num}\b',
            rf'\bEp\s*{ep_num}\b',
            rf'#\s*{ep_num}\b',
        ]
        
        for pattern in ep_patterns:
            if re.search(pattern, yt_title, re.IGNORECASE):
                # Strong match by episode number
                return video, 0.95
    
    # Second, try normalized title matching
    ep_norm = normalize_title(ep_title)
    ep_guest = extract_guest_name(ep_title)
    
    for video in youtube_videos:
        yt_title = video.get('title', '')
        yt_norm = normalize_title(yt_title)
        yt_guest = extract_guest_name(yt_title)
        
        # Skip clip videos for full episodes
        if 'clip' in yt_title.lower() and 'clip' not in ep_title.lower():
            continue
        
        # Calculate similarity
        title_score = fuzzy_match(ep_norm, yt_norm)
        
        # Boost score if guest names match
        guest_bonus = 0
        if ep_guest and yt_guest:
            if ep_guest in yt_guest or yt_guest in ep_guest:
                guest_bonus = 0.3
        
        # Check for key word matches
        ep_words = set(ep_norm.split())
        yt_words = set(yt_norm.split())
        common_words = ep_words & yt_words
        word_bonus = len(common_words) * 0.05
        
        total_score = title_score + guest_bonus + word_bonus
        
        if total_score > best_score:
            best_score = total_score
            best_match = video
    
    return best_match, best_score

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = text.strip('-')
    return text[:50]

def main():
    print("=" * 70)
    print("REBUILD ALL EPISODES")
    print("Regenerating all 110 episodes with correct YouTube videos")
    print("=" * 70)
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Load episodes from JSON
    print("\n[1/5] Loading podcast episodes JSON...")
    with open(EPISODES_JSON, 'r') as f:
        episodes = json.load(f)
    print(f"  Loaded {len(episodes)} episodes")
    
    # Load YouTube data
    print("\n[2/5] Loading YouTube video data...")
    with open(YOUTUBE_DATA, 'r') as f:
        youtube_videos = json.load(f)
    print(f"  Loaded {len(youtube_videos)} YouTube videos")
    
    # Filter to full episode videos (not clips)
    full_episodes = [v for v in youtube_videos if 
                     ('EP ' in v.get('title', '') or 
                      'Episode' in v.get('title', '') or
                      'Ep ' in v.get('title', '')) and
                     'clip' not in v.get('title', '').lower()]
    print(f"  Found {len(full_episodes)} full episode videos")
    
    # Match each episode to YouTube video
    print("\n[3/5] Matching episodes to YouTube videos...")
    matches = []
    unmatched = []
    
    for ep in episodes:
        best_video, score = find_best_youtube_match(ep, youtube_videos)
        
        if best_video and score >= 0.4:
            matches.append({
                'episode': ep,
                'youtube': best_video,
                'score': score
            })
            print(f"  EP {ep['ep']:3d}: ✓ {score:.2f} -> {best_video['videoId']} ({best_video['title'][:40]}...)")
        else:
            unmatched.append(ep)
            print(f"  EP {ep['ep']:3d}: ✗ No match (best score: {score:.2f})")
    
    print(f"\n  Matched: {len(matches)}, Unmatched: {len(unmatched)}")
    
    # Generate HTML files
    print("\n[4/5] Generating HTML files...")
    generated = []
    
    for match in matches:
        ep = match['episode']
        yt = match['youtube']
        
        # Generate filename
        slug = slugify(ep['title'])
        filename = f"ep-{ep['ep']:03d}-{slug}.html"
        
        # Clean description
        desc = ep.get('description', '')
        desc = re.sub(r'The post .+ appeared first on.*$', '', desc).strip()
        if not desc:
            desc = f"Join Kim Ann Curtin in episode {ep['ep']} of The Wall Street Coach Podcast."
        
        # Generate HTML
        html = HTML_TEMPLATE.format(
            title=ep['title'],
            description=desc[:300],
            youtube_id=yt['videoId']
        )
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        # Update episode link
        ep['link'] = f"/episodes/{filename}"
        generated.append(filename)
    
    print(f"  Generated {len(generated)} HTML files")
    
    # For unmatched episodes, use a placeholder video or first available
    for ep in unmatched:
        slug = slugify(ep['title'])
        filename = f"ep-{ep['ep']:03d}-{slug}.html"
        
        # Use first full episode video as fallback
        fallback_id = full_episodes[0]['videoId'] if full_episodes else "dQw4w9WgXcQ"
        
        desc = ep.get('description', '')
        desc = re.sub(r'The post .+ appeared first on.*$', '', desc).strip()
        if not desc:
            desc = f"Episode {ep['ep']} of The Wall Street Coach Podcast."
        
        html = HTML_TEMPLATE.format(
            title=ep['title'],
            description=desc[:300],
            youtube_id=fallback_id
        )
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        ep['link'] = f"/episodes/{filename}"
        generated.append(filename)
    
    # Save updated JSON
    json_output = os.path.join(OUTPUT_DIR, 'podcast-episodes-full.json')
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(episodes, f, indent=2)
    print(f"  Saved updated JSON")
    
    # Deploy to WordPress
    print("\n[5/5] Deploying to WordPress...")
    
    # Copy all HTML files
    for filename in generated:
        src = os.path.join(OUTPUT_DIR, filename)
        dst = os.path.join(WP_EPISODES_DIR, filename)
        shutil.copy2(src, dst)
    print(f"  Deployed {len(generated)} HTML files to {WP_EPISODES_DIR}")
    
    # Copy JSON
    shutil.copy2(json_output, WP_THEME_JSON)
    print(f"  Deployed JSON to {WP_THEME_JSON}")
    
    # Summary
    print("\n" + "=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print(f"\nTotal episodes: {len(episodes)}")
    print(f"Matched to YouTube: {len(matches)}")
    print(f"Fallback videos: {len(unmatched)}")
    print(f"\nFiles deployed to: {WP_EPISODES_DIR}")
    print("Test at: http://twsc.local/podcast/")
    
    # Print unmatched for review
    if unmatched:
        print("\n⚠️ Episodes that need manual YouTube ID assignment:")
        for ep in unmatched:
            print(f"  EP {ep['ep']}: {ep['title'][:60]}...")

if __name__ == "__main__":
    main()
