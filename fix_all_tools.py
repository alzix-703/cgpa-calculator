import os

domain = "https://cgpa-calculator-beige-nu.vercel.app"

# 1. Generate 20+ Dedicated University CGPA Converters
universities = [
    ("AKTU", "aktu-cgpa-calculator.html", 10.0),
    ("DU", "du-cgpa-calculator.html", 9.5),
    ("SPPU", "sppu-cgpa-calculator.html", 8.8),
    ("VTU", "vtu-cgpa-calculator.html", 10.0),
    ("GTU", "gtu-cgpa-calculator.html", 10.0),
    ("RGPV", "rgpv-cgpa-calculator.html", 10.0),
    ("Anna University", "anna-univ-cgpa-calculator.html", 10.0),
    ("Mumbai University", "mumbai-univ-cgpa-calculator.html", 9.5),
    ("Calcutta University", "calcutta-univ-cgpa-calculator.html", 9.5),
    ("JNTU", "jntu-cgpa-calculator.html", 10.0),
    ("MG Kashi Vidyapith", "mgkvp-cgpa-calculator.html", 9.5),
    ("CCS University", "ccsu-cgpa-calculator.html", 9.5),
    ("Bangalore University", "bangalore-univ-cgpa-calculator.html", 9.5),
    ("Madras University", "madras-univ-cgpa-calculator.html", 9.5),
    ("Panjab University", "panjab-univ-cgpa-calculator.html", 9.5),
    ("Patna University", "patna-univ-cgpa-calculator.html", 9.5),
    ("BGU", "bgu-cgpa-calculator.html", 10.0),
    ("GGSIPU", "ggsipu-cgpa-calculator.html", 9.5),
    ("LNCT", "lnct-cgpa-calculator.html", 10.0),
    (" SRM", "srm-cgpa-calculator.html", 10.0),
    ("AMITY", "amity-cgpa-calculator.html", 10.0),
    ("VIT", "vit-cgpa-calculator.html", 10.0)
]

for name, filename, factor in universities:
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} CGPA to Percentage Calculator 2026</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white min-h-screen p-6 max-w-2xl mx-auto space-y-6">
    <a href="/" class="text-indigo-400 hover:underline">&larr; Back to Home</a>
    <h1 class="text-3xl font-bold text-indigo-400">{name} CGPA Converter</h1>
    <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 space-y-4">
        <label class="block text-sm">Enter Your {name} CGPA</label>
        <input type="number" step="0.01" id="cgpa" placeholder="e.g. 8.5" class="w-full bg-slate-700 border border-slate-600 rounded p-2 text-white">
        <button onclick="calc()" class="w-full bg-indigo-600 hover:bg-indigo-500 py-2 rounded font-semibold">Convert to Percentage</button>
        <div id="res" class="hidden p-4 bg-slate-700 rounded-lg text-emerald-400 font-bold text-xl"></div>
    </div>
    <script>
        function calc() {{
            const val = parseFloat(document.getElementById('cgpa').value);
            if(!val) return;
            const pct = (val * {factor}).toFixed(2);
            const r = document.getElementById('res');
            r.classList.remove('hidden');
            r.innerText = 'Percentage: ' + pct + '% (Formula: CGPA × {factor})';
        }}
    </script>
