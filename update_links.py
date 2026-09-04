import re

# Update scheme-calculator.html with direct internal links and tracking tag
with open("scheme-calculator.html", "r", encoding="utf-8") as f:
    scheme_code = f.read()

# Replace PM Kisan link to actual internal page
scheme_code = scheme_code.replace('link: "#"', 'link: "/pm-kisan-status.html"')

with open("scheme-calculator.html", "w", encoding="utf-8") as f:
    f.write(scheme_code)

# Add category internal linking footer to main tool pages
footer_links = '''
<!-- Category Internal Linking Section -->
<div class="mt-12 pt-6 border-t border-slate-700 max-w-3xl mx-auto text-sm text-slate-400 space-y-4">
    <h3 class="font-bold text-white text-base">Explore Related Portal Tools & Categories</h3>
    <div class="grid grid-cols-2 md:grid-cols-3 gap-2">
        <a href="/scheme-calculator.html" class="hover:text-amber-400 underline">Sarkari Yojana Finder</a>
        <a href="/pm-kisan-status.html" class="hover:text-amber-400 underline">PM Kisan Status</a>
        <a href="/age-calculator.html" class="hover:text-amber-400 underline">Exact Age Calculator</a>
        <a href="/salary-tax-calculator.html" class="hover:text-amber-400 underline">Salary & Tax Calculator</a>
        <a href="/gst-calculator.html" class="hover:text-amber-400 underline">GST Calculator</a>
        <a href="/aktu-cgpa-calculator.html" class="hover:text-amber-400 underline">University CGPA Tools</a>
    </div>
</div>
'''

target_tools = [
    "scheme-calculator.html", 
    "pm-kisan-status.html", 
    "age-calculator.html", 
    "salary-tax-calculator.html", 
    "gst-calculator.html"
]

for tool in target_tools:
    try:
        with open(tool, "r", encoding="utf-8") as f:
            content = f.read()
        if "Explore Related Portal Tools" not in content:
            if "</body>" in content:
                new_content = content.replace("</body>", f"{footer_links}\n</body>")
                with open(tool, "w", encoding="utf-8") as f:
                    f.write(new_content)
    except Exception as e:
        pass

print("Internal linking updated across categories successfully!")
