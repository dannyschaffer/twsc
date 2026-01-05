import re

# Read Markdown
with open('TWSCsite/thewallstreetcoach.com_privacy-policy_.md', 'r') as f:
    md_content = f.read()

# Extract body (skip frontmatter and navigation links at top)
# Content starts after "## Privacy Policy"
if "## Privacy Policy" in md_content:
    body_md = md_content.split("## Privacy Policy")[1]
else:
    body_md = md_content

# Clean up bottom (remove footer links if present in md)
if "#### **Sign up" in body_md:
    body_md = body_md.split("#### **Sign up")[0]

# Simple Markdown to HTML converter
html_body = ""
lines = body_md.split('\n')
in_list = False

for line in lines:
    line = line.strip()
    if not line:
        continue
        
    # Headers
    if line.startswith('**') and line.endswith('**') and len(line) < 100:
        # Treat standalone bold lines as headers
        header = line.strip('**')
        html_body += f"<h3 style='color: var(--navy); margin-top: 2rem; margin-bottom: 1rem;'>{header}</h3>\n"
    elif line.startswith('#### '):
        html_body += f"<h4>{line[5:]}</h4>\n"
    elif line.startswith('- '):
        if not in_list:
            html_body += "<ul>\n"
            in_list = True
        html_body += f"<li>{line[2:]}</li>\n"
    else:
        if in_list:
            html_body += "</ul>\n"
            in_list = False
        # Text processing
        # Replace links [text](url) -> <a href="url">text</a>
        line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
        html_body += f"<p style='margin-bottom: 1rem; color: var(--text-primary); line-height: 1.6;'>{line}</p>\n"

if in_list:
    html_body += "</ul>\n"

# Read Template (resources.html)
with open('resources.html', 'r') as f:
    template = f.read()

# Replace Hero
hero_replacement = """
    <section class="resource-hero">
        <div class="container">
            <h1 style="color: var(--navy); margin-bottom: 1rem;">Privacy Policy</h1>
            <p style="color: var(--text-primary); max-width: 600px; margin: 0 auto;">Last Updated on 6/1/2023</p>
        </div>
    </section>
"""
# Regex replace the hero section
template = re.sub(r'<section class="resource-hero">.*?</section>', hero_replacement, template, flags=re.DOTALL)

# Replace Main Section
# Find section after hero
main_section = f"""
    <section class="section" style="padding-top: 4rem;">
        <div class="container" style="max-width: 800px; margin: 0 auto;">
            {html_body}
        </div>
    </section>
"""

# Replace the existing main section (assuming it starts with <section class="section" style="padding-top: 0;">)
# Use a marker or just replace from hero end to footer start?
# resources.html structure: Hero -> Section -> Footer.
# I'll split by </section> and reconstruct.

parts = template.split('<!-- Main Section: Books & Free Tools -->')
top = parts[0]
# Find footer start
footer_parts = template.split('<!-- Footer -->')
bottom = footer_parts[1]

new_html = top + main_section + "\n    <!-- Footer -->" + bottom

with open('privacy-policy.html', 'w') as f:
    f.write(new_html)

print("Created privacy-policy.html")