</body>
</html>'''
    with open(filename, "w") as f:
        f.write(html_content)

# 2. Fix PM Kisan Yojana Logic
pm_kisan_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PM Kisan Samman Nidhi Status & Eligibility Checker 2026</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white min-h-screen p-6 max-w-2xl mx-auto space-y-6">
    <a href="/" class="text-indigo-400 hover:underline">&larr; Back to Home</a>
    <h1 class="text-3xl font-bold text-amber-400">PM Kisan Eligibility & Installment Checker</h1>
    <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 space-y-4">
        <div>
            <label class="block text-sm mb-1">Do you have cultivable land in your name?</label>
            <select id="land" class="w-full bg-slate-700 border border-slate-600 rounded p-2 text-white">
                <option value="yes">Yes</option>
                <option value="no">No</option>
            </select>
        </div>
        <div>
            <label class="block text-sm mb-1">Is e-KYC & Aadhaar Seeding Completed?</label>
            <select id="ekyc" class="w-full bg-slate-700 border border-slate-600 rounded p-2 text-white">
                <option value="yes">Yes</option>
                <option value="no">No</option>
            </select>
        </div>
        <button onclick="checkStatus()" class="w-full bg-amber-600 hover:bg-amber-500 py-2 rounded font-semibold text-slate-900">Check Eligibility</button>
        <div id="status-res" class="hidden p-4 bg-slate-700 rounded-lg text-lg font-medium"></div>
    </div>
    <script>
        function checkStatus() {
            const l = document.getElementById('land').value;
            const k = document.getElementById('ekyc').value;
            const r = document.getElementById('status-res');
            r.classList.remove('hidden');
            if(l === 'yes' && k === 'yes') {
                r.className = "p-4 bg-emerald-900/80 text-emerald-200 rounded-lg";
                r.innerText = " Eligible! You will receive the ₹2,000 installment directly in your bank account.";
            } else {
                r.className = "p-4 bg-rose-900/80 text-rose-200 rounded-lg";
                r.innerText = " Action Needed: Complete land seeding and e-KYC on pmkisan.gov.in to receive installments.";
            }
        }
    </script>
</body>
</html>'''

with open("pm-kisan-status.html", "w") as f:
    f.write(pm_kisan_html)

# 3. Update Homepage with All 22 Universities
uni_links_html = "".join([f'<a href="/{fn}" class="bg-slate-800 p-3 rounded border border-slate-700 hover:border-indigo-500 text-center block text-slate-200 font-medium">{un}</a>' for un, fn, _ in universities])

index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All-in-One Utility Portal - University CGPA, Tax & Yojana Calculators</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white min-h-screen flex flex-col justify-between p-4 md:p-8">
    <div class="max-w-5xl mx-auto w-full space-y-8">
        
        <header class="text-center space-y-2">
            <h1 class="text-4xl font-extrabold text-indigo-400">All-in-One Utility Portal</h1>
            <p class="text-slate-400">Fast, free, and privacy-focused online calculation tools.</p>
        </header>

        <section class="space-y-4">
            <h2 class="text-2xl font-bold text-emerald-400 border-b border-slate-700 pb-2">💰 Financial & Tax Tools</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <a href="/salary-tax-calculator.html" class="bg-slate-800 p-5 rounded-xl border border-slate-700 hover:border-emerald-500 transition block">
                    <h3 class="text-lg font-bold text-emerald-300">In-Hand Salary & Tax Calculator</h3>
                    <p class="text-sm text-slate-400 mt-1">Calculate monthly take-home salary and income tax under New vs Old regime.</p>
                </a>
                <a href="/gst-calculator.html" class="bg-slate-800 p-5 rounded-xl border border-slate-700 hover:border-emerald-500 transition block">
                    <h3 class="text-lg font-bold text-emerald-300">GST Calculator (Add/Remove GST)</h3>
                    <p class="text-sm text-slate-400 mt-1">Calculate 5%, 12%, 18%, and 28% GST amounts instantly for invoices.</p>
                </a>
            </div>
        </section>

        <section class="space-y-4">
            <h2 class="text-2xl font-bold text-amber-400 border-b border-slate-700 pb-2">🏛️ Sarkari Yojana Utilities</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <a href="/pm-kisan-status.html" class="bg-slate-800 p-5 rounded-xl border border-slate-700 hover:border-amber-500 transition block">
                    <h3 class="text-lg font-bold text-amber-300">PM Kisan Eligibility & Status Checker</h3>
                    <p class="text-sm text-slate-400 mt-1">Check e-KYC status, land seeding requirements, and installment eligibility.</p>
                </a>
            </div>
        </section>

        <section class="space-y-4">
            <h2 class="text-2xl font-bold text-indigo-400 border-b border-slate-700 pb-2">🎓 20+ University CGPA Converters</h2>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3 text-sm">
                {uni_links_html}
            </div>
        </section>

    </div>

    <footer class="mt-12 text-center text-xs text-slate-500 space-x-6 border-t border-slate-800 pt-6">
        <a href="/privacy-policy.html" class="hover:underline hover:text-slate-300">Privacy Policy</a>
        <a href="/terms.html" class="hover:underline hover:text-slate-300">Terms & Conditions</a>
    </footer>
</body>
</html>'''

with open("index.html", "w") as f:
    f.write(index_html)

print("All 22 University converters, PM Kisan, and Homepage generated successfully!")
