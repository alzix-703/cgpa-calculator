import os

domain = "https://cgpa-calculator-beige-nu.vercel.app"

pages = [
    {"file": "index.html", "title": "All-in-One Utility Portal 2026 - Free Calculators", "desc": "Free CGPA converters, tax calculator, age calculator, and sarkari yojana finder."},
    {"file": "aktu-cgpa-calculator.html", "title": "AKTU CGPA to Percentage Calculator 2026 (Official Formula)", "desc": "Convert AKTU CGPA to percentage instantly using official AKTU formula (CGPA - 0.75) * 10."},
    {"file": "du-cgpa-calculator.html", "title": "DU CGPA to Percentage Calculator 2026 - Delhi University", "desc": "Convert Delhi University (DU) CGPA to percentage using official DU formula CGPA * 9.5."},
    {"file": "vtu-cgpa-calculator.html", "title": "VTU CGPA to Percentage Calculator 2026", "desc": "Calculate VTU percentage from CGPA instantly with accurate formula."},
    {"file": "rgpv-cgpa-calculator.html", "title": "RGPV CGPA to Percentage Calculator 2026", "desc": "Official RGPV CGPA to percentage converter for diploma and engineering students."},
    {"file": "age-calculator.html", "title": "Exact Age Calculator Online for Sarkari Jobs 2026", "desc": "Calculate exact age in years, months, and days for online form filling."},
    {"file": "salary-tax-calculator.html", "title": "In-Hand Salary & Income Tax Calculator 2026", "desc": "Calculate take-home salary and compare New vs Old Tax Regime."},
    {"file": "gst-calculator.html", "title": "GST Calculator Online (Add / Remove GST)", "desc": "Calculate 5%, 12%, 18%, 28% GST amounts easily for billing."},
    {"file": "privacy-policy.html", "title": "Privacy Policy - Utility Portal", "desc": "Our commitment to user data privacy and security."},
    {"file": "terms.html", "title": "Terms and Conditions - Utility Portal", "desc": "Terms of service and legal disclaimer for tool usage."}
]

# Generate sitemap.xml
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for p in pages:
    sitemap_content += f'  <url>\n    <loc>{domain}/{p["file"]}</loc>\n    <priority>0.80</priority>\n  </url>\n'
sitemap_content += '</urlset>'

with open("sitemap.xml", "w") as f:
    f.write(sitemap_content)

print("✅ sitemap.xml successfully generated with all URLs!")
