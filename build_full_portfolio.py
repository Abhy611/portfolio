from pathlib import Path

def write_file(root: Path, rel_path: str, content: str):
    path = root / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"[OK] Wrote {rel_path}")

def main():
    root = Path(__file__).resolve().parent

    # ============= INDEX (Landing + Hero + Journey Road) =============
    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abhyuday Singh | AI Portfolio</title>
    <link rel="stylesheet" href="css/base.css">
    <link rel="stylesheet" href="css/layout.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/pages.css">
    <script defer src="js/main.js"></script>
</head>
<body>

<header class="site-header">
    <div class="brand-block">
        <div class="brand-avatar">AS</div>
        <div class="brand-meta">
            <span class="brand-name">Abhyuday Singh</span>
            <span class="brand-role">AI / ML Engineer · Applied Research</span>
        </div>
    </div>
    <nav class="nav-main">
        <a href="index.html" class="nav-link active">Home</a>
        <a href="pages/projects.html" class="nav-link">Projects</a>
        <a href="pages/experience.html" class="nav-link">Experience</a>
        <a href="pages/publications.html" class="nav-link">Publications</a>
        <a href="pages/skills.html" class="nav-link">Skills</a>
        <a href="pages/contact.html" class="nav-link nav-cta">Contact</a>
    </nav>
</header>

<main>
    <!-- HERO -->
    <section class="hero-shell">
        <div class="hero-copy">
            <p class="hero-kicker">LLMs · RAG · Computer Vision · MLOps</p>
            <h1 class="hero-title">
                Building <span>production-grade AI systems</span> that move from
                prototype to measurable impact.
            </h1>
            <p class="hero-subtitle">
                AI/ML Engineer with hands-on experience in Generative AI, RAG pipelines,
                document intelligence and real-time computer vision across defense,
                HR automation and document-heavy workflows.
            </p>
            <div class="hero-actions">
                <a href="pages/projects.html" class="btn-primary">View Case Studies</a>
                <a href="pages/experience.html" class="btn-ghost">Career Snapshot</a>
            </div>
            <div class="hero-metrics">
                <div class="metric">
                    <span class="metric-label">Experience</span>
                    <span class="metric-value">3.5+ years</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Focus</span>
                    <span class="metric-value">LLMs · CV · RAG</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Domains</span>
                    <span class="metric-value">Defense · HR · Document AI</span>
                </div>
            </div>
        </div>

        <div class="hero-visual">
            <div class="hero-photo-frame">
                <div class="hero-photo-glow"></div>
                <img src="assets/images/hero/profile.jpg" alt="Portrait of Abhyuday Singh" class="hero-photo">
            </div>
            <div class="hero-quote-card">
                <p class="hero-quote">
                    “Machines learn patterns. Engineers design outcomes.”
                </p>
                <p class="hero-quote-meta">
                    Translating research into stable, production-ready AI systems.
                </p>
            </div>
        </div>
    </section>

    <!-- JOURNEY ROAD SECTION -->
    <section class="journey-shell" id="journey">
        <h2 class="section-title">Journey at a Glance</h2>
        <p class="section-subtitle">
            A continuous path across experience, education and research — structured as one story rather than isolated bullets.
        </p>

        <div class="journey-road">
            <div class="journey-line"></div>

            <article class="journey-node left">
                <div class="node-dot"></div>
                <div class="node-card">
                    <h3>Aarav Global · AI/ML Engineer</h3>
                    <p>
                        Designed LLM & SLM powered document intelligence, RAG pipelines and agentic HR
                        workflows for resume screening and JD-matching.
                    </p>
                </div>
            </article>

            <article class="journey-node right">
                <div class="node-dot"></div>
                <div class="node-card">
                    <h3>DRDO ARDE · Junior Research Fellow</h3>
                    <p>
                        Built YOLO-based, real-time surveillance pipelines on 1.5M+ images with A100 / RTX
                        optimisation and deployment in secure defense systems.
                    </p>
                </div>
            </article>

            <article class="journey-node left">
                <div class="node-dot"></div>
                <div class="node-card">
                    <h3>Freelancing · ML & Analytics</h3>
                    <p>
                        Delivered dashboards, ML experiments and research assistance for PhD scholars and
                        early-stage projects in multiple domains.
                    </p>
                </div>
            </article>

            <article class="journey-node right">
                <div class="node-dot"></div>
                <div class="node-card">
                    <h3>Education · B.Tech & M.Tech AI/ML</h3>
                    <p>
                        B.Tech CSE (Cloud & Virtualization) and M.Tech AI/ML (Symbiosis) — combining
                        systems fundamentals with deep learning and applied research.
                    </p>
                </div>
            </article>

            <article class="journey-node left">
                <div class="node-dot"></div>
                <div class="node-card">
                    <h3>Research & Publications</h3>
                    <p>
                        Peer-reviewed work in multimodal gas detection, reinforcement learning for fault
                        diagnosis and medical imaging — focused on reproducible, real-world impact.
                    </p>
                </div>
            </article>
        </div>
    </section>
