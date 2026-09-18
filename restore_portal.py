import os

# Main Portal HTML (All Calculators & Tools Restored)
main_index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AIOUTP - All In One Utility Tools Portal & University CGPA Converters</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
        body { background-color: #0f172a; color: #f8fafc; padding: 20px; min-height: 100vh; }
        .container { max-width: 900px; margin: 0 auto; }
        header { text-align: center; padding: 20px 0; border-bottom: 1px solid #334155; margin-bottom: 25px; }
        h1 { font-size: 1.8rem; color: #38bdf8; margin-bottom: 8px; }
        p.subtitle { color: #94a3b8; font-size: 0.95rem; }
        
        .grid-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-top: 20px; }
        .card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 18px; transition: transform 0.2s, border-color 0.2s; }
        .card:hover { transform: translateY(-3px); border-color: #38bdf8; }
        .card h3 { font-size: 1.1rem; color: #f1f5f9; margin-bottom: 8px; }
        .card p { font-size: 0.85rem; color: #94a3b8; margin-bottom: 12px; line-height: 1.4; }
        .card a { display: inline-block; padding: 8px 14px; background: #2563eb; color: #fff; text-decoration: none; border-radius: 6px; font-size: 0.82rem; font-weight: 600; }
        
        .viral-banner { background: linear-gradient(135deg, #e11d48, #be123c); border-radius: 12px; padding: 16px; margin-bottom: 25px; text-align: center; }
        .viral-banner h2 { font-size: 1.2rem; color: #fff; margin-bottom: 6px; }
        .viral-banner p { font-size: 0.85rem; color: #fecdd3; margin-bottom: 10px; }
        .viral-banner a { display: inline-block; padding: 10px 18px; background: #fff; color: #be123c; font-weight: 700; text-decoration: none; border-radius: 8px; font-size: 0.85rem; }
        
        footer { text-align: center; padding: 30px 0 10px; color: #64748b; font-size: 0.8rem; border-top: 1px solid #334155; margin-top: 40px; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>⚡ AIOUTP Web Utility Portal</h1>
            <p class="subtitle">Multi-functional Calculators, CGPA Converters & Smart Online Utilities</p>
        </header>

        <div class="viral-banner">
            <h2>🔥 Premium Shayari & Love Stories Hub</h2>
            <p>Explore exclusive high-dopamine content with direct share integration!</p>
            <a href="/viral/sarkari-eligibility-quiz.html">Open Shayari & Stories Hub →</a>
        </div>

        <h2 style="font-size: 1.3rem; color: #f1f5f9; margin-bottom: 15px;">🛠️ General Utility Tools</h2>
        <div class="grid-container">
            <div class="card">
                <h3>📅 Exact Age Calculator</h3>
                <p>Calculate your precise age in years, months, weeks, and days instant with date picker.</p>
                <a href="#age-calculator">Use Age Calculator</a>
            </div>
            <div class="card">
                <h3>💰 Income Tax Regime Calculator</h3>
                <p>Compare tax liability under New vs Old tax regime for FY 2025-26 easily.</p>
                <a href="#tax-calculator">Calculate Tax</a>
            </div>
            <div class="card">
                <h3>📊 GST Calculator</h3>
                <p>Calculate net amount, gross amount, and GST split (CGST & SGST) for 5%, 12%, 18%, 28%.</p>
                <a href="#gst-calculator">Calculate GST</a>
            </div>
            <div class="card">
                <h3>📜 Sarkari Yojana Eligibility Checker</h3>
                <p>Check eligibility for major central and state government schemes instantly.</p>
                <a href="#yojana-checker">Check Eligibility</a>
            </div>
        </div>

        <h2 style="font-size: 1.3rem; color: #f1f5f9; margin-top: 35px; margin-bottom: 15px;">🎓 Indian University CGPA Converters</h2>
        <div class="grid-container">
            <div class="card">
                <h3>🏛️ AKTU CGPA to Percentage</h3>
                <p>Dr. A.P.J. Abdul Kalam Technical University formula based CGPA converter.</p>
                <a href="/aktu-cgpa-calculator">Open Converter</a>
            </div>
            <div class="card">
                <h3>🏛️ DU CGPA to Percentage</h3>
                <p>Delhi University official 9.5 multiplier CGPA to percentage tool.</p>
                <a href="/du-cgpa-calculator">Open Converter</a>
            </div>
            <div class="card">
                <h3>🏛️ Anna University CGPA Calculator</h3>
                <p>Grade point and credit based CGPA calculation for Anna University students.</p>
                <a href="/anna-univ-cgpa-calculator">Open Converter</a>
            </div>
            <div class="card">
                <h3>🏛️ VTU CGPA Converter</h3>
                <p>Visvesvaraya Technological University official grading scheme calculator.</p>
                <a href="/vtu-cgpa-calculator">Open Converter</a>
            </div>
        </div>

        <footer>
            <p>© 2026 AIOUTP Portal | Created by Arpit Singh | Powered by Vercel</p>
        </footer>
    </div>
</body>
</html>"""

# Write main index.html
with open("index.html", "w") as f:
    f.write(main_index_html)

print("Main Portal index.html restored successfully!")
