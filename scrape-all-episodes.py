#!/usr/bin/env python3
"""
Complete Episode Scraper - Finds ALL episodes by searching sitemap and blog archives
"""

import requests
from bs4 import BeautifulSoup
import re
import os
import json
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

OUTPUT_DIR = "episodes"
EXISTING_DATA = "podcast-episodes-full.json"

# Episode page template (same as before)
EPISODE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - The Wall Street Coach Podcast</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="../styles.css?v=2">
    <link rel="stylesheet" href="../styles-enhanced.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        .episode-hero {{ background-color: #08333A; color: #fff; padding: 6rem 0 4rem; text-align: center; }}
        .episode-content {{ background-color: #F9F9F7; padding: 4rem 0; }}
        .episode-container {{ max-width: 800px; margin: 0 auto; padding: 0 2rem; }}
        .episode-number {{ color: var(--gold); font-family: 'Space Mono', monospace; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1rem; }}
        .audio-player {{ background: #fff; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); margin-bottom: 2rem; }}
        .audio-player audio {{ width: 100%; }}
        .episode-body {{ background: #fff; padding: 3rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); }}
        .episode-body p {{ color: var(--text-secondary); line-height: 1.8; margin-bottom: 1.5rem; }}
        .episode-image {{ width: 100%; max-width: 600px; margin: 0 auto 2rem; border-radius: 12px; display: block; }}
        .episode-cta {{ background: var(--navy); padding: 3rem; border-radius: 12px; text-align: center; margin-top: 2rem; }}
        .episode-cta h3 {{ color: #fff; margin-bottom: 1rem; }}
        .episode-cta p {{ color: rgba(255,255,255,0.7); margin-bottom: 1.5rem; }}
        .back-link {{ color: rgba(255,255,255,0.7); text-decoration: none; display: inline-block; margin-bottom: 2rem; }}
        .back-link:hover {{ color: var(--gold); }}
        .nav-episodes {{ display: flex; justify-content: space-between; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(0,0,0,0.1); }}
        .nav-episodes a {{ color: var(--navy); text-decoration: none; font-weight: 600; }}
        .nav-episodes a:hover {{ color: var(--gold); }}
        .episode-tag {{ background: rgba(255,255,255,0.1); padding: 0.5rem 1rem; border-radius: 50px; font-size: 0.85rem; color: rgba(255,255,255,0.8); display: inline-block; margin-top: 1rem; }}
    </style>
</head>
<body>
    <nav class="nav-bar" id="mainNav">
        <div class="nav-container">
            <div class="nav-logo">
                <a href="../index.html"><img src="../TWSCsite/Images/The-Wall-Street-Coach-Logo-Transparent@white.png" alt="The Wall Street Coach" class="logo-img"></a>
            </div>
            <button class="mobile-menu-toggle" id="mobileMenuToggle"><span></span><span></span><span></span></button>
            <div class="nav-links" id="navLinks">
                <a href="../tpi.html" class="nav-link">The TPI Assessment</a>
                <a href="../coaching.html" class="nav-link">Coaching & Consulting</a>
                <a href="../about.html" class="nav-link">About Kim</a>
                <a href="../podcast.html" class="nav-link nav-link-featured">Podcast</a>
                <a href="../resources.html" class="nav-link">Resources</a>
            </div>
        </div>
    </nav>

    <section class="episode-hero">
        <div class="episode-container">
            <a href="../podcast.html" class="back-link">← Back to All Episodes</a>
            <div class="episode-number">Episode {ep_number}</div>
            <h1 style="font-size: 2.2rem; margin-bottom: 1rem; line-height: 1.3;">{title}</h1>
            <span class="episode-tag">{category}</span>
        </div>
    </section>

    <section class="episode-content">
        <div class="episode-container">
            <img src="{image_url}" alt="{title}" class="episode-image" onerror="this.style.display='none'">
            
            <div class="audio-player">
                <h3 style="color: var(--navy); margin-bottom: 1rem;">🎧 Listen to this Episode</h3>
                {audio_embed}
                <p style="margin-top: 1rem; font-size: 0.9rem; color: var(--text-secondary);">
                    Also available on 
                    <a href="https://podcasts.apple.com/us/podcast/the-wall-street-coach-with-kim-ann-curtin/id1480748536" target="_blank" style="color: var(--gold);">Apple Podcasts</a>, 
                    <a href="https://open.spotify.com/show/14yIEC46UAHIoO7wsJUAN1" target="_blank" style="color: var(--gold);">Spotify</a>, and 
                    <a href="https://www.youtube.com/channel/UCuApZQaw2UATpJums6cw3HA" target="_blank" style="color: var(--gold);">YouTube</a>
                </p>
            </div>

            <div class="episode-body">
                {body_content}
                
                <div class="episode-cta">
                    <h3>Ready to Transform Your Trading?</h3>
                    <p>Discover your Trader Positioning Index and unlock your psychological edge.</p>
                    <a href="../tpi.html" class="btn-primary" style="background: var(--gold); color: var(--navy);">Get Your TPI Score</a>
                </div>
            </div>

            <div class="nav-episodes">
                {prev_link}
                {next_link}
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand"><h3>The Wall Street Coach</h3><p>Transforming Wall Street from the inside out.</p></div>
                <div class="footer-links">
                    <h4>Quick Links</h4>
                    <a href="../tpi.html">TPI Assessment</a>
                    <a href="../coaching.html">Coaching</a>
                    <a href="../about.html">About Kim</a>
                    <a href="../podcast.html">Podcast</a>
                    <a href="../resources.html">Resources</a>
                </div>
                <div class="footer-contact"><h4>Connect</h4><p>Email: hello@thewallstreetcoach.com</p></div>
            </div>
            <div class="footer-bottom"><p>&copy; 2025 The Wall Street Coach. All rights reserved.</p></div>
        </div>
    </footer>
    <script src="../script.js"></script>
</body>
</html>
'''

def search_for_episode(ep_num):
    """Search for an episode URL using Google-style site search"""
    search_patterns = [
        f"https://thewallstreetcoach.com/ep-{ep_num}-",
        f"https://thewallstreetcoach.com/blog/*/ep-{ep_num}-",
    ]
    
    # Try sitemap first
    try:
        sitemap_url = "https://thewallstreetcoach.com/sitemap.xml"
        resp = requests.get(sitemap_url, headers=HEADERS, timeout=10)
        if f"ep-{ep_num}-" in resp.text.lower() or f"ep-{ep_num:02d}-" in resp.text.lower():
            # Find the URL
            matches = re.findall(rf'<loc>([^<]*ep-{ep_num}[^<]*)</loc>', resp.text, re.IGNORECASE)
            if matches:
                return matches[0]
    except:
        pass
    
    return None

def scrape_episode(url):
    """Scrape episode content from URL"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code != 200:
            return None
            
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # Title
        title_elem = soup.find('h1')
        title = title_elem.get_text(strip=True) if title_elem else "Episode"
        
        # Episode number
        ep_match = re.search(r'[Ee][Pp]\s*(\d+)', title)
        ep_number = ep_match.group(1) if ep_match else "0"
        
        # Description
        meta_desc = soup.find('meta', {'property': 'og:description'})
        description = meta_desc['content'] if meta_desc else ""
        
        # Image
        og_image = soup.find('meta', {'property': 'og:image'})
        image_url = og_image['content'] if og_image else ""
        
        # Audio
        audio_url = ""
        audio_link = soup.find('a', href=re.compile(r'blubrry.*\.mp3'))
        if audio_link:
            audio_url = audio_link.get('href')
        
        # Content
        content_div = soup.find('div', class_='entry-content') or soup.find('article')
        body_content = ""
        if content_div:
            for p in content_div.find_all('p'):
                text = p.get_text(strip=True)
                if text and len(text) > 30 and 'Podcast:' not in text and 'Download' not in text:
                    body_content += f"<p>{text}</p>\n"
        
        # Category
        category = "Mindset & Psychology"
        title_lower = title.lower()
        if 'wizard' in title_lower:
            category = "Market Wizards"
        elif 'neuro' in title_lower or 'brain' in title_lower:
            category = "Neuroscience"
        elif 'risk' in title_lower or 'strategy' in title_lower or 'journal' in title_lower:
            category = "Strategy & Tools"
        elif any(w in title_lower for w in ['million', 'success', 'journey', 'profitable', '$']):
            category = "Success Stories"
        
        return {
            'url': url,
            'title': title,
            'ep_number': ep_number,
            'description': description,
            'image_url': image_url,
            'audio_url': audio_url,
            'body_content': body_content,
            'category': category
        }
    except Exception as e:
        print(f"  Error: {e}")
        return None

def generate_page(episode, all_eps):
    """Generate HTML page"""
    ep_num = int(episode['ep_number'])
    
    # Audio embed
    if episode['audio_url']:
        audio_embed = f'<audio controls><source src="{episode["audio_url"]}" type="audio/mpeg"></audio>'
    else:
        audio_embed = '<p>Listen on your favorite podcast platform above.</p>'
    
    # Navigation
    prev_link = next_link = '<span></span>'
    ep_nums = sorted([int(e['ep_number']) for e in all_eps])
    idx = ep_nums.index(ep_num) if ep_num in ep_nums else -1
    if idx > 0:
        prev_ep = ep_nums[idx - 1]
        prev_link = f'<a href="ep-{prev_ep}.html">← Episode {prev_ep}</a>'
    if idx < len(ep_nums) - 1 and idx >= 0:
        next_ep = ep_nums[idx + 1]
        next_link = f'<a href="ep-{next_ep}.html">Episode {next_ep} →</a>'
    
    content = episode['body_content'] or f"<p>{episode['description']}</p>"
    
    html = EPISODE_TEMPLATE.format(
        title=episode['title'],
        description=episode['description'][:160] if episode['description'] else '',
        ep_number=episode['ep_number'],
        category=episode['category'],
        image_url=episode['image_url'],
        audio_embed=audio_embed,
        body_content=content,
        prev_link=prev_link,
        next_link=next_link
    )
    
    filename = f"{OUTPUT_DIR}/ep-{episode['ep_number']}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Generated: ep-{episode['ep_number']}.html")

def main():
    print("=" * 60)
    print("COMPLETE EPISODE SCRAPER")
    print("=" * 60)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Load existing data
    existing = []
    if os.path.exists(EXISTING_DATA):
        with open(EXISTING_DATA, 'r') as f:
            existing = json.load(f)
    
    existing_nums = {int(e['ep_number']) for e in existing}
    print(f"\nExisting episodes: {len(existing)}")
    print(f"Missing episode numbers to find: 1-110 excluding {sorted(existing_nums)}")
    
    # Find missing episodes by searching the blog
    print("\n[1/2] Searching for missing episodes...")
    
    # Try blog archive pages
    all_episode_urls = set()
    
    # Get URLs from blog category
    for year in range(2019, 2026):
        for month in range(1, 13):
            url = f"https://thewallstreetcoach.com/{year}/{month:02d}/"
            try:
                resp = requests.get(url, headers=HEADERS, timeout=10)
                links = re.findall(r'href="([^"]*(?:ep-\d+|episode)[^"]*)"', resp.text, re.IGNORECASE)
                for link in links:
                    if 'thewallstreetcoach.com' in link and ('ep-' in link.lower() or 'episode' in link.lower()):
                        all_episode_urls.add(link)
            except:
                pass
    
    # Also search blog category
    for page in range(1, 30):
        url = f"https://thewallstreetcoach.com/blog/category/podcast/page/{page}/" if page > 1 else "https://thewallstreetcoach.com/blog/category/podcast/"
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            if resp.status_code != 200:
                break
            links = re.findall(r'href="([^"]*blog/\d{4}/\d{2}/[^"]*)"', resp.text)
            for link in links:
                if 'ep-' in link.lower():
                    all_episode_urls.add(link)
            time.sleep(0.3)
        except:
            break
    
    print(f"  Found {len(all_episode_urls)} episode URLs from archives")
    
    # Scrape new episodes
    new_episodes = []
    for url in sorted(all_episode_urls):
        # Check if we already have this episode
        ep_match = re.search(r'ep-(\d+)', url.lower())
        if ep_match:
            ep_num = int(ep_match.group(1))
            if ep_num in existing_nums:
                continue
        
        print(f"  Scraping: {url[:60]}...")
        episode = scrape_episode(url)
        if episode and episode['ep_number'] != "0":
            new_episodes.append(episode)
            existing_nums.add(int(episode['ep_number']))
        time.sleep(0.5)
    
    # Combine all episodes
    all_episodes = existing + new_episodes
    all_episodes.sort(key=lambda x: int(x['ep_number']), reverse=True)
    
    # Save updated data
    with open(EXISTING_DATA, 'w', encoding='utf-8') as f:
        json.dump(all_episodes, f, indent=2)
    
    print(f"\n  Total episodes now: {len(all_episodes)}")
    
    # Generate all pages
    print("\n[2/2] Generating HTML pages...")
    for ep in all_episodes:
        generate_page(ep, all_episodes)
    
    # Generate podcast-data.js for the listing
    print("\n  Generating podcast-data.js...")
    js_data = "const podcastEpisodes = " + json.dumps([
        {
            'ep': int(e['ep_number']),
            'title': e['title'],
            'description': e['description'][:200] if e['description'] else '',
            'category': e['category'].lower().replace(' & ', '-').replace(' ', '-'),
            'image': e['image_url'],
            'link': f"episodes/ep-{e['ep_number']}.html"
        }
        for e in all_episodes
    ], indent=2) + ";"
    
    with open('podcast-data.js', 'w', encoding='utf-8') as f:
        f.write(js_data)
    
    print("\n" + "=" * 60)
    print(f"COMPLETE! {len(all_episodes)} episode pages generated")
    print("=" * 60)

if __name__ == "__main__":
    main()
