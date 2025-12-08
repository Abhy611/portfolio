from pathlib import Path
import os

def main():
    root = Path(__file__).resolve().parent

    # ---------- 1. Ensure directory structure ----------
    folders = [
        "assets/images/hero",
        "assets/images/logos",
        "assets/images/gallery",
        "assets/icons",
        "assets/fonts",
        "css",
        "js",
        "pages",
        "data",
        "utils"
    ]

    for folder in folders:
        (root / folder).mkdir(parents=True, exist_ok=True)

    # ---------- 2. Define file contents ----------

    files = {}

    # ========== HTML: BASE NAV + HOME ==========
    files["index.html"] = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abhyuday Singh | Portfolio</title>
    <link rel="stylesheet" href="css/base.css">
    <link rel="stylesheet" href="css/layout.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/pages.css">
    <script defer src="js/main.js"></script>
</head>
<body>

<header class="navbar">
    <div class="nav-brand">
        <div class="brand-mark">AS</div>
        <div class="brand-text">
            <span class="brand-name">Abhyuday Singh</span>
            <span class="brand-tagline">AI Engineer · Research & Product</span>
        </div>
    </div>

    <nav class="nav-links">
        <a href="index.html" class="active">Home</a>
        <a href="pages/about.html">About</a>
        <a href="pages/projects.html">Projects</a>
        <a href="pages/experience.html">Experience</a>
        <a href="pages/publications.html">Publications</a>
        <a href="pages/skills.html">Skills</a>
        <a href="pages/contact.html" class="btn-nav-ghost">Contact</a>
    </nav>
</header>

<main class="hero-grid">

    <!-- Left: Photo -->
    <section class="hero-left">
        <div class="hero-photo-wrapper">
            <img src="assets/images/hero/profile.jpg"
                 alt="Portrait of Abhyuday Singh"
                 class="hero-photo-img">
        </div>
        <div class="hero-photo-meta">
            <span class="badge-soft">Available for AI / ML roles</span>
        </div>
    </section>

    <!-- Right: Copy -->
    <section class="hero-right">
        <p class="hero-eyebrow">AI · Machine Learning · Applied Research</p>
        <h1 class="hero-title">
            Designing and delivering <span>intelligent systems</span> that move from
            prototype to production.
        </h1>
        <p class="hero-subtitle">
            This portfolio highlights solution-focused work across computer vision,
            LLM-based automation, and data-driven decision systems.
        </p>

        <div class="hero-actions">
            <a href="pages/projects.html" class="btn-primary">View Case Studies</a>
            <a href="pages/about.html" class="btn-secondary">Quick Profile</a>
        </div>

        <div class="hero-metrics">
            <div class="metric">
                <span class="metric-label">Focus</span>
                <span class="metric-value">End-to-end AI delivery</span>
            </div>
            <div class="metric">
                <span class="metric-label">Strength</span>
                <span class="metric-value">Execution & ownership</span>
            </div>
        </div>
    </section>

</main>

<footer class="site-footer">
    <p>© {year} Abhyuday Singh · Portfolio</p>
</footer>

