index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All-in-One Utility Portal - University CGPA, Tax & Yojana Calculators</title>
    <meta name="description" content="Free online utility tools: University CGPA to Percentage converters, Income Tax & Salary calculator, GST calculator, and Sarkari Yojana status checkers.">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white min-h-screen flex flex-col justify-between p-4 md:p-8">
    <div class="max-w-5xl mx-auto w-full space-y-8">
        
        <!-- Header -->
        <header class="text-center space-y-2">
            <h1 class="text-4xl font-extrabold text-indigo-400">All-in-One Utility Portal</h1>
            <p class="text-slate-400">Fast, free, and privacy-focused online calculation tools.</p>
        </header>

        <!-- Category 1: Financial & Tax Utilities -->
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

        <!-- Category 2: Government Schemes -->
        <section class="space-y-4">
            <h2 class="text-2xl font-bold text-amber-400 border-b border-slate-700 pb-2">🏛️ Sarkari Yojana Utilities</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <a href="/pm-kisan-status.html" class="bg-slate-800 p-5 rounded-xl border border-slate-700 hover:border-amber-500 transition block">
                    <h3 class="text-lg font-bold text-amber-300">PM Kisan Eligibility & Status Guide</h3>
                    <p class="text-sm text-slate-400 mt-1">Check e-KYC status, land seeding requirements, and installment updates.</p>
                </a>
            </div>
        </section>

        <!-- Category 3: Academic CGPA Converters -->
        <section class="space-y-4">
            <h2 class="text-2xl font-bold text-indigo-400 border-b border-slate-700 pb-2">🎓 University CGPA Converters</h2>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3 text-sm">
                <a href="/aktu-cgpa-calculator.html" class="bg-slate-800 p-3 rounded border border-slate-700 hover:border-indigo-500 text-center block">AKTU Converter</a>
                <a href="/du-cgpa-calculator.html" class="bg-slate-800 p-3 rounded border border-slate-700 hover:border-indigo-500 text-center block">DU Converter</a>
                <a href="/sppu-cgpa-calculator.html" class="bg-slate-800 p-3 rounded border border-slate-700 hover:border-indigo-500 text-center block">SPPU Converter</a>
                <a href="/vtu-cgpa-calculator.html" class="bg-slate-800 p-3 rounded border border-slate-700 hover:border-indigo-500 text-center block">VTU Converter</a>
                <a href="/gtu-cgpa-calculator.html" class="bg-slate-800 p-3 rounded border border-slate-700 hover:border-indigo-500 text-center block">GTU Converter</a>
                <a href="/rgpv-cgpa-calculator.html" class="bg-slate-800 p-3 rounded border border-slate-700 hover:border-indigo-500 text-center block">RGPV Converter</a>
            </div>
        </section>

    </div>

    <!-- Mandatory Legal Footer -->
    <footer class="mt-12 text-center text-xs text-slate-500 space-x-6 border-t border-slate-800 pt-6">
        <a href="/privacy-policy.html" class="hover:underline hover:text-slate-300">Privacy Policy</a>
        <a href="/terms.html" class="hover:underline hover:text-slate-300">Terms & Conditions</a>
    </footer>
</body>
</html>'''

with open("index.html", "w") as f:
    f.write(index_html)

print("Homepage updated with all tools and internal links!")