</main>

<footer class="site-footer">
    <p>© 2025 · Abhyuday Singh · Portfolio</p>
</footer>

</body>
</html>
"""
    write_file(root, "index.html", index_html)

    # ============= CSS: base.css =============
    base_css = """*,
*::before,
*::after{
    box-sizing:border-box;
}

:root{
    --bg-main:#f4f7fb;
    --bg-surface:#ffffff;
    --bg-soft:#ecf3ff;
    --primary:#2563eb;
    --primary-soft:#a5c4ff;
    --accent:#f97373;
    --text-main:#0f172a;
    --text-soft:#6b7280;
    --border-soft:#e2e8f0;
    --radius-lg:20px;
    --radius-md:14px;
    --shadow-soft:0 18px 45px rgba(15,23,42,0.14);
    --shadow-subtle:0 10px 25px rgba(15,23,42,0.08);
}

html,body{
    margin:0;
    padding:0;
    font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    background:var(--bg-main);
    color:var(--text-main);
    scroll-behavior:smooth;
}

a{
    color:inherit;
    text-decoration:none;
}

img{
    max-width:100%;
    display:block;
}
"""
    write_file(root, "css/base.css", base_css)

    # ============= CSS: layout.css =============
    layout_css = """.site-header{
    position:sticky;
    top:0;
    z-index:50;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:14px 72px;
    background:rgba(255,255,255,0.96);
    backdrop-filter:blur(18px);
    box-shadow:0 14px 40px rgba(15,23,42,0.12);
}

.brand-block{
    display:flex;
    align-items:center;
    gap:12px;
}

