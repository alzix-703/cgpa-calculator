import os, glob

smart_finder_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Sarkari Yojana Finder - Personalized Scheme Eligibility</title>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-TPS02BQ6B4"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-TPS02BQ6B4');
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen font-sans p-4 md:p-8">
    <div class="max-w-4xl mx-auto space-y-6">
        
        <!-- Header -->
        <div class="flex items-center justify-between border-b border-slate-800 pb-4">
            <a href="/" class="text-indigo-400 hover:text-indigo-300 text-sm font-semibold">&larr; Back to Home</a>
            <span class="text-xs bg-amber-500/10 text-amber-400 px-3 py-1 rounded-full border border-amber-500/20 font-medium">100% Free & Live Official Portal Direct Links</span>
        </div>

        <div class="text-center space-y-2">
            <h1 class="text-3xl md:text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-indigo-400">
                Smart Sarkari Yojana Finder 🚀
            </h1>
            <p class="text-slate-400 text-sm max-w-xl mx-auto">
                Apni accurate details daalein aur janein ki aapke liye abhi kon-kon si Sarkari Yojnaayein aur unke Official Forms open hain!
            </p>
        </div>

        <!-- Dynamic Multi-Step Form -->
        <div class="bg-slate-800/90 border border-slate-700 p-6 rounded-2xl shadow-xl space-y-6">
            <form id="yojanaForm" class="space-y-6">
                
                <!-- Section 1: Basic Information -->
                <div class="space-y-4">
                    <h2 class="text-lg font-bold text-amber-300 flex items-center gap-2">
                        <i class="fas fa-user-circle"></i> 1. Basic Information
                    </h2>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Age (Umar)*</label>
                            <input type="number" id="userAge" required placeholder="e.g. 21" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm focus:border-amber-400 focus:outline-none">
                        </div>
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Gender*</label>
                            <select id="userGender" required class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm focus:border-amber-400 focus:outline-none">
                                <option value="male">Male</option>
                                <option value="female">Female</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Category*</label>
                            <select id="userCategory" required class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm focus:border-amber-400 focus:outline-none">
                                <option value="GEN">General</option>
                                <option value="OBC">OBC</option>
                                <option value="SC">SC</option>
                                <option value="ST">ST</option>
                                <option value="EWS">EWS</option>
                            </select>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Annual Family Income (Varshik Aay)*</label>
                            <select id="userIncome" required class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm focus:border-amber-400 focus:outline-none">
                                <option value="below_1lakh">Below ₹1,00,000</option>
                                <option value="1lakh_2.5lakh">₹1 Lakh - ₹2.5 Lakhs</option>
                                <option value="2.5lakh_5lakh">₹2.5 Lakhs - ₹5 Lakhs</option>
                                <option value="above_5lakh">Above ₹5 Lakhs</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Profession / Work Profile*</label>
                            <select id="userProfession" required onchange="toggleProfessionFields()" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm focus:border-amber-400 focus:outline-none">
                                <option value="student">Student (School / College)</option>
                                <option value="farmer">Farmer (Kisan)</option>
                                <option value="unemployed">Unemployed / Job Seeker</option>
                                <option value="laborer">Worker / Artisan / Labourer</option>
                                <option value="business">Small Business / Self-Employed</option>
                            </select>
                        </div>
                    </div>
                </div>

                <!-- Section 2 Dynamic: Student Specific Fields -->
                <div id="studentFields" class="space-y-4 border-t border-slate-700 pt-4">
                    <h2 class="text-lg font-bold text-indigo-300 flex items-center gap-2">
                        <i class="fas fa-graduation-cap"></i> 2. Student Details
                    </h2>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Institution Type</label>
                            <select id="instType" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm">
                                <option value="govt">Government School/College</option>
                                <option value="private">Private College/School</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Education Level / Class</label>
                            <select id="eduLevel" onchange="toggleMathOption()" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm">
                                <option value="9_10">Class 9th - 10th</option>
                                <option value="11_12">Class 11th - 12th</option>
                                <option value="ug_diploma">UG Degree / ITI / Diploma</option>
                                <option value="pg">Post Graduation (PG)</option>
                            </select>
                        </div>
                        <div id="mathTypeDiv">
                            <label class="block text-xs text-slate-400 mb-1">Math Type (Class 9th/10th)</label>
                            <select id="mathType" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm">
                                <option value="standard">Standard Maths</option>
                                <option value="basic">Basic Maths</option>
                            </select>
                        </div>
                    </div>
                </div>

                <!-- Section 2 Dynamic: Farmer Specific Fields -->
                <div id="farmerFields" class="hidden space-y-4 border-t border-slate-700 pt-4">
                    <h2 class="text-lg font-bold text-emerald-300 flex items-center gap-2">
                        <i class="fas fa-tractor"></i> 2. Farmer (Kisan) Details
                    </h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Land Holding (Khet / Zameen)</label>
                            <select id="landHolding" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm">
                                <option value="small">Small / Marginal (< 2 Hectares)</option>
                                <option value="large">Large (> 2 Hectares)</option>
                                <option value="landless">Landless / Tenant Farmer</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Khasra / Land Papers Registered?</label>
                            <select id="landRecord" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm">
                                <option value="yes">Yes (Own Name / Family)</option>
                                <option value="no">No</option>
                            </select>
                        </div>
                    </div>
                </div>

                <!-- Submit Button -->
                <button type="submit" class="w-full bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-600 hover:to-amber-700 text-slate-950 font-bold py-3 rounded-xl transition shadow-lg text-center">
                    🔍 Find Eligible Schemes Now
                </button>
            </form>
        </div>

        <!-- Results Container -->
        <div id="resultsArea" class="hidden space-y-4">
            <h2 class="text-xl font-bold text-slate-100 flex items-center gap-2">
                <i class="fas fa-check-circle text-emerald-400"></i> Schemes You Are Eligible For:
            </h2>
            <div id="schemesList" class="grid grid-cols-1 md:grid-cols-2 gap-4"></div>
        </div>

    </div>

    <!-- Modal for Detailed Scheme Info & Official Form Link -->
    <div id="schemeModal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm hidden items-center justify-center p-4 z-50">
        <div class="bg-slate-800 border border-slate-700 max-w-xl w-full rounded-2xl p-6 space-y-4 text-slate-200">
            <div class="flex justify-between items-start">
                <h3 id="modalTitle" class="text-xl font-bold text-amber-400"></h3>
                <button onclick="closeModal()" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
            </div>
            
            <div class="space-y-3 text-sm">
                <div>
                    <h4 class="text-xs uppercase tracking-wider text-slate-400 font-bold">Why You Are Eligible:</h4>
                    <p id="modalReason" class="text-slate-200 bg-slate-900/60 p-2.5 rounded-lg border border-slate-700/50 mt-1"></p>
                </div>
                <div>
                    <h4 class="text-xs uppercase tracking-wider text-slate-400 font-bold">Required Documents:</h4>
                    <ul id="modalDocs" class="list-disc list-inside text-slate-300 space-y-1 mt-1"></ul>
                </div>
                <div>
                    <h4 class="text-xs uppercase tracking-wider text-slate-400 font-bold">Application Status:</h4>
                    <span id="modalStatus" class="inline-block mt-1 text-xs px-2.5 py-1 rounded font-semibold"></span>
                </div>
            </div>

            <div class="pt-4 border-t border-slate-700 flex gap-3">
                <a id="modalOfficialLink" href="#" target="_blank" class="flex-1 bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-2.5 rounded-lg text-center transition flex items-center justify-center gap-2">
                    <span>Apply on Official Govt Portal</span> <i class="fas fa-external-link-alt text-xs"></i>
                </a>
                <button onclick="closeModal()" class="bg-slate-700 hover:bg-slate-600 px-4 py-2.5 rounded-lg font-bold text-xs">Close</button>
            </div>
        </div>
    </div>

    <script>
        function toggleProfessionFields() {
            const prof = document.getElementById('userProfession').value;
            document.getElementById('studentFields').classList.toggle('hidden', prof !== 'student');
            document.getElementById('farmerFields').classList.toggle('hidden', prof !== 'farmer');
        }

        function toggleMathOption() {
            const edu = document.getElementById('eduLevel').value;
            document.getElementById('mathTypeDiv').classList.toggle('hidden', edu !== '9_10');
        }

        const databaseSchemes = [
            {
                id: 'pm_kisan',
                title: 'PM Kisan Samman Nidhi',
                dept: 'Ministry of Agriculture',
                check: (d) => d.prof === 'farmer' && d.landRec === 'yes',
                reason: 'Aap Registered Farmer hain aur land records verified hain.',
                docs: ['Aadhar Card', 'Khasra/Khatauni Land Record', 'Bank Passbook linked with NPCI', 'E-KYC Mobile'],
                status: 'Active (₹6000/year)',
                link: 'https://pmkisan.gov.in/'
            },
            {
                id: 'nsp_scholarship',
                title: 'National Scholarship Portal (NSP)',
                dept: 'Ministry of Education',
                check: (d) => d.prof === 'student' && (d.inc === 'below_1lakh' || d.inc === '1lakh_2.5lakh'),
                reason: 'Aap Student hain aur Varshik Aay ₹2.5 Lakh se kam hai.',
                docs: ['Mark Sheet', 'Income Certificate (Aay Praman Patra)', 'Caste Certificate', 'College/School Bonafide', 'Bank Passbook'],
                status: 'Forms Open',
                link: 'https://scholarships.gov.in/'
            },
            {
                id: 'pm_internship',
                title: 'PM Internship Scheme 2026',
                dept: 'Ministry of Corporate Affairs',
                check: (d) => d.age >= 21 && d.age <= 24 && (d.prof === 'unemployed' || (d.prof === 'student' && d.edu === 'ug_diploma')),
                reason: 'Aapki Umar 21-24 ke beech hai aur aap Youth/Student criteria fit karte hain.',
                docs: ['Aadhar Card', 'Degree/Diploma Certificate', 'Bank Account details'],
                status: 'Apply Online',
                link: 'https://pminternship.mca.gov.in/'
            },
            {
                id: 'pm_vishwakarma',
                title: 'PM Vishwakarma Scheme',
                dept: 'MSME Ministry',
                check: (d) => d.age >= 18 && d.prof === 'laborer',
                reason: 'Aap Skilled Artisan / Labourer / Traditional Craftsman category me aate hain.',
                docs: ['Aadhar Card', 'Ration Card', 'Registered Mobile Number', 'Skill Trade Proof'],
                status: 'Free Toolkits + ₹3 Lakh Loan',
                link: 'https://pmvishwakarma.gov.in/'
            },
            {
                id: 'subhadra_scheme',
                title: 'Subhadra / Nari Shakti Welfare',
                dept: 'Women & Child Development',
                check: (d) => d.gender === 'female' && d.age >= 21 && d.age <= 60 && d.inc !== 'above_5lakh',
                reason: 'Aap Eligible Female beneficiary hain under state financial support.',
                docs: ['Aadhar Card (e-KYC)', 'Bank Passbook', 'Income Certificate', 'Resident Proof'],
                status: 'Active Form Phase',
                link: 'https://subhadra.odisha.gov.in/'
            }
        ];

        document.getElementById('yojanaForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = {
                age: parseInt(document.getElementById('userAge').value),
                gender: document.getElementById('userGender').value,
                category: document.getElementById('userCategory').value,
                inc: document.getElementById('userIncome').value,
                prof: document.getElementById('userProfession').value,
                edu: document.getElementById('eduLevel').value,
                landRec: document.getElementById('landRecord').value
            };

            const eligible = databaseSchemes.filter(s => s.check(formData));
            const container = document.getElementById('schemesList');
            container.innerHTML = '';

            if(eligible.length === 0) {
                container.innerHTML = `<div class="col-span-2 text-center p-6 bg-slate-800 rounded-xl text-slate-400">Aapke criteria ke hisab se specific scheme mismatch hai. Kripya details check karein.</div>`;
            } else {
                eligible.forEach(s => {
                    container.innerHTML += `
                        <div onclick="openModal('${s.id}')" class="bg-slate-800 border border-slate-700 hover:border-amber-400/50 p-5 rounded-xl cursor-pointer transition transform hover:-translate-y-1 space-y-2 shadow-lg">
                            <div class="flex justify-between items-start">
                                <h3 class="font-bold text-amber-300 text-lg">${s.title}</h3>
                                <span class="text-[10px] bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-2 py-0.5 rounded-full font-bold">${s.status}</span>
                            </div>
                            <p class="text-xs text-slate-400"><i class="fas fa-building mr-1"></i> ${s.dept}</p>
                            <div class="text-xs text-indigo-400 font-semibold flex items-center gap-1 pt-2">
                                View Details & Apply Online &rarr;
                            </div>
                        </div>
                    `;
                });
            }
            document.getElementById('resultsArea').classList.remove('hidden');
            window.scrollTo({ top: document.getElementById('resultsArea').offsetTop - 20, behavior: 'smooth' });
        });

        let currentEligible = databaseSchemes;

        function openModal(id) {
            const scheme = currentEligible.find(s => s.id === id);
            if(!scheme) return;

            document.getElementById('modalTitle').innerText = scheme.title;
            document.getElementById('modalReason').innerText = scheme.reason;
            
            const docsList = document.getElementById('modalDocs');
            docsList.innerHTML = '';
            scheme.docs.forEach(d => {
                docsList.innerHTML += `<li>${d}</li>`;
            });

            const statusElem = document.getElementById('modalStatus');
            statusElem.innerText = scheme.status;
            statusElem.className = 'inline-block mt-1 text-xs px-2.5 py-1 rounded font-semibold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30';

            document.getElementById('modalOfficialLink').href = scheme.link;
            document.getElementById('schemeModal').classList.remove('hidden');
            document.getElementById('schemeModal').classList.add('flex');
        }

        function closeModal() {
            document.getElementById('schemeModal').classList.add('hidden');
            document.getElementById('schemeModal').classList.remove('flex');
        }
    </script>
</body>
</html>'''

with open("smart-scheme-finder.html", "w", encoding="utf-8") as f:
    f.write(smart_finder_html)

# Add Smart Finder to Footer/Header of all existing pages
link_html = '<a href="/smart-scheme-finder.html" class="text-amber-400 font-bold hover:underline">Smart Yojana Finder</a>'

for file_path in glob.glob("*.html"):
    if file_path != "smart-scheme-finder.html":
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "smart-scheme-finder.html" not in content and "</footer>" in content:
            content = content.replace("</footer>", f'  <div class="text-center mt-2">{link_html}</div>\n</footer>')
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

print("Smart Yojana Finder created and linked successfully!")
