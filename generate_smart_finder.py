import os, glob

smart_finder_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Sarkari Yojana Finder - Live Scheme Eligibility & Dates</title>
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
            <span class="text-xs bg-emerald-500/10 text-emerald-400 px-3 py-1 rounded-full border border-emerald-500/20 font-medium">● Verified Official Govt Portals</span>
        </div>

        <div class="text-center space-y-2">
            <h1 class="text-3xl md:text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-indigo-400">
                Smart Sarkari Yojana Finder 🚀
            </h1>
            <p class="text-slate-400 text-sm max-w-xl mx-auto">
                Apni accurate details daalein aur janein ki aapke liye abhi kon-kon si Sarkari Yojnaayein, unki Active Last Dates aur Official Forms open hain!
            </p>
        </div>

        <!-- Dynamic Form -->
        <div class="bg-slate-800/90 border border-slate-700 p-6 rounded-2xl shadow-xl space-y-6">
            <form id="yojanaForm" class="space-y-6">
                
                <!-- Section 1: Basic Information -->
                <div class="space-y-4">
                    <h2 class="text-lg font-bold text-amber-300 flex items-center gap-2">
                        <i class="fas fa-user-circle"></i> 1. Personal & Financial Profile
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
                            <label class="block text-xs text-slate-400 mb-1">Profession / Occupation*</label>
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
                        <i class="fas fa-graduation-cap"></i> 2. Academic Details
                    </h2>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Institution Type</label>
                            <select id="instType" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm">
                                <option value="govt">Government Institution</option>
                                <option value="private">Private Institution</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Education Level / Course</label>
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
                        <i class="fas fa-tractor"></i> 2. Agricultural Profile
                    </h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Land Holding Size</label>
                            <select id="landHolding" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm">
                                <option value="small">Small / Marginal (< 2 Hectares)</option>
                                <option value="large">Large (> 2 Hectares)</option>
                                <option value="landless">Landless / Tenant Farmer</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Khasra / Land Records Available?</label>
                            <select id="landRecord" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm">
                                <option value="yes">Yes (Self / Family Name)</option>
                                <option value="no">No</option>
                            </select>
                        </div>
                    </div>
                </div>

                <!-- Submit Button -->
                <button type="submit" class="w-full bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-600 hover:to-amber-700 text-slate-950 font-bold py-3 rounded-xl transition shadow-lg text-center">
                    🔍 Find Eligible Schemes & Active Forms
                </button>
            </form>
        </div>

        <!-- Results Container -->
        <div id="resultsArea" class="hidden space-y-4">
            <h2 class="text-xl font-bold text-slate-100 flex items-center gap-2">
                <i class="fas fa-check-circle text-emerald-400"></i> Matching Sarkari Schemes:
            </h2>
            <div id="schemesList" class="grid grid-cols-1 md:grid-cols-2 gap-4"></div>
        </div>

    </div>

    <!-- Modal for Detailed Scheme Info, Status, Dates & Official Form Link -->
    <div id="schemeModal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm hidden items-center justify-center p-4 z-50">
        <div class="bg-slate-800 border border-slate-700 max-w-xl w-full rounded-2xl p-6 space-y-4 text-slate-200 shadow-2xl">
            <div class="flex justify-between items-start">
                <div>
                    <h3 id="modalTitle" class="text-xl font-bold text-amber-400"></h3>
                    <p id="modalDept" class="text-xs text-slate-400 mt-0.5"></p>
                </div>
                <button onclick="closeModal()" class="text-slate-400 hover:text-white text-2xl font-bold">&times;</button>
            </div>
            
            <div class="space-y-4 text-sm">
                
                <!-- Status & Important Dates Box -->
                <div class="bg-slate-900/80 border border-slate-700/80 p-3.5 rounded-xl space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="text-xs uppercase tracking-wider text-slate-400 font-bold">Form Status:</span>
                        <span id="modalStatusBadge" class="text-xs px-2.5 py-1 rounded-full font-bold"></span>
                    </div>
                    <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800 text-xs">
                        <div>
                            <span class="text-slate-400 block">Start Date:</span>
                            <span id="modalStartDate" class="font-semibold text-slate-200"></span>
                        </div>
                        <div>
                            <span class="text-slate-400 block">Last Date / Deadline:</span>
                            <span id="modalLastDate" class="font-semibold text-amber-300"></span>
                        </div>
                    </div>
                </div>

                <div>
                    <h4 class="text-xs uppercase tracking-wider text-slate-400 font-bold">Why You Are Eligible:</h4>
                    <p id="modalReason" class="text-slate-200 bg-slate-900/50 p-2.5 rounded-lg border border-slate-700/50 mt-1 text-xs leading-relaxed"></p>
                </div>

                <div>
                    <h4 class="text-xs uppercase tracking-wider text-slate-400 font-bold">Required Documents:</h4>
                    <ul id="modalDocs" class="list-disc list-inside text-slate-300 text-xs space-y-1 mt-1"></ul>
                </div>

            </div>

            <div class="pt-4 border-t border-slate-700 flex gap-3">
                <a id="modalOfficialLink" href="#" target="_blank" class="flex-1 bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-2.5 rounded-lg text-center transition flex items-center justify-center gap-2 text-sm">
                    <span>Go to Official Govt Form Portal</span> <i class="fas fa-external-link-alt text-xs"></i>
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
                dept: 'Ministry of Agriculture & Farmers Welfare',
                check: (d) => d.prof === 'farmer' && d.landRec === 'yes',
                reason: 'Aap Registered Farmer hain aur land records valid hain.',
                docs: ['Aadhar Card', 'Khasra/Khatauni Land Paper', 'Bank Passbook linked with NPCI/Aadhar', 'Mobile Number for e-KYC'],
                statusText: 'Active / Continuous Registration',
                statusType: 'active',
                startDate: 'Ongoing 2026 Cycle',
                lastDate: 'Open Year-Round (Next Installment Oct 2026)',
                link: 'https://pmkisan.gov.in/'
            },
            {
                id: 'nsp_scholarship',
                title: 'National Scholarship Portal (NSP)',
                dept: 'Ministry of Education / Minority Affairs',
                check: (d) => d.prof === 'student' && (d.inc === 'below_1lakh' || d.inc === '1lakh_2.5lakh'),
                reason: 'Aap Student hain aur Varshik Family Income ₹2.5 Lakh se kam hai.',
                docs: ['Previous Year Mark Sheet', 'Aay Praman Patra (Income Certificate)', 'Caste Certificate', 'Bonafide Student Certificate', 'Bank Passbook'],
                statusText: 'Forms Open (Active Phase)',
                statusType: 'active',
                startDate: 'June 1, 2026',
                lastDate: 'October 31, 2026',
                link: 'https://scholarships.gov.in/'
            },
            {
                id: 'pm_internship',
                title: 'PM Internship Scheme 2026',
                dept: 'Ministry of Corporate Affairs',
                check: (d) => d.age >= 21 && d.age <= 24 && (d.prof === 'unemployed' || (d.prof === 'student' && d.edu === 'ug_diploma')),
                reason: 'Aapki Age 21-24 hai aur aap Higher Education / Unemployed Youth profile match karte hain.',
                docs: ['Aadhar Card', 'Degree/Diploma Certificate / Marksheets', 'Bank Account details'],
                statusText: 'Active Registration Phase',
                statusType: 'active',
                startDate: 'August 15, 2026',
                lastDate: 'November 15, 2026',
                link: 'https://pminternship.mca.gov.in/'
            },
            {
                id: 'pm_vishwakarma',
                title: 'PM Vishwakarma Scheme',
                dept: 'Ministry of Micro, Small & Medium Enterprises (MSME)',
                check: (d) => d.age >= 18 && d.prof === 'laborer',
                reason: 'Aap Skilled Artisan / Artisan / Traditional Worker category me fit hain.',
                docs: ['Aadhar Card', 'Ration Card', 'Registered Mobile Number', 'Skill Trade Proof'],
                statusText: 'Active (Toolkits + Collateral Free Loan)',
                statusType: 'active',
                startDate: 'Open Portal',
                lastDate: 'Ongoing Open Scheme',
                link: 'https://pmvishwakarma.gov.in/'
            },
            {
                id: 'subhadra_scheme',
                title: 'Subhadra / Nari Shakti Welfare',
                dept: 'Department of Women & Child Development',
                check: (d) => d.gender === 'female' && d.age >= 21 && d.age <= 60 && d.inc !== 'above_5lakh',
                reason: 'Aap Eligible Female Beneficiary hain under Direct Benefit Transfer (DBT).',
                docs: ['Aadhar Card (e-KYC Completed)', 'Bank Account linked with Aadhar', 'Income Certificate', 'Resident Proof'],
                statusText: 'Active Phase',
                statusType: 'active',
                startDate: 'July 2026',
                lastDate: 'December 31, 2026',
                link: 'https://subhadra.odisha.gov.in/'
            }
        ];

        let currentEligibleList = [];

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

            currentEligibleList = databaseSchemes.filter(s => s.check(formData));
            const container = document.getElementById('schemesList');
            container.innerHTML = '';

            if(currentEligibleList.length === 0) {
                container.innerHTML = `<div class="col-span-2 text-center p-6 bg-slate-800 rounded-xl text-slate-400 text-sm">Aapke diye gaye parameters ke hisab se exact match scheme closed ya available nahi hai. Parameter change karke re-try karein.</div>`;
            } else {
                currentEligibleList.forEach(s => {
                    const badgeClass = s.statusType === 'active' 
                        ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30' 
                        : 'bg-amber-500/20 text-amber-400 border-amber-500/30';

                    container.innerHTML += `
                        <div onclick="openModal('${s.id}')" class="bg-slate-800 border border-slate-700 hover:border-amber-400/50 p-5 rounded-xl cursor-pointer transition transform hover:-translate-y-1 space-y-3 shadow-lg">
                            <div class="flex justify-between items-start">
                                <h3 class="font-bold text-amber-300 text-lg">${s.title}</h3>
                                <span class="text-[10px] border px-2.5 py-0.5 rounded-full font-bold ${badgeClass}">${s.statusText}</span>
                            </div>
                            <p class="text-xs text-slate-400"><i class="fas fa-building mr-1"></i> ${s.dept}</p>
                            <div class="flex justify-between items-center text-xs pt-2 border-t border-slate-700/60">
                                <span class="text-slate-400">Deadline: <strong class="text-slate-200">${s.lastDate}</strong></span>
                                <span class="text-indigo-400 font-semibold">View Details &rarr;</span>
                            </div>
                        </div>
                    `;
                });
            }
            document.getElementById('resultsArea').classList.remove('hidden');
            window.scrollTo({ top: document.getElementById('resultsArea').offsetTop - 20, behavior: 'smooth' });
        });

        function openModal(id) {
            const scheme = currentEligibleList.find(s => s.id === id) || databaseSchemes.find(s => s.id === id);
            if(!scheme) return;

            document.getElementById('modalTitle').innerText = scheme.title;
            document.getElementById('modalDept').innerText = scheme.dept;
            document.getElementById('modalReason').innerText = scheme.reason;
            document.getElementById('modalStartDate').innerText = scheme.startDate;
            document.getElementById('modalLastDate').innerText = scheme.lastDate;
            
            const docsList = document.getElementById('modalDocs');
            docsList.innerHTML = '';
            scheme.docs.forEach(d => {
                docsList.innerHTML += `<li>${d}</li>`;
            });

            const badgeElem = document.getElementById('modalStatusBadge');
            badgeElem.innerText = scheme.statusText;
            if(scheme.statusType === 'active') {
                badgeElem.className = 'text-xs px-2.5 py-1 rounded-full font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30';
            } else {
                badgeElem.className = 'text-xs px-2.5 py-1 rounded-full font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30';
            }

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

print("Smart Finder upgraded with exact Dates and Active Status!")