</body>
</html>
""".replace("{year}", "2025")

    # Helper function: shared head + nav for subpages
    def subpage(title: str, body_content: str, active: str) -> str:
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Abhyuday Singh</title>
    <link rel="stylesheet" href="../css/base.css">
    <link rel="stylesheet" href="../css/layout.css">
    <link rel="stylesheet" href="../css/components.css">
    <link rel="stylesheet" href="../css/pages.css">
    <script defer src="../js/main.js"></script>
</head>
<body>

<header class="navbar">
    <div class="nav-brand">
        <div class="brand-mark">AS</div>
        <div class="brand-text">
            <span class="brand-name">Abhyuday Singh</span>
            <span class="brand-tagline">AI Engineer · Research & Product</span>
        </div>
    </div>

    <nav class="nav-links">
        <a href="../index.html" class="{ 'active' if active=='home' else '' }">Home</a>
        <a href="about.html" class="{ 'active' if active=='about' else '' }">About</a>
        <a href="projects.html" class="{ 'active' if active=='projects' else '' }">Projects</a>
        <a href="experience.html" class="{ 'active' if active=='experience' else '' }">Experience</a>
        <a href="publications.html" class="{ 'active' if active=='publications' else '' }">Publications</a>
        <a href="skills.html" class="{ 'active' if active=='skills' else '' }">Skills</a>
        <a href="contact.html" class="btn-nav-ghost { 'active' if active=='contact' else '' }">Contact</a>
    </nav>
</header>

<main class="page-shell">
{body_content}
</main>

<footer class="site-footer">
    <p>© 2025 Abhyuday Singh · Portfolio</p>
</footer>

</body>
</html>
"""

    # ========== ABOUT ==========
    about_body = """
<section class="page-header">
    <h1>About</h1>
    <p class="page-subtitle">
        Concise overview of background, problem-solving style, and how I approach
        building AI-driven systems.
    </p>
</section>

<section class="grid-two">
    <article class="card">
        <h2>Profile Snapshot</h2>
        <p>
            AI engineer with hands-on work across model development, evaluation, and
            deployment. Comfortable running end-to-end cycles: from understanding the
            business objective to designing data pipelines, experimenting with models,
            and shipping usable tools.
        </p>
    </article>

    <article class="card">
        <h2>How I Work</h2>
        <ul class="bullet">
            <li>Translate open-ended requirements into measurable targets.</li>
            <li>Prototype quickly, then iterate based on metrics and feedback.</li>
            <li>Keep solutions practical: simple when possible, sophisticated only when required.</li>
        </ul>
    </article>
</section>
"""
    files["pages/about.html"] = subpage("About", about_body, "about")

    # ========== EXPERIENCE ==========
    exp_body = """
<section class="page-header">
    <h1>Experience</h1>
    <p class="page-subtitle">
        High-level snapshot of roles and responsibilities. The intent is to show ownership,
        impact, and technical depth.
    </p>
</section>

<section class="timeline">
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-content">
            <h2>AI / ML Engineering</h2>
            <p class="timeline-meta">Role-level summary</p>
            <p>
                Worked on applied AI use-cases including document understanding, intelligent
                chatbots, and computer vision workflows. Responsibilities typically cover
                problem framing, data strategy, model selection, evaluation, and deployment
                in collaboration with product and engineering teams.
            </p>
        </div>
    </div>

    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-content">
            <h2>Research & Prototyping</h2>
            <p class="timeline-meta">Academic / lab-style work</p>
            <p>
                Explored model architectures, benchmarking strategies, and optimisation
                techniques with emphasis on reliability, tiny-object detection, and
                compute-efficient design.
            </p>
        </div>
    </div>
</section>
"""
    files["pages/experience.html"] = subpage("Experience", exp_body, "experience")

    # ========== PROJECTS ==========
    projects_body = """
<section class="page-header">
    <h1>Projects</h1>
    <p class="page-subtitle">
        Representative projects grouped by theme. Case studies can be expanded later with
        full write-ups, diagrams, and metrics.
    </p>
</section>

<section class="cards-grid">
    <article class="card card-project">
        <h2>LLM + Retrieval-based Assistant</h2>
        <p>
            Conversational interface connected to document stores that provides context-aware
            answers, summarisation, and workflow automation. Designed with a focus on latency,
            safety, and interpretability.
        </p>
        <p class="tagline">Stack: Python · Vector DB · LLM APIs</p>
    </article>

    <article class="card card-project">
        <h2>Document Intelligence & Verification</h2>
        <p>
            Pipeline for extracting, cleaning, and validating information from semi-structured
            and unstructured documents using OCR, classical NLP and modern transformer models.
        </p>
        <p class="tagline">Stack: OCR · Transformers · Rule+ML hybrid</p>
    </article>

    <article class="card card-project">
        <h2>Computer Vision for Real-time Detection</h2>
        <p>
            Vision system designed for detecting small or low-contrast objects in challenging
            environments, optimised for both accuracy and inference speed.
        </p>
        <p class="tagline">Stack: PyTorch · YOLO-family · Optimisation</p>
    </article>
</section>
"""
    files["pages/projects.html"] = subpage("Projects", projects_body, "projects")

    # ========== PUBLICATIONS ==========
    pub_body = """
<section class="page-header">
    <h1>Publications & Writing</h1>
    <p class="page-subtitle">
        Space reserved for formal publications, preprints, technical blogs, and talks.
        Entries can be expanded with links once they are public.
    </p>
</section>

<section class="card">
    <h2>Selected Work</h2>
    <ul class="bullet">
        <li>Research on efficient object detection with emphasis on tiny-object scenarios.</li>
        <li>Concept notes around automated document verification and trust in AI systems.</li>
        <li>Internal write-ups on how to move from PoC to production with lightweight MLOps.</li>
    </ul>
</section>
"""
    files["pages/publications.html"] = subpage("Publications", pub_body, "publications")

    # ========== SKILLS ==========
    skills_body = """
<section class="page-header">
    <h1>Skills</h1>
    <p class="page-subtitle">
        Overview of tools, frameworks, and areas of competence relevant for AI/ML engineering,
        applied research, and solution delivery.
    </p>
</section>

<section class="grid-two">
    <article class="card">
        <h2>Core</h2>
        <ul class="bullet">
            <li>Python · Data structures and algorithmic thinking</li>
            <li>Machine Learning lifecycle: data → model → evaluation → deployment</li>
            <li>Deep learning for NLP and computer vision</li>
        </ul>
    </article>

    <article class="card">
        <h2>Ecosystem</h2>
        <ul class="bullet">
            <li>PyTorch / TensorFlow · scikit-learn</li>
            <li>LLM tooling and retrieval-augmented generation</li>
            <li>API development, basic CI/CD and cloud deployment concepts</li>
        </ul>
    </article>
</section>
"""
    files["pages/skills.html"] = subpage("Skills", skills_body, "skills")

    # ========== CONTACT ==========
    contact_body = """
<section class="page-header">
    <h1>Contact</h1>
    <p class="page-subtitle">
        Preferred way to reach out for opportunities, collaborations, or discussions.
    </p>
</section>

<section class="grid-two">
    <article class="card">
        <h2>Quick Message</h2>
        <form class="contact-form">
            <div class="form-row">
                <label>Name</label>
                <input type="text" placeholder="Your name">
            </div>
            <div class="form-row">
                <label>Email</label>
                <input type="email" placeholder="you@example.com">
            </div>
            <div class="form-row">
                <label>Message</label>
                <textarea rows="4" placeholder="Short context or query"></textarea>
            </div>
            <button type="submit" class="btn-primary">Send (static demo)</button>
        </form>
    </article>

    <article class="card">
        <h2>Direct Links</h2>
        <ul class="bullet">
            <li>GitHub: add-link-here</li>
            <li>LinkedIn: add-link-here</li>
            <li>Email: add-email-here</li>
        </ul>
    </article>
</section>
"""
    files["pages/contact.html"] = subpage("Contact", contact_body, "contact")

    # ========== CSS: BASE ==========
    files["css/base.css"] = r"""
*,
*::before,
*::after{
    box-sizing:border-box;
}

:root{
    --bg-main:#f5f8fb;
    --bg-surface:#ffffff;
    --primary:#2b7fa5;
    --primary-soft:#9bcfe3;
    --accent:#ffc6d3;
    --text-main:#1f2933;
    --text-muted:#6b7280;
    --border-soft:#e2e8f0;
    --radius-lg:20px;
    --radius-md:14px;
    --shadow-soft:0 18px 40px rgba(15,35,52,0.10);
}

html,body{
    margin:0;
    padding:0;
    font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    background:var(--bg-main);
    color:var(--text-main);
}

body{
    min-height:100vh;
}

h1,h2,h3,h4{
    margin:0;
}

p{
    margin:0;
}

a{
    color:inherit;
}
"""

    # ========== CSS: LAYOUT (NAV + SHELL + FOOTER) ==========
    files["css/layout.css"] = r"""
.navbar{
    position:sticky;
    top:0;
    z-index:20;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:16px 64px;
    background:rgba(255,255,255,0.92);
    backdrop-filter:blur(18px);
    box-shadow:0 10px 30px rgba(15,35,52,0.12);
}

.nav-brand{
    display:flex;
    align-items:center;
    gap:10px;
}

.brand-mark{
    width:36px;
    height:36px;
    border-radius:14px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:700;
    color:#fff;
    background:linear-gradient(135deg,var(--primary),var(--accent));
}

.brand-text{
    display:flex;
    flex-direction:column;
    line-height:1.1;
}

.brand-name{
    font-size:15px;
    font-weight:600;
}

.brand-tagline{
    font-size:11px;
    color:var(--text-muted);
}

.nav-links{
    display:flex;
    align-items:center;
    gap:20px;
}

.nav-links a{
    text-decoration:none;
    font-size:14px;
    color:#4b5563;
    position:relative;
}

.nav-links a.active:not(.btn-nav-ghost){
    color:var(--primary);
}

.nav-links a.active:not(.btn-nav-ghost)::after{
    content:"";
    position:absolute;
    left:0;
    bottom:-4px;
    width:100%;
    height:2px;
    border-radius:999px;
    background:var(--primary);
}

.hero-grid{
    min-height:calc(100vh - 80px);
    display:grid;
    grid-template-columns:0.9fr 1.1fr;
    gap:64px;
    padding:72px 80px 80px;
}

.page-shell{
    padding:56px 80px 80px;
}

.site-footer{
    padding:18px 40px;
    text-align:center;
    font-size:12px;
    color:var(--text-muted);
}

/* Responsive */
@media (max-width: 900px){
    .navbar{
        padding:14px 20px;
        flex-direction:column;
        align-items:flex-start;
        gap:10px;
    }

    .nav-links{
        flex-wrap:wrap;
        gap:14px;
    }

    .hero-grid{
        grid-template-columns:1fr;
        padding:32px 20px 40px;
        gap:40px;
    }

    .page-shell{
        padding:32px 20px 40px;
    }
}
"""

    # ========== CSS: COMPONENTS ==========
    files["css/components.css"] = r"""
.btn-primary,
.btn-secondary,
.btn-nav-ghost{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    padding:10px 22px;
    border-radius:999px;
    font-size:14px;
    font-weight:500;
    border:none;
    cursor:pointer;
    text-decoration:none;
    transition:all .2s ease;
}

.btn-primary{
    background:linear-gradient(135deg,var(--primary),#45a9c5);
    color:#ffffff;
    box-shadow:0 14px 32px rgba(43,127,165,0.40);
}

.btn-primary:hover{
    transform:translateY(-1px);
    box-shadow:0 18px 40px rgba(43,127,165,0.50);
}

.btn-secondary{
    background:#ffffff;
    color:var(--primary);
    border:1px solid rgba(43,127,165,0.25);
}

.btn-secondary:hover{
    background:rgba(43,127,165,0.06);
}

.btn-nav-ghost{
    padding:8px 16px;
    border-radius:999px;
    border:1px solid rgba(43,127,165,0.20);
    color:var(--primary);
    background:rgba(43,127,165,0.03);
}

.btn-nav-ghost:hover{
    background:rgba(43,127,165,0.10);
}

/* Cards */
.card{
    background:var(--bg-surface);
    border-radius:var(--radius-lg);
    padding:22px 24px;
    box-shadow:var(--shadow-soft);
}

.card-project h2{
    margin-bottom:8px;
}

.tagline{
    margin-top:10px;
    font-size:13px;
    color:var(--text-muted);
}

/* Grids & utilities */
.grid-two{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:24px;
}

.cards-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
    gap:24px;
}

.page-header{
    margin-bottom:28px;
}

.page-header h1{
    font-size:28px;
    margin-bottom:6px;
}

.page-subtitle{
    font-size:14px;
    color:var(--text-muted);
}

.bullet{
    padding-left:18px;
    margin:8px 0 0;
}

.bullet li{
    margin-bottom:4px;
}

/* Timeline */
.timeline{
    position:relative;
    padding-left:20px;
    border-left:2px solid var(--border-soft);
    display:flex;
    flex-direction:column;
    gap:26px;
}

.timeline-item{
    position:relative;
}

.timeline-dot{
    width:10px;
    height:10px;
    border-radius:50%;
    background:var(--primary);
    position:absolute;
    left:-26px;
    top:6px;
}

.timeline-content{
    background:var(--bg-surface);
    border-radius:var(--radius-md);
    padding:18px 20px;
    box-shadow:0 10px 26px rgba(15,35,52,0.08);
}

.timeline-meta{
    font-size:12px;
    color:var(--text-muted);
    margin:4px 0 8px;
}

/* Contact form */
.contact-form{
    display:flex;
    flex-direction:column;
    gap:12px;
}

.form-row{
    display:flex;
    flex-direction:column;
    gap:4px;
}

.form-row label{
    font-size:13px;
}

.form-row input,
.form-row textarea{
    border-radius:10px;
    border:1px solid var(--border-soft);
    padding:8px 10px;
    font-size:13px;
    font-family:inherit;
}

/* Responsive */
@media (max-width: 900px){
    .grid-two{
        grid-template-columns:1fr;
    }
}
"""

    # ========== CSS: PAGES (HERO SPECIFIC) ==========
    files["css/pages.css"] = r"""
.hero-left{
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:flex-start;
}

.hero-photo-wrapper{
    background:linear-gradient(135deg,rgba(155,207,227,0.75),rgba(255,198,211,0.70));
    padding:10px;
    border-radius:24px;
    box-shadow:0 24px 50px rgba(15,35,52,0.30);
    display:flex;
    justify-content:center;
}

.hero-photo-img{
    display:block;
    width:100%;
    max-width:320px;
    border-radius:18px;
}

.hero-photo-meta{
    margin-top:16px;
}

.badge-soft{
    padding:7px 14px;
    border-radius:999px;
    font-size:12px;
    background:rgba(43,127,165,0.06);
    color:#1f4f66;
}

.hero-right{
    display:flex;
    flex-direction:column;
    justify-content:center;
    max-width:580px;
}

.hero-eyebrow{
    font-size:13px;
    letter-spacing:0.16em;
    text-transform:uppercase;
    color:var(--text-muted);
    margin-bottom:10px;
}

.hero-title{
    font-size:36px;
    line-height:1.25;
    font-weight:700;
    margin-bottom:12px;
}

.hero-title span{
    color:var(--primary);
}

.hero-subtitle{
    font-size:15px;
    line-height:1.7;
    color:var(--text-muted);
}

.hero-actions{
    margin-top:24px;
    display:flex;
    gap:14px;
    flex-wrap:wrap;
}

.hero-metrics{
    margin-top:28px;
    display:flex;
    gap:26px;
    flex-wrap:wrap;
}

.metric{
    display:flex;
    flex-direction:column;
    gap:3px;
}

.metric-label{
    font-size:11px;
    text-transform:uppercase;
    letter-spacing:0.14em;
    color:var(--text-muted);
}

.metric-value{
    font-size:14px;
    font-weight:600;
}
"""

    # ========== JS: MAIN ==========
    files["js/main.js"] = r"""
document.addEventListener("DOMContentLoaded", () => {
    console.log("Portfolio loaded.");

    // Simple enhancement: mark nav active link based on URL
    const links = document.querySelectorAll(".nav-links a:not(.btn-nav-ghost)");
    const path = window.location.pathname.replace(/\\/g, "/");

    links.forEach(link => {
        const href = link.getAttribute("href");
        if (!href) return;

        if (path.endsWith(href) || path.includes("/" + href)) {
            link.classList.add("active");
        }
    });
});
"""

    # ========== JS: navigation placeholder ==========
    files["js/navigation.js"] = "// Reserved for mobile menu / advanced navigation.\n"

    # ========== DATA ==========
    files["data/experience.json"] = "{}\n"
    files["data/projects.json"] = "{}\n"
    files["data/publications.json"] = "{}\n"

    # ========== UTILS ==========
    files["utils/helpers.js"] = "// Helper utilities can be added here later.\n"

    # ========== META FILES ==========
    files["README.md"] = """# Personal Portfolio

Static multi-page portfolio for Abhyuday Singh.

Structure:
- Landing page with hero (photo + positioning)
- About, Projects, Experience, Publications, Skills, Contact
- Pure HTML/CSS/JS, deployment-ready for GitHub Pages or Vercel.
"""

    files[".gitignore"] = """# Python
__pycache__/
*.pyc

# Misc
.DS_Store
"""

    files["vercel.json"] = '{ "cleanUrls": true }\n'

    # ---------- 3. Write all files ----------
    for rel_path, content in files.items():
        file_path = root / rel_path
        file_path.write_text(content, encoding="utf-8")
        print(f"[OK] wrote {rel_path}")

    print("\n[DONE] Portfolio reset completed.")
    print("Important: ensure your hero image is at 'assets/images/hero/profile.jpg'.")

if __name__ == "__main__":
    main()
