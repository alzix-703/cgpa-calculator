import glob
import re

# Comprehensive Category Navigation HTML Snippet
internal_nav_html = '''
<!-- GLOBAL INTERNAL LINKING & CATEGORY MATRIX -->
<section class="mt-12 pt-8 border-t border-slate-700 text-sm max-w-4xl mx-auto space-y-6">
    <div class="bg-slate-800 p-6 rounded-2xl border border-slate-700">
        <h2 class="text-xl font-bold text-amber-400 mb-4">Explore Popular Tools & Categories</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Category 1: Sarkari Yojana Tools -->
            <div>
                <h3 class="font-bold text-indigo-300 mb-2 border-b border-slate-700 pb-1">🏛️ Sarkari Yojana</h3>
                <ul class="space-y-1 text-slate-300">
                    <li><a href="/scheme-calculator.html" class="hover:text-amber-400 underline">Age-Wise Scheme Finder</a></li>
                    <li><a href="/pm-kisan-status.html" class="hover:text-amber-400 underline">PM Kisan Status Checker</a></li>
                </ul>
            </div>

            <!-- Category 2: Utility & Tax Calculators -->
            <div>
                <h3 class="font-bold text-emerald-300 mb-2 border-b border-slate-700 pb-1">🧮 Utility & Finance</h3>
                <ul class="space-y-1 text-slate-300">
                    <li><a href="/salary-tax-calculator.html" class="hover:text-amber-400 underline">Salary & Income Tax Calc</a></li>
                    <li><a href="/gst-calculator.html" class="hover:text-amber-400 underline">GST Calculator India</a></li>
                    <li><a href="/age-calculator.html" class="hover:text-amber-400 underline">Exact Age Calculator</a></li>
                </ul>
            </div>

            <!-- Category 3: Top University CGPA Converters -->
            <div>
                <h3 class="font-bold text-sky-300 mb-2 border-b border-slate-700 pb-1">🎓 Top Universities</h3>
                <ul class="space-y-1 text-slate-300">
                    <li><a href="/aktu-cgpa-calculator.html" class="hover:text-amber-400 underline">AKTU CGPA Converter</a></li>
                    <li><a href="/du-cgpa-calculator.html" class="hover:text-amber-400 underline">DU Percentage Calc</a></li>
                    <li><a href="/sppu-cgpa-calculator.html" class="hover:text-amber-400 underline">SPPU Pune CGPA</a></li>
                    <li><a href="/vtu-cgpa-calculator.html" class="hover:text-amber-400 underline">VTU Percentage Calc</a></li>
                    <li><a href="/gtu-cgpa-calculator.html" class="hover:text-amber-400 underline">GTU CGPA to % Calc</a></li>
                </ul>
            </div>
        </div>

        <div class="mt-6 pt-4 border-t border-slate-700 text-center">
            <a href="/" class="text-amber-400 hover:underline font-semibold">&larr; Return to All Tools Homepage</a>
        </div>
    </div>
</section>
'''

html_files = glob.glob("*.html")
updated_files = 0

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip index.html from adding duplicate category matrix if already present
    if file_path == "index.html":
        continue

    # Clean previous temporary footers if any
    if "GLOBAL INTERNAL LINKING" not in content:
        if "</body>" in content:
            new_content = content.replace("</body>", f"{internal_nav_html}\n</body>")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated_files += 1

print(f"Successfully added Global Category Linking to {updated_files} HTML pages!")
