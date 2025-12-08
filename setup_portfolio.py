import os

# ---------- CONFIG ----------
project_name = "abhyuday-portfolio"  # you can rename it anytime

# Folder Structure
folders = [
    f"{project_name}/assets/images/hero",
    f"{project_name}/assets/images/logos",
    f"{project_name}/assets/images/gallery",
    f"{project_name}/assets/icons",
    f"{project_name}/assets/fonts",

    f"{project_name}/pages",
    f"{project_name}/css",
    f"{project_name}/js",
    f"{project_name}/data",
    f"{project_name}/utils"
]

# Files with boilerplate content
files = {
    f"{project_name}/index.html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Abhyuday Portfolio</title>
<link rel="stylesheet" href="css/base.css">
<link rel="stylesheet" href="css/layout.css">
<link rel="stylesheet" href="css/components.css">
<link rel="stylesheet" href="css/pages.css">
<script defer src="js/main.js"></script>
</head>
<body>

<!-- ================= NAVBAR ================= -->
<header class="navbar">
    <div class="logo">ABHYUDAY</div>
    <nav>
        <a href="index.html">Home</a>
        <a href="pages/about.html">About</a>
        <a href="pages/projects.html">Projects</a>
        <a href="pages/experience.html">Experience</a>
        <a href="pages/publications.html">Publications</a>
        <a href="pages/contact.html">Contact</a>
    </nav>
</header>

<!-- ================= HERO SECTION ================= -->
<section class="hero">
    <div class="hero-left">
        <img src="assets/images/hero/profile.jpg" alt="Profile Image Placeholder">
    </div>

    <div class="hero-right">
        <h1 class="title">A Visionary Leader</h1>
        <h2 class="sub-title">Driving Innovation & Research in AI</h2>
        <p class="desc">This quote section will be replaced by your custom quote later.</p>
        <button class="btn-primary">Explore My Work →</button>
    </div>
</section>

</body>
</html>
""",

    # ---------- Pages ----------
    f"{project_name}/pages/about.html": "<h1>About Page</h1>",
    f"{project_name}/pages/experience.html": "<h1>Experience Page</h1>",
    f"{project_name}/pages/projects.html": "<h1>Projects Page</h1>",
    f"{project_name}/pages/publications.html": "<h1>Publications Page</h1>",
    f"{project_name}/pages/skills.html": "<h1>Skills Page</h1>",
    f"{project_name}/pages/contact.html": "<h1>Contact Page</h1>",

    # ---------- CSS Boilerplate ----------
    f"{project_name}/css/base.css": """
*{margin:0;padding:0;box-sizing:border-box;font-family:'Poppins',sans-serif;}
:root{
    --primary:#9BCFE3;  /* pastel blue */
    --secondary:#FFC6D3;/* pastel pink */
    --text:#222;
    --bg:#F7F9FA;
}
body{background:var(--bg);color:var(--text);}
""",

    f"{project_name}/css/layout.css": """
.navbar{
    width:100%;display:flex;justify-content:space-between;
    padding:20px 60px;background:white;box-shadow:0 2px 10px rgba(0,0,0,.05);
}
.navbar nav a{
    margin-left:20px;text-decoration:none;color:#333;font-weight:500;
}
.hero{
    display:flex;align-items:center;justify-content:center;
    padding:80px;gap:60px;
}
.hero-left img{width:350px;border-radius:12px;}
.hero-right .title{font-size:42px;font-weight:700;}
.hero-right .sub-title{font-size:22px;margin:10px 0;color:#555;}
.btn-primary{
    margin-top:15px;padding:12px 26px;border:none;border-radius:8px;
    background:var(--primary);cursor:pointer;font-size:16px;
}
""",

    f"{project_name}/css/components.css": "/* button, cards, UI components later */",
    f"{project_name}/css/pages.css": "/* hero animations and page styling later */",

    # ---------- JS Boilerplate ----------
    f"{project_name}/js/main.js": "console.log('Portfolio Loaded');",
    f"{project_name}/js/hero.js": "// future animation scripts",
    f"{project_name}/js/navigation.js": "// mobile menu, scroll events",
    f"{project_name}/js/analytics.js": "// analytics or events",

    # ---------- Data JSON ----------
    f"{project_name}/data/experience.json": "{}",
    f"{project_name}/data/projects.json": "{}",
    f"{project_name}/data/publications.json": "{}", 

    f"{project_name}/utils/helpers.js": "// helper functions will be added here",
    f"{project_name}/README.md": "# Portfolio Project Setup\nGenerated via Python script.",
    f"{project_name}/.gitignore": "# cache/logs/node_modules ignored later",
    f"{project_name}/vercel.json": '{ "cleanUrls": true }'
}

# ---------- Script Execution ----------
for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file, content in files.items():
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print(f"\n✔ Portfolio structure for '{project_name}' created successfully!")
