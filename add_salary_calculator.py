salary_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>In-Hand Salary & Tax Calculator 2026 (New vs Old Regime)</title>
    <meta name="description" content="Calculate your exact monthly in-hand salary, PF deductions, and income tax breakdown easily.">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white min-h-screen p-4 md:p-8">
    <div class="max-w-3xl mx-auto space-y-6">
        <a href="/" class="text-indigo-400 hover:underline">&larr; Back to Portal Home</a>
        <h1 class="text-3xl font-bold text-indigo-400">In-Hand Salary & Income Tax Calculator</h1>
        
        <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 space-y-4">
            <div class="space-y-3">
                <label class="block text-sm">Cost to Company (CTC) per Annum (₹)</label>
                <input type="number" id="ctc" placeholder="e.g. 600000" class="w-full bg-slate-700 border border-slate-600 rounded p-2 text-white">

                <label class="block text-sm">Monthly PF / EPF Contribution (₹)</label>
                <input type="number" id="pf" value="1800" class="w-full bg-slate-700 border border-slate-600 rounded p-2 text-white">

                <button onclick="calculateSalary()" class="w-full bg-indigo-600 hover:bg-indigo-500 py-2 rounded font-semibold transition">Calculate In-Hand Salary</button>
            </div>

            <div id="salary-result" class="hidden p-4 rounded-lg bg-slate-700 space-y-2">
                <p class="text-lg font-semibold text-emerald-400" id="in-hand"></p>
                <p class="text-sm text-slate-300" id="tax-details"></p>
            </div>
        </div>

        <footer class="text-center text-xs text-slate-500 space-x-4">
            <a href="/privacy-policy.html" class="hover:underline">Privacy Policy</a>
            <a href="/terms.html" class="hover:underline">Terms & Conditions</a>
        </footer>
    </div>

    <script>
        function calculateSalary() {
            const ctc = parseFloat(document.getElementById('ctc').value);
            const pf = parseFloat(document.getElementById('pf').value) || 0;
            if(!ctc || ctc <= 0) return;

            let annualTax = 0;
            const taxableIncome = Math.max(0, ctc - 75000); // Standard deduction 75k

            if (taxableIncome > 1200000) {
                annualTax = (taxableIncome - 1200000) * 0.20 + 90000;
            } else if (taxableIncome > 700000) {
                annualTax = (taxableIncome - 700000) * 0.10;
            }

            const annualInHand = ctc - (pf * 12) - annualTax;
            const monthlyInHand = Math.round(annualInHand / 12);

            document.getElementById('salary-result').classList.remove('hidden');
            document.getElementById('in-hand').innerText = `Estimated Monthly In-Hand Salary: ₹${monthlyInHand.toLocaleString('en-IN')}`;
            document.getElementById('tax-details').innerText = `Annual Estimated Tax (New Regime): ₹${Math.round(annualTax).toLocaleString('en-IN')} | Monthly PF: ₹${pf}`;
        }
    </script>
</body>
</html>'''

with open("salary-tax-calculator.html", "w") as f:
    f.write(salary_html)

print("Salary & Tax Tool created successfully!")