.brand-avatar{
    width:40px;
    height:40px;
    border-radius:16px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:700;
    font-size:18px;
    color:#fff;
    background:linear-gradient(135deg,#2563eb,#f97373);
}

.brand-meta{
    display:flex;
    flex-direction:column;
}

.brand-name{
    font-size:15px;
    font-weight:600;
}

.brand-role{
    font-size:11px;
    color:var(--text-soft);
}

.nav-main{
    display:flex;
    align-items:center;
    gap:18px;
}

.nav-link{
    font-size:14px;
    padding:6px 4px;
    position:relative;
    color:#4b5563;
}

.nav-link.active:not(.nav-cta){
    color:var(--primary);
}

.nav-link.active:not(.nav-cta)::after{
    content:"";
    position:absolute;
    left:0;
    bottom:-4px;
    width:100%;
    height:2px;
    border-radius:999px;
    background:var(--primary);
}

.nav-cta{
    padding:7px 14px;
    border-radius:999px;
    border:1px solid rgba(37,99,235,0.3);
    background:rgba(37,99,235,0.04);
    font-weight:500;
}

.nav-cta:hover{
    background:rgba(37,99,235,0.1);
}

.hero-shell{
    display:grid;
    grid-template-columns: minmax(0,1.1fr) minmax(0,1fr);
    gap:56px;
    padding:72px 80px 40px;
}

.site-footer{
    padding:20px 40px 32px;
    text-align:center;
    font-size:12px;
    color:var(--text-soft);
}

/* Inner pages container */
.page-shell{
    padding:56px 80px 72px;
}

/* Generic section titles */
.section-title{
    font-size:26px;
    font-weight:700;
    margin-bottom:6px;
}

.section-subtitle{
    font-size:14px;
    color:var(--text-soft);
    max-width:600px;
}

/* Responsive */
@media (max-width: 960px){
    .site-header{
        padding:12px 18px;
        flex-direction:column;
        align-items:flex-start;
        gap:10px;
    }
    .nav-main{
        flex-wrap:wrap;
        gap:12px;
    }
    .hero-shell{
        grid-template-columns:1fr;
        padding:32px 18px 24px;
    }
    .page-shell{
        padding:32px 18px 48px;
    }
}
"""
    write_file(root, "css/layout.css", layout_css)

    # ============= CSS: components.css =============
    components_css = """.btn-primary,
.btn-ghost{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    padding:10px 20px;
    border-radius:999px;
    font-size:14px;
    font-weight:500;
    border:none;
    cursor:pointer;
    text-decoration:none;
    transition:all .16s ease-out;
}

.btn-primary{
    background:linear-gradient(135deg,#2563eb,#3b82f6);
    color:#fff;
    box-shadow:0 16px 36px rgba(37,99,235,0.4);
}

.btn-primary:hover{
    transform:translateY(-1px);
    box-shadow:0 22px 44px rgba(37,99,235,0.5);
}

.btn-ghost{
    background:#fff;
    color:var(--primary);
    border:1px solid rgba(37,99,235,0.25);
}

.btn-ghost:hover{
    background:rgba(37,99,235,0.06);
}

.card{
    background:var(--bg-surface);
    border-radius:var(--radius-lg);
    padding:20px 22px;
    box-shadow:var(--shadow-subtle);
}

.chip{
    display:inline-flex;
    align-items:center;
    padding:4px 10px;
    border-radius:999px;
    font-size:11px;
    background:rgba(37,99,235,0.06);
    color:#1d4ed8;
}

.badge-soft{
    padding:6px 10px;
    border-radius:999px;
    font-size:11px;
    background:rgba(15,23,42,0.04);
    color:#4b5563;
}
"""
    write_file(root, "css/components.css", components_css)

    # ============= CSS: pages.css (hero + journey + inner) =============
    pages_css = """.hero-copy{
    display:flex;
    flex-direction:column;
    justify-content:center;
    gap:18px;
}

.hero-kicker{
    font-size:12px;
    letter-spacing:0.18em;
    text-transform:uppercase;
    color:var(--text-soft);
}

.hero-title{
    font-size:34px;
    line-height:1.25;
    font-weight:700;
}

.hero-title span{
    color:var(--primary);
}

.hero-subtitle{
    font-size:15px;
    line-height:1.7;
    color:var(--text-soft);
}

.hero-actions{
    display:flex;
    flex-wrap:wrap;
    gap:12px;
    margin-top:4px;
}

.hero-metrics{
    display:flex;
    flex-wrap:wrap;
    gap:20px;
    margin-top:8px;
}

.metric-label{
    font-size:11px;
    text-transform:uppercase;
    letter-spacing:0.12em;
    color:var(--text-soft);
}

.metric-value{
    font-size:14px;
    font-weight:600;
}

.hero-visual{
    display:flex;
    flex-direction:column;
    gap:16px;
    align-items:flex-end;
    justify-content:center;
}

.hero-photo-frame{
    position:relative;
    padding:10px;
    border-radius:26px;
    background:radial-gradient(circle at 0 0,#bfdbfe,#fee2e2);
    box-shadow:var(--shadow-soft);
}

.hero-photo-glow{
    position:absolute;
    inset:8px;
    border-radius:22px;
    background:radial-gradient(circle at 15% 0,rgba(59,130,246,0.28),transparent 60%);
    pointer-events:none;
}

.hero-photo{
    position:relative;
    border-radius:20px;
    width:100%;
    max-width:380px;
}

.hero-quote-card{
    max-width:320px;
    background:rgba(15,23,42,0.9);
    color:#e5e7eb;
    border-radius:18px;
    padding:14px 16px 14px;
    box-shadow:0 14px 40px rgba(15,23,42,0.7);
}

.hero-quote{
    font-size:14px;
    line-height:1.6;
    font-style:italic;
}

.hero-quote-meta{
    margin-top:8px;
    font-size:11px;
    color:#9ca3af;
}

/* Journey curved road */
.journey-shell{
    padding:32px 80px 72px;
    background:linear-gradient(180deg,#f3f6ff 0%,#f9fafb 40%,#ffffff 100%);
}

.journey-road{
    position:relative;
    margin-top:32px;
    padding:16px 0 8px;
}

.journey-line{
    position:absolute;
    left:50%;
    top:0;
    bottom:0;
    width:4px;
    transform:translateX(-50%);
    background:linear-gradient(180deg,#bfdbfe,#fecaca);
    border-radius:999px;
    filter:drop-shadow(0 0 6px rgba(37,99,235,0.35));
}

.journey-node{
    position:relative;
    display:flex;
    margin:22px 0;
}

.journey-node.left{
    justify-content:flex-start;
}

.journey-node.right{
    justify-content:flex-end;
}

.node-dot{
    position:absolute;
    left:50%;
    top:18px;
    transform:translate(-50%,-50%);
    width:16px;
    height:16px;
    border-radius:999px;
    background:#fff;
    box-shadow:0 0 0 4px rgba(37,99,235,0.45);
}

.node-card{
    max-width:420px;
    background:var(--bg-surface);
    border-radius:var(--radius-md);
    padding:14px 16px 14px;
    box-shadow:var(--shadow-subtle);
    font-size:14px;
    line-height:1.6;
}

.journey-node.left .node-card{
    margin-right:auto;
    margin-left:0;
}

.journey-node.right .node-card{
    margin-left:auto;
    margin-right:0;
}

/* Inner pages generic */
.page-title{
    font-size:30px;
    font-weight:700;
    margin-bottom:8px;
}

.page-subtitle{
    font-size:14px;
    color:var(--text-soft);
    margin-bottom:26px;
}

.grid-two{
    display:grid;
    grid-template-columns: minmax(0,1.1fr) minmax(0,1fr);
    gap:22px;
}

.list-bullet{
    padding-left:18px;
    margin:8px 0 0;
}

.list-bullet li{
    margin-bottom:4px;
    font-size:14px;
}

/* Timeline */
.timeline{
    display:flex;
    flex-direction:column;
    gap:16px;
}

.timeline-item{
    position:relative;
    padding-left:18px;
}

.timeline-item::before{
    content:"";
    position:absolute;
    left:4px;
    top:4px;
    bottom:4px;
    width:2px;
    background:var(--border-soft);
}

.timeline-dot{
    width:10px;
    height:10px;
    border-radius:999px;
    background:var(--primary);
    position:absolute;
    left:0;
    top:4px;
}

.timeline-body{
    margin-left:18px;
}

.timeline-meta{
    font-size:12px;
    color:var(--text-soft);
    margin-bottom:4px;
}

/* Contact */
.contact-grid{
    display:grid;
    grid-template-columns:minmax(0, minmax(260px, 340px)) minmax(0,1fr);
    gap:26px;
}

.contact-form{
    display:flex;
    flex-direction:column;
    gap:12px;
}

.contact-field{
    display:flex;
    flex-direction:column;
    gap:4px;
}

.contact-field label{
    font-size:13px;
    color:var(--text-soft);
}

.contact-field input,
.contact-field textarea{
    border-radius:12px;
    border:1px solid var(--border-soft);
    padding:8px 10px;
    font-size:13px;
    font-family:inherit;
    background:#f9fafb;
}

.contact-links{
    display:flex;
    flex-direction:column;
    gap:10px;
    font-size:14px;
}

/* Responsive sections */
@media (max-width:960px){
    .journey-shell{
        padding:24px 18px 48px;
    }
    .journey-line{
        left:10px;
        transform:none;
    }
    .node-dot{
        left:10px;
        transform:translate(-50%,-50%);
    }
    .journey-node{
        justify-content:flex-start;
    }
    .node-card{
        margin-left:32px !important;
        margin-right:0 !important;
        max-width:100%;
    }
    .grid-two,
    .contact-grid{
        grid-template-columns:1fr;
    }
}
"""
    write_file(root, "css/pages.css", pages_css)

    # ============= JS: main.js =============
    main_js = """document.addEventListener("DOMContentLoaded", () => {
    console.log("Modern portfolio UI loaded");
});
"""
    write_file(root, "js/main.js", main_js)

    # ============= INNER PAGES (Projects, Experience, Publications, Skills, Contact) =============

    def wrap_page(title, active, body_inner):
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
<header class="site-header">
    <div class="brand-block">
        <div class="brand-avatar">AS</div>
        <div class="brand-meta">
            <span class="brand-name">Abhyuday Singh</span>
            <span class="brand-role">AI / ML Engineer · Applied Research</span>
        </div>
    </div>
    <nav class="nav-main">
        <a href="../index.html" class="nav-link {'active' if active=='home' else ''}">Home</a>
        <a href="projects.html" class="nav-link {'active' if active=='projects' else ''}">Projects</a>
        <a href="experience.html" class="nav-link {'active' if active=='experience' else ''}">Experience</a>
        <a href="publications.html" class="nav-link {'active' if active=='publications' else ''}">Publications</a>
        <a href="skills.html" class="nav-link {'active' if active=='skills' else ''}">Skills</a>
        <a href="contact.html" class="nav-link nav-cta {'active' if active=='contact' else ''}">Contact</a>
    </nav>
</header>

<main class="page-shell">
{body_inner}
</main>

<footer class="site-footer">
    <p>© 2025 · Abhyuday Singh · Portfolio</p>
</footer>
</body>
</html>
"""

    # Projects page
    projects_body = """<section>
    <h1 class="page-title">Projects</h1>
    <p class="page-subtitle">Representative work across LLMs, RAG, computer vision and multimodal systems.</p>

    <div class="grid-two">
        <article class="card">
            <span class="chip">RAG · LLM</span>
            <h2>Enterprise QA Chatbot with Custom Retrieval</h2>
            <p>
                Domain-tuned question-answering assistant using LangChain, Sentence-BERT and FAISS.
                Includes summarisation, keyword extraction and robust fallback flows for document-heavy environments.
            </p>
        </article>

        <article class="card">
            <span class="chip">Defense CV</span>
            <h2>Real-time Surveillance Detection (DRDO)</h2>
            <p>
                YOLO-based pipeline over 1.5M+ labeled frames with mAP@50 > 0.90, optimised for A100 / RTX hardware
                with custom training workflows and secure deployment in defense systems.
            </p>
        </article>

        <article class="card">
            <span class="chip">Govt. Project</span>
            <h2>TRACER · Advanced Person Re-identification</h2>
            <p>
                Combined SRGAN deblurring with YOLOv8 feature extraction to identify subjects from partial, noisy CCTV frames
                for a large-scale surveillance use case.
            </p>
        </article>

        <article class="card">
            <span class="chip">Multimodal</span>
            <h2>Gas Detection with SRGAN & Sparse Autoencoder</h2>
            <p>
                Fusion of thermal imagery and e-nose sensor data using SRGAN super-resolution and sparse autoencoders
                to enhance interpretability and detection reliability.
            </p>
        </article>
    </div>
</section>
"""
    write_file(root, "pages/projects.html", wrap_page("Projects", "projects", projects_body))

    # Experience page
    exp_body = """<section>
    <h1 class="page-title">Experience</h1>
    <p class="page-subtitle">Roles that combine research depth with delivery responsibility.</p>

    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-body card">
                <h2>AI-ML Engineer – Aarav Global Products and Services</h2>
                <p class="timeline-meta">April 2025 – Present · Mumbai, India</p>
                <ul class="list-bullet">
                    <li>LLM/SLM based document intelligence for summarisation, sentiment and keyword extraction.</li>
                    <li>RAG pipelines for semantic search and contextual enterprise Q&A.</li>
                    <li>Agentic AI frameworks for HR agents handling resume screening and JD matching.</li>
                </ul>
            </div>
        </div>

        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-body card">
                <h2>Junior Research Fellow – DRDO ARDE</h2>
                <p class="timeline-meta">June 2024 – March 2025 · Pune, India</p>
                <ul class="list-bullet">
                    <li>Real-time surveillance object detection and classification using YOLO-based models.</li>
                    <li>Led a team annotating 1.5M+ image-label pairs with GPU-efficient dataset design.</li>
                    <li>Handled A100 and RTX A4000 environments, optimisation and deployment in secure systems.</li>
                </ul>
            </div>
        </div>

        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-body card">
                <h2>Freelancer – Data Viz & ML</h2>
                <p class="timeline-meta">September 2021 – May 2023 · Bangalore, India</p>
                <ul class="list-bullet">
                    <li>Built Power BI dashboards and ML utilities for business and academic partners.</li>
                    <li>Supported multiple PhD researchers with analysis, modelling and paper support.</li>
                </ul>
            </div>
        </div>

        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-body card">
                <h2>Java Developer Intern – Tosscall Services</h2>
                <p class="timeline-meta">Jan 2021 – June 2021 · Durg, India</p>
                <ul class="list-bullet">
                    <li>Contributed to a diagnostic management system using Java, JDBC and REST APIs.</li>
                </ul>
            </div>
        </div>
    </div>
</section>
"""
    write_file(root, "pages/experience.html", wrap_page("Experience", "experience", exp_body))

    # Publications page
    pubs_body = """<section>
    <h1 class="page-title">Publications</h1>
    <p class="page-subtitle">Selected peer-reviewed work across multimodal sensing, reinforcement learning and medical AI.</p>

    <div class="card">
        <ul class="list-bullet">
            <li><strong>Multimodal Gas Detection Using E-Nose and Thermal Images</strong> – SRGAN and Sparse Autoencoder based approach, CMC 2025.</li>
            <li><strong>Reinforcement Learning for Rolling Bearing Fault Diagnosis</strong> – Journal Européen des Systèmes Automatisés (JESA), 2024.</li>
            <li><strong>Binary Classification of Brain Tumors Using Fusion Techniques</strong> – International Journal of Intelligent Systems, 2024.</li>
        </ul>
    </div>
</section>
"""
    write_file(root, "pages/publications.html", wrap_page("Publications", "publications", pubs_body))

    # Skills page
    skills_body = """<section>
    <h1 class="page-title">Skills</h1>
    <p class="page-subtitle">Balanced across modelling, systems and deployment.</p>

    <div class="grid-two">
        <article class="card">
            <h2>Core</h2>
            <ul class="list-bullet">
                <li>Python, SQL, JavaScript fundamentals.</li>
                <li>Machine learning workflows and evaluation.</li>
                <li>Deep learning for NLP and Computer Vision.</li>
                <li>LLMs, RAG pipelines and Agentic AI frameworks.</li>
            </ul>
        </article>

        <article class="card">
            <h2>Ecosystem & MLOps</h2>
            <ul class="list-bullet">
                <li>PyTorch, TensorFlow, scikit-learn, OpenCV, HuggingFace.</li>
                <li>FastAPI, Docker, MLflow, DVC, Git, CI/CD awareness.</li>
                <li>AWS, GCP, Streamlit and dashboarding tools.</li>
            </ul>
        </article>
    </div>
</section>
"""
    write_file(root, "pages/skills.html", wrap_page("Skills", "skills", skills_body))

    # Contact page
    contact_body = """<section>
    <h1 class="page-title">Contact</h1>
    <p class="page-subtitle">Best ways to reach out for roles, collaborations or technical discussions.</p>

    <div class="contact-grid">
        <form class="card contact-form" onsubmit="event.preventDefault();">
            <div class="contact-field">
                <label>Name</label>
                <input type="text" placeholder="Your name">
            </div>
            <div class="contact-field">
                <label>Email</label>
                <input type="email" placeholder="you@example.com">
            </div>
            <div class="contact-field">
                <label>Message</label>
                <textarea rows="4" placeholder="Short context or query"></textarea>
            </div>
            <button type="submit" class="btn-primary">Send (static)</button>
        </form>

        <div class="contact-links">
            <span class="badge-soft">Direct Links</span>
            <span>Email: <strong>udit61198@gmail.com</strong></span>
            <span>GitHub: add GitHub profile URL here.</span>
            <span>LinkedIn: add LinkedIn profile URL here.</span>
        </div>
    </div>
</section>
"""
    write_file(root, "pages/contact.html", wrap_page("Contact", "contact", contact_body))

    print("\n[DONE] Modern UI applied. Open index.html to review.")

if __name__ == "__main__":
    main()
