#!/usr/bin/env python3
"""
Podcast Episode Scraper and Page Generator
Scrapes all podcast episodes from thewallstreetcoach.com and generates local HTML pages
"""

import requests
from bs4 import BeautifulSoup
import re
import os
import json
import time

# Configuration
BASE_URL = "https://thewallstreetcoach.com/twsc-podcast/"
OUTPUT_DIR = "episodes"
DATA_FILE = "podcast-episodes-full.json"

# Headers to mimic browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Episode page template
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
        .episode-hero {{
            background-color: #08333A;
            color: #fff;
            padding: 6rem 0 4rem;
            text-align: center;
        }}
        .episode-content {{
            background-color: #F9F9F7;
            padding: 4rem 0;
        }}
        .episode-container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 0 2rem;
        }}
        .episode-meta {{
            display: flex;
            gap: 1rem;
            justify-content: center;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }}
        .episode-tag {{
            background: rgba(255,255,255,0.1);
            padding: 0.5rem 1rem;
            border-radius: 50px;
            font-size: 0.85rem;
            color: rgba(255,255,255,0.8);
        }}
        .episode-number {{
            color: var(--gold);
            font-family: 'Space Mono', monospace;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 1rem;
        }}
        .audio-player {{
            background: #fff;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            margin-bottom: 2rem;
        }}
        .audio-player audio {{
            width: 100%;
        }}
        .episode-body {{
            background: #fff;
            padding: 3rem;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        }}
        .episode-body p {{
            color: var(--text-secondary);
            line-height: 1.8;
            margin-bottom: 1.5rem;
        }}
        .episode-body h2 {{
            color: var(--navy);
            margin: 2rem 0 1rem;
        }}
        .episode-image {{
            width: 100%;
            max-width: 600px;
            margin: 0 auto 2rem;
            border-radius: 12px;
            display: block;
        }}
        .episode-cta {{
            background: var(--navy);
            padding: 3rem;
            border-radius: 12px;
            text-align: center;
            margin-top: 2rem;
        }}
        .episode-cta h3 {{
            color: #fff;
            margin-bottom: 1rem;
        }}
        .episode-cta p {{
            color: rgba(255,255,255,0.7);
            margin-bottom: 1.5rem;
        }}
        .guest-links {{
            background: #F9F9F7;
            padding: 1.5rem;
            border-radius: 8px;
            margin: 2rem 0;
        }}
        .guest-links h4 {{
            color: var(--navy);
            margin-bottom: 0.5rem;
        }}
        .guest-links a {{
            color: var(--gold);
            text-decoration: none;
            margin-right: 1rem;
        }}
        .back-link {{
            color: rgba(255,255,255,0.7);
            text-decoration: none;
            display: inline-block;
            margin-bottom: 2rem;
        }}
        .back-link:hover {{
            color: var(--gold);
        }}
        .nav-episodes {{
            display: flex;
            justify-content: space-between;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(0,0,0,0.1);
        }}
        .nav-episodes a {{
            color: var(--navy);
            text-decoration: none;
            font-weight: 600;
        }}
        .nav-episodes a:hover {{
            color: var(--gold);
        }}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="nav-bar" id="mainNav">
        <div class="nav-container">
            <div class="nav-logo">
                <a href="../index.html"><img src="../TWSCsite/Images/The-Wall-Street-Coach-Logo-Transparent@white.png" alt="The Wall Street Coach" class="logo-img"></a>
            </div>
            <button class="mobile-menu-toggle" id="mobileMenuToggle">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <div class="nav-links" id="navLinks">
                <a href="../tpi.html" class="nav-link">The TPI Assessment</a>
                <a href="../coaching.html" class="nav-link">Coaching & Consulting</a>
                <a href="../about.html" class="nav-link">About Kim</a>
                <a href="../podcast.html" class="nav-link nav-link-featured">Podcast</a>
                <a href="../resources.html" class="nav-link">Resources</a>
            </div>
        </div>
    </nav>

    <!-- Episode Hero -->
    <section class="episode-hero">
        <div class="episode-container">
            <a href="../podcast.html" class="back-link">← Back to All Episodes</a>
            <div class="episode-number">Episode {ep_number}</div>
            <h1 style="font-size: 2.5rem; margin-bottom: 1rem;">{guest_name}</h1>
            <p style="font-size: 1.2rem; color: rgba(255,255,255,0.8); max-width: 600px; margin: 0 auto;">{short_title}</p>
            <div class="episode-meta">
                <span class="episode-tag">{category}</span>
            </div>
        </div>
    </section>

    <!-- Episode Content -->
    <section class="episode-content">
        <div class="episode-container">
            <!-- Featured Image -->
            <img src="{image_url}" alt="{title}" class="episode-image" onerror="this.style.display='none'">
            
            <!-- Audio Player -->
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

            <!-- Episode Body -->
            <div class="episode-body">
                {body_content}
                
                {guest_links}

                <!-- Resources CTA -->
                <div class="episode-cta">
                    <h3>Ready to Transform Your Trading?</h3>
                    <p>Discover your Trader Positioning Index and unlock your psychological edge.</p>
                    <a href="../tpi.html" class="btn-primary" style="background: var(--gold); color: var(--navy);">Get Your TPI Score</a>
                </div>
            </div>

            <!-- Episode Navigation -->
            <div class="nav-episodes">
                {prev_link}
                {next_link}
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <h3>The Wall Street Coach</h3>
                    <p>Transforming Wall Street from the inside out.</p>
                </div>
                <div class="footer-links">
                    <h4>Quick Links</h4>
                    <a href="../tpi.html">TPI Assessment</a>
                    <a href="../coaching.html">Coaching</a>
                    <a href="../about.html">About Kim</a>
                    <a href="../podcast.html">Podcast</a>
                    <a href="../resources.html">Resources</a>
                </div>
                <div class="footer-contact">
                    <h4>Connect</h4>
                    <p>Email: hello@thewallstreetcoach.com</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 The Wall Street Coach. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="../script.js"></script>
