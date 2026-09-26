import streamlit as st

# ============================================================
# ✿ CUTE PROFESSIONAL PORTFOLIO
# Streamlit Template
# ============================================================

st.set_page_config(
    page_title="Lumi Folio",
    page_icon="🌷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# 🎨 THEME
# ============================================================

THEMES = {
    "Strawberry": {
        "primary": "#E96B8B",
        "secondary": "#FFDCE6",
        "accent": "#FFF0B5",
        "background": "#FFF9F6",
        "card": "#FFFFFF",
        "text": "#40343C",
        "muted": "#796D75"
    },
    "Lavender": {
        "primary": "#9B7EBD",
        "secondary": "#EDE4F7",
        "accent": "#DDF4FF",
        "background": "#FBF9FE",
        "card": "#FFFFFF",
        "text": "#40384A",
        "muted": "#756C80"
    },
    "Baby Blue": {
        "primary": "#5DADE2",
        "secondary": "#DDF3FF",
        "accent": "#FFF0B5",
        "background": "#F8FCFF",
        "card": "#FFFFFF",
        "text": "#35404A",
        "muted": "#687780"
    },
    "Matcha": {
        "primary": "#78A77A",
        "secondary": "#E4F2E2",
        "accent": "#FFF0C7",
        "background": "#FAFCF8",
        "card": "#FFFFFF",
        "text": "#354238",
        "muted": "#68746A"
    }
}

# ============================================================
# 🎛️ SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🌷 Lumi Folio")
    st.caption("Cute • Clean • Professional")

    st.divider()

    theme_name = st.selectbox(
        "🎨 Choose a theme",
        list(THEMES.keys())
    )

    theme = THEMES[theme_name]

    st.divider()

    st.markdown("### ✿ Quick Menu")

    page = st.radio(
        "Go to",
        [
            "🏠 Home",
            "🌷 About",
            "💼 Projects",
            "🧰 Skills",
            "📖 Experience",
            "💌 Contact"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.caption("Made with ♡ using Streamlit")

# ============================================================
# 🎨 CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {{
        background-color: {theme["background"]};
    }}

    .main .block-container {{
        max-width: 1120px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }}

    h1, h2, h3, h4 {{
        color: {theme["text"]} !important;
        letter-spacing: -0.5px;
    }}

    p, li {{
        color: {theme["text"]};
        line-height: 1.7;
    }}

    /* ---------- SIDEBAR ---------- */

    section[data-testid="stSidebar"] {{
        background-color: {theme["card"]};
        border-right: 1px solid {theme["secondary"]};
    }}

    /* ---------- BUTTON ---------- */

    .stButton > button {{
        border-radius: 16px;
        border: 1px solid {theme["primary"]};
        background-color: {theme["primary"]};
        color: white;
        font-weight: 700;
        min-height: 42px;
        transition: 0.2s;
    }}

    .stButton > button:hover {{
        background-color: {theme["text"]};
        border-color: {theme["text"]};
        color: white;
    }}

    /* ---------- INPUT ---------- */

    .stTextInput input,
    .stTextArea textarea {{
        border-radius: 14px;
        border: 1px solid {theme["secondary"]};
        background-color: white;
    }}

    /* ---------- SELECT ---------- */

    [data-baseweb="select"] > div {{
        border-radius: 14px;
        border: 1px solid {theme["secondary"]};
    }}

    /* ---------- METRICS ---------- */

    [data-testid="stMetric"] {{
        background-color: white;
        border: 1px solid {theme["secondary"]};
        border-radius: 18px;
        padding: 18px;
    }}

    [data-testid="stMetricValue"] {{
        color: {theme["primary"]};
    }}

    /* ---------- PROGRESS ---------- */

    .stProgress > div > div > div > div {{
        background-color: {theme["primary"]};
    }}

    /* ---------- ALERTS ---------- */

    [data-testid="stAlert"] {{
        border-radius: 16px;
    }}

    /* ---------- DIVIDER ---------- */

    hr {{
        border-color: {theme["secondary"]};
    }}

    /* ---------- MOBILE ---------- */

    @media (max-width: 768px) {{
        .main .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# ✏️ TEMPLATE DATA
# ============================================================

NAME = "Your Name"
ROLE = "Creative Professional"
LOCATION = "Jakarta, Indonesia"

EMAIL = "hello@example.com"
INSTAGRAM = "@yourusername"
LINKEDIN = "linkedin.com/in/yourusername"
GITHUB = "github.com/yourusername"

ABOUT = """
I'm a curious and creative professional who enjoys turning
ideas into useful, thoughtful and visually pleasing work.
This section is fully editable for your own story.
"""

# ============================================================
# 🧩 PROJECT DATA
# ============================================================

projects = {
    "Bloom — Creative Website": {
        "category": "Web Design",
        "emoji": "🌷",
        "description": (
            "A soft and friendly website concept designed "
            "to present a creative brand."
        ),
        "tools": ["Figma", "UI Design", "Research"],
        "year": "2026"
    },

    "Cloudy — Portfolio Website": {
        "category": "Development",
        "emoji": "☁️",
        "description": (
            "An interactive portfolio concept focused on "
            "clarity, personality and responsive design."
        ),
        "tools": ["Python", "Streamlit", "UI"],
        "year": "2026"
    },

    "Sunny — Data Dashboard": {
        "category": "Data",
        "emoji": "🍋",
        "description": (
            "A simple dashboard concept that transforms "
            "data into an easier visual experience."
        ),
        "tools": ["Python", "Data", "Visualization"],
        "year": "2025"
    },

    "Little Lab — Research Project": {
        "category": "Research",
        "emoji": "🧪",
        "description": (
            "A research project presenting observations, "
            "analysis and findings in a clean format."
        ),
        "tools": ["Research", "Analysis", "Documentation"],
        "year": "2025"
    }
}

# ============================================================
# 🏠 HOME
# ============================================================

if page == "🏠 Home":

    # HEADER
    left, right = st.columns([2.2, 1])

    with left:

        st.caption("✦ HELLO, I'M")

        st.title(f"{NAME} ♡")

        st.subheader(ROLE)

        st.write(
            "I create thoughtful digital experiences, "
            "projects and ideas with a little bit of personality."
        )

        st.write("")

        a, b = st.columns(2)

        with a:
            if st.button(
                "💼 Explore My Work",
                use_container_width=True
            ):
                st.session_state["go_projects"] = True

        with b:
            if st.button(
                "💌 Let's Connect",
                use_container_width=True
            ):
                st.session_state["go_contact"] = True

        st.write("")

        st.caption(
            f"📍 {LOCATION}  ·  ✨ Open to new opportunities"
        )

    with right:

        st.markdown("## 🌷")
        st.markdown("### A little space for ideas")

        st.info(
            "Creative thinking, thoughtful work "
            "and a tiny bit of sparkle. ✦"
        )

        st.success("Currently creating something lovely ♡")

    st.divider()

    # STATS
    st.markdown("### ✿ A few numbers")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Projects", "12+")

    with c2:
        st.metric("Skills", "15+")

    with c3:
        st.metric("Certificates", "05")

    with c4:
        st.metric("Experience", "2+ yrs")

    st.write("")

    # FEATURED PROJECT
    st.markdown("### 🌷 Featured Project")

    fp1, fp2 = st.columns([1, 2])

    with fp1:
        st.markdown("## 🌸")
        st.markdown("### Bloom")

        st.caption("Featured · Web Design")

    with fp2:

        st.write(
            "A clean and playful digital experience "
            "designed to make a brand feel approachable "
            "while maintaining a professional identity."
        )

        st.write("")

        st.write(
            "🎨 Visual Design   ·   🧠 Research   ·   💻 Web"
        )

        if st.button(
            "See Project Details →",
            key="featured_project"
        ):
            st.session_state["selected_project"] = (
                "Bloom — Creative Website"
            )
            st.session_state["page_override"] = "💼 Projects"

    st.divider()

    # MINI ABOUT
    st.markdown("### ♡ A little about me")

    about1, about2 = st.columns([2, 1])

    with about1:
        st.write(ABOUT)

    with about2:
        st.info(
            "🌱 Always learning\n\n"
            "✨ Always creating\n\n"
            "♡ Always improving"
        )

# ============================================================
# 🌷 ABOUT
# ============================================================

elif page == "🌷 About":

    st.caption("✦ GET TO KNOW ME")

    st.title("A little about me 🌷")

    st.write(
        "Every portfolio needs a little story behind "
        "the work."
    )

    st.divider()

    c1, c2 = st.columns([1.5, 1])

    with c1:

        st.subheader(f"Hi, I'm {NAME}! 🧸")

        st.write(ABOUT)

        st.write(
            "I enjoy working on projects where creativity, "
            "problem solving and attention to detail "
            "come together."
        )

    with c2:

        st.info(
            "### ♡ My values\n\n"
            "🌱 Continuous learning\n\n"
            "🎯 Purposeful work\n\n"
            "🤝 Good collaboration\n\n"
            "✨ Attention to detail"
        )

    st.write("")
    st.divider()

    st.subheader("What I enjoy ✿")

    a, b, c = st.columns(3)

    with a:
        st.info(
            "### 🎨 Creativity\n\n"
            "Exploring ideas and turning them "
            "into meaningful experiences."
        )

    with b:
        st.success(
            "### 💻 Technology\n\n"
            "Using digital tools to solve problems "
            "and build useful things."
        )

    with c:
        st.warning(
            "### 🌱 Learning\n\n"
            "Continuously developing skills through "
            "projects and new experiences."
        )

# ============================================================
# 💼 PROJECTS
# ============================================================

elif page == "💼 Projects":

    st.caption("✦ SELECTED WORK")

    st.title("Projects I'm proud of 🦋")

    st.write(
        "Choose a project to explore its details."
    )

    st.divider()

    # CATEGORY FILTER
    categories = ["All"]

    for data in projects.values():

        if data["category"] not in categories:
            categories.append(data["category"])

    selected_category = st.selectbox(
        "Filter projects",
        categories
    )

    filtered_projects = projects

    if selected_category != "All":

        filtered_projects = {
            name: data
            for name, data in projects.items()
            if data["category"] == selected_category
        }

    # PROJECT SELECTOR
    project_names = list(filtered_projects.keys())

    selected_project = st.selectbox(
        "Select a project",
        project_names
    )

    data = filtered_projects[selected_project]

    st.write("")

    left, right = st.columns([1, 2])

    with left:

        st.markdown(f"## {data['emoji']}")

        st.metric(
            "Year",
            data["year"]
        )

        st.metric(
            "Category",
            data["category"]
        )

    with right:

        st.subheader(selected_project)

        st.write(data["description"])

        st.write("")

        st.markdown("**Tools & skills**")

        for tool in data["tools"]:
            st.write(f"✦ {tool}")

        st.write("")

        if st.button(
            "♡ Mark as Favorite",
            key="favorite"
        ):

            st.success(
                "Project added to your favorites! ✨"
            )

    st.divider()

    st.subheader("All projects")

    for name, item in filtered_projects.items():

        with st.expander(
            f"{item['emoji']}  {name}"
        ):

            st.write(item["description"])

            st.caption(
                f"{item['category']} · {item['year']}"
            )

            st.write(
                " · ".join(item["tools"])
            )

# ============================================================
# 🧰 SKILLS
# ============================================================

elif page == "🧰 Skills":

    st.caption("✦ MY TOOLBOX")

    st.title("Skills & abilities 🎀")

    st.write(
        "A quick overview of the skills I use "
        "across my projects."
    )

    st.divider()

    skill_category = st.selectbox(
        "Choose a skill category",
        [
            "Creative",
            "Technical",
            "Professional"
        ]
    )

    skill_sets = {

        "Creative": {
            "Visual Design": 88,
            "Creative Thinking": 92,
            "Content Creation": 80,
            "Storytelling": 82
        },

        "Technical": {
            "Python": 80,
            "Data Analysis": 84,
            "Web Development": 76,
            "Research": 88
        },

        "Professional": {
            "Communication": 90,
            "Teamwork": 92,
            "Project Management": 80,
            "Problem Solving": 89
        }
    }

    selected_skills = skill_sets[skill_category]

    left, right = st.columns(2)

    items = list(selected_skills.items())

    for index, (skill, value) in enumerate(items):

        target = left if index % 2 == 0 else right

        with target:

            st.markdown(f"**{skill}**")

            st.progress(value / 100)

            st.caption(f"{value}%")

            st.write("")

    st.divider()

    st.subheader("Tools I like ✿")

    tools = [
        "Python",
        "Streamlit",
        "Excel",
        "Figma",
        "Canva",
        "GitHub",
        "Notion"
    ]

    selected_tools = st.multiselect(
        "Select tools",
        tools,
        default=["Python", "Streamlit"]
    )

    if selected_tools:

        st.success(
            "Selected: " + " · ".join(selected_tools)
        )

# ============================================================
# 📖 EXPERIENCE
# ============================================================

elif page == "📖 Experience":

    st.caption("✦ MY JOURNEY")

    st.title("Experience & education 🌱")

    st.write(
        "A simple timeline of important experiences."
    )

    st.divider()

    experiences = [

        (
            "2026 — Now",
            "Current Experience",
            "Your Company / Organization",
            "Describe your current position, internship "
            "or responsibility."
        ),

        (
            "2024 — 2026",
            "Education",
            "Your University",
            "Add your major, achievements and activities."
        ),

        (
            "2024",
            "First Big Project",
            "Personal / Academic",
            "Describe an important project or milestone."
        )
    ]

    for year, title, place, description in experiences:

        st.markdown(f"### 🌷 {title}")

        st.caption(f"{year} · {place}")

        st.write(description)

        st.divider()

    st.subheader("Certificates ✨")

    certs = [
        "Professional Training",
        "Workshop Certificate",
        "Course Completion",
        "Achievement Certificate"
    ]

    for cert in certs:

        st.write(f"🎀 {cert}")

# ============================================================
# 💌 CONTACT
# ============================================================

elif page == "💌 Contact":

    st.caption("✦ LET'S CONNECT")

    st.title("Let's create something lovely 💌")

    st.write(
        "Have a project, collaboration or just want "
        "to say hello? Send a message."
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Find me online 🌷")

        st.write(f"📧 {EMAIL}")
        st.write(f"📸 {INSTAGRAM}")
        st.write(f"💼 {LINKEDIN}")
        st.write(f"💻 {GITHUB}")

        st.write("")

        st.info(
            "Replace these placeholders with "
            "your actual contact information."
        )

    with right:

        st.subheader("Send a message ♡")

        name = st.text_input(
            "Name",
            placeholder="Your name"
        )

        email = st.text_input(
            "Email",
            placeholder="hello@example.com"
        )

        message = st.text_area(
            "Message",
            placeholder="Tell me something nice..."
        )

        if st.button(
            "💌 Send Message",
            use_container_width=True
        ):

            if name and email and message:

                st.success(
                    f"Thank you, {name}! "
                    "Your message is ready to be sent. 🌷"
                )

            else:

                st.warning(
                    "Please complete all fields first ♡"
                )

    st.write("")
    st.divider()

    st.markdown("### 🌸 Thank you for visiting!")

    st.write(
        "Made with curiosity, creativity and a little sparkle. ✨"
    )

# ============================================================
# FOOTER
# ============================================================

st.write("")
st.write("")
st.divider()

footer_left, footer_right = st.columns(2)

with footer_left:
    st.caption("🌷 Lumi Folio · Cute Professional Template")

with footer_right:
    st.caption("Made with ♡ using Streamlit")
