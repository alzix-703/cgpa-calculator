import os

domain = "https://cgpa-calculator-beige-nu.vercel.app"

# Current directory ke saare HTML files list karega
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Generate sitemap.xml
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for file in html_files:
    loc = f"{domain}/{file}" if file != "index.html" else f"{domain}/"
    sitemap_content += f'  <url>\n    <loc>{loc}</loc>\n    <priority>0.80</priority>\n  </url>\n'

sitemap_content += '</urlset>'

with open("sitemap.xml", "w") as f:
    f.write(sitemap_content)

# Generate robots.txt
robots_content = f"User-agent: *\nAllow: /\n\nSitemap: {domain}/sitemap.xml"
with open("robots.txt", "w") as f:
    f.write(robots_content)

print("SEO Files (sitemap.xml & robots.txt) successfully generated!")
