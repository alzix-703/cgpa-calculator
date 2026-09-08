import re, glob

# Fix AKTU formula on all AKTU specific pages
for fpath in glob.glob("*aktu*.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    # Replace old formula JS with correct one: (cgpa - 0.75) * 10
    content = re.sub(r'(\(.*?cgpa.*?\)\s*\*?\s*10)', '(cgpa - 0.75) * 10', content, flags=re.IGNORECASE)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("University formulas synchronized with official circulars!")
