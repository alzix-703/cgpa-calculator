import os

domain = "https://cgpa-calculator-beige-nu.vercel.app"

# Base Template
def create_page_html(title, desc, heading, content_text):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: -apple-system, sans-serif; }}
        body {{ background: #0b1120; color: #f8fafc; padding: 25px 15px; max-width: 600px; margin: 0 auto; }}
        h1 {{ color: #818cf8; font-size: 1.8rem; margin-bottom: 12px; }}
        p {{ color: #94a3b8; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; }}
        .card {{ background: #131c31; border: 1px solid #1e293b; border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 20px; }}
        a {{ color: #38bdf8; text-decoration: none; font-weight: bold; font-size: 1rem; display: inline-block; margin-top: 10px; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>{heading}</h1>
    <p>{content_text}</p>
    <div class="card">
        <h3>Use Official Calculator Tool</h3>
        <p>Calculate your percentage, age, or eligibility using our fast tool.</p>
        <a href="/">Go to Main Portal Tool 🚀</a>
    </div>
</body>
</html>"""

# 50 University Pages
universities = [
    "AKTU", "DU", "VTU", "RGPV", "SPPU", "Anna University", "Mumbai University", "Calcutta University", "JNTU", "MG Kashi Vidyapith",
    "CCS University", "Bangalore University", "Madras University", "Panjab University", "Patna University", "BGU", "GGSIPU", "LNCT", "SRM", "AMITY",
    "VIT", "KIIT", "Chandigarh University", "LPU", "Manipal", "BITS Pilani", "BHU", "AMU", "Jamia Millia", "Osmania University",
    "Gujarat University", "Calicut University", "Kerala University", "Andhra University", "Mysore University", "Gauhati University", "Utkal University", "Ranchi University", "Kurukshetra University", "MDU Rohtak",
    "AKU Patna", "RTU Kota", "BTU Bikaner", "CSVTU", "ASTU Assam", "HPTU Hamirpur", "UKTU Dehradun", "JNTUH", "JNTUK", "JNTUA"
]

pages = []

# Main pages
pages.append({"file": "index.html", "title": "All-in-One Utility Portal 2026 - Free Calculators", "desc": "Free CGPA converters, tax calculator, age calculator, and sarkari yojana finder.", "h1": "All-in-One Utility Portal", "txt": "Access 100+ free online calculation tools for education, finance, age, and government schemes."})
pages.append({"file": "age-calculator.html", "title": "Exact Age Calculator Online for Sarkari Jobs 2026", "desc": "Calculate exact age in years, months, and days.", "h1": "Exact Age Calculator", "txt": "Calculate your exact age for all government exam recruitment forms."})
pages.append({"file": "salary-tax-calculator.html", "title": "In-Hand Salary & Income Tax Calculator 2026", "desc": "Calculate take-home salary and compare New vs Old Tax Regime.", "h1": "Salary & Income Tax Calculator", "txt": "Find out your monthly in-hand salary after PF and tax deductions."})
pages.append({"file": "gst-calculator.html", "title": "GST Calculator Online (Add / Remove GST)", "desc": "Calculate 5%, 12%, 18%, 28% GST amounts.", "h1": "GST Calculator Online", "txt": "Easily add or remove GST from any amount instantly."})
pages.append({"file": "privacy-policy.html", "title": "Privacy Policy - Utility Portal", "desc": "Privacy policy and data handling rules.", "h1": "Privacy Policy", "txt": "We respect user privacy and do not store personal financial data."})
pages.append({"file": "terms.html", "title": "Terms and Conditions - Utility Portal", "desc": "Terms of service and legal disclaimers.", "h1": "Terms & Conditions", "txt": "Terms of use for All-in-One Utility Portal tools."})

# Uni Pages (50)
for uni in universities:
    slug = uni.lower().replace(" ", "-") + "-cgpa-calculator.html"
    pages.append({
        "file": slug,
        "title": f"{uni} CGPA to Percentage Calculator 2026 (Official Formula)",
        "desc": f"Convert {uni} CGPA/CPI to percentage instantly using official {uni} formula.",
        "h1": f"{uni} CGPA to Percentage Calculator",
        "txt": f"Easily convert your {uni} semester CGPA into equivalent percentage using official university guidelines."
    })

# Exam Age Pages (22)
exams = ["SSC CGL", "UPSC IAS", "Railway ALP", "IBPS PO", "UP Police Constable", "MP Police", "SSC GD", "NEET UG", "JEE Main", "SBI PO", "RRB NTPC", "CDS", "NDA", "AFCAT", "CTET", "REET", "Bihar Teacher", "LIC AAO", "RBI Grade B", "SEBI Grade A", "Indian Navy", "Indian Army"]
for ex in exams:
    slug = ex.lower().replace(" ", "-") + "-age-calculator.html"
    pages.append({
        "file": slug,
        "title": f"{ex} Age Limit Calculator 2026 - Check Eligibility",
        "desc": f"Calculate exact age eligibility for {ex} 2026 exam form filling.",
        "h1": f"{ex} Age Eligibility Calculator",
        "txt": f"Check if you meet the minimum and maximum age criteria for {ex} recruitment."
    })

# Yojana Pages (22)
schemes = ["PM Kisan Samman Nidhi", "Ladli Behna Yojana", "Kanya Sumangala", "PM Mudra Loan", "Post Matric Scholarship", "Lakhpati Didi", "PM Awas Yojana", "Ayushman Bharat", "Subhadra Yojana Odisha", "Majhi Ladki Bahin", "Free Scooty Scheme", "UP Free Smartphone", "Bihar Student Credit Card", "Mukhyamantri Yuva Udyami", "PM Vishwakarma", "Sukanya Samriddhi", "E-Shram Card", "PM SVANidhi", "Kisan Credit Card", "Mahila Samman Savings", "PM Surya Ghar", "Abhyudaya Yojana"]
for sch in schemes:
    slug = sch.lower().replace(" ", "-") + "-yojana.html"
    pages.append({
        "file": slug,
        "title": f"{sch} Eligibility & Online Status Check 2026",
        "desc": f"Check eligibility criteria, required documents, and online application details for {sch}.",
        "h1": f"{sch} Portal",
        "txt": f"Complete guide and eligibility checker for {sch} 2026."
    })

# Generate Files
for p in pages:
    if p["file"] != "index.html" and not os.path.exists(p["file"]):
        with open(p["file"], "w") as f:
            f.write(create_page_html(p["title"], p["desc"], p["h1"], p["txt"]))

# Sitemap Generator
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for p in pages:
    sitemap_content += f'  <url>\n    <loc>{domain}/{p["file"]}</loc>\n    <priority>0.80</priority>\n  </url>\n'
sitemap_content += '</urlset>'

with open("sitemap.xml", "w") as f:
    f.write(sitemap_content)

print(f"🎉 SUCCESS: Generated {len(pages)} Smart SEO Pages and updated sitemap.xml!")
