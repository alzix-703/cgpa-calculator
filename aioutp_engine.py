import os
import xml.etree.ElementTree as ET
from datetime import datetime

# 1. Viral Trends Data Structure for AIOUTP
trends = [
    {
        "slug": "sarkari-eligibility-quiz",
        "title": "Sarkari Yojana Eligibility Check 2026",
        "desc": "Check which government schemes & benefits you are eligible for in 30 seconds!",
        "target": "./sarkari-yojana.html",
        "bg_color": "#1e1b4b"
    },
    {
        "slug": "aktu-score-predictor",
        "title": "AKTU Semester CGPA & Grade Predictor",
        "desc": "Calculate exact AKTU SGPA/CGPA percentage instantly.",
        "target": "./index.html",
        "bg_color": "#0f172a"
    },
    {
        "slug": "exact-age-tax-check",
        "title": "Exact Age & Tax Saving Assessment",
        "desc": "Calculate your exact age in days & check your tax regime benefits.",
        "target": "./index.html",
        "bg_color": "#111827"
    }
]

def generate_viral_pages():
    os.makedirs("viral", exist_ok=True)
    generated_urls = []

    for item in trends:
        file_path = f"viral/{item['slug']}.html"
        generated_urls.append(f"https://cgpa-calculator-beige-nu.vercel.app/viral/{item['slug']}.html")
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{item['title']} - AIOUTP Tool</title>
    <meta property="og:title" content="{item['title']}" />
    <meta property="og:description" content="{item['desc']}" />
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }}
        body {{ background-color: {item['bg_color']}; color: #fff; padding: 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
        .card {{ background: #1e293b; border: 1px solid #334155; padding: 24px; border-radius: 16px; max-width: 480px; width: 100%; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }}
        h1 {{ font-size: 1.5rem; color: #f59e0b; margin-bottom: 12px; }}
        p {{ color: #94a3b8; font-size: 0.95rem; margin-bottom: 20px; line-height: 1.4; }}
        .q-box {{ background: #0f172a; padding: 16px; border-radius: 10px; margin-bottom: 16px; text-align: left; border: 1px solid #1e293b; }}
        .q-box label {{ font-size: 0.85rem; color: #cbd5e1; display: block; margin-bottom: 6px; }}
        .q-box select {{ width: 100%; padding: 10px; border-radius: 6px; background: #1e293b; color: #fff; border: 1px solid #334155; }}
        .btn-action {{ width: 100%; padding: 12px; background: #6366f1; color: #fff; border: none; border-radius: 8px; font-weight: 700; font-size: 1rem; cursor: pointer; }}
        .share-box {{ display: none; background: #0284c7; padding: 12px; border-radius: 8px; margin-top: 15px; color: #fff; font-size: 0.85rem; }}
        .whatsapp-btn {{ display: inline-block; width: 100%; padding: 12px; background: #22c55e; color: #fff; text-decoration: none; font-weight: 700; border-radius: 8px; margin-top: 10px; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{item['title']}</h1>
        <p>{item['desc']}</p>
        
        <div id="quizForm">
            <div class="q-box">
                <label>Select Your Profile / Requirement:</label>
                <select id="userOpt">
                    <option>General Category / Student</option>
                    <option>Farmer / Daily Wager</option>
                    <option>Working Professional</option>
                </select>
            </div>
            <button class="btn-action" onclick="processQuiz()">Check Result Instant</button>
        </div>

        <div id="resultBox" style="display:none;">
            <h2 style="color: #22c55e; margin-bottom: 8px;">Analysis Ready!</h2>
            <p>Share with friends to compare & unlock full detailed report on main portal.</p>
            
            <a id="waShare" href="#" target="_blank" class="whatsapp-btn" onclick="unlockMain()">📲 Share on WhatsApp to Continue</a>
            <a id="mainLink" href="{item['target']}" class="btn-action" style="display:none; margin-top: 12px; background: #eab308; color: #000; text-decoration: none;">🚀 Go to Main Utility Tool</a>
        </div>
    </div>

    <script>
        function processQuiz() {{
            document.getElementById('quizForm').style.display = 'none';
            document.getElementById('resultBox').style.display = 'block';
            let msg = encodeURIComponent("Check your score on AIOUTP Tool: " + window.location.href);
            document.getElementById('waShare').href = "https://api.whatsapp.com/send?text=" + msg;
        }}
        function unlockMain() {{
            setTimeout(() => {{
                document.getElementById('mainLink').style.display = 'block';
            }}, 1500);
        }}
    </script>
</body>
</html>"""
        with open(file_path, "w") as f:
            f.write(html_content)

    print(f"Generated {len(trends)} viral AIOUTP pages successfully!")
    return generated_urls

if __name__ == "__main__":
    generate_viral_pages()