</body>
</html>
'''

def get_podcast_pages():
    """Get all podcast listing page URLs"""
    pages = [BASE_URL]
    # Add paginated pages (there are 19 pages total)
    for i in range(2, 20):
        pages.append(f"{BASE_URL}page/{i}")
    return pages

def scrape_episode_links(page_url):
    """Scrape episode links from a podcast listing page"""
    try:
        response = requests.get(page_url, headers=HEADERS, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        episodes = []
        # Find all episode cards
        cards = soup.find_all('a', href=re.compile(r'/blog/\d{4}/\d{2}/'))
        
        seen_urls = set()
        for card in cards:
            url = card.get('href')
            if url and url not in seen_urls and 'ep-' in url.lower():
                seen_urls.add(url)
                episodes.append(url)
        
        return episodes
    except Exception as e:
        print(f"Error scraping {page_url}: {e}")
        return []

def scrape_episode_content(url):
    """Scrape full content from an episode page"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get title
        title_elem = soup.find('h1', class_='entry-title') or soup.find('h1')
        title = title_elem.get_text(strip=True) if title_elem else "Episode"
        
        # Extract episode number
        ep_match = re.search(r'[Ee][Pp]\s*(\d+)', title)
        ep_number = ep_match.group(1) if ep_match else "0"
        
        # Get meta description
        meta_desc = soup.find('meta', {'property': 'og:description'})
        description = meta_desc['content'] if meta_desc else ""
        
        # Get featured image
        og_image = soup.find('meta', {'property': 'og:image'})
        image_url = og_image['content'] if og_image else ""
        
        # Get audio URL (Blubrry embed)
        audio_url = ""
        audio_link = soup.find('a', href=re.compile(r'blubrry.*\.mp3'))
        if audio_link:
            audio_url = audio_link.get('href')
        
        # Get main content
        content_div = soup.find('div', class_='entry-content') or soup.find('article')
        body_content = ""
        if content_div:
            # Get all paragraphs
            paragraphs = content_div.find_all('p')
            for p in paragraphs:
                text = p.get_text(strip=True)
                if text and len(text) > 20 and 'Podcast:' not in text and 'Download' not in text:
                    body_content += f"<p>{text}</p>\n"
        
        # Extract guest name from title
        guest_name = title
        if ':' in title:
            guest_name = title.split(':')[-1].strip()
            if ' with ' in guest_name:
                guest_name = guest_name.split(' with ')[-1].strip()
        
        # Determine category based on keywords
        category = "Mindset & Psychology"
        title_lower = title.lower()
        if 'wizard' in title_lower:
            category = "Market Wizards"
        elif 'neuro' in title_lower or 'brain' in title_lower:
            category = "Neuroscience"
        elif 'risk' in title_lower or 'strategy' in title_lower:
            category = "Strategy & Tools"
        elif any(word in title_lower for word in ['million', 'success', 'journey', 'profitable']):
            category = "Success Stories"
        
        return {
            'url': url,
            'title': title,
            'ep_number': ep_number,
            'description': description,
            'image_url': image_url,
            'audio_url': audio_url,
            'body_content': body_content,
            'guest_name': guest_name,
            'category': category
        }
    except Exception as e:
        print(f"Error scraping episode {url}: {e}")
        return None

def generate_episode_page(episode, all_episodes):
    """Generate HTML page for an episode"""
    ep_num = int(episode['ep_number'])
    
    # Create audio embed
    if episode['audio_url']:
        audio_embed = f'<audio controls><source src="{episode["audio_url"]}" type="audio/mpeg">Your browser does not support the audio element.</audio>'
    else:
        audio_embed = '<p style="color: var(--text-secondary);">Audio player loading... Listen on your favorite podcast platform.</p>'
    
    # Create navigation links
    prev_link = ""
    next_link = ""
    
    for ep in all_episodes:
        if int(ep['ep_number']) == ep_num - 1:
            prev_link = f'<a href="ep-{ep["ep_number"]}.html">← EP {ep["ep_number"]}: Previous Episode</a>'
        if int(ep['ep_number']) == ep_num + 1:
            next_link = f'<a href="ep-{ep["ep_number"]}.html">EP {ep["ep_number"]}: Next Episode →</a>'
    
    if not prev_link:
        prev_link = '<span></span>'
    if not next_link:
        next_link = '<span></span>'
    
    # Short title (after the colon)
    short_title = episode['title']
    if ':' in short_title:
        short_title = short_title.split(':', 1)[1].strip()
    
    # Generate HTML
    html = EPISODE_TEMPLATE.format(
        title=episode['title'],
        description=episode['description'][:160],
        ep_number=episode['ep_number'],
        guest_name=episode['guest_name'],
        short_title=short_title,
        category=episode['category'],
        image_url=episode['image_url'],
        audio_embed=audio_embed,
        body_content=episode['body_content'] or f"<p>{episode['description']}</p>",
        guest_links='',
        prev_link=prev_link,
        next_link=next_link
    )
    
    # Write file
    filename = f"{OUTPUT_DIR}/ep-{episode['ep_number']}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Generated: {filename}")

def main():
    print("=" * 60)
    print("PODCAST EPISODE SCRAPER & PAGE GENERATOR")
    print("=" * 60)
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Step 1: Get all episode URLs
    print("\n[1/3] Collecting episode URLs from all pages...")
    all_urls = []
    for page_url in get_podcast_pages():
        print(f"  Scanning: {page_url}")
        urls = scrape_episode_links(page_url)
        all_urls.extend(urls)
        time.sleep(0.5)  # Be nice to the server
    
    # Remove duplicates while preserving order
    all_urls = list(dict.fromkeys(all_urls))
    print(f"\n  Found {len(all_urls)} unique episode URLs")
    
    # Step 2: Scrape each episode
    print("\n[2/3] Scraping episode content...")
    episodes = []
    for i, url in enumerate(all_urls):
        print(f"  [{i+1}/{len(all_urls)}] Scraping: {url}")
        episode = scrape_episode_content(url)
        if episode:
            episodes.append(episode)
        time.sleep(0.5)  # Be nice to the server
    
    # Sort by episode number
    episodes.sort(key=lambda x: int(x['ep_number']), reverse=True)
    
    # Save to JSON for reference
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(episodes, f, indent=2)
    print(f"\n  Saved episode data to {DATA_FILE}")
    
    # Step 3: Generate HTML pages
    print("\n[3/3] Generating HTML pages...")
    for episode in episodes:
        generate_episode_page(episode, episodes)
    
    print("\n" + "=" * 60)
    print(f"COMPLETE! Generated {len(episodes)} episode pages in /{OUTPUT_DIR}/")
    print("=" * 60)

if __name__ == "__main__":
    main()
