import requests
import xml.etree.ElementTree as ET
import json
import re
import os
from datetime import datetime

# Configuration
RSS_FEED_URL = "https://www.thewallstreetcoach.com/feed/podcast/"
OUTPUT_FILE = "podcast-episodes-full.json"

def fetch_rss_feed(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/rss+xml, application/xml, text/xml, */*'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        return None

def parse_rss_feed(xml_content):
    episodes = []
    try:
        root = ET.fromstring(xml_content)
        channel = root.find("channel")
        
        # Namespaces often used in podcast feeds
        namespaces = {
            'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
            'content': 'http://purl.org/rss/1.0/modules/content/'
        }
        
        items = channel.findall("item")
        
        for item in items:
            title = item.find("title").text if item.find("title") is not None else "No Title"
            link = item.find("link").text if item.find("link") is not None else ""
            
            description = ""
            desc_elem = item.find("description")
            if desc_elem is not None:
                description = desc_elem.text
            
            # Try to get content:encoded if description is short or empty
            content_encoded = item.find("content:encoded", namespaces)
            if content_encoded is not None and content_encoded.text:
                # If we want full html content, we can use this. 
                # For now, let's stick to description but clean it up if needed.
                pass

            # Clean up description (remove HTML tags if any, limit length for summary)
            clean_description = re.sub(r'<[^>]+>', '', description) if description else ""
            # Unescape html entities
            import html
            clean_description = html.unescape(clean_description)
            
            # Short summary for card (first ~200 chars)
            summary = clean_description[:200] + "..." if len(clean_description) > 200 else clean_description

            # Episode number
            episode_num = item.find("itunes:episode", namespaces)
            ep_num_val = episode_num.text if episode_num is not None else None
            
            # If no explicit episode number, try to extract from title
            if not ep_num_val:
                match = re.search(r'(?:Ep|Episode)\.?\s*(\d+)', title, re.IGNORECASE)
                if match:
                    ep_num_val = match.group(1)
                else:
                    # Fallback or keep as None/0
                    # For sorting, maybe use 0 or index
                    ep_num_val = 0

            # Image
            image_url = ""
            itunes_image = item.find("itunes:image", namespaces)
            if itunes_image is not None:
                image_url = itunes_image.get("href")
            else:
                # Fallback to channel image
                channel_image = channel.find("itunes:image", namespaces)
                if channel_image is not None:
                    image_url = channel_image.get("href")

            # Category - Simple logic based on title/desc keywords or default
            category = "all"
            title_lower = title.lower()
            if "clip" in title_lower or "short" in title_lower:
                category = "clips"
            elif "interview" in title_lower or "with" in title_lower:
                category = "interviews"
            elif "psychology" in title_lower or "mindset" in title_lower:
                category = "psychology"
            
            # Date
            pub_date = item.find("pubDate").text if item.find("pubDate") is not None else ""

            episode = {
                "ep": int(ep_num_val) if ep_num_val else 0,
                "title": title,
                "description": summary,
                "category": category, # This might need better heuristic or manual tagging support
                "image": image_url,
                "link": link,
                "pubDate": pub_date
            }
            episodes.append(episode)
            
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []

    return episodes

def main():
    print(f"Fetching RSS feed from {RSS_FEED_URL}...")
    xml_content = fetch_rss_feed(RSS_FEED_URL)
    
    if xml_content:
        print("Parsing RSS feed...")
        episodes = parse_rss_feed(xml_content)
        
        print(f"Found {len(episodes)} episodes.")
        
        # Sort by episode number desc
        episodes.sort(key=lambda x: x['ep'], reverse=True)
        
        # Write to JSON
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(episodes, f, indent=4, ensure_ascii=False)
        
        print(f"Successfully wrote {len(episodes)} episodes to {OUTPUT_FILE}")
    else:
        print("Failed to update podcast data.")

if __name__ == "__main__":
    main()
