import streamlit as st

# ============================================================
# ANNISA WIDIYASTUTI PUTRI
# Cute Professional Chemical Analysis Portfolio
# ============================================================

st.set_page_config(
    page_title="Annisa | Chemical Analysis",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# THEME DATA
# ============================================================

THEMES = {
    "🍓 Strawberry Milk": {
        "bg": "#FFF5F7",
        "bg2": "#FFE8EE",
        "primary": "#E96B8B",
        "primary_dark": "#C94F70",
        "soft": "#FFE1E9",
        "card": "#FFFFFF",
        "text": "#44363D",
        "muted": "#796B72",
        "accent": "#FFD166",
    },

    "🪻 Lavender Dream": {
        "bg": "#FAF7FD",
        "bg2": "#EEE5F7",
        "primary": "#9A7BB5",
        "primary_dark": "#76548F",
        "soft": "#E9DDF2",
        "card": "#FFFFFF",
        "text": "#443B4B",
        "muted": "#766C7E",
        "accent": "#BDE0FE",
    },

    "🦋 Baby Blue": {
        "bg": "#F4FBFF",
        "bg2": "#DFF3FC",
        "primary": "#5CA9D6",
        "primary_dark": "#397EA8",
        "soft": "#D9F0FC",
        "card": "#FFFFFF",
        "text": "#35414A",
        "muted": "#697780",
        "accent": "#FFD166",
    },

    "🍵 Matcha Garden": {
        "bg": "#F6FBF7",
        "bg2": "#E1F0E4",
        "primary": "#78A77A",
        "primary_dark": "#568359",
        "soft": "#DDEDDD",
        "card": "#FFFFFF",
        "text": "#354239",
        "muted": "#69756B",
        "accent": "#F4D58D",
    }
}

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🌷 Annisa's Folio")

    st.caption(
        "Chemical Analysis · R&D · Laboratory"
    )

    st.divider()

    theme_name = st.selectbox(
        "🎨 Change portfolio theme",
        list(THEMES.keys())
    )

    theme = THEMES[theme_name]

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "👩🏻‍🔬 About Me",
            "🧪 Projects",
            "🔬 Laboratory Skills",
            "🌱 Experience",
            "🏅 Certifications",
            "💌 Contact"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.caption(
        "Made with ♡ by Annisa"
    )

# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* =========================
       BACKGROUND
       ========================= */

    .stApp {{
        background:
            radial-gradient(
                circle at 5% 5%,
                {theme["bg2"]} 0px,
                transparent 240px
            ),
            radial-gradient(
                circle at 95% 15%,
                {theme["soft"]} 0px,
                transparent 280px
            ),
            linear-gradient(
                135deg,
                {theme["bg"]},
                #FFFFFF
            );
        color: {theme["text"]};
    }}

    .main .block-container {{
        max-width: 1120px;
        padding-top: 30px;
        padding-bottom: 70px;
    }}

    /* =========================
       TEXT
       ========================= */

    h1, h2, h3, h4 {{
        color: {theme["text"]} !important;
    }}

    p, li {{
        color: {theme["text"]};
        line-height: 1.75;
    }}

    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {{
        background:
            linear-gradient(
                180deg,
                {theme["card"]},
                {theme["bg"]}
            );
        border-right: 1px solid {theme["soft"]};
    }}

    /* =========================
       BUTTON
       ========================= */

    .stButton > button {{
        border-radius: 16px;
        border: 1px solid {theme["primary"]};
        background: {theme["primary"]};
        color: white;
        font-weight: 700;
        min-height: 43px;
        transition: all .2s ease;
    }}

    .stButton > button:hover {{
        background: {theme["primary_dark"]};
        border-color: {theme["primary_dark"]};
        color: white;
        transform: translateY(-1px);
    }}

    /* =========================
       METRIC
       ========================= */

    [data-testid="stMetric"] {{
        background: {theme["card"]};
        border: 1px solid {theme["soft"]};
        border-radius: 20px;
        padding: 18px;
        box-shadow: 0 5px 18px rgba(60,50,60,.05);
    }}

    [data-testid="stMetricValue"] {{
        color: {theme["primary"]};
    }}

    /* =========================
       INPUT
       ========================= */

    .stTextInput input,
    .stTextArea textarea {{
        border-radius: 14px;
        border: 1px solid {theme["soft"]};
        background: white;
    }}

    [data-baseweb="select"] > div {{
        border-radius: 14px;
        border: 1px solid {theme["soft"]};
    }}

    /* =========================
       PROGRESS
       ========================= */

    .stProgress > div > div > div > div {{
        background: {theme["primary"]};
    }}

    /* =========================
       ALERTS
       ========================= */

    [data-testid="stAlert"] {{
        border-radius: 16px;
    }}

    /* =========================
       DIVIDER
       ========================= */

    hr {{
        border-color: {theme["soft"]};
    }}

    /* =========================
       MOBILE
       ========================= */

    @media (max-width: 768px) {{
        .main .block-container {{
            padding-left: 18px;
            padding-right: 18px;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# PERSONAL DATA
# ============================================================

NAME = "Annisa Widiyastuti Putri"

ROLE = "Chemical Analysis Student"

LOCATION = "Bogor, Indonesia"

EDUCATION = "Politeknik AKA Bogor"

MAJOR = "Analis Kimia"

CURRENT_ROLE = "R&D Laboratory Intern"

COMPANY = "PT ADEV Natural Indonesia"

EMAIL = "your-email@example.com"
LINKEDIN = "linkedin.com/in/yourusername"
GITHUB = "github.com/yourusername"

# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    left, right = st.columns([1.65, 1])

    with left:

        st.caption("✦ CHEMICAL ANALYSIS × R&D")

        st.title(
            "Annisa Widiyastuti Putri ♡"
        )

        st.subheader(
            "Chemical Analysis Student"
        )

        st.write(
            "Mahasiswi Analis Kimia yang memiliki ketertarikan "
            "pada analisis laboratorium, R&D, quality control, "
            "dan pengembangan produk."
        )

        st.write("")

        st.caption(
            "📍 Bogor, Indonesia"
        )

        st.write("")

        if st.button(
            "🧪 Explore My Portfolio",
            use_container_width=True
        ):

            st.success(
                "Welcome to my little laboratory world! 🌷"
            )

    with right:

        st.markdown("## 🧪")

        st.markdown(
            "### Research, analysis & curiosity"
        )

        st.info(
            "Currently learning and gaining hands-on "
            "experience in an R&D laboratory environment."
        )

        st.success(
            "♡ Always learning, always improving."
        )

    st.write("")
    st.divider()

    # STATS

    st.markdown("### ✿ Quick Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Education",
            "2024–Now"
        )

    with c2:
        st.metric(
            "Current Role",
            "R&D Intern"
        )

    with c3:
        st.metric(
            "Laboratory",
            "R&D"
        )

    with c4:
        st.metric(
            "Location",
            "Bogor"
        )

    st.write("")
    st.divider()

    # FEATURED

    st.markdown("### 🌷 Currently Learning")

    f1, f2 = st.columns([1, 2])

    with f1:

        st.markdown("## 🧴")

        st.subheader(
            "Product Formulation"
        )

        st.caption(
            "R&D Laboratory"
        )

    with f2:

        st.write(
            "Dalam kegiatan PKL di PT ADEV Natural Indonesia, "
            "saya mendapatkan pengalaman langsung dalam proses "
            "pembuatan dan pengujian formulasi skincare."
        )

        st.write(
            "Beberapa aktivitas yang dipelajari meliputi "
            "preparasi sampel, penimbangan bahan, pembuatan "
            "emulsi lotion menggunakan multimix, pengukuran "
            "pH dan viskositas, penggunaan centrifuge, serta "
            "dokumentasi dan input data."
        )

# ============================================================
# ABOUT
# ============================================================

elif page == "👩🏻‍🔬 About Me":

    st.caption("✦ GET TO KNOW ME")

    st.title("A little about me 🌷")

    st.write(
        "Perjalanan saya sebagai mahasiswa Analis Kimia "
        "dimulai dari rasa ingin tahu terhadap dunia "
        "laboratorium dan proses analisis."
    )

    st.divider()

    left, right = st.columns([1.4, 1])

    with left:

        st.subheader(
            "Hello, I'm Annisa! 🧪"
        )

        st.write(
            """
            Saya merupakan mahasiswi Program Studi Analis Kimia
            di Politeknik AKA Bogor.

            Saya tertarik pada kegiatan laboratorium,
            analisis kimia, R&D, quality control, serta
            pengembangan dan pengujian produk.

            Selama perkuliahan dan kegiatan praktik, saya
            mempelajari berbagai teknik analisis dan
            preparasi sampel yang menjadi dasar untuk
            pengembangan kemampuan profesional saya.
            """
        )

    with right:

        st.info(
            """
            ### ♡ My Focus

            🧪 Laboratory Analysis

            🔬 Research & Development

            📋 Quality Control

            🧴 Product Formulation

            📊 Laboratory Documentation
            """
        )

    st.write("")
    st.divider()

    st.subheader("What describes me? ✿")

    a, b, c = st.columns(3)

    with a:

        st.info(
            """
            ### 🌱 Curious

            Suka mempelajari hal baru,
            terutama yang berkaitan dengan
            pekerjaan laboratorium.
            """
        )

    with b:

        st.success(
            """
            ### 🔎 Detail-oriented

            Terbiasa memperhatikan proses,
            data dan dokumentasi dalam
            kegiatan praktikum.
            """
        )

    with c:

        st.warning(
            """
            ### 🤝 Collaborative

            Memiliki pengalaman dalam
            organisasi, kepanitiaan dan
            kerja sama tim.
            """
        )

# ============================================================
# PROJECTS
# ============================================================

elif page == "🧪 Projects":

    st.caption("✦ MY PRACTICAL WORK")

    st.title("Projects & Laboratory Experience 🧪")

    st.write(
        "Beberapa kegiatan dan project yang merepresentasikan "
        "pengalaman akademik serta praktik laboratorium saya."
    )

    st.divider()

    projects = {

        "🧴 Lotion Emulsion Formulation": {
            "category": "R&D",
            "description":
                "Mempelajari proses pembuatan emulsi lotion "
                "meliputi fase minyak, fase air, bahan aktif, "
                "fungsi bahan, penggunaan multimix, serta "
                "pengaruh kondisi proses terhadap pembentukan emulsi.",
            "skills":
                "Formulation · Emulsion · Multimix · pH · Viscosity"
        },

        "🧪 Iodometric Analysis": {
            "category": "Chemical Analysis",
            "description":
                "Mempelajari analisis secara iodometri sebagai "
                "bagian dari pengalaman analisis kimia dan "
                "penerapan prinsip titrasi dalam laboratorium.",
            "skills":
                "Titration · Standardization · Calculation"
        },

        "🔬 Instrumental Analysis": {
            "category": "Instrumentation",
            "description":
                "Memiliki pengalaman pembelajaran terkait "
                "instrumen analisis seperti UV-Vis, FTIR, "
                "AAS/SSA, GC, HPLC dan TLC.",
            "skills":
                "UV-Vis · FTIR · AAS · GC · HPLC · TLC"
        },

        "📋 Laboratory Documentation": {
            "category": "Documentation",
            "description":
                "Melakukan pencatatan dan input data hasil "
                "penimbangan maupun pengujian menggunakan "
                "spreadsheet serta mempelajari dokumentasi "
                "kegiatan laboratorium.",
            "skills":
                "Excel · Data Entry · Documentation"
        }
    }

    category = st.selectbox(
        "Filter project",
        [
            "All",
            "R&D",
            "Chemical Analysis",
            "Instrumentation",
            "Documentation"
        ]
    )

    if category == "All":

        filtered = projects

    else:

        filtered = {
            key: value
            for key, value in projects.items()
            if value["category"] == category
        }

    st.write("")

    selected_project = st.selectbox(
        "Choose a project to explore",
        list(filtered.keys())
    )

    project = filtered[selected_project]

    left, right = st.columns([1, 2])

    with left:

        st.markdown(
            f"# {selected_project.split(' ')[0]}"
        )

        st.metric(
            "Category",
            project["category"]
        )

    with right:

        st.subheader(
            selected_project
        )

        st.write(
            project["description"]
        )

        st.write("")

        st.markdown("**Skills involved**")

        st.success(
            project["skills"]
        )

    st.divider()

    st.subheader("All projects")

    for title, data in filtered.items():

        with st.expander(title):

            st.write(
                data["description"]
            )

            st.caption(
                data["skills"]
            )

# ============================================================
# LABORATORY SKILLS
# ============================================================

elif page == "🔬 Laboratory Skills":

    st.caption("✦ TECHNICAL SKILLS")

    st.title("Laboratory & Technical Skills 🔬")

    st.write(
        "Kemampuan yang saya pelajari melalui perkuliahan, "
        "praktikum dan pengalaman PKL."
    )

    st.divider()

    skill_category = st.selectbox(
        "Choose a category",
        [
            "Basic Laboratory",
            "Physical & Chemical Analysis",
            "Instrumentation",
            "Documentation"
        ]
    )

    if skill_category == "Basic Laboratory":

        skills = [
            "Sample preparation",
            "Weighing",
            "Pipetting",
            "Solution preparation",
            "Dissolution",
            "Dilution"
        ]

    elif skill_category == "Physical & Chemical Analysis":

        skills = [
            "Titration",
            "pH measurement",
            "Viscosity measurement",
            "Iodometric analysis",
            "Standardization",
            "Laboratory calculations"
        ]

    elif skill_category == "Instrumentation":

        skills = [
            "UV-Vis",
            "FTIR",
            "AAS / SSA",
            "GC",
            "HPLC",
            "TLC"
        ]

    else:

        skills = [
            "Excel / Spreadsheet",
            "Laboratory documentation",
            "Data entry",
            "SOP reading",
            "Sample coding",
            "Data recording"
        ]

    for skill in skills:

        st.write(
            f"♡ {skill}"
        )

    st.divider()

    st.subheader(
        "Current PKL skills 🌷"
    )

    current_skills = [
        "Multimix",
        "pH Meter",
        "Viscosity",
        "Centrifuge",
        "Lotion Emulsion",
        "Sample Preparation"
    ]

    selected = st.multiselect(
        "Select the skills you want to highlight",
        current_skills,
        default=current_skills[:3]
    )

    if selected:

        st.success(
            "Highlighted: " +
            " · ".join(selected)
        )

# ============================================================
# EXPERIENCE
# ============================================================

elif page == "🌱 Experience":

    st.caption("✦ MY JOURNEY")

    st.title("Experience & Education 🌱")

    st.divider()

    st.subheader(
        "🧴 R&D Laboratory Intern"
    )

    st.caption(
        "PT ADEV Natural Indonesia · Bogor"
    )

    st.write(
        """
        Saat ini menjalani PKL di bagian Research &
        Development Laboratory pada perusahaan maklon
        skincare.

        Kegiatan yang dilakukan antara lain preparasi dan
        pencarian sampel, penimbangan bahan, pembuatan
        emulsi lotion, penggunaan multimix, pengukuran pH
        dan viskositas, penggunaan centrifuge, input data,
        serta mempelajari fungsi bahan dan proses formulasi.
        """
    )

    st.divider()

    st.subheader(
        "🎓 Chemical Analysis Student"
    )

    st.caption(
        "Politeknik AKA Bogor · 2024 — Present"
    )

    st.write(
        """
        Menempuh pendidikan di bidang Analis Kimia dengan
        pembelajaran mengenai analisis kimia, preparasi
        sampel, analisis instrumental, titrasi, validasi
        metode dan sistem mutu laboratorium.
        """
    )

    st.divider()

    st.subheader(
        "🤝 Organization & Committee Experience"
    )

    st.write(
        """
        Memiliki pengalaman dalam kegiatan organisasi dan
        kepanitiaan kampus yang melatih kemampuan komunikasi,
        koordinasi, administrasi, teamwork dan tanggung jawab.
        """
    )

    st.write("")

    a, b, c = st.columns(3)

    with a:
        st.info("📣 Public Relations")

    with b:
        st.success("🤝 Coordination")

    with c:
        st.warning("📋 Administration")

# ============================================================
# CERTIFICATIONS
# ============================================================

elif page == "🏅 Certifications":

    st.caption("✦ TRAINING & CERTIFICATIONS")

    st.title("Certifications & Training 🏅")

    st.write(
        "Pelatihan yang mendukung pemahaman saya terhadap "
        "quality, food safety dan sistem kerja industri."
    )

    st.divider()

    certifications = [
        (
            "GMP",
            "Good Manufacturing Practices"
        ),
        (
            "HACCP",
            "Hazard Analysis and Critical Control Point"
        ),
        (
            "ISO 22000:2018",
            "Food Safety Management System"
        ),
        (
            "FSSC 22000 Version 6.0",
            "Food Safety System Certification"
        ),
        (
            "QA & QC in Food Industry",
            "Quality Assurance & Quality Control"
        ),
        (
            "HACCP Documentation",
            "Penyusunan Dokumen HACCP"
        )
    ]

    for title, description in certifications:

        with st.expander(
            f"🎀 {title}"
        ):

            st.write(description)

    st.divider()

    st.info(
        "Additional training can be added here as your "
        "professional portfolio grows. ✨"
    )

# ============================================================
# CONTACT
# ============================================================

elif page == "💌 Contact":

    st.caption("✦ LET'S CONNECT")

    st.title("Let's connect ♡")

    st.write(
        "I'm always open to learning, collaboration and "
        "new professional opportunities."
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Find me online 🌷")

        st.write(
            f"📧 {EMAIL}"
        )

        st.write(
            f"💼 {LINKEDIN}"
        )

        st.write(
            f"💻 {GITHUB}"
        )

        st.write("")

        st.info(
            "Replace the placeholder contact information "
            "with your actual accounts."
        )

    with right:

        st.subheader("Send a message 💌")

        visitor_name = st.text_input(
            "Name"
        )

        visitor_email = st.text_input(
            "Email"
        )

        visitor_message = st.text_area(
            "Message"
        )

        if st.button(
            "Send Message ♡",
            use_container_width=True
        ):

            if (
                visitor_name
                and visitor_email
                and visitor_message
            ):

                st.success(
                    f"Thank you, {visitor_name}! 🌷"
                )

            else:

                st.warning(
                    "Please complete all fields first."
                )

# ============================================================
# FOOTER
# ============================================================

st.write("")
st.divider()

left, right = st.columns(2)

with left:

    st.caption(
        "🧪 Annisa Widiyastuti Putri · Chemical Analysis"
    )

with right:

    st.caption(
        "Made with ♡ · Politeknik AKA Bogor"
    )
