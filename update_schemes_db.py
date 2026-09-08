
smart_scheme_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Sarkari Yojana Finder 2026 - Find Eligible Government Schemes</title>
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
        <div class="flex justify-between items-center border-b border-slate-800 pb-4">
            <a href="/" class="text-xs text-amber-400 hover:underline flex items-center gap-1">
                <i class="fas fa-arrow-left"></i> Back to All Tools
            </a>
            <span class="text-xs bg-amber-500/10 text-amber-400 border border-amber-500/20 px-2.5 py-1 rounded-full font-medium">Updated 2026</span>
        </div>

        <div class="text-center space-y-2">
            <h1 class="text-2xl md:text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-orange-400">
                Smart Sarkari Yojana Finder
            </h1>
            <p class="text-xs md:text-sm text-slate-400">Find eligible schemes for Students, Farmers, Businessmen, Women, Senior Citizens & Job Seekers.</p>
        </div>

        <!-- Filter Form -->
        <div class="bg-slate-800/90 border border-slate-700/80 p-5 rounded-2xl shadow-xl space-y-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">Age (Years)</label>
                    <input type="number" id="userAge" placeholder="e.g. 24" value="22" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-sm text-white focus:outline-none focus:border-amber-500">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">Gender</label>
                    <select id="userGender" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-sm text-white focus:outline-none focus:border-amber-500">
                        <option value="all">All / Any</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">Profession / Status</label>
                    <select id="userCategory" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-sm text-white focus:outline-none focus:border-amber-500">
                        <option value="all">All Categories</option>
                        <option value="student">Student</option>
                        <option value="farmer">Farmer / Agriculture</option>
                        <option value="business">Business / Entrepreneur</option>
                        <option value="unemployed">Unemployed / Job Seeker</option>
                        <option value="salaried">Salaried Employee</option>
                        <option value="senior">Senior Citizen</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">Annual Family Income</label>
                    <select id="userIncome" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-sm text-white focus:outline-none focus:border-amber-500">
                        <option value="all">Any Income Limit</option>
                        <option value="below2.5l">Below ₹2.5 Lakhs</option>
                        <option value="below8l">Below ₹8.0 Lakhs (EWS)</option>
                        <option value="above8l">Above ₹8.0 Lakhs</option>
                    </select>
                </div>
            </div>

            <button onclick="findSchemes()" class="w-full bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-slate-900 font-bold py-3 rounded-xl transition shadow-lg text-sm flex items-center justify-center gap-2">
                <i class="fas fa-search"></i> Check Eligible Sarkari Schemes
            </button>
        </div>

        <!-- Results Section -->
        <div id="resultsCount" class="text-sm font-semibold text-slate-300 px-1"></div>
        <div id="schemesList" class="grid grid-cols-1 md:grid-cols-2 gap-4"></div>

    </div>

    <script>
    const schemesData = [
        // Students
        {
            name: "National Means-cum-Merit Scholarship (NMMSS)",
            category: "student",
            minAge: 12, maxAge: 18,
            gender: "all",
            income: "below2.5l",
            benefits: "₹12,000 per year for Class 9 to 12 students.",
            docs: "Income Certificate, Class 8 Marksheet, Aadhaar Card, Bank Account",
            applyUrl: "https://scholarships.gov.in"
        },
        {
            name: "PM Yasasvi Post-Matric Scholarship",
            category: "student",
            minAge: 14, maxAge: 28,
            gender: "all",
            income: "below2.5l",
            benefits: "Scholarship upto ₹1,25,000/year for OBC, EBC & DNT students.",
            docs: "Caste Certificate, Income Certificate, Previous Class Marksheet",
            applyUrl: "https://yet.nta.ac.in"
        },
        {
            name: "Central Sector Scheme of Scholarship (CSSS)",
            category: "student",
            minAge: 17, maxAge: 25,
            gender: "all",
            income: "below8l",
            benefits: "₹12,000 to ₹20,000/year for College & University pursuing students.",
            docs: "12th Board Marksheet (Top 20th percentile), Income Certificate",
            applyUrl: "https://scholarships.gov.in"
        },

        // Farmers
        {
            name: "PM Kisan Samman Nidhi Scheme",
            category: "farmer",
            minAge: 18, maxAge: 75,
            gender: "all",
            income: "all",
            benefits: "₹6,000 direct income support per year (3 installments of ₹2000).",
            docs: "Land Ownership Record (Khata/Khasra), Aadhaar, Bank Passbook, e-KYC",
            applyUrl: "https://pmkisan.gov.in"
        },
        {
            name: "PM Fasal Bima Yojana (PMFBY)",
            category: "farmer",
            minAge: 18, maxAge: 80,
            gender: "all",
            income: "all",
            benefits: "Low-premium crop insurance against natural disasters & loss.",
            docs: "Land Possession Certificate, Crop Details, Bank Account",
            applyUrl: "https://pmfby.gov.in"
        },
        {
            name: "Kisan Credit Card (KCC) Scheme",
            category: "farmer",
            minAge: 18, maxAge: 70,
            gender: "all",
            income: "all",
            benefits: "Low-interest agricultural loan up to ₹3 Lakh at 4% effective interest.",
            docs: "Aadhaar Card, Land Record documents, Passport Photo",
            applyUrl: "https://pmkisan.gov.in/KCC.aspx"
        },

        // Business / Entrepreneurs
        {
            name: "Pradhan Mantri MUDRA Yojana (PMMY)",
            category: "business",
            minAge: 18, maxAge: 65,
            gender: "all",
            income: "all",
            benefits: "Collateral-free business loans up to ₹10 Lakhs (Shishu, Kishor, Tarun).",
            docs: "Business Plan, KYC Documents, Bank Statements",
            applyUrl: "https://www.mudra.org.in"
        },
        {
            name: "PMEGP (PM Employment Generation Programme)",
            category: "business",
            minAge: 18, maxAge: 60,
            gender: "all",
            income: "all",
            benefits: "Up to 35% government subsidy on business loans up to ₹50 Lakhs.",
            docs: "Project Report, Educational Qualification Certificate, Caste/Category Cert",
            applyUrl: "https://www.kviconline.gov.in/pmegpeportal/"
        },
        {
            name: "PM Vishwakarma Yojana",
            category: "business",
            minAge: 18, maxAge: 65,
            gender: "all",
            income: "all",
            benefits: "₹15,000 Toolkit Incentive + ₹3 Lakh collateral-free loan at 5% interest.",
            docs: "Aadhaar, Bank Details, Skill/Trade verification",
            applyUrl: "https://pmvishwakarma.gov.in"
        },

        // Unemployed / Job Seekers
        {
            name: "PM Kaushal Vikas Yojana (PMKVY 4.0)",
            category: "unemployed",
            minAge: 15, maxAge: 45,
            gender: "all",
            income: "all",
            benefits: "Free Industry Skill Training, Govt Certification & Job Placement Assistance.",
            docs: "Aadhaar Card, Bank Account Details",
            applyUrl: "https://www.pmkvyofficial.org"
        },
        {
            name: "National Career Service (NCS) Portal",
            category: "unemployed",
            minAge: 18, maxAge: 50,
            gender: "all",
            income: "all",
            benefits: "Direct registration for Government job fairs, career counseling & job listings.",
            docs: "Educational Certificates, Resume, Aadhaar",
            applyUrl: "https://www.ncs.gov.in"
        },

        // Women / Nari Shakti
        {
            name: "Lakhpati Didi Yojana",
            category: "all",
            minAge: 18, maxAge: 55,
            gender: "female",
            income: "below2.5l",
            benefits: "Interest-free financial support & training for Self Help Group (SHG) women.",
            docs: "Aadhaar Card, SHG Membership ID, Bank Account",
            applyUrl: "https://nrlm.gov.in"
        },
        {
            name: "Mahila Samman Savings Certificate",
            category: "all",
            minAge: 10, maxAge: 80,
            gender: "female",
            income: "all",
            benefits: "Guaranteed 7.5% fixed interest rate for 2-year deposit up to ₹2 Lakhs.",
            docs: "Aadhaar Card, PAN Card, Passport Photo",
            applyUrl: "https://www.indiapost.gov.in"
        },

        // Senior Citizens
        {
            name: "Ayushman Bharat 70+ Universal Health Coverage",
            category: "senior",
            minAge: 70, maxAge: 100,
            gender: "all",
            income: "all",
            benefits: "Free health coverage up to ₹5 Lakhs per year for all seniors above 70 age.",
            docs: "Aadhaar Card with correct Date of Birth",
            applyUrl: "https://dashboard.pmjay.gov.in/setu/"
        },
        {
            name: "Senior Citizens Savings Scheme (SCSS)",
            category: "senior",
            minAge: 60, maxAge: 100,
            gender: "all",
            income: "all",
            benefits: "High guaranteed interest rate (8.2%) with tax exemptions under 80C.",
            docs: "Age Proof, PAN Card, Aadhaar Card",
            applyUrl: "https://www.indiapost.gov.in"
        },

        // Salaried / Universal
        {
            name: "Pradhan Mantri Awas Yojana (PMAY-Urban/Gramin)",
            category: "salaried",
            minAge: 21, maxAge: 65,
            gender: "all",
            income: "below8l",
            benefits: "Up to ₹2.67 Lakh interest subsidy on home construction/purchase.",
            docs: "Income Certificate, Land/Property Docs, Aadhaar, Bank Details",
            applyUrl: "https://pmaymis.gov.in"
        },
        {
            name: "PM Suraksha Bima Yojana (PMSBY)",
            category: "all",
            minAge: 18, maxAge: 70,
            gender: "all",
            income: "all",
            benefits: "₹2 Lakh accidental death/disability coverage at just ₹20 per year.",
            docs: "Aadhaar Card linked Bank Account",
            applyUrl: "https://www.financialservices.gov.in"
        }
    ];

    function findSchemes() {
        const age = parseInt(document.getElementById('userAge').value) || 0;
        const gender = document.getElementById('userGender').value;
        const category = document.getElementById('userCategory').value;
        const income = document.getElementById('userIncome').value;

        const filtered = schemesData.filter(s => {
            const ageMatch = age >= s.minAge && age <= s.maxAge;
            const genderMatch = (gender === 'all' || s.gender === 'all' || s.gender === gender);
            const categoryMatch = (category === 'all' || s.category === 'all' || s.category === category);
            
            let incomeMatch = true;
            if (income === 'above8l' && s.income === 'below2.5l') incomeMatch = false;
            if (income === 'above8l' && s.income === 'below8l') incomeMatch = false;

            return ageMatch && genderMatch && categoryMatch && incomeMatch;
        });

        const listContainer = document.getElementById('schemesList');
        const countContainer = document.getElementById('resultsCount');

        countContainer.innerHTML = `Found <span class="text-amber-400 font-bold">\${filtered.length}</span> eligible schemes for your criteria:`;

        if (filtered.length === 0) {
            listContainer.innerHTML = `
                <div class="col-span-2 text-center py-10 bg-slate-800/50 rounded-xl border border-slate-700/50">
                    <p class="text-slate-400 text-sm">No specific scheme found for this exact combination.</p>
                    <button onclick="document.getElementById('userCategory').value='all'; findSchemes();" class="mt-2 text-xs text-amber-400 hover:underline">
                        Try viewing all general schemes
                    </button>
                </div>
            `;
            return;
        }

        listContainer.innerHTML = filtered.map(s => `
            <div class="bg-slate-800/80 border border-slate-700/80 hover:border-amber-500/40 p-4 rounded-xl space-y-3 flex flex-col justify-between shadow-md">
                <div class="space-y-2">
                    <div class="flex justify-between items-start gap-2">
                        <h3 class="font-bold text-amber-400 text-base">\${s.name}</h3>
                        <span class="text-[10px] bg-slate-700 text-slate-300 px-2 py-0.5 rounded capitalize">\${s.category}</span>
                    </div>
                    <p class="text-xs text-slate-300 bg-slate-900/60 p-2 rounded-lg border border-slate-800">
                        <strong class="text-emerald-400">Benefit:</strong> \${s.benefits}
                    </p>
                    <p class="text-[11px] text-slate-400">
                        <strong class="text-slate-300">Required Docs:</strong> \${s.docs}
                    </p>
                </div>
                <a href="\${s.applyUrl}" target="_blank" rel="noopener noreferrer" class="block text-center bg-slate-700 hover:bg-amber-500 hover:text-slate-950 text-amber-300 font-semibold text-xs py-2 rounded-lg transition">
                    Apply on Official Portal <i class="fas fa-external-link-alt ml-1 text-[10px]"></i>
                </a>
            </div>
        `).join('');
    }

    // Initial load
    findSchemes();
    </script>
</body>
</html>'''

with open("smart-scheme-finder.html", "w", encoding="utf-8") as f:
    f.write(smart_scheme_html)

print("Smart Scheme Finder Database expanded successfully with multi-category support!")
