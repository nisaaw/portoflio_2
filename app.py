import streamlit as st

# ============================================================
# SWEETIE FOLIO
# Cute • Colorful • Playful Portfolio Template
# ============================================================

st.set_page_config(
    page_title="Sweetie Folio ♡",
    page_icon="🌷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# COLOR PALETTE
# ============================================================

CREAM = "#FFF9F3"
WHITE = "#FFFFFF"
PINK = "#FF8FAB"
DARK_PINK = "#E85D82"
LIGHT_PINK = "#FFE1EA"
YELLOW = "#FFD166"
LIGHT_YELLOW = "#FFF0B8"
BLUE = "#A9DEF9"
LIGHT_BLUE = "#E2F6FF"
PURPLE = "#CDB4DB"
LIGHT_PURPLE = "#F0E7F7"
MINT = "#B8E0D2"
LIGHT_MINT = "#E7F7F1"
TEXT = "#493548"
MUTED = "#786575"

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* ================= MAIN ================= */

    .stApp {{
        background: {CREAM};
    }}

    .main .block-container {{
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }}

    html {{
        scroll-behavior: smooth;
    }}

    /* ================= TEXT ================= */

    h1, h2, h3, h4 {{
        color: {TEXT} !important;
    }}

    p, span, label {{
        color: {TEXT};
    }}

    /* ================= NAVBAR ================= */

    .cute-nav {{
        background: white;
        border: 2px solid {LIGHT_PINK};
        border-radius: 30px;
        padding: 13px 22px;
        box-shadow: 0 8px 25px rgba(73,53,72,0.07);
        text-align: center;
        margin-bottom: 30px;
    }}

    .nav-logo {{
        color: {DARK_PINK};
        font-weight: 900;
        font-size: 18px;
        letter-spacing: 1px;
    }}

    .nav-links {{
        color: {MUTED};
        font-size: 13px;
        font-weight: 700;
        letter-spacing: .5px;
    }}

    /* ================= HERO ================= */

    .hero {{
        position: relative;
        overflow: hidden;
        background:
            radial-gradient(circle at 8% 15%, #ffffff 0 4%, transparent 4.5%),
            radial-gradient(circle at 90% 20%, #ffffff 0 5%, transparent 5.5%),
            linear-gradient(135deg, #FFE2EC, #FFF7D9 52%, #E4F6FF);
        border: 3px solid white;
        border-radius: 42px;
        padding: 55px 45px;
        box-shadow: 0 15px 45px rgba(73,53,72,.09);
        min-height: 430px;
    }}

    .hero-small {{
        color: {DARK_PINK};
        font-size: 15px;
        font-weight: 900;
        letter-spacing: 2px;
        text-transform: uppercase;
    }}

    .hero-title {{
        font-size: clamp(42px, 6vw, 76px);
        line-height: .95;
        font-weight: 950;
        color: {TEXT};
        margin: 15px 0;
    }}

    .hero-title span {{
        color: {PINK};
    }}

    .hero-description {{
        max-width: 580px;
        font-size: 17px;
        line-height: 1.8;
        color: {MUTED};
    }}

    .sticker {{
        display: inline-block;
        padding: 8px 15px;
        border-radius: 100px;
        background: white;
        border: 2px solid {LIGHT_PINK};
        font-weight: 800;
        margin: 5px;
        box-shadow: 0 5px 15px rgba(73,53,72,.08);
        transform: rotate(-2deg);
    }}

    .sticker.yellow {{
        border-color: {YELLOW};
        transform: rotate(3deg);
    }}

    .sticker.blue {{
        border-color: {BLUE};
        transform: rotate(-3deg);
    }}

    /* ================= DECORATIONS ================= */

    .floating-flower {{
        font-size: 75px;
        text-align: center;
        padding-top: 40px;
    }}

    .floating-small {{
        font-size: 35px;
        text-align: center;
        margin-top: 15px;
    }}

    /* ================= SECTION ================= */

    .section {{
        margin-top: 70px;
    }}

    .section-label {{
        color: {DARK_PINK};
        font-weight: 900;
        letter-spacing: 2px;
        font-size: 13px;
        text-transform: uppercase;
        text-align: center;
    }}

    .section-title {{
        text-align: center;
        font-size: 39px;
        font-weight: 950;
        margin: 8px 0;
    }}

    .section-subtitle {{
        text-align: center;
        color: {MUTED};
        font-size: 15px;
        margin-bottom: 30px;
    }}

    /* ================= CARDS ================= */

    .cute-card {{
        background: white;
        border-radius: 28px;
        padding: 28px;
        border: 3px solid white;
        box-shadow: 0 10px 30px rgba(73,53,72,.07);
        min-height: 190px;
    }}

    .pink-card {{
        background: {LIGHT_PINK};
        border-color: #FFD0DC;
    }}

    .blue-card {{
        background: {LIGHT_BLUE};
        border-color: #C7EDFC;
    }}

    .yellow-card {{
        background: {LIGHT_YELLOW};
        border-color: #FFE59A;
    }}

    .purple-card {{
        background: {LIGHT_PURPLE};
        border-color: #E3D4ED;
    }}

    .mint-card {{
        background: {LIGHT_MINT};
        border-color: #D1EFE4;
    }}

    .card-icon {{
        font-size: 42px;
        margin-bottom: 8px;
    }}

    .card-heading {{
        font-size: 21px;
        font-weight: 900;
        color: {TEXT};
        margin-bottom: 8px;
    }}

    .card-text {{
        color: {MUTED};
        line-height: 1.7;
        font-size: 14px;
    }}

    /* ================= STATS ================= */

    .stat-card {{
        background: white;
        border-radius: 24px;
        padding: 22px 15px;
        text-align: center;
        border: 2px solid {LIGHT_PINK};
        box-shadow: 0 8px 22px rgba(73,53,72,.05);
    }}

    .stat-number {{
        font-size: 30px;
        font-weight: 950;
        color: {DARK_PINK};
    }}

    .stat-label {{
        font-size: 12px;
        font-weight: 700;
        color: {MUTED};
    }}

    /* ================= PROJECT ================= */

    .project-card {{
        background: white;
        border-radius: 30px;
        overflow: hidden;
        border: 3px solid white;
        box-shadow: 0 10px 30px rgba(73,53,72,.08);
        margin-bottom: 20px;
    }}

    .project-visual {{
        min-height: 190px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 70px;
    }}

    .visual-pink {{
        background: linear-gradient(135deg, #FFDCE7, #FFF0F5);
    }}

    .visual-blue {{
        background: linear-gradient(135deg, #DDF5FF, #EAFBFF);
    }}

    .visual-yellow {{
        background: linear-gradient(135deg, #FFF0B5, #FFF8DA);
    }}

    .visual-purple {{
        background: linear-gradient(135deg, #E9DDF2, #F6EFF9);
    }}

    .project-body {{
        padding: 25px;
    }}

    .project-tag {{
        display: inline-block;
        background: {LIGHT_PINK};
        color: {DARK_PINK};
        padding: 6px 13px;
        border-radius: 50px;
        font-size: 11px;
        font-weight: 900;
        margin-bottom: 10px;
    }}

    .project-title {{
        font-size: 23px;
        font-weight: 950;
        margin-bottom: 8px;
    }}

    .project-description {{
        color: {MUTED};
        font-size: 14px;
        line-height: 1.7;
    }}

    /* ================= TIMELINE ================= */

    .timeline-card {{
        background: white;
        border-radius: 25px;
        padding: 22px;
        border-left: 7px solid {PINK};
        box-shadow: 0 8px 25px rgba(73,53,72,.06);
        margin-bottom: 18px;
    }}

    .timeline-year {{
        color: {DARK_PINK};
        font-size: 12px;
        font-weight: 900;
        letter-spacing: 1px;
    }}

    .timeline-title {{
        font-size: 20px;
        font-weight: 900;
        margin-top: 5px;
    }}

    .timeline-company {{
        color: {MUTED};
        font-size: 13px;
        margin-top: 3px;
    }}

    /* ================= SKILLS ================= */

    .skill-name {{
        font-weight: 900;
        margin-bottom: 5px;
    }}

    /* ================= CONTACT ================= */

    .contact-box {{
        background:
            radial-gradient(circle at 10% 20%, #ffffff 0 4%, transparent 4.5%),
            radial-gradient(circle at 90% 70%, #ffffff 0 5%, transparent 5.5%),
            linear-gradient(135deg, #FFE2EC, #E4F6FF);
        border-radius: 38px;
        padding: 50px 35px;
        text-align: center;
        border: 3px solid white;
        box-shadow: 0 12px 35px rgba(73,53,72,.08);
    }}

    .contact-title {{
        font-size: 38px;
        font-weight: 950;
    }}

    /* ================= BUTTON ================= */

    .stButton > button {{
        border-radius: 50px !important;
        border: 2px solid white !important;
        background: {PINK} !important;
        color: white !important;
        font-weight: 900 !important;
        box-shadow: 0 7px 18px rgba(232,93,130,.22);
        min-height: 45px;
    }}

    .stButton > button:hover {{
        background: {DARK_PINK} !important;
        border-color: white !important;
        color: white !important;
    }}

    /* ================= INPUT ================= */

    .stTextInput input,
    .stTextArea textarea {{
        border-radius: 18px !important;
        border: 2px solid {LIGHT_PINK} !important;
        background: white !important;
    }}

    /* ================= FOOTER ================= */

    .footer {{
        text-align: center;
        padding: 50px 10px 15px;
        color: {MUTED};
        font-size: 13px;
    }}

    .footer-heart {{
        color: {PINK};
        font-size: 22px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# EDIT HERE — TEMPLATE OWNER INFORMATION
# ============================================================

NAME = "Your Name"
ROLE = "Creative Professional"
LOCATION = "Your City"

ABOUT = """
Hi! I'm a curious creative who enjoys turning ideas into
beautiful, useful and meaningful projects. Replace this
paragraph with your own story, background and personality.
"""

EMAIL = "hello@example.com"
INSTAGRAM = "@yourusername"
LINKEDIN = "linkedin.com/in/yourusername"
GITHUB = "github.com/yourusername"

# ============================================================
# NAVBAR
# ============================================================

st.markdown(
    """
    <div class="cute-nav">
        <span class="nav-logo">🌷 SWEETIE FOLIO ♡</span>
        &nbsp;&nbsp;&nbsp;
        <span class="nav-links">
            HOME　 ABOUT　 WORK　 SKILLS　 CONTACT
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO
# ============================================================

hero_left, hero_right = st.columns([1.65, 1])

with hero_left:

    st.markdown(
        """
        <div class="hero-small">
            ✦ HELLO, LOVELY PEOPLE ✦
        </div>

        <div class="hero-title">
            I'm <span>Your Name</span><br>
            and I make things<br>
            with ♡
        </div>

        <div class="hero-description">
            A cute little corner of the internet where
            creativity, curiosity and ideas come together.
            Replace this text with your own introduction.
        </div>

        <br>

        <span class="sticker">🌷 Creative</span>
        <span class="sticker yellow">✨ Curious</span>
        <span class="sticker blue">🦋 Dreamer</span>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("🌸 Explore My Portfolio", use_container_width=True):
        st.balloons()

with hero_right:

    st.markdown(
        """
        <div class="floating-flower">
            🌷
        </div>

        <div style="
            background:white;
            border-radius:35px;
            padding:25px;
            text-align:center;
            border:3px solid #FFE1EA;
            box-shadow:0 10px 30px rgba(73,53,72,.08);
        ">

            <div style="font-size:65px;">
                🧸
            </div>

            <div style="
                font-size:20px;
                font-weight:900;
                color:#493548;
            ">
                Welcome ♡
            </div>

            <div style="
                color:#786575;
                font-size:13px;
                margin-top:8px;
            ">
                Thanks for stopping by!
            </div>

            <div class="floating-small">
                ✦ 🌸 ✦
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# STATS
# ============================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-label">A FEW LITTLE NUMBERS</div>
    <div class="section-title">My tiny achievements ✨</div>
    """,
    unsafe_allow_html=True
)

s1, s2, s3, s4 = st.columns(4)

stats = [
    ("12+", "Projects"),
    ("15+", "Skills"),
    ("05", "Certificates"),
    ("∞", "Ideas")
]

for col, (number, label) in zip([s1, s2, s3, s4], stats):

    with col:

        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{number}</div>
                <div class="stat-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# ABOUT
# ============================================================

st.markdown(
    """
    <div class="section-label" style="margin-top:70px;">
        GET TO KNOW ME
    </div>

    <div class="section-title">
        A little about me 🌷
    </div>

    <div class="section-subtitle">
        Because every portfolio should have a little personality.
    </div>
    """,
    unsafe_allow_html=True
)

about1, about2 = st.columns([1.25, 1])

with about1:

    st.markdown(
        f"""
        <div class="cute-card pink-card">

            <div class="card-icon">🌸</div>

            <div class="card-heading">
                Hi, I'm {NAME}!
            </div>

            <div class="card-text">
                {ABOUT}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with about2:

    st.markdown(
        """
        <div class="cute-card yellow-card">

            <div class="card-icon">🍓</div>

            <div class="card-heading">
                My little philosophy
            </div>

            <div class="card-text">
                Stay curious.<br>
                Make things better.<br>
                Don't forget to enjoy the process. ♡
            </div>

            <br>

            <span class="sticker">
                keep growing 🌱
            </span>

        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# WHAT I DO
# ============================================================

st.markdown(
    """
    <div class="section-label" style="margin-top:70px;">
        WHAT I DO
    </div>

    <div class="section-title">
        Things I enjoy ✿
    </div>
    """,
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

cards = [
    (
        "🎨",
        "Creative Work",
        "Designing ideas, visuals and experiences that feel fresh and memorable.",
        "pink-card"
    ),
    (
        "💻",
        "Digital Projects",
        "Building websites, dashboards and interactive digital experiences.",
        "blue-card"
    ),
    (
        "🌱",
        "Learning",
        "Exploring new skills, tools and ideas while continuously improving.",
        "mint-card"
    )
]

for col, (icon, title, text, color) in zip([c1, c2, c3], cards):

    with col:

        st.markdown(
            f"""
            <div class="cute-card {color}">

                <div class="card-icon">
                    {icon}
                </div>

                <div class="card-heading">
                    {title}
                </div>

                <div class="card-text">
                    {text}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# PROJECTS
# ============================================================

st.markdown(
    """
    <div class="section-label" style="margin-top:70px;">
        MY LITTLE CREATIONS
    </div>

    <div class="section-title">
        Selected works 🦋
    </div>

    <div class="section-subtitle">
        Replace these cards with your own portfolio projects.
    </div>
    """,
    unsafe_allow_html=True
)

p1, p2 = st.columns(2)

with p1:

    st.markdown(
        """
        <div class="project-card">

            <div class="project-visual visual-pink">
                🌷 ✨ 🎀
            </div>

            <div class="project-body">

                <div class="project-tag">
                    FEATURED
                </div>

                <div class="project-title">
                    Bloom Project
                </div>

                <div class="project-description">
                    A creative project focused on creating
                    a beautiful and friendly digital experience.
                </div>

                <br>

                <span class="sticker">
                    Design
                </span>

                <span class="sticker yellow">
                    Creative
                </span>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with p2:

    st.markdown(
        """
        <div class="project-card">

            <div class="project-visual visual-blue">
                🦋 💻 ☁️
            </div>

            <div class="project-body">

                <div class="project-tag">
                    DIGITAL
                </div>

                <div class="project-title">
                    Cloudy Website
                </div>

                <div class="project-description">
                    An interactive website designed to make
                    information feel simple, friendly and fun.
                </div>

                <br>

                <span class="sticker blue">
                    Web
                </span>

                <span class="sticker">
                    Python
                </span>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

p3, p4 = st.columns(2)

with p3:

    st.markdown(
        """
        <div class="project-card">

            <div class="project-visual visual-yellow">
                🍋 📊 ✨
            </div>

            <div class="project-body">

                <div class="project-tag">
                    DATA
                </div>

                <div class="project-title">
                    Sunny Dashboard
                </div>

                <div class="project-description">
                    A colorful dashboard that turns numbers
                    into something easier and more enjoyable to understand.
                </div>

                <br>

                <span class="sticker yellow">
                    Data
                </span>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with p4:

    st.markdown(
        """
        <div class="project-card">

            <div class="project-visual visual-purple">
                🪻 📚 💡
            </div>

            <div class="project-body">

                <div class="project-tag">
                    RESEARCH
                </div>

                <div class="project-title">
                    Little Research
                </div>

                <div class="project-description">
                    A research-based project where curiosity
                    became an interesting little discovery.
                </div>

                <br>

                <span class="sticker">
                    Research
                </span>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# EXPERIENCE
# ============================================================

st.markdown(
    """
    <div class="section-label" style="margin-top:70px;">
        MY JOURNEY
    </div>

    <div class="section-title">
        Experience & education 🌱
    </div>
    """,
    unsafe_allow_html=True
)

experience = [
    (
        "2026 — NOW",
        "Current Experience",
        "Your Company / Organization",
        "Add your current position, internship or activity here."
    ),
    (
        "2024 — 2026",
        "Education",
        "Your University",
        "Add your major, achievements or interesting activities here."
    ),
    (
        "2024",
        "First Big Project",
        "Personal / Academic",
        "Describe an important project or experience."
    )
]

for year, title, company, description in experience:

    st.markdown(
        f"""
        <div class="timeline-card">

            <div class="timeline-year">
                {year}
            </div>

            <div class="timeline-title">
                {title}
            </div>

            <div class="timeline-company">
                {company}
            </div>

            <div class="card-text" style="margin-top:10px;">
                {description}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# SKILLS
# ============================================================

st.markdown(
    """
    <div class="section-label" style="margin-top:70px;">
        MY TOOLBOX
    </div>

    <div class="section-title">
        Skills & abilities 🧰
    </div>

    <div class="section-subtitle">
        These percentages are only placeholders — customize them!
    </div>
    """,
    unsafe_allow_html=True
)

skill_left, skill_right = st.columns(2)

skills_left = {
    "Creative Thinking": 90,
    "Communication": 85,
    "Problem Solving": 88,
    "Project Management": 78
}

skills_right = {
    "Python": 80,
    "Design": 82,
    "Research": 87,
    "Data Analysis": 76
}

with skill_left:

    for skill, value in skills_left.items():

        st.markdown(
            f"""
            <div class="skill-name">
                {skill}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(value / 100)

with skill_right:

    for skill, value in skills_right.items():

        st.markdown(
            f"""
            <div class="skill-name">
                {skill}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(value / 100)

# ============================================================
# FUN INTERACTIVE SECTION
# ============================================================

st.markdown(
    """
    <div class="section-label" style="margin-top:70px;">
        A LITTLE SOMETHING FUN
    </div>

    <div class="section-title">
        Pick your mood today ✨
    </div>
    """,
    unsafe_allow_html=True
)

mood = st.selectbox(
    "Choose one:",
    [
        "🌷 Soft & Sweet",
        "🍓 Productive",
        "🦋 Creative",
        "☁️ Taking It Easy",
        "✨ Full of Ideas"
    ]
)

messages = {
    "🌷 Soft & Sweet":
        "Today feels like flowers, pastel colors and a little bit of sunshine. 🌷",

    "🍓 Productive":
        "Let's get things done! One little step at a time. 🍓",

    "🦋 Creative":
        "Your brain is full of butterflies and new ideas today. 🦋",

    "☁️ Taking It Easy":
        "Rest is part of the process too. Be gentle with yourself. ☁️",

    "✨ Full of Ideas":
        "Write those ideas down before they fly away! ✨"
}

st.success(messages[mood])

# ============================================================
# CONTACT
# ============================================================

st.markdown(
    """
    <div class="section-label" style="margin-top:70px;">
        SAY HELLO
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="contact-box">

        <div class="contact-title">
            Let's create something cute! 💌
        </div>

        <p style="
            color:#786575;
            font-size:16px;
            margin-top:10px;
        ">
            Have a project, idea or just want to say hello?
        </p>

        <div style="
            font-size:40px;
            margin-top:20px;
        ">
            🌷 🦋 🍓 ✨
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

contact1, contact2 = st.columns(2)

with contact1:

    with st.form("contact_form"):

        name = st.text_input("Your name ✿")
        email = st.text_input("Your email 💌")
        message = st.text_area("Your message 🌷")

        submitted = st.form_submit_button(
            "Send a little message ♡",
            use_container_width=True
        )

        if submitted:

            if name and email and message:
                st.success(
                    "Thank you! Your message has been received. 🌸"
                )
            else:
                st.warning(
                    "Please fill in all the fields first ♡"
                )

with contact2:

    st.markdown(
        f"""
        <div class="cute-card purple-card">

            <div class="card-icon">
                💌
            </div>

            <div class="card-heading">
                Find me around the internet
            </div>

            <div class="card-text">

                📧 {EMAIL}<br><br>

                📸 {INSTAGRAM}<br><br>

                💼 {LINKEDIN}<br><br>

                💻 {GITHUB}

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        <div class="footer-heart">
            ♡
        </div>

        Made with a little creativity & lots of love.

        <br>

        <b>Sweetie Folio</b> · Cute Streamlit Portfolio Template

        <br><br>

        🌷 ✦ 🦋 ✦ 🍓 ✦ ✨

    </div>
    """,
    unsafe_allow_html=True
)
