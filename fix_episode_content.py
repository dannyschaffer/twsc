#!/usr/bin/env python3
"""
Episode Content Fixer - Fixes HTML files to have correct content matching episode titles

The problem: HTML files exist but have WRONG content (wrong videos, wrong text).
The solution: Use the JSON as source of truth, and regenerate HTML files with correct content
scraped from the main site's episode pages.
"""

import requests
from bs4 import BeautifulSoup
import re
import os
import json
import time
import shutil

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

# Paths
SOURCE_JSON = "podcast-episodes-full.json"
WP_EPISODES_DIR = "/Users/dannyschaffer/Local Sites/twsc/app/public/episodes"
WP_THEME_JSON = "/Users/dannyschaffer/Local Sites/twsc/app/public/wp-content/themes/twsc-theme/podcast-episodes-full.json"
OUTPUT_DIR = "episodes_fixed"

# Main site base URL  
BASE_URL = "https://thewallstreetcoach.com"

# Episode page URL patterns we found on the main site
EPISODE_URLS = {
    110: "/blog/2025/11/market-wizards-secrets-coyle/",
    109: "/blog/2025/10/ep-109-why-99-of-profitable-traders-use-a-journal-with-edgewonk/",
    108: "/blog/2025/06/ep-108-mastering-risk-and-self-awareness-with-gregg-sciabica/",
    107: "/blog/2025/04/ep-107-unshakeable-how-jeremy-aguiar-plays-the-long-game-in-day-trading/",
    106: "/blog/2025/03/ep-106-mastering-risk-w-neuroscience-w-dr-michael-platt/",
    105: "/blog/2025/02/the-mindset-training-of-top-traders-with-jeff-holden-of-smb-capital/",
    104: "/blog/2025/02/ep-104-from-2000-to-1-million-matthew-monacos-road-to-trading-success/",
    103: "/blog/2024/12/ep-103-trader-bryce-tuohey/",
    102: "/blog/2024/11/ep-102-turning-2k-into-1-6-million-with-eduardo-briceno/",
    101: "/blog/2024/10/ep-101-how-to-biohack-your-trading/",
    100: "/blog/2024/10/ep-100-teacher-to-trading-mentor-breaking-stereotypes-with-danielle-shay/",
    99: "/blog/2024/09/ep-99-one-good-trade-with-mike-bellafiore/",
    98: "/blog/2024/09/ep-98-trading-mastery-uncovering-success-with-pradeep-bonde/",
    97: "/blog/2024/06/ep-97-why-most-traders-fail-at-risk-management-brianleetrades/",
}

