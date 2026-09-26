import streamlit as st

# =========================================================
# 🌷 SWEETIE FOLIO
# Cute & Colorful Streamlit Portfolio Template
# =========================================================

st.set_page_config(
    page_title="Sweetie Folio ♡",
    page_icon="🌷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# 🎨 COLOR PALETTE
# =========================================================

PINK = "#FF8FAB"
DARK_PINK = "#E85D82"
SOFT_PINK = "#FFE5EC"

BLUE = "#8FD3F4"
SOFT_BLUE = "#E4F7FF"

YELLOW = "#FFD166"
SOFT_YELLOW = "#FFF4C7"

PURPLE = "#CDB4DB"
SOFT_PURPLE = "#F2E9F7"

MINT = "#9ED9C5"
SOFT_MINT = "#E5F7F0"

CREAM = "#FFF9F3"
TEXT = "#493548"
MUTED = "#766474"

# =========================================================
# 🎀 CUSTOM CSS
# ONLY CSS — NO HTML CONTENT
# =========================================================

st.markdown(
    f"""
    <style>

    /* =========================
       GENERAL
       ========================= */

    .stApp {{
        background-color: {CREAM};
    }}

    .main .block-container {{
        max-width: 1150px;
        padding-top: 25px;
        padding-bottom: 60px;
    }}

    h1, h2, h3, h4 {{
        color: {TEXT} !important;
    }}

    p {{
        color: {TEXT};
    }}

    /* =========================
       HIDE DEFAULT MENU
       ========================= */

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    /* =========================
       TITLE
       ========================= */

    .big-title {{
        font-size: 58px !important;
        font-weight: 900 !important;
        line-height: 1.05 !important;
        color: {TEXT} !important;
    }}

    /* =========================
       BUTTONS
       ========================= */

    .stButton > button {{
        border-radius: 30px;
        border: 2px solid white;
        background-color: {PINK};
        color: white;
        font-weight: 800;
        min-height: 45px;
        box-shadow: 0 5px 15px rgba(232,93,130,0.20);
    }}

    .stButton > button:hover {{
        background-color: {DARK_PINK};
        color: white;
        border-color: white;
    }}

    /* =========================
       METRIC
       ========================= */

    [data-testid="stMetric"] {{
        background-color: white;
        border: 2px solid {SOFT_PINK};
        border-radius: 22px;
        padding: 18px;
        box-shadow: 0 5px 18px rgba(73,53,72,0.05);
    }}

    [data-testid="stMetricValue"] {{
        color: {DARK_PINK};
    }}

    /* =========================
       PROGRESS BAR
       ========================= */

    .stProgress > div > div > div > div {{
        background-color: {PINK};
    }}

    /* =========================
       INPUT
       ========================= */

    .stTextInput input,
    .stTextArea textarea {{
        border-radius: 18px;
        border: 2px solid {SOFT_PINK};
        background-color: white;
    }}

    /* =========================
       SELECT BOX
       ========================= */

    [data-baseweb="select"] > div {{
        border-radius: 18px;
        border: 2px solid {SOFT_PINK};
    }}

    /* =========================
       INFO / SUCCESS
       ========================= */

    [data-testid="stAlert"] {{
        border-radius: 20px;
    }}

    /* =========================
       MOBILE
       ========================= */

    @media (max-width: 768px) {{

        .big-title {{
            font-size: 40px !important;
        }}

    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# ✏️ EDIT THIS SECTION
# Template buyers can change these
# =========================================================

NAME = "Your Name"
ROLE = "Creative Professional"
LOCATION = "Your City"

EMAIL = "hello@example.com"
INSTAGRAM = "@yourusername"
LINKEDIN = "linkedin.com/in/yourusername"
GITHUB = "github.com/yourusername"

ABOUT = """
Hi! I'm a curious and creative person who loves learning,
creating new things and turning simple ideas into meaningful
projects. Replace this text with your own introduction.
"""

# =========================================================
# 🌷 TOP NAVIGATION
# =========================================================

top1, top2, top3 = st.columns([2, 4, 2])

with top1:
    st.markdown("## 🌷 Sweetie Folio")

with top2:
    st.markdown(
        "### ♡ Home　 About　 Work　 Skills　 Contact"
    )

with top3:
    st.markdown("### ✨ Portfolio")

st.divider()

# =========================================================
# 🎀 HERO SECTION
# =========================================================

hero_left, hero_right = st.columns([1.5, 1])

with hero_left:

    st.markdown("### ✦ HELLO, LOVELY PEOPLE ✦")

    st.markdown(
        '<p class="big-title">'
        'I\'m <span style="color:#FF8FAB;">Your Name</span><br>'
        'and I create<br>'
        'with ♡'
        '</p>',
        unsafe_allow_html=True
    )

    st.write(
        "A tiny corner of the internet where creativity, "
        "curiosity and ideas come together."
    )

    st.write("")

    tag1, tag2, tag3 = st.columns(3)

    with tag1:
        st.info("🌷 Creative")

    with tag2:
        st.success("🦋 Curious")

    with tag3:
        st.warning("✨ Dreamer")

    st.write("")

    if st.button(
        "🌸 Explore My World",
        use_container_width=True
    ):
        st.balloons()

with hero_right:

    st.markdown("## 🌷")
    st.markdown("## 🧸")

    st.markdown("### Welcome ♡")

    st.write(
        "Thank you for stopping by! "
        "Have fun exploring this little portfolio."
    )

    st.markdown("### ✦ 🌸 ✦")

    st.info(
        "A little space for ideas, projects and dreams."
    )

# =========================================================
# 🍓 QUICK STATS
# =========================================================

st.write("")
st.write("")

st.markdown("## ✿ A Few Little Numbers")

st.caption(
    "Tiny achievements, big smiles ♡"
)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("🌷 Projects", "12+")

with m2:
    st.metric("🦋 Skills", "15+")

with m3:
    st.metric("🎀 Certificates", "05")

with m4:
    st.metric("✨ Ideas", "∞")

# =========================================================
# 🌸 ABOUT ME
# =========================================================

st.write("")
st.write("")

st.markdown("## 🌸 A Little About Me")

about_left, about_right = st.columns([1.3, 1])

with about_left:

    st.info(
        f"""
        ### 🧸 Hi, I'm {NAME}!

        {ABOUT}
        """
    )

with about_right:

    st.success(
        """
        ### 🍓 My Little Philosophy

        🌱 Stay curious.

        ✨ Keep learning.

        🎀 Make things better.

        🌷 Enjoy the process.
        """
    )

# =========================================================
# 💕 WHAT I DO
# =========================================================

st.write("")
st.write("")

st.markdown("## ♡ Things I Love Working With")

st.caption(
    "Replace these with your own interests, services or specialties."
)

c1, c2, c3 = st.columns(3)

with c1:

    st.info(
        """
        ## 🎨

        ### Creative Work

        Creating visuals, ideas and experiences
        that feel fresh and memorable.
        """
    )

with c2:

    st.success(
        """
        ## 💻

        ### Digital Projects

        Building websites, dashboards and
        interactive digital experiences.
        """
    )

with c3:

    st.warning(
        """
        ## 🌱

        ### Learning

        Exploring new skills, tools and ideas
        while continuously improving.
        """
    )

# =========================================================
# 🦋 PROJECTS
# =========================================================

st.write("")
st.write("")

st.markdown("## 🦋 Selected Works")

st.caption(
    "Show your favorite projects here ♡"
)

p1, p2 = st.columns(2)

with p1:

    st.info(
        """
        ## 🌷 Bloom Project

        **FEATURED PROJECT**

        A creative project focused on creating
        a beautiful and friendly digital experience.

        **Tools**

        🎨 Design  
        💻 Development  
        ✨ Creative Thinking
        """
    )

    if st.button(
        "View Bloom Project →",
        key="project1",
        use_container_width=True
    ):
        st.success(
            "This is where your project details can appear! 🌷"
        )

with p2:

    st.success(
        """
        ## 🦋 Cloudy Website

        **DIGITAL PROJECT**

        An interactive website designed to make
        information feel simple and enjoyable.

        **Tools**

        💻 Python  
        🌐 Web  
        🎨 Design
        """
    )

    if st.button(
        "View Cloudy Website →",
        key="project2",
        use_container_width=True
    ):
        st.success(
            "This is where your website details can appear! 🦋"
        )

p3, p4 = st.columns(2)

with p3:

    st.warning(
        """
        ## 🍋 Sunny Dashboard

        **DATA PROJECT**

        A colorful dashboard that transforms
        numbers into something easier to understand.

        **Tools**

        📊 Data  
        💻 Python  
        ✨ Visualization
        """
    )

    if st.button(
        "View Dashboard →",
        key="project3",
        use_container_width=True
    ):
        st.success(
            "Dashboard project selected! 🍋"
        )

with p4:

    st.markdown(
        """
        <style>
        </style>
        """,
        unsafe_allow_html=True
    )

    st.info(
        """
        ## 🪻 Little Research

        **RESEARCH PROJECT**

        A research-based project where curiosity
        became an interesting discovery.

        **Tools**

        📚 Research  
        🔬 Analysis  
        💡 Problem Solving
        """
    )

    if st.button(
        "View Research →",
        key="project4",
        use_container_width=True
    ):
        st.success(
            "Research project selected! 🪻"
        )

# =========================================================
# 🌱 EXPERIENCE
# =========================================================

st.write("")
st.write("")

st.markdown("## 🌱 My Little Journey")

st.caption(
    "Education, work, internship or organization experience."
)

st.markdown(
    """
    ### 🌷 2026 — Now
    **Current Experience**

    Your Company / Organization

    Add your current position, internship or activity here.
    """
)

st.divider()

st.markdown(
    """
    ### 🦋 2024 — 2026
    **Education**

    Your University

    Add your major, achievements or interesting activities here.
    """
)

st.divider()

st.markdown(
    """
    ### 🍓 2024
    **First Big Project**

    Personal / Academic Project

    Describe an important project or experience here.
    """
)

# =========================================================
# 🎀 SKILLS
# =========================================================

st.write("")
st.write("")

st.markdown("## 🎀 My Skills")

st.caption(
    "The percentages below are placeholders."
)

skill1, skill2 = st.columns(2)

with skill1:

    st.markdown("### 🎨 Creative Thinking")
    st.progress(90)

    st.markdown("### 💬 Communication")
    st.progress(85)

    st.markdown("### 🧠 Problem Solving")
    st.progress(88)

    st.markdown("### 📋 Project Management")
    st.progress(78)

with skill2:

    st.markdown("### 💻 Python")
    st.progress(80)

    st.markdown("### 🎨 Design")
    st.progress(82)

    st.markdown("### 🔬 Research")
    st.progress(87)

    st.markdown("### 📊 Data Analysis")
    st.progress(76)

# =========================================================
# ✨ FUN INTERACTIVE SECTION
# =========================================================

st.write("")
st.write("")

st.markdown("## ✨ A Little Something Fun")

st.caption(
    "Because portfolios don't have to be boring ♡"
)

mood = st.selectbox(
    "🌷 Pick your mood today:",
    [
        "🌷 Soft & Sweet",
        "🍓 Productive",
        "🦋 Creative",
        "☁️ Taking It Easy",
        "✨ Full of Ideas"
    ]
)

if mood == "🌷 Soft & Sweet":

    st.info(
        "Today feels like flowers, pastel colors "
        "and a little sunshine. 🌷"
    )

elif mood == "🍓 Productive":

    st.success(
        "Let's get things done! "
        "One little step at a time. 🍓"
    )

elif mood == "🦋 Creative":

    st.info(
        "Your brain is full of butterflies "
        "and new ideas today. 🦋"
    )

elif mood == "☁️ Taking It Easy":

    st.warning(
        "Rest is part of the process too. "
        "Be gentle with yourself. ☁️"
    )

else:

    st.success(
        "Write those ideas down before "
        "they fly away! ✨"
    )

# =========================================================
# 💌 CONTACT
# =========================================================

st.write("")
st.write("")

st.markdown("## 💌 Let's Connect")

st.caption(
    "Have an idea, project or just want to say hello?"
)

contact_left, contact_right = st.columns(2)

with contact_left:

    st.markdown("### 🌷 Find Me")

    st.write(f"📧 **{EMAIL}**")
    st.write(f"📸 **{INSTAGRAM}**")
    st.write(f"💼 **{LINKEDIN}**")
    st.write(f"💻 **{GITHUB}**")

    st.write("")

    st.info(
        "Replace these placeholders with your real "
        "social media links."
    )

with contact_right:

    st.markdown("### 🧸 Send a Little Message")

    visitor_name = st.text_input(
        "Your name",
        placeholder="Type your name..."
    )

    visitor_email = st.text_input(
        "Your email",
        placeholder="hello@example.com"
    )

    visitor_message = st.text_area(
        "Message",
        placeholder="Write something nice ♡"
    )

    if st.button(
        "💌 Send Message",
        use_container_width=True
    ):

        if (
            visitor_name
            and visitor_email
            and visitor_message
        ):

            st.success(
                "Thank you for your message! 🌸"
            )

        else:

            st.warning(
                "Please fill everything in first ♡"
            )

# =========================================================
# 🌷 FOOTER
# =========================================================

st.write("")
st.write("")
st.divider()

st.markdown(
    """
    ### 🌷 ♡ 🦋 ♡ 🍓 ♡ ✨

    """
)

st.caption(
    "Made with ♡ and a little bit of magic."
)

st.caption(
    "Sweetie Folio — Cute Streamlit Portfolio Template"
)
