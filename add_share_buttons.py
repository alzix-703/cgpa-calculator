import glob

share_snippet = '''
<!-- VIRAL SOCIAL SHARE BUTTONS -->
<div class="mt-8 p-4 bg-slate-800/80 rounded-xl border border-slate-700 max-w-xl mx-auto text-center space-y-3">
    <p class="text-sm font-semibold text-amber-300">Apne Dosto Aur Family Ke Sath Share Karein! 🚀</p>
    <div class="flex justify-center gap-3 flex-wrap">
        <a href="https://api.whatsapp.com/send?text=Check%20out%20this%20awesome%20Sarkari%20Yojana%20%26%20CGPA%20Calculator%20Portal%20for%20Free!%20%F0%9F%91%89%20https%3A%2F%2Fcgpa-calculator-beige-nu.vercel.app" target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded-lg text-sm font-bold flex items-center gap-2 transition">
            📲 WhatsApp Par Bhejein
        </a>
        <a href="https://t.me/share/url?url=https://cgpa-calculator-beige-nu.vercel.app&text=Check%20all%20Sarkari%20Schemes%20and%20Utility%20Calculators" target="_blank" class="bg-sky-600 hover:bg-sky-500 text-white px-4 py-2 rounded-lg text-sm font-bold flex items-center gap-2 transition">
            ✈️ Telegram Par Share Karein
        </a>
    </div>
</div>
'''

main_pages = ["index.html", "scheme-calculator.html", "age-calculator.html", "pm-kisan-status.html"]

for page in main_pages:
    try:
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()
        if "VIRAL SOCIAL SHARE BUTTONS" not in content and "</body>" in content:
            new_content = content.replace("</body>", f"{share_snippet}\n</body>")
            with open(page, "w", encoding="utf-8") as f:
                f.write(new_content)
    except Exception:
        pass

print("Share buttons added successfully!")
