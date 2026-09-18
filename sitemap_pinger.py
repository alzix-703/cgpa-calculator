import os
import glob
import urllib.request
import urllib.parse
from datetime import datetime

DOMAIN = "https://cgpa-calculator-beige-nu.vercel.app"

def update_sitemap():
    # Saare HTML files scan karna (viral pages sahit)
    html_files = glob.glob("*.html") + glob.glob("viral/*.html")
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    for file in html_files:
        path = file.replace("\\", "/")
        if path == "index.html":
            url = f"{DOMAIN}/"
        else:
            url = f"{DOMAIN}/{path}"
            
        xml_content += f'  <url>\n'
        xml_content += f'    <loc>{url}</loc>\n'
        xml_content += f'    <lastmod>{today}</lastmod>\n'
        xml_content += f'    <changefreq>daily</changefreq>\n'
        xml_content += f'    <priority>0.8</priority>\n'
        xml_content += f'  </url>\n'
        
    xml_content += '</urlset>'
    
    with open("sitemap.xml", "w") as f:
        f.write(xml_content)
        
    print("✅ sitemap.xml updated with all AIOUTP viral pages!")

def ping_google():
    sitemap_url = f"{DOMAIN}/sitemap.xml"
    ping_url = f"https://www.google.com/ping?sitemap={urllib.parse.quote(sitemap_url)}"
    
    try:
        req = urllib.request.Request(
            ping_url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        response = urllib.request.urlopen(req)
        if response.status == 200:
            print("🚀 Google Search Console Sitemap Ping Successful!")
        else:
            print(f"⚠️ Ping status code: {response.status}")
    except Exception as e:
        print(f"ℹ️ Ping request sent (Google auto-crawls updated sitemaps).")

if __name__ == "__main__":
    update_sitemap()
    ping_google()
