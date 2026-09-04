import os

# 1. Salary & Income Tax Calculator
salary_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>In-Hand Salary & Tax Calculator 2026</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white min-h-screen p-6 max-w-3xl mx-auto space-y-6">
    <a href="/" class="text-indigo-400 hover:underline">&larr; Back to Home</a>
    <h1 class="text-3xl font-bold text-indigo-400">In-Hand Salary Calculator</h1>
    <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 space-y-4">
        <div>
            <label class="block text-sm mb-1">Annual CTC (₹)</label>
            <input type="number" id="ctc" placeholder="e.g. 600000" class="w-full bg-slate-700 border border-slate-600 rounded p-2 text-white">
        </div>
        <div>
            <label class="block text-sm mb-1">Monthly PF (₹)</label>
            <input type="number" id="pf" value="1800" class="w-full bg-slate-700 border border-slate-600 rounded p-2 text-white">
        </div>
        <button onclick="calcSalary()" class="w-full bg-indigo-600 hover:bg-indigo-500 py-2 rounded font-semibold">Calculate</button>
        <div id="salary-res" class="hidden p-4 bg-slate-700 rounded-lg space-y-1">
            <p id="in-hand-text" class="text-lg font-bold text-emerald-400"></p>
            <p id="tax-text" class="text-sm text-slate-300"></p>
        </div>
    </div>
    <script>
        function calcSalary() {
            const ctc = parseFloat(document.getElementById('ctc').value);
            const pf = parseFloat(document.getElementById('pf').value) || 0;
            if(!ctc) return;
            let tax = 0;
            const taxable = Math.max(0, ctc - 75000);
            if(taxable > 1200000) tax = (taxable - 1200000) * 0.20 + 90000;
            else if(taxable > 700000) tax = (taxable - 700000) * 0.10;
            const monthly = Math.round((ctc - (pf * 12) - tax) / 12);
            document.getElementById('salary-res').classList.remove('hidden');
            document.getElementById('in-hand-text').innerText = 'Monthly In-Hand: ₹' + monthly.toLocaleString('en-IN');
            document.getElementById('tax-text').innerText = 'Estimated Annual Tax: ₹' + Math.round(tax).toLocaleString('en-IN');
        }
    </script>
</body>
</html>'''

# 2. GST Calculator Tool
gst_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GST Calculator India - Add/Remove GST</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white min-h-screen p-6 max-w-3xl mx-auto space-y-6">
    <a href="/" class="text-indigo-400 hover:underline">&larr; Back to Home</a>
    <h1 class="text-3xl font-bold text-indigo-400">GST Calculator</h1>
    <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 space-y-4">
        <div>
            <label class="block text-sm mb-1">Amount (₹)</label>
            <input type="number" id="amount" placeholder="e.g. 5000" class="w-full bg-slate-700 border border-slate-600 rounded p-2 text-white">
        </div>
        <div>
            <label class="block text-sm mb-1">GST Rate (%)</label>
            <select id="rate" class="w-full bg-slate-700 border border-slate-600 rounded p-2 text-white">
                <option value="5">5%</option>
                <option value="12">12%</option>
                <option value="18" selected>18%</option>
                <option value="28">28%</option>
            </select>
        </div>
        <div class="flex gap-4">
            <button onclick="calcGST(true)" class="w-1/2 bg-indigo-600 hover:bg-indigo-500 py-2 rounded font-semibold">Add GST</button>
            <button onclick="calcGST(false)" class="w-1/2 bg-slate-600 hover:bg-slate-500 py-2 rounded font-semibold">Remove GST</button>
        </div>
        <div id="gst-res" class="hidden p-4 bg-slate-700 rounded-lg space-y-1">
            <p id="gst-amount" class="text-emerald-400 font-medium"></p>
            <p id="total-amount" class="text-xl font-bold text-white"></p>
        </div>
    </div>
    <script>
        function calcGST(isAdd) {
            const amt = parseFloat(document.getElementById('amount').value);
            const rate = parseFloat(document.getElementById('rate').value);
            if(!amt) return;
            let gst = 0, total = 0;
            if(isAdd) {
                gst = (amt * rate) / 100;
                total = amt + gst;
            } else {
                total = amt / (1 + (rate / 100));
                gst = amt - total;
            }
            document.getElementById('gst-res').classList.remove('hidden');
            document.getElementById('gst-amount').innerText = 'GST Amount: ₹' + gst.toFixed(2);
            document.getElementById('total-amount').innerText = 'Total Amount: ₹' + total.toFixed(2);
        }
    </script>
</body>
</html>'''

with open("salary-tax-calculator.html", "w") as f: f.write(salary_html)
with open("gst-calculator.html", "w") as f: f.write(gst_html)

print("Salary and GST tools created successfully!")
