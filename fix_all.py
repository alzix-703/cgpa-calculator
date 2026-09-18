import os

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AIOUTP Premium Shayari & Emotional Stories Portal 2026</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
        body { background-color: #0b1120; color: #fff; padding: 16px; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
        .card { background: #1e293b; border: 1px solid #334155; padding: 20px; border-radius: 16px; max-width: 480px; width: 100%; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        h1 { font-size: 1.3rem; color: #f43f5e; margin-bottom: 8px; font-weight: 700; }
        p { color: #94a3b8; font-size: 0.85rem; margin-bottom: 16px; line-height: 1.4; }
        
        .mode-btn-container { display: flex; gap: 8px; margin-bottom: 16px; }
        .mode-btn { flex: 1; padding: 10px; background: #0f172a; border: 1px solid #334155; color: #fff; border-radius: 8px; font-weight: 700; cursor: pointer; font-size: 0.8rem; transition: all 0.3s; }
        .mode-btn.active { background: #e11d48; border-color: #f43f5e; }

        .teaser-box { background: #0f172a; border: 1px solid #334155; border-radius: 10px; padding: 14px; text-align: left; margin-bottom: 16px; position: relative; overflow: hidden; }
        .teaser-text { font-size: 0.9rem; line-height: 1.5; color: #e2e8f0; }
        .blur-overlay { filter: blur(4px); opacity: 0.4; user-select: none; }
        
        .note-box { background: #451a03; border: 1px solid #78350f; color: #fcd34d; padding: 10px; border-radius: 8px; font-size: 0.78rem; text-align: left; margin-bottom: 14px; line-height: 1.3; }
        
        .share-status { font-size: 0.85rem; color: #f59e0b; margin-bottom: 10px; font-weight: 600; }
        .whatsapp-btn { display: block; width: 100%; padding: 12px; background: #22c55e; color: #fff; text-decoration: none; font-weight: 700; border-radius: 8px; margin-bottom: 16px; font-size: 0.9rem; text-align: center; cursor: pointer; }

        .divider { border-top: 1px dashed #334155; margin: 18px 0; }

        .code-search-box { background: #0f172a; padding: 14px; border-radius: 12px; border: 1px solid #3b82f6; text-align: left; margin-top: 10px; }
        .code-search-box label { font-size: 0.82rem; color: #60a5fa; display: block; margin-bottom: 8px; font-weight: 700; }
        .type-select { width: 100%; padding: 8px; background: #1e293b; border: 1px solid #334155; color: #fff; border-radius: 6px; font-size: 0.85rem; outline: none; margin-bottom: 8px; }
        .input-group { display: flex; gap: 8px; }
        .code-search-box input { flex: 1; padding: 9px; background: #1e293b; border: 1px solid #334155; color: #fff; border-radius: 6px; font-size: 0.85rem; outline: none; }
        .code-search-box button { padding: 9px 16px; background: #2563eb; border: none; color: #fff; border-radius: 6px; font-weight: 700; cursor: pointer; font-size: 0.85rem; }

        .select-box { background: #0f172a; padding: 12px; border-radius: 8px; margin-top: 12px; text-align: left; border: 1px solid #334155; display: none; }
        .select-box label { font-size: 0.8rem; color: #cbd5e1; display: block; margin-bottom: 6px; font-weight: 600; }
        .select-box select { width: 100%; padding: 10px; border-radius: 6px; background: #1e293b; color: #fff; border: 1px solid #334155; outline: none; font-size: 0.85rem; }

        .content-display { background: #0f172a; border: 1px solid #22c55e; border-radius: 10px; padding: 16px; text-align: left; margin-top: 16px; display: none; font-size: 0.9rem; line-height: 1.6; color: #f8fafc; }
        .code-tag { background: #1e293b; border: 1px solid #eab308; color: #eab308; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; display: inline-block; margin-bottom: 10px; }
        .error-msg { color: #ef4444; font-weight: bold; font-size: 0.82rem; margin-top: 8px; display: none; text-align: left; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🔥 Premium Shayari & Stories Hub</h1>
        <p>Choose what you want to read & unlock extreme dopamine content!</p>

        <div class="mode-btn-container">
            <button id="btnShayari" class="mode-btn active" onclick="switchMode('shayari')">✨ Shayaris</button>
            <button id="btnStory" class="mode-btn" onclick="switchMode('story')">📖 One-Sided Love Stories</button>
        </div>

        <div id="mainFlow">
            <div class="teaser-box">
                <div id="teaserContent" class="teaser-text">
                    "Dil ke kone se ek hi aawaaz aati hai, Unhe chaahna hamari sabse haseen galti thi..." <br>
                    <span class="blur-overlay">Par unka kisi aur ke sath muskuraana hamare dil par khanjar ki tarah chal gaya. Woh nahi jaante ki unke ek message ke liye kitna intezaar...</span>
                </div>
            </div>

            <div class="note-box" id="noteWarning">
                📌 <b>Note:</b> Share to <b>3 WhatsApp friends/groups</b>. Total validation takes minimum <b>30 seconds</b> on WhatsApp. Direct fast unlock without waiting will not work!
            </div>

            <div class="share-status" id="shareCounter">🔒 Progress: 0/3 Shares Done</div>
            
            <a id="waShare" href="javascript:void(0)" class="whatsapp-btn" onclick="startShareProcess()">📲 Share on WhatsApp Direct</a>
        </div>

        <div class="divider"></div>

        <div class="code-search-box">
            <label>🔍 Find Saved Content (Enter valid code with 5 digits):</label>
            <select id="contentTypeSelect" class="type-select">
                <option value="shayari">✨ Shayari Code</option>
                <option value="story">📖 Story Code</option>
            </select>
            <div class="input-group">
                <input type="text" id="codeInput" placeholder="Enter code / secret key">
                <button onclick="fetchByCode()">Search</button>
            </div>
            <div class="error-msg" id="codeError"></div>
        </div>

        <div class="select-box" id="categorySelectBox">
            <label id="selectLabel">Choose Category:</label>
            <select id="userCategory" onchange="loadContent()">
                <option value="">-- Select Category --</option>
            </select>
        </div>

        <div class="content-display" id="finalOutput"></div>
    </div>

    <script>
        let currentMode = 'shayari';
        let shareCount = 0;
        let requiredShares = 3;
        let requiredTime = 30.0;
        let leaveTime = 0;
        let isWaitingForReturn = false;
        let isOwnerUnlocked = false;

        const OWNER_SECRET_CODE = "AlzixF703T";

        const database = {
            "shayari": {
                "10001": "🔥 <b>7 Unseen Shayaris (One-Sided Love):</b><br><br>1. Tumhe chaahna hamari galti thi...<br>2. Ek tarfa pyaar ki taaqat hi alag hai...<br>3. Khamoshi par mat jaao...<br>4. Unke reply ka intezaar...<br>5. Dil ki dua...<br>6. Gehra dard...<br>7. Zid hoti toh baahon mein hoti!"
            },
            "story": {
                "10001": "📖 <b>One-Sided Love: The Silent Sacrifice:</b><br><br>Rohan hamesha library ke corner table par baithta tha, sirf Ananya ko dekhne ke liye... Usne letter kitaab mein hi chupa diya aur kabhi nahi diya."
            }
        };

        function switchMode(mode) {
            currentMode = mode;
            shareCount = 0;
            document.getElementById('finalOutput').style.display = 'none';
            document.getElementById('categorySelectBox').style.display = 'none';
            document.getElementById('waShare').style.display = 'block';

            if(mode === 'shayari') {
                document.getElementById('btnShayari').classList.add('active');
                document.getElementById('btnStory').classList.remove('active');
                requiredShares = 3;
                requiredTime = 30.0;
                document.getElementById('noteWarning').innerHTML = "📌 <b>Note:</b> Share to <b>3 WhatsApp friends/groups</b>. Total process takes minimum <b>30 seconds</b> on WhatsApp for validation.";
                document.getElementById('shareCounter').innerText = "🔒 Progress: 0/3 Shares Done";
            } else {
                document.getElementById('btnStory').classList.add('active');
                document.getElementById('btnShayari').classList.remove('active');
                requiredShares = 5;
                requiredTime = 50.0;
                document.getElementById('noteWarning').innerHTML = "📌 <b>Note:</b> Share to <b>5 WhatsApp friends/groups</b>. Total process takes minimum <b>50 seconds</b> on WhatsApp for validation.";
                document.getElementById('shareCounter').innerText = "🔒 Progress: 0/5 Shares Done";
            }

            if(isOwnerUnlocked) {
                unlockContentOptions();
            }
        }

        function startShareProcess() {
            if(isOwnerUnlocked) {
                unlockContentOptions();
                return;
            }

            let originUrl = window.location.origin;
            let rawMsg = (currentMode === 'shayari') 
                ? "Bhai maine toh socha hi nahi tha par yahan par 7 zabardast Shayaris hain jo dil ko chhoo gayi! Tu bhi ek baar padh: " + originUrl
                : "Bhai iss One-Sided Love Story ko padhkar sach mein mere aankhon mein aansu aa gaye! Ek baar tu bhi padh: " + originUrl;

            let waUrl = "whatsapp://send?text=" + encodeURIComponent(rawMsg);
            leaveTime = Date.now();
            isWaitingForReturn = true;

            window.location.href = waUrl;
        }

        document.addEventListener("visibilitychange", function() {
            if (document.visibilityState === "visible" && isWaitingForReturn) {
                isWaitingForReturn = false;
                let returnTime = Date.now();
                let timeSpent = (returnTime - leaveTime) / 1000;

                if (timeSpent >= requiredTime || isOwnerUnlocked) {
                    shareCount++;
                    if (shareCount < requiredShares && !isOwnerUnlocked) {
                        document.getElementById('shareCounter').innerText = "⏳ Progress: " + shareCount + "/" + requiredShares + " Shares Done. Share " + (requiredShares - shareCount) + " more times!";
                    } else {
                        unlockContentOptions();
                    }
                } else {
                    alert("⚠️ Process Incomplete! Minimum " + requiredTime + " seconds WhatsApp par spend karna zaroori hai real share validation ke liye.");
                }
            }
        });

        function unlockContentOptions() {
            document.getElementById('shareCounter').innerHTML = "🎉 <span style='color:#22c55e;'>Unlocked! Options Revealed.</span>";
            document.getElementById('waShare').style.display = 'none';
            showCategoryOptions();
        }

        function showCategoryOptions() {
            let selectBox = document.getElementById('categorySelectBox');
            let selectDropdown = document.getElementById('userCategory');
            selectBox.style.display = 'block';
            selectDropdown.innerHTML = '<option value="">-- Select Category --</option>';

            if(currentMode === 'shayari') {
                document.getElementById('selectLabel').innerText = "Select Shayari Category (Gets 7 Fresh Shayaris):";
                let opts = ["One-Sided Love Shayari", "Attitude & Self-Respect", "Heartbreak & Sad Shayari", "Deep Emotional Shayari"];
                opts.forEach(opt => {
                    selectDropdown.innerHTML += `<option value="${opt}">${opt}</option>`;
                });
            } else {
                document.getElementById('selectLabel').innerText = "Select Emotional Story Type:";
                let opts = ["One-Sided Love: The Silent Sacrifice", "College Romance: Unsaid Goodbye", "Heartbreak: The Last Message", "Second Chance: Destiny Returns"];
                opts.forEach(opt => {
                    selectDropdown.innerHTML += `<option value="${opt}">${opt}</option>`;
                });
            }
        }

        function loadContent() {
            let val = document.getElementById('userCategory').value;
            let output = document.getElementById('finalOutput');
            if(!val) return;

            let randomCode = Math.floor(10000 + Math.random() * 90000);

            output.style.display = 'block';

            if(currentMode === 'shayari') {
                let shayarisList = [
                    "1. Tumhe chaahna hamari sabse haseen galti thi, hum bas tumhare ek reply ka intezaar karte rahe...",
                    "2. Ek tarfa pyaar ki taaqat hi kuch aur hoti hai, isme doosre ke haan ya naa ka darr nahi hota!",
                    "3. Khamoshi par mat jaao hamari, jab bolenge toh seedha dil par chot karenge.",
                    "4. Humne toh bas wafa ki thi, lekin unhone hume bewafai ka tohfa de diya.",
                    "5. Aaj fir se uski yaad aayi, aur dil ne chupchap uski khushi ki dua maang li.",
                    "6. Dil ke jazbaat ko likhna aasaan nahi hota, har shabd ke peeche ek gehra dard chhupa hota hai.",
                    "7. Mohabbat thi isiliye jaane diya, zid hoti toh baahon mein hoti!"
                ];
                output.innerHTML = `<span class="code-tag">Saved Code: ${randomCode}</span><br>🔥 <b>7 Unseen Shayaris (${val}):</b><br><br>` + shayarisList.join('<br><br>');
            } else {
                output.innerHTML = `<span class="code-tag">Saved Code: ${randomCode}</span><br>📖 <b>${val} (High Dopamine Story):</b><br><br>Rohan hamesha library ke corner table par baithta tha, sirf Ananya ko dekhne ke liye. Ananya jab bhi wahan se guzarti, Rohan ka heart rate double ho jaata tha. Ek din Rohan ne apna poora sach ek letter mein likha... Par shayad kismat ko kuch aur manzoor tha. Ananya ki shaadi kisi aur se fixed ho chuki thi. Rohan ne woh letter kabhi Ananya ko nahi diya, balki apni kitaab ke beech chhupa diya. Aaj bhi jab woh kitaab khulti hai, toh wahi silent sacrifice ki mehak aati hai...`;
            }
        }

        function fetchByCode() {
            let code = document.getElementById('codeInput').value.trim();
            let selectedType = document.getElementById('contentTypeSelect').value;
            let output = document.getElementById('finalOutput');
            let err = document.getElementById('codeError');

            if(code === OWNER_SECRET_CODE) {
                isOwnerUnlocked = true;
                err.style.display = 'none';
                alert("⚡ Welcome Arpit Bhai! Owner Bypass Activated.");
                unlockContentOptions();
                return;
            }

            if(code.length !== 5 || isNaN(code)) {
                output.style.display = 'none';
                err.style.display = 'block';
                err.innerText = "❌ Invalid Code! Code must be exactly 5 digits.";
                return;
            }

            if(database[selectedType] && database[selectedType][code]) {
                err.style.display = 'none';
                output.style.display = 'block';
                output.innerHTML = `<span class="code-tag">Retrieved Code (${selectedType.toUpperCase()}): ${code}</span><br>` + database[selectedType][code];
            } else {
                output.style.display = 'none';
                err.style.display = 'block';
                err.innerText = "❌ Invalid Code! Ye code exist nahi karta.";
            }
        }
    </script>
</body>
</html>"""

os.makedirs("viral", exist_ok=True)
with open("index.html", "w") as f:
    f.write(html_code)

with open("viral/sarkari-eligibility-quiz.html", "w") as f:
    f.write(html_code)

print("Files updated successfully!")
