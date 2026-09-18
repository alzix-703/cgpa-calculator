import os

trends = [
    {
        "slug": "sarkari-eligibility-quiz",
        "title": "Sarkari Yojana Eligibility Check 2026",
        "desc": "Check which government schemes & benefits you are eligible for in 30 seconds!",
        "target": "/sarkari-yojana.html",
        "bg_color": "#0b1120"
    },
    {
        "slug": "aktu-score-predictor",
        "title": "AKTU Semester CGPA & Grade Predictor",
        "desc": "Calculate exact AKTU SGPA/CGPA percentage instantly.",
        "target": "/index.html",
        "bg_color": "#0b1120"
    },
    {
        "slug": "exact-age-tax-check",
        "title": "Exact Age & Tax Saving Assessment",
        "desc": "Calculate your exact age in days & check your tax regime benefits.",
        "target": "/index.html",
        "bg_color": "#0b1120"
    }
]

def generate_viral_pages():
    os.makedirs("viral", exist_ok=True)

    for item in trends:
        file_path = f"viral/{item['slug']}.html"
        
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
        h1 {{ font-size: 1.4rem; color: #eab308; margin-bottom: 12px; font-weight: 700; }}
        p {{ color: #94a3b8; font-size: 0.9rem; margin-bottom: 20px; line-height: 1.4; }}
        .q-box {{ background: #0f172a; padding: 16px; border-radius: 10px; margin-bottom: 16px; text-align: left; border: 1px solid #334155; }}
        .q-box label {{ font-size: 0.85rem; color: #cbd5e1; display: block; margin-bottom: 6px; }}
        .q-box select {{ width: 100%; padding: 10px; border-radius: 6px; background: #1e293b; color: #fff; border: 1px solid #334155; outline: none; }}
        .btn-action {{ width: 100%; padding: 12px; background: #ca8a04; color: #000; border: none; border-radius: 8px; font-weight: 700; font-size: 1rem; cursor: pointer; }}
        .whatsapp-btn {{ display: inline-block; width: 100%; padding: 12px; background: #22c55e; color: #fff; text-decoration: none; font-weight: 700; border-radius: 8px; margin-bottom: 12px; font-size: 0.95rem; }}
        .main-btn {{ display: block; width: 100%; padding: 12px; background: #eab308; color: #000; text-decoration: none; font-weight: 700; border-radius: 8px; font-size: 0.95rem; }}
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
            <h2 style="color: #22c55e; margin-bottom: 8px; font-size: 1.3rem;">Analysis Ready!</h2>
            <p style="margin-bottom: 16px;">Share with friends to compare & unlock full detailed report on main portal.</p>
            
            <a id="waShare" href="#" target="_blank" class="whatsapp-btn" onclick="unlockMain()">📲 Share on WhatsApp to Continue</a>
            <a id="mainLink" href="{item['target']}" class="main-btn" style="display:none;">🚀 Go to Main Utility Tool</a>
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
            }}, 1200);
        }}
    </script>
</body>
</html>"""
        with open(file_path, "w") as f:
            f.write(html_content)

    print("Fixed paths in AIOUTP viral pages successfully!")

if __name__ == "__main__":
    generate_viral_pages()
