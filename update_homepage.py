import re, glob

# Homepage index.html ko update karenge
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Purane Age-Wise card ko Naye Smart Scheme Finder card se replace karna
old_card_pattern = r'<a href="[^"]*scheme-calculator\.html"[^>]*>.*?Age-Wise Sarkari Yojana Finder.*?</a>'

new_card = '''<a href="/smart-scheme-finder.html" class="block p-5 bg-slate-800/80 hover:bg-slate-800 border border-slate-700/80 hover:border-amber-500/50 rounded-xl transition duration-200 shadow-md">
    <h3 class="text-lg font-bold text-amber-400 mb-1">Smart Sarkari Yojana Finder 🚀</h3>
    <p class="text-xs text-slate-400">Enter age, income, board/profession & get exact eligible schemes with live official form links.</p>
</a>'''

# Replace if found
if "Age-Wise Sarkari Yojana Finder" in content:
    content = re.sub(r'<a href="[^"]* scheme-calculator\.html"[^>]*>[\s\S]*?Age-Wise Sarkari Yojana Finder[\s\S]*?</a>', new_card, content)
    content = re.sub(r'<a href="[^"]*"[^>]*>[\s\S]*?Age-Wise Sarkari Yojana Finder[\s\S]*?</a>', new_card, content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Homepage card updated to Smart Sarkari Yojana Finder!")
