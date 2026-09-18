with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

banner_html = '''
    <!-- AIOUTP Viral Tool Banner -->
    <div style="background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); border-radius: 12px; padding: 18px; margin: 20px 0; text-align: center; color: #fff;">
        <h3 style="margin-bottom: 6px;">⚡ Try AIOUTP Smart Assessment Quizzes</h3>
        <p style="font-size: 0.85rem; color: #e0e7ff; margin-bottom: 12px;">Check your Sarkari Yojana eligibility & AKTU SGPA score instantly!</p>
        <a href="./viral/sarkari-eligibility-quiz.html" style="background: #10b981; color: #fff; padding: 8px 16px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.9rem; display: inline-block;">Launch AIOUTP Tool →</a>
    </div>
'''

if "AIOUTP Viral Tool Banner" not in content:
    # Adding banner right after body tag or header
    content = content.replace("<body>", "<body>\n" + banner_html, 1)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Banner added to index.html!")
else:
    print("Banner already exists!")
