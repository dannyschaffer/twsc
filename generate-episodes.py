#!/usr/bin/env python3
"""
Generate podcast episode pages from YouTube data with Takeaways
Creates individual HTML pages and updates podcast-data.js
"""

import csv
import json
import os
import re
from html import escape

# Configuration
TAKEAWAYS_CSV = "Youtube Trascripts - NoDAsh.csv"
OUTPUT_DIR = "episodes"
DATA_FILE = "podcast-data.js"
MIN_WORDS = 500  # Reduced to include more episodes

# Episode page template with takeaways
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
            margin-top: 1.5rem;
        }}
        .episode-body h2:first-child, .episode-body h3:first-child {{
            margin-top: 0;
        }}
        .episode-body p {{
            color: var(--text-secondary);
            line-height: 1.8;
            margin-bottom: 1rem;
        }}
        .episode-body ul {{
            margin: 1rem 0 1.5rem 1.5rem;
            color: var(--text-secondary);
        }}
        .episode-body li {{
            margin-bottom: 0.75rem;
            line-height: 1.7;
        }}
        .episode-body strong {{
            color: var(--navy);
        }}
        .actionable-takeaway {{
            background: linear-gradient(135deg, #f0f9f4 0%, #e8f5e9 100%);
            border-left: 4px solid var(--gold);
            padding: 1.5rem;
            margin: 2rem 0;
            border-radius: 0 8px 8px 0;
        }}
        .actionable-takeaway strong {{
            color: var(--navy);
        }}
        .closing-quote {{
            font-style: italic;
            font-size: 1.1rem;
            color: var(--navy);
            text-align: center;
            padding: 1.5rem;
            background: #f8f9fa;
            border-radius: 8px;
            margin-top: 2rem;
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
                <a href="../tpi.html" class="nav-link">Assessment</a>
                <a href="../coaching.html" class="nav-link">Coaching</a>
                <a href="../about.html" class="nav-link">About</a>
                <a href="../podcast.html" class="nav-link nav-link-featured">Podcast</a>
                <a href="../resources.html" class="nav-link">Resources</a>
            </div>
        </div>
    </nav>

    <!-- Hero - Light Background -->
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

    <!-- Video Section - Dark Background -->
    <section class="video-section">
        <div class="video-container">
            <div class="video-wrapper">
                <iframe 
                    src="https://www.youtube.com/embed/{video_id}" 
                    title="{title}"
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
                </iframe>
            </div>
        </div>
    </section>

    <!-- Content - Light Background -->
    <section class="episode-content">
        <div class="episode-container">
            <div class="episode-body">
                {takeaways_section}
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
                        <li><a href="../tpi.html">TPI Assessment</a></li>
                        <li><a href="../coaching.html">Coaching</a></li>
                        <li><a href="../about.html">About</a></li>
                        <li><a href="../podcast.html">Podcast</a></li>
                        <li><a href="../resources.html">Resources</a></li>
                    </ul>
                </div>
                <div class="footer-right">
                    <div class="footer-legal">
                        <a href="mailto:info@thewallstreetcoach.com">Contact</a>
                        <a href="#">Privacy Policy</a>
                        <a href="#">Terms Of Use</a>
                    </div>
                    <div class="footer-social">
                        <span class="footer-social-label">Ways To Follow Us</span>
                        <a href="https://twitter.com/twscoach" target="_blank" rel="noopener" aria-label="Twitter">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                        </a>
                        <a href="https://www.linkedin.com/in/kimanncurtin/" target="_blank" rel="noopener" aria-label="LinkedIn">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                        </a>
                        <a href="https://www.instagram.com/thewallstreetcoach/" target="_blank" rel="noopener" aria-label="Instagram">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                        </a>
                        <a href="https://www.youtube.com/channel/UCuApZQaw2UATpJums6cw3HA" target="_blank" rel="noopener" aria-label="YouTube">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
                        </a>
                        <a href="https://www.tiktok.com/@thewallstreetcoach" target="_blank" rel="noopener" aria-label="TikTok">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <script src="../script.js"></script>
</body>
</html>
'''

def clean_title(title):
    """Clean title for use in filenames"""
    clean = re.sub(r'[^\w\s-]', '', title)
    clean = re.sub(r'\s+', '-', clean.strip())
    clean = clean.lower()[:60]
    return clean

def format_takeaways(takeaways_text):
    """Convert takeaways text to HTML with proper formatting"""
    if not takeaways_text or not takeaways_text.strip():
        return ""
    
    # Clean up the text
    text = takeaways_text.strip()
    
    # Remove em dashes and en dashes, replace with regular dashes or remove
    text = text.replace(' - ', ' - ')  # em dash
    text = text.replace('–', ' - ')  # en dash
    text = text.replace('−', '-')    # minus sign
    
    # First, handle "Actionable Takeaway:" - add newline before it and format it
    # This handles cases like "...past behavior.Actionable Takeaway: ..."
    text = re.sub(r'\.?\s*Actionable Takeaway:\s*', '\n\n**Actionable Takeaway:** ', text, flags=re.IGNORECASE)
    
    # Convert markdown bold **text** to HTML <strong>
    # Handle properly paired asterisks first
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    
    # Handle malformed bold like **text* or *text** (single asterisk on one side)
    text = re.sub(r'\*\*([^*]+)\*(?!\*)', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    
    # Clean up any remaining stray asterisks that aren't bullet points
    # Remove asterisks that are at the end of text (like "Discomfort:*")
    text = re.sub(r':\*(?=\s|$)', ':', text)
    # Remove standalone asterisks with spaces around them
    text = re.sub(r'\s\*\s', ' ', text)
    # Remove asterisks at start of words (not bullet points)
    text = re.sub(r'(?<=\s)\*\*(?=\w)', '', text)
    text = re.sub(r'(?<=\s)\*(?=\w)', '', text)
    # Remove asterisks at end of words
    text = re.sub(r'(?<=\w)\*(?=\s|$|\.)', '', text)
    
    # Handle bullet points - convert * or - or • at start of line to list items
    lines = text.split('\n')
    html_lines = []
    in_list = False
    first_line = True
    
    for line in lines:
        line = line.strip()
        if not line:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            continue
        
        # First non-empty line becomes the header (bold h3)
        if first_line:
            # Remove any # prefix if present
            heading = re.sub(r'^#+\s*', '', line)
            # Clean any remaining asterisks from heading
            heading = heading.replace('*', '')
            html_lines.append(f'<h3>{heading}</h3>')
            first_line = False
            continue
        
        # Check if it's a bullet point
        if line.startswith('* ') or line.startswith('- ') or line.startswith('• '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            # Remove the bullet marker
            content = re.sub(r'^[*\-•]\s+', '', line)
            html_lines.append(f'<li>{content}</li>')
        # Check if it's a heading (starts with #)
        elif line.startswith('### '):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            heading = line[4:].strip().replace('*', '')
            html_lines.append(f'<h3>{heading}</h3>')
        elif line.startswith('## '):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            heading = line[3:].strip().replace('*', '')
            html_lines.append(f'<h3>{heading}</h3>')
        # Check for Actionable Takeaway
        elif '<strong>Actionable Takeaway:</strong>' in line or 'actionable takeaway:' in line.lower():
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # Extract content after the label
            if '<strong>Actionable Takeaway:</strong>' in line:
                content = line.replace('<strong>Actionable Takeaway:</strong>', '').strip()
            else:
                match = re.search(r'actionable takeaway:\s*(.*)', line, re.IGNORECASE)
                content = match.group(1).strip() if match else line
            html_lines.append(f'<div class="actionable-takeaway"><strong>Actionable Takeaway:</strong><br>{content}</div>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # Regular paragraph
            html_lines.append(f'<p>{line}</p>')
    
    if in_list:
        html_lines.append('</ul>')
    
    return '\n'.join(html_lines)

def format_transcript(captions):
    """Format captions as readable transcript"""
    if not captions:
        return "<p>Transcript not available.</p>"
    
    text = captions.replace('&gt;', '').replace('&lt;', '').replace('&amp;', '&')
    text = re.sub(r'&#\d+;', "'", text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
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
    captions_text = captions or ''
    captions_lower = captions_text.lower()[:1000]
    caption_length = len(captions_text)
    
    # Short videos (under ~2 minutes) based on caption length
    # Roughly 150 words per minute spoken, ~6 chars per word = ~1800 chars per minute
    # So under 2 minutes would be roughly under 3600 chars
    if caption_length > 0 and caption_length < 3500:
        return 'clips'
    
    # Known guest names for interview detection
    guest_names = [
        'matthew mcconaughey', 'mcconaughey', 'mike bellafiore', 'bellafiore', 
        'jason shapiro', 'jack kellogg', 'jack schwager', 'pradeep bonde', 
        'lance breitstein', 'thomas vozzo', 'peter atwater', 'joe fahmy', 
        'anand sanghvi', 'sang lucci', 'humbled trader', 'shay huang',
        'megan marlow', 'eduardo briceño', 'bryce tuohey', 'jeff holden',
        'george coyle', 'gregg sciabica', 'doomberg', 'celeste headlee',
        'brian lee', 'jane gallina', 'zach schellhaas', 'jason caldwell',
        'brice foose', 'tom canfield', 'alex sposito', 'william beebe',
        'andres armienta', 'matthew monaco', 'ian ostrosky', 'jeremy aguiar',
        'chris langan', 'danielle shay', 'joseph gasperoni', 'jtrader',
        'vwaptrader1', 'jj of confessions', 'charles harris', 'jason apollo voss'
    ]
    
    # Check for "EP XX:" or "Episode XX" pattern (formal interviews)
    ep_pattern = re.search(r'\bep\.?\s*\d+[:\s]|\bepisode\s+\d+[:\s]', title_lower)
    if ep_pattern:
        return 'interviews'
    
    # Check for guest names in title
    for guest in guest_names:
        if guest in title_lower:
            return 'interviews'
    
    # Check for X Space (Twitter/X live sessions - these are interviews)
    if 'x space' in title_lower or 'x-space' in title_lower:
        return 'interviews'
    
    # Check for short-form content indicators in title (backup for missing captions)
    short_form_indicators = [
        'said it best', 'on why', 'on how', 'protect the frequency',
        'mastering rejection', 'bouncing back', 'why you need',
        'the story', 'never forgot', 'the mom who', 'why stress',
        'what evolution', 'old school', 'journaling saved',
        'stillness leads', 'hard seasons', 'losing alignment'
    ]
    for indicator in short_form_indicators:
        if indicator in title_lower:
            return 'clips'
    
    # Check for tools category
    tools_keywords = ['journal', 'strategy', 'technical', 'tool', 'system', 'indicator', 
                      'biohack', 'routine', 'checklist', 'edgewonk', 'risk management',
                      'pre-market', 'premarket']
    for word in tools_keywords:
        if word in title_lower or word in captions_lower:
            return 'tools'
    
    # Default to psychology (mindset content)
    return 'psychology'

def main():
    print("Loading takeaways from CSV...")
    
    # Load takeaways from CSV
    takeaways_map = {}
    with open(TAKEAWAYS_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            video_id = row.get('videoId', '').strip()
            takeaways = row.get('Takeaways', '').strip()
            captions = row.get('captions', '').strip()
            title = row.get('title', '').strip()
            if video_id:
                takeaways_map[video_id] = {
                    'title': title,
                    'takeaways': takeaways,
                    'captions': captions
                }
    
    print(f"Loaded {len(takeaways_map)} episodes from CSV")
    
    # Filter for episodes with takeaways (include all with takeaways)
    episodes = []
    for video_id, data in takeaways_map.items():
        takeaways = data.get('takeaways', '') or ''
        
        # Include if has takeaways OR has enough words
        if takeaways.strip():
            episodes.append({
                'title': data['title'],
                'videoId': video_id,
                'captions': data.get('captions', ''),
                'takeaways': takeaways,
                'words': len((data.get('captions', '') or '').split())
            })
    
    print(f"Episodes with takeaways: {len(episodes)}")
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Generate episode pages
    podcast_data = []
    episode_num = len(episodes)
    
    with_takeaways = 0
    without_takeaways = 0
    
    for i, ep in enumerate(episodes):
        title = ep['title']
        video_id = ep['videoId']
        captions = ep['captions']
        takeaways = ep['takeaways']
        
        # Generate filename
        filename = f"ep-{episode_num:03d}-{clean_title(title)}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Format takeaways (first line becomes header automatically)
        if takeaways and takeaways.strip():
            takeaways_html = format_takeaways(takeaways)
            with_takeaways += 1
        else:
            takeaways_html = ''
            without_takeaways += 1
        
        # Category for filtering
        category = categorize_episode(title, captions)
        
        # Meta description from takeaways
        if takeaways:
            meta_desc = takeaways[:155].replace('"', "'").replace('\n', ' ')
        else:
            meta_desc = "Watch this episode of The Wall Street Coach Podcast with Kim Ann Curtin."
        
        # Generate HTML (no transcript parameter needed)
        html = EPISODE_TEMPLATE.format(
            title=escape(title),
            meta_description=escape(meta_desc),
            video_id=video_id,
            takeaways_section=takeaways_html
        )
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        # Add to podcast data
        desc = takeaways[:200] if takeaways else f"Watch {title} on The Wall Street Coach Podcast"
        podcast_data.append({
            'ep': episode_num,
            'title': title,
            'description': desc.replace('"', "'").replace('\n', ' '),
            'category': category,
            'image': f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
            'link': f"episodes/{filename}"
        })
        
        episode_num -= 1
        
        if (i + 1) % 50 == 0:
            print(f"  Generated {i + 1}/{len(episodes)} episodes...")
    
    # Sort by episode number (descending)
    podcast_data.sort(key=lambda x: x['ep'], reverse=True)
    
    # Generate podcast-data.js
    js_content = "// Podcast Episodes Data - Auto-generated with Takeaways\n"
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
    print(f"   - With takeaways: {with_takeaways}")
    print(f"   - Without takeaways: {without_takeaways}")
    print(f"✅ Updated '{DATA_FILE}' with all episode data")

if __name__ == "__main__":
    main()
