import csv

redirects = []
try:
    with open('redirects.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            redirects.append((row['source'], row['target']))
except FileNotFoundError:
    print("redirects.csv not found")

htaccess_content = """# Enable Rewrite Engine
RewriteEngine On

# Force HTTPS
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Core Page Redirects
Redirect 301 /trader-coaching/ /coaching.html
Redirect 301 /executive-coaching/ /coaching.html
Redirect 301 /coaching-for-executives/ /coaching.html
Redirect 301 /coaching-for-everyone/ /coaching.html
Redirect 301 /about-kim-ann-curtin/ /about.html
Redirect 301 /privacy-policy/ /privacy-policy.html
Redirect 301 /terms-and-conditions/ /privacy-policy.html
Redirect 301 /contact-form/ /index.html

# Blog/Episode Redirects
"""

for source, target in redirects:
    # Ensure source starts with /
    if not source.startswith('/'): source = '/' + source
    # .htaccess Redirect directive requires absolute matches for simplified syntax, 
    # or RewriteRule for pattern matching.
    # Redirect 301 /old /new
    # Note: Redirect matches path prefix. 
    # To be safe, we use simple Redirect 301.
    
    htaccess_content += f"Redirect 301 {source} {target}\n"
    # Also handle trailing slash if strict? 
    # Usually Apache handles /foo and /foo/ if not specified otherwise, 
    # but strictly Redirect /foo /bar redirects /foo AND /foo/bar.
    # For exact matching, RedirectMatch or RewriteRule is safer, 
    # but for blog posts migration, this is usually fine.

with open('.htaccess', 'w') as f:
    f.write(htaccess_content)

print(f"Generated .htaccess with {len(redirects) + 8} rules")
