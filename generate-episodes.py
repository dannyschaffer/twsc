#!/usr/bin/env python3
"""
Generate podcast episode pages from YouTube data
Creates individual HTML pages and updates podcast-data.js
"""

import json
import os
import re
from html import escape

# Configuration
YOUTUBE_DATA_FILE = "dataset_youtube-full-channel-transcripts-extractor_2025-11-22_08-07-57-187 (1).json"
OUTPUT_DIR = "episodes"
DATA_FILE = "podcast-data.js"
MIN_WORDS = 1500  # Minimum word count for a full episode

# Episode page template
EPISODE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - The Wall Street Coach Podcast</title>
    <meta name="description" content="{meta_description}">
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
        .episode-hero h1 {{
            font-size: 2.5rem;
            max-width: 900px;
            margin: 0 auto 1.5rem;
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
        .video-wrapper {{
            position: relative;
            padding-bottom: 56.25%;
            height: 0;
            overflow: hidden;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.15);
            margin-bottom: 3rem;
        }}
        .video-wrapper iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }}
        .episode-body {{
            background: #fff;
            padding: 3rem;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        }}
        .transcript-toggle {{
            background: var(--gold);
            color: var(--navy);
            border: none;
            padding: 1rem 2rem;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            margin-bottom: 2rem;
            transition: all 0.3s;
        }}
        .transcript-toggle:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(201, 162, 39, 0.3);
        }}
        .transcript {{
            display: none;
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 8px;
            font-size: 0.95rem;
            line-height: 1.8;
            color: var(--text-secondary);
            max-height: 500px;
            overflow-y: auto;
        }}
        .transcript.show {{
            display: block;
        }}
        .back-link {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: rgba(255,255,255,0.7);
            text-decoration: none;
            margin-bottom: 2rem;
            transition: color 0.3s;
        }}
        .back-link:hover {{
            color: var(--gold);
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
    <!-- Navigation -->
    <nav class="nav-bar" id="mainNav">
        <div class="nav-container">
            <div class="nav-logo">
                <a href="../index.html"><img src="../TWSCsite/Images/The-Wall-Street-Coach-Logo-Transparent@white.png" alt="The Wall Street Coach" class="logo-img"></a>
            </div>
            <button class="mobile-menu-toggle" id="mobileMenuToggle">
                <span></span><span></span><span></span>
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

    <!-- Hero -->
    <section class="episode-hero">
        <div class="container">
            <a href="../podcast.html" class="back-link">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M19 12H5M12 19l-7-7 7-7"/>
                </svg>
                Back to All Episodes
            </a>
            <h1>{title}</h1>
        </div>
    </section>

    <!-- Content -->
    <section class="episode-content">
        <div class="episode-container">
            <!-- Video Embed -->
            <div class="video-wrapper">
                <iframe 
                    src="https://www.youtube.com/embed/{video_id}" 
                    title="{title}"
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
                </iframe>
            </div>

            <div class="episode-body">
                <h2>Episode Overview</h2>
                <p>{description}</p>
                
                <button class="transcript-toggle" onclick="toggleTranscript()">
                    📝 Show Transcript
                </button>
                
                <div class="transcript" id="transcript">
                    {transcript}
                </div>
            </div>

            <!-- CTA -->
            <div class="episode-cta">
                <h3>Ready to Transform Your Trading Psychology?</h3>
                <p>Take the Trader Positioning Index assessment to uncover your blind spots.</p>
                <a href="../tpi.html" class="btn-primary" style="background: var(--gold); color: var(--navy);">Get Your TPI Profile</a>
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
    <script>
        function toggleTranscript() {{
            const transcript = document.getElementById('transcript');
            const btn = document.querySelector('.transcript-toggle');
            transcript.classList.toggle('show');
            btn.textContent = transcript.classList.contains('show') ? '📝 Hide Transcript' : '📝 Show Transcript';
        }}
    </script>
</body>
</html>
'''

def clean_title(title):
    """Clean title for use in filenames"""
    # Remove special chars but keep spaces, then convert to kebab case
    clean = re.sub(r'[^\w\s-]', '', title)
    clean = re.sub(r'\s+', '-', clean.strip())
    clean = clean.lower()[:60]  # Limit length
    return clean

def extract_description(captions, max_chars=300):
    """Extract a clean description from captions"""
    if not captions:
        return "Join Kim Ann Curtin for another exploration into trading psychology and performance."
    
    # Clean up the captions
    text = captions.replace('&gt;', '').replace('&lt;', '').replace('&amp;', '&')
    text = re.sub(r'\[.*?\]', '', text)  # Remove [music], [laughter], etc.
    text = re.sub(r'&#\d+;', '', text)  # Remove HTML entities
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Get first few sentences
    sentences = text.split('.')[:3]
    description = '. '.join(sentences).strip()
    
    if len(description) > max_chars:
        description = description[:max_chars].rsplit(' ', 1)[0] + '...'
    
    return description if description else "Join Kim Ann Curtin for another exploration into trading psychology and performance."

def format_transcript(captions):
    """Format captions as readable transcript"""
    if not captions:
        return "<p>Transcript not available.</p>"
    
    # Clean up the captions
    text = captions.replace('&gt;', '').replace('&lt;', '').replace('&amp;', '&')
    text = re.sub(r'&#\d+;', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Split into paragraphs (roughly every 200 words)
    words = text.split()
    paragraphs = []
    current = []
    
    for word in words:
        current.append(word)
        if len(current) >= 200:
            paragraphs.append(' '.join(current))
            current = []
    
    if current:
        paragraphs.append(' '.join(current))
    
    return '\n'.join([f'<p>{escape(p)}</p>' for p in paragraphs])

def categorize_episode(title, captions):
    """Assign category based on content"""
    title_lower = title.lower()
    captions_lower = (captions or '').lower()
    
    keywords = {
        'wizards': ['wizard', 'market wizard', 'legend'],
        'psychology': ['psychology', 'mindset', 'emotional', 'fear', 'greed', 'discipline', 'meditation', 'breath'],
        'success': ['million', 'success', 'journey', 'profitable', 'turned'],
        'tools': ['journal', 'strategy', 'technical', 'tool', 'system', 'indicator']
    }
    
    for category, words in keywords.items():
        for word in words:
            if word in title_lower or word in captions_lower[:500]:
                return category
    
    return 'psychology'  # Default category

def main():
    print("Loading YouTube data...")
    with open(YOUTUBE_DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Total videos found: {len(data)}")
    
    # Filter for full episodes (based on transcript length)
    episodes = []
    for item in data:
        captions = item.get('captions', '') or ''
        word_count = len(captions.split())
        
        if word_count >= MIN_WORDS:
            episodes.append({
                'title': item.get('title', 'Untitled Episode'),
                'videoId': item.get('videoId', ''),
                'captions': captions,
                'words': word_count
            })
    
    print(f"Full episodes (>={MIN_WORDS} words): {len(episodes)}")
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Generate episode pages and collect data for podcast-data.js
    podcast_data = []
    episode_num = len(episodes)  # Start from highest and count down
    
    for i, ep in enumerate(episodes):
        title = ep['title']
        video_id = ep['videoId']
        captions = ep['captions']
        
        # Generate filename
        filename = f"ep-{episode_num:03d}-{clean_title(title)}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Extract description and format transcript
        description = extract_description(captions)
        meta_description = description[:155] if len(description) > 155 else description
        transcript = format_transcript(captions)
        category = categorize_episode(title, captions)
        
        # Generate HTML
        html = EPISODE_TEMPLATE.format(
            title=escape(title),
            meta_description=escape(meta_description),
            video_id=video_id,
            description=escape(description),
            transcript=transcript
        )
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        # Add to podcast data
        podcast_data.append({
            'ep': episode_num,
            'title': title,
            'description': description,
            'category': category,
            'image': f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
            'link': f"episodes/{filename}"
        })
        
        episode_num -= 1
        
        if (i + 1) % 20 == 0:
            print(f"  Generated {i + 1}/{len(episodes)} episodes...")
    
    # Sort by episode number (descending)
    podcast_data.sort(key=lambda x: x['ep'], reverse=True)
    
    # Generate podcast-data.js
    js_content = "// Podcast Episodes Data - Auto-generated\n"
    js_content += f"// Total Episodes: {len(podcast_data)}\n\n"
    js_content += "const podcastEpisodes = [\n"
    
    for ep in podcast_data:
        title_escaped = ep['title'].replace('"', '\\"')
        desc_escaped = ep['description'].replace('"', '\\"')
        js_content += '    {\n'
        js_content += f'        ep: {ep["ep"]},\n'
        js_content += f'        title: "{title_escaped}",\n'
        js_content += f'        description: "{desc_escaped}",\n'
        js_content += f'        category: "{ep["category"]}",\n'
        js_content += f'        image: "{ep["image"]}",\n'
        js_content += f'        link: "{ep["link"]}"\n'
        js_content += '    },\n'
    
    js_content += "];\n"
    
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"\n✅ Generated {len(episodes)} episode pages in '{OUTPUT_DIR}/'")
    print(f"✅ Updated '{DATA_FILE}' with all episode data")
    print(f"\nCategories breakdown:")
    
    categories = {}
    for ep in podcast_data:
        cat = ep['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  - {cat}: {count} episodes")

if __name__ == "__main__":
    main()
