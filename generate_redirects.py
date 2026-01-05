import os
import re

# 1. Get List of New Episodes
if os.path.exists('episodes'):
    episodes = sorted([f for f in os.listdir('episodes') if f.endswith('.html')])
else:
    episodes = []
print(f"Total new episodes: {len(episodes)}")

# 2. Get Old URLs from Sitemap
path = 'TWSCsite/thewallstreetcoach.com_post-sitemap.xml.md'
if os.path.exists(path):
    with open(path, 'r') as f:
        content = f.read()
else:
    content = ""
    print("Sitemap missing")

# Split by https:// to separate mashed URLs
parts = content.split('https://')
candidates = []
for p in parts:
    if p.startswith('thewallstreetcoach.com/blog/'):
        # Format usually: thewallstreetcoach.com/blog/YYYY/MM/slug/...
        subparts = p.split('/')
        # ['thewallstreetcoach.com', 'blog', '2022', '09', 'slug', '...']
        if len(subparts) >= 5:
            # Reconstruct URL up to slug
            cand = "https://" + "/".join(subparts[:5])
            candidates.append(cand)

print(f"Found {len(candidates)} potential old URLs")

redirects = set()
for old in candidates:
    slug = old.split('/')[-1]
    if not slug: slug = old.split('/')[-2] # Handle trailing slash case
    
    # Matching logic
    match = None
    # 1. Exact slug match
    for new in episodes:
        if slug in new:
            match = new
            break
            
    # 2. Heuristic match (remove ep-XX prefix or handle mismatches)
    if not match:
        # e.g. ep-64-tom-brammar vs ep-064-ep-64-tom-brammar
        parts = slug.split('-')
        if len(parts) > 2 and parts[0] == 'ep':
            # Extract core name "tom-brammar"
            core_slug = "-".join(parts[2:]) 
            for new in episodes:
                if core_slug in new:
                    match = new
                    break
                    
    # 3. Match by ID (ep-64 vs ep-064)
    if not match:
         parts = slug.split('-')
         if len(parts) > 1 and parts[0] == 'ep' and parts[1].isdigit():
             ep_id = int(parts[1])
             id_str = f"ep-{ep_id:03d}"
             for new in episodes:
                 if id_str in new:
                     match = new
                     break

    if match:
        # Construct Source Path
        # /blog/YYYY/MM/slug
        source = "/" + "/".join(old.split('thewallstreetcoach.com/')[1].split('/')[:4]) + "/" + slug
        target = f"/episodes/{match}"
        redirects.add((source, target))

# Write CSV
with open('redirects.csv', 'w') as f:
    f.write("source,target\n")
    for s, t in redirects:
        f.write(f"{s},{t}\n")

# Write _redirects (Netlify/Generic)
with open('_redirects', 'w') as f:
    # Essential Redirects
    f.write("/trader-coaching/ /coaching.html 301\n")
    f.write("/executive-coaching/ /coaching.html 301\n")
    f.write("/coaching-for-executives/ /coaching.html 301\n")
    f.write("/coaching-for-everyone/ /coaching.html 301\n")
    f.write("/about-kim-ann-curtin/ /about.html 301\n")
    f.write("/privacy-policy/ /privacy-policy.html 301\n")
    f.write("/terms-and-conditions/ /privacy-policy.html 301\n") 
    f.write("/contact-form/ /index.html 301\n")
    
    for s, t in list(redirects):
        f.write(f"{s} {t} 301\n")
        # Ensure trailing slash version too
        if not s.endswith('/'):
            f.write(f"{s}/ {t} 301\n")

print(f"Generated {len(redirects)} redirects")