# WordPress-compatible HTML template (matches current site styling)
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
        .audio-section {{
            background-color: #1a1a2e;
            padding: 2rem 0;
        }}
        .audio-container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 0 2rem;
            text-align: center;
            color: #fff;
        }}
        .audio-container h3 {{
            color: #fff;
            margin-bottom: 1rem;
        }}
        .audio-container audio {{
            width: 100%;
            max-width: 600px;
        }}
        .audio-container p {{
            color: rgba(255,255,255,0.7);
            margin-top: 1rem;
        }}
        .audio-container a {{
            color: var(--gold);
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
            margin-top: 1.5rem;
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

    {media_section}

    <section class="episode-content">
        <div class="episode-container">
            <div class="episode-body">
                {body_content}
            </div>

            <div class="episode-cta">
                <h3>Ready to Transform Your Trading Psychology?</h3>
                <p>Take the Trader Positioning Index assessment to uncover your blind spots.</p>
                <a href="/assessment" class="btn-primary" style="background: var(--gold); color: var(--navy);">Get Your TPI Profile</a>
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

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = text.strip('-')
    return text[:50]

def scrape_episode_from_main_site(ep_num, url_path):
    """Scrape episode content from main site"""
    url = BASE_URL + url_path
    print(f"  Scraping: {url}")
    
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code != 200:
            print(f"    HTTP {resp.status_code}")
            return None
        
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # Extract YouTube video ID
        youtube_id = None
        iframes = soup.find_all('iframe', src=True)
        for iframe in iframes:
            src = iframe.get('src', '')
            yt_match = re.search(r'youtube\.com/embed/([a-zA-Z0-9_-]{11})', src)
            if yt_match:
                youtube_id = yt_match.group(1)
                break
        
        # Extract audio URL
        audio_url = None
        audio_links = soup.find_all('a', href=re.compile(r'blubrry.*\.mp3'))
        if audio_links:
            audio_url = audio_links[0].get('href')
        
        # Extract body content
        content_div = soup.find('div', class_='entry-content') or soup.find('article')
        body_paragraphs = []
        if content_div:
            for p in content_div.find_all('p'):
                text = p.get_text(strip=True)
                if text and len(text) > 30:
                    if not any(skip in text for skip in ['Podcast:', 'Download', 'Play in new window', 'Duration:']):
                        body_paragraphs.append(f"<p>{text}</p>")
        
        body_content = "\n".join(body_paragraphs[:3])  # First 3 paragraphs
        
        return {
            'youtube_id': youtube_id,
            'audio_url': audio_url,
            'body_content': body_content
        }
        
    except Exception as e:
        print(f"    Error: {e}")
        return None

def generate_media_section(youtube_id, audio_url, title):
    """Generate the video/audio section HTML"""
    sections = []
    
    if youtube_id:
        sections.append(f'''<section class="video-section">
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
        </div>
    </section>''')
    
    if audio_url:
        sections.append(f'''<section class="audio-section">
        <div class="audio-container">
            <h3>🎧 Listen to this Episode</h3>
            <audio controls>
                <source src="{audio_url}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
            <p>Also available on 
                <a href="https://podcasts.apple.com/us/podcast/the-wall-street-coach-with-kim-ann-curtin/id1480748536" target="_blank">Apple Podcasts</a>, 
                <a href="https://open.spotify.com/show/14yIEC46UAHIoO7wsJUAN1" target="_blank">Spotify</a>, and 
                <a href="https://www.youtube.com/channel/UCuApZQaw2UATpJums6cw3HA" target="_blank">YouTube</a>
            </p>
        </div>
    </section>''')
    
    if not sections:
        sections.append('''<section class="audio-section">
        <div class="audio-container">
            <p>Listen to this episode on 
                <a href="https://podcasts.apple.com/us/podcast/the-wall-street-coach-with-kim-ann-curtin/id1480748536" target="_blank">Apple Podcasts</a>, 
                <a href="https://open.spotify.com/show/14yIEC46UAHIoO7wsJUAN1" target="_blank">Spotify</a>, or 
                <a href="https://www.youtube.com/channel/UCuApZQaw2UATpJums6cw3HA" target="_blank">YouTube</a>
            </p>
        </div>
    </section>''')
    
    return "\n\n".join(sections)

def main():
    print("=" * 70)
    print("EPISODE CONTENT FIXER")
    print("Fixing HTML files for episodes 97-110 with correct content")
    print("=" * 70)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Load the JSON source of truth
    print("\n[1/3] Loading episode data from JSON...")
    with open(SOURCE_JSON, 'r') as f:
        episodes = json.load(f)
    
    # Get episodes 97-110 from the JSON
    target_episodes = [ep for ep in episodes if ep['ep'] >= 97 and ep['ep'] <= 110]
    print(f"  Found {len(target_episodes)} episodes to fix (97-110)")
    
    # Scrape correct content from main site
    print("\n[2/3] Scraping correct content from main site...")
    fixed_episodes = []
    
    for ep in target_episodes:
        ep_num = ep['ep']
        print(f"\nEpisode {ep_num}: {ep['title'][:50]}...")
        
        if ep_num in EPISODE_URLS:
            scraped = scrape_episode_from_main_site(ep_num, EPISODE_URLS[ep_num])
            if scraped:
                if scraped.get('youtube_id'):
                    print(f"    ✓ Found YouTube: {scraped['youtube_id']}")
                if scraped.get('audio_url'):
                    print(f"    ✓ Found Audio")
                
                # Generate the fixed HTML
                media_section = generate_media_section(
                    scraped.get('youtube_id'),
                    scraped.get('audio_url'),
                    ep['title']
                )
                
                body_content = scraped.get('body_content') or f"<p>{ep['description']}</p>"
                
                html = HTML_TEMPLATE.format(
                    title=ep['title'],
                    description=ep['description'][:160],
                    media_section=media_section,
                    body_content=body_content
                )
                
                # Generate filename from link in JSON
                original_link = ep.get('link', '')
                if original_link:
                    filename = os.path.basename(original_link)
                else:
                    slug = slugify(ep['title'])
                    filename = f"ep-{ep_num:03d}-{slug}.html"
                
                filepath = os.path.join(OUTPUT_DIR, filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                
                print(f"    ✓ Saved: {filename}")
                fixed_episodes.append(filename)
            else:
                print(f"    ✗ Could not scrape")
        else:
            print(f"    ⚠ No URL mapping for episode {ep_num}")
        
        time.sleep(0.3)  # Be polite
    
    # Deploy to WordPress
    print("\n[3/3] Deploying fixed files to WordPress...")
    for filename in fixed_episodes:
        src = os.path.join(OUTPUT_DIR, filename)
        dst = os.path.join(WP_EPISODES_DIR, filename)
        shutil.copy2(src, dst)
        print(f"  ✓ Deployed: {filename}")
    
    print("\n" + "=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print(f"\nFixed {len(fixed_episodes)} episode files.")
    print(f"Files deployed to: {WP_EPISODES_DIR}")
    print("\nTest at: http://twsc.local/podcast/")

if __name__ == "__main__":
    main()
