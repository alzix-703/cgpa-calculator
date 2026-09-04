age_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Age Calculator Online - Sarkari Form & Exact Age Finder</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white min-h-screen p-6 max-w-2xl mx-auto space-y-6">
    <a href="/" class="text-indigo-400 hover:underline">&larr; Back to Home</a>
    <h1 class="text-3xl font-bold text-indigo-400">Exact Age Calculator</h1>
    <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 space-y-4">
        <div>
            <label class="block text-sm mb-1">Date of Birth</label>
            <input type="date" id="dob" class="w-full bg-slate-700 border border-slate-600 rounded p-2 text-white">
        </div>
        <div>
            <label class="block text-sm mb-1">Age at Date (e.g., Today or Form Cut-off)</label>
            <input type="date" id="target" class="w-full bg-slate-700 border border-slate-600 rounded p-2 text-white">
        </div>
        <button onclick="calcAge()" class="w-full bg-indigo-600 hover:bg-indigo-500 py-2 rounded font-semibold">Calculate Age</button>
        <div id="age-res" class="hidden p-4 bg-slate-700 rounded-lg text-emerald-400 font-bold text-xl"></div>
    </div>
    <script>
        document.getElementById('target').valueAsDate = new Date();
        function calcAge() {
            const dob = new Date(document.getElementById('dob').value);
            const target = new Date(document.getElementById('target').value);
            if(!dob || isNaN(dob)) return;
            
            let y = target.getFullYear() - dob.getFullYear();
            let m = target.getMonth() - dob.getMonth();
            let d = target.getDate() - dob.getDate();

            if (d < 0) {
                m--;
                d += new Date(target.getFullYear(), target.getMonth(), 0).getDate();
            }
            if (m < 0) {
                y--;
                m += 12;
            }
            const r = document.getElementById('age-res');
            r.classList.remove('hidden');
            r.innerText = `${y} Years, ${m} Months, ${d} Days`;
        }
    </script>
</body>
</html>'''

with open("age-calculator.html", "w") as f:
    f.write(age_html)

# Read current index.html and insert Age Calculator link if not present
with open("index.html", "r") as f:
    content = f.read()

if "age-calculator.html" not in content:
    target_str = '💰 Financial & Tax Tools</h2>'
    new_card = '''<a href="/age-calculator.html" class="bg-slate-800 p-5 rounded-xl border border-slate-700 hover:border-indigo-500 transition block">
                    <h3 class="text-lg font-bold text-indigo-300">Exact Age Calculator</h3>
                    <p class="text-sm text-slate-400 mt-1">Calculate exact age in years, months, and days for Sarkari job forms.</p>
                </a>\n'''
    content = content.replace(target_str, target_str + "\n" + new_card)
    with open("index.html", "w") as f:
        f.write(content)

print("Age Calculator and Homepage link created successfully!")
