import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Annisa Widiyastuti Putri | Portfolio",
    page_icon="🌷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# THEME
# =========================================================

THEMES = {
    "🍓 Strawberry Milk": {
        "bg": "#FFE8EF",
        "bg2": "#FFD1DE",
        "primary": "#E85D7A",
        "primary_dark": "#C94766",
        "soft": "#FFC4D3",
        "card": "#FFFFFF",
        "text": "#49343D",
        "muted": "#78646C",
        "accent": "#FFD166"
    },

    "🪻 Lavender Dream": {
        "bg": "#EEE5FA",
        "bg2": "#DCC9EF",
        "primary": "#9470B7",
        "primary_dark": "#735296",
        "soft": "#D3BCE8",
        "card": "#FFFFFF",
        "text": "#44364F",
        "muted": "#71657A",
        "accent": "#BDE0FE"
    },

    "🦋 Baby Blue": {
        "bg": "#DFF3FF",
        "bg2": "#C2E9FA",
        "primary": "#4D9CCB",
        "primary_dark": "#357DA8",
        "soft": "#B5E0F5",
        "card": "#FFFFFF",
        "text": "#35434C",
        "muted": "#687780",
        "accent": "#FFD166"
    },

    "🍵 Matcha Garden": {
        "bg": "#E4F3E5",
        "bg2": "#CBE6CE",
        "primary": "#6F9E72",
        "primary_dark": "#527A55",
        "soft": "#BBD8BE",
        "card": "#FFFFFF",
        "text": "#344239",
        "muted": "#68746A",
        "accent": "#F4D58D"
    }
}

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🌷 Annisa's Portfolio")
    st.caption("Chemical Analysis Student")

    st.divider()

    theme_name = st.selectbox(
        "🎨 Pilih tema",
        list(THEMES.keys())
    )

    theme = THEMES[theme_name]

    st.divider()

    page = st.radio(
        "📌 Navigasi",
        [
            "🏠 Home",
            "👩🏻‍🔬 About Me",
            "🧴 PKL Experience",
            "🧪 Laboratory Skills",
            "🎓 Education & Organization",
            "📜 Certifications",
            "💌 Contact"
        ]
    )

    st.divider()

    st.caption("Made with ♡ using Streamlit")


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {theme["bg"]};

        background-image:
            radial-gradient(
                circle at 0% 0%,
                {theme["primary"]}55 0px,
                transparent 300px
            ),
            radial-gradient(
                circle at 100% 10%,
                {theme["accent"]}70 0px,
                transparent 350px
            ),
            radial-gradient(
                circle at 80% 80%,
                {theme["primary"]}35 0px,
                transparent 400px
            ),
            linear-gradient(
                135deg,
                {theme["bg"]} 0%,
                {theme["bg2"]} 50%,
                {theme["bg"]} 100%
            );

        background-attachment: fixed;
    }}

    [data-testid="stAppViewContainer"] {{
        background: transparent !important;
    }}

    [data-testid="stMain"] {{
        background: transparent !important;
    }}

    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    .main {{
        background: transparent !important;
    }}

    .main .block-container {{
        max-width: 1120px;
        padding-top: 30px;
        padding-bottom: 80px;
        background: transparent !important;
    }}

    section[data-testid="stSidebar"] {{
        background:
            linear-gradient(
                180deg,
                {theme["primary"]}18,
                {theme["bg2"]},
                {theme["card"]}
            );

        border-right: 2px solid {theme["primary"]}35;
    }}

    h1, h2, h3, h4 {{
        color: {theme["text"]} !important;
    }}

    p, li {{
        color: {theme["text"]};
        line-height: 1.75;
    }}

    .stButton > button {{
        border-radius: 16px;
        border: 2px solid {theme["primary"]};
        background: {theme["primary"]};
        color: white;
        font-weight: 800;
        min-height: 45px;
        box-shadow: 0 7px 20px {theme["primary"]}45;
    }}

    .stButton > button:hover {{
        background: {theme["primary_dark"]};
        border-color: {theme["primary_dark"]};
        color: white;
        transform: translateY(-2px);
    }}

    [data-testid="stMetric"] {{
        background: {theme["card"]};
        border: 2px solid {theme["primary"]}35;
        border-radius: 22px;
        padding: 20px;
        box-shadow: 0 10px 25px rgba(60,50,60,.07);
    }}

    [data-testid="stMetricValue"] {{
        color: {theme["primary"]} !important;
    }}

    [data-testid="stAlert"] {{
        border-radius: 20px !important;
        border-width: 2px !important;
    }}

    .stTextInput input,
    .stTextArea textarea {{
        background: white !important;
        border: 2px solid {theme["primary"]}30 !important;
        border-radius: 16px !important;
    }}

    [data-baseweb="select"] > div {{
        background: white !important;
        border: 2px solid {theme["primary"]}30 !important;
        border-radius: 16px !important;
    }}

    .stProgress > div > div > div > div {{
        background: {theme["primary"]} !important;
    }}

    hr {{
        border-color: {theme["primary"]}35 !important;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.title("🌷 Annisa Widiyastuti Putri")

    st.subheader("Mahasiswi Analis Kimia | R&D Laboratory Intern")

    st.write(
        "Halo! Saya Annisa, mahasiswi Analis Kimia di Politeknik AKA Bogor "
        "yang memiliki ketertarikan pada kegiatan laboratorium, analisis kimia, "
        "dan pengembangan pengetahuan di bidang kosmetik."
    )

    st.info(
        "🧪 Saat ini saya sedang menjalani PKL di laboratorium Research & Development "
        "PT ADEV Natural Indonesia."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🎓 Pendidikan", "Analis Kimia")

    with col2:
        st.metric("🧪 Bidang", "Laboratorium R&D")

    with col3:
        st.metric("📍 Lokasi", "Bogor")

    st.divider()

    st.subheader("✨ Tentang Portfolio Ini")

    st.write(
        "Portfolio ini berisi gambaran singkat mengenai latar belakang pendidikan, "
        "pengalaman PKL, keterampilan laboratorium, kegiatan organisasi, serta "
        "pelatihan yang pernah saya ikuti."
    )

    st.success(
        "🌱 Saya terus belajar dan mengembangkan kemampuan melalui pengalaman "
        "akademik, organisasi, dan praktik laboratorium."
    )


# =========================================================
# ABOUT ME
# =========================================================

elif page == "👩🏻‍🔬 About Me":

    st.title("👩🏻‍🔬 About Me")

    st.subheader("Halo, saya Annisa! 🌷")

    st.write(
        "Saya merupakan mahasiswi Program Studi Analis Kimia di Politeknik AKA Bogor. "
        "Saya memiliki ketertarikan terhadap kegiatan laboratorium dan penerapan "
        "ilmu kimia dalam dunia industri."
    )

    st.write(
        "Melalui kegiatan perkuliahan dan PKL, saya berkesempatan mempelajari "
        "berbagai kegiatan laboratorium mulai dari preparasi sampel, penimbangan, "
        "pembuatan larutan, pengujian sifat fisik, hingga pencatatan data."
    )

    st.write(
        "Saya juga tertarik untuk terus meningkatkan ketelitian, kemampuan bekerja "
        "sesuai prosedur, serta kemampuan bekerja sama dalam lingkungan profesional."
    )

    st.divider()

    st.subheader("🌱 Personal Highlights")

    col1, col2 = st.columns(2)

    with col1:
        st.write("🔬 **Ketertarikan**")
        st.write("- Analisis kimia")
        st.write("- Kegiatan laboratorium")
        st.write("- R&D kosmetik")
        st.write("- Mikrobiologi")

    with col2:
        st.write("💡 **Soft Skills**")
        st.write("- Teliti")
        st.write("- Bertanggung jawab")
        st.write("- Komunikasi")
        st.write("- Kerja sama tim")


# =========================================================
# PKL EXPERIENCE
# =========================================================

elif page == "🧴 PKL Experience":

    st.title("🧴 PKL Experience")

    st.subheader("R&D Laboratory Intern")

    st.write("**PT ADEV Natural Indonesia — Bogor**")

    st.caption("2026 • Research & Development Laboratory")

    st.write(
        "Selama menjalani PKL, saya mendapatkan kesempatan untuk mengenal secara "
        "langsung kegiatan laboratorium pada bagian Research & Development (R&D) "
        "di industri kosmetik."
    )

    st.write(
        "Kegiatan yang saya lakukan terutama berupa membantu pelaksanaan pekerjaan "
        "laboratorium dan mempelajari tahapan kerja yang berkaitan dengan preparasi "
        "sampel, penimbangan bahan, pembuatan formulasi, pengujian sifat fisik, "
        "serta pencatatan data."
    )

    st.divider()

    st.subheader("🧪 Kegiatan yang Dipelajari")

    activities = [
        "Preparasi dan pencarian sampel sesuai kebutuhan kegiatan laboratorium",
        "Penimbangan bahan menggunakan timbangan laboratorium",
        "Membantu proses pembuatan emulsi lotion menggunakan multimix",
        "Mempelajari tahapan fase minyak dan fase air dalam pembuatan emulsi",
        "Melakukan pengukuran pH",
        "Melakukan pengujian viskositas",
        "Mempelajari penggunaan centrifuge",
        "Melakukan pencatatan dan input data hasil kegiatan ke spreadsheet",
        "Menjaga kerapian alat, bahan, dan area kerja laboratorium",
        "Mempelajari fungsi bahan dan alat yang digunakan dalam kegiatan R&D"
    ]

    for activity in activities:
        st.write(f"• {activity}")

    st.divider()

    st.subheader("🌱 Hal yang Saya Pelajari")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            "🔬 **Praktik Laboratorium**\n\n"
            "Memahami pentingnya ketelitian dalam penimbangan, preparasi, "
            "pengujian sifat fisik, penggunaan alat, dan pencatatan data."
        )

    with col2:
        st.info(
            "🤝 **Lingkungan Kerja**\n\n"
            "Belajar mengikuti prosedur kerja, menjaga kerapian area laboratorium, "
            "berkomunikasi dengan tim, serta bekerja di bawah arahan pembimbing."
        )

    st.divider()

    st.subheader("🏢 Tentang PT ADEV Natural Indonesia")

    st.write(
        "PT ADEV Natural Indonesia merupakan perusahaan yang bergerak di bidang "
        "jasa maklon kosmetik dan personal care. Berdasarkan informasi pada situs "
        "resminya, ADEV menyediakan layanan yang mencakup formulasi, produksi, "
        "serta layanan pendukung legalitas produk."
    )

    st.write(
        "Dalam proses formulasi, tim R&D berperan dalam pengembangan dan pembuatan "
        "sampel produk sebelum produk dapat masuk ke tahap produksi."
    )

    st.caption(
        "Sumber: PT ADEV Natural Indonesia — Company Profile dan informasi "
        "layanan formulasi."
    )

    st.markdown(
        "🔗 [Company Profile PT ADEV](https://adev.co.id/company/)"
    )

    st.markdown(
        "🔗 [Jasa Formulasi Kosmetik PT ADEV](https://adev.co.id/blog/jasa-formulasi-kosmetik/)"
    )

    st.markdown(
        "🔗 [Proses Maklon Produk Kosmetik PT ADEV](https://adev.co.id/maklon/proses-maklon-kosmetik/)"
    )


# =========================================================
# LABORATORY SKILLS
# =========================================================

elif page == "🧪 Laboratory Skills":

    st.title("🧪 Laboratory Skills")

    st.write(
        "Beberapa keterampilan yang saya pelajari melalui perkuliahan, praktikum, "
        "dan pengalaman PKL."
    )

    st.divider()

    skill_category = st.selectbox(
        "Pilih kategori keterampilan",
        [
            "🧴 Preparasi & Formulasi",
            "⚗️ Analisis Dasar",
            "🔬 Instrumentasi",
            "💻 Dokumentasi & Data"
        ]
    )

    if skill_category == "🧴 Preparasi & Formulasi":

        skills = [
            "Penimbangan bahan",
            "Pipetting",
            "Pelarutan",
            "Pengenceran",
            "Preparasi sampel",
            "Pembuatan emulsi",
            "Penggunaan multimix",
            "Penggunaan centrifuge"
        ]

    elif skill_category == "⚗️ Analisis Dasar":

        skills = [
            "Titrasi",
            "Pengukuran pH",
            "Pengujian viskositas",
            "Perhitungan konsentrasi larutan",
            "Standardisasi larutan"
        ]

    elif skill_category == "🔬 Instrumentasi":

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
            "Pencatatan hasil analisis",
            "Input data menggunakan Microsoft Excel",
            "Dokumentasi kegiatan laboratorium",
            "Pengelolaan data sederhana",
            "Membaca SOP"
        ]

    for skill in skills:
        st.write(f"🩷 {skill}")


# =========================================================
# EDUCATION & ORGANIZATION
# =========================================================

elif page == "🎓 Education & Organization":

    st.title("🎓 Education & Organization")

    st.subheader("📚 Education")

    st.write("**Politeknik AKA Bogor**")
    st.write("Program Studi Analis Kimia")
    st.caption("Angkatan 2024")

    st.divider()

    st.subheader("🤝 Organization & Activities")

    st.write(
        "Selain kegiatan akademik, saya juga aktif dalam kegiatan organisasi "
        "dan kepanitiaan kampus yang membantu saya mengembangkan kemampuan "
        "komunikasi, koordinasi, administrasi, dan kerja sama tim."
    )

    activities = [
        "Lembaga Dakwah Kampus",
        "Humas PPBY",
        "Koordinator kepanitiaan",
        "Wakil Bendahara Donatur PPBY",
        "Mengikuti kegiatan kepanitiaan kampus"
    ]

    for item in activities:
        st.write(f"• {item}")

    st.divider()

    st.subheader("💗 Skills from Organization")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📣 Komunikasi")

    with col2:
        st.info("🤝 Kerja Sama")

    with col3:
        st.info("📋 Koordinasi")


# =========================================================
# CERTIFICATIONS
# =========================================================

elif page == "📜 Certifications":

    st.title("📜 Certifications & Training")

    st.write(
        "Beberapa pelatihan dan sertifikat yang pernah saya ikuti "
        "sebagai bagian dari pengembangan kompetensi."
    )

    certificates = [
        "GMP — Good Manufacturing Practices",
        "HACCP — Hazard Analysis and Critical Control Points",
        "ISO 22000:2018",
        "FSSC 22000 Version 6.0",
        "QA & QC in Food Industry",
        "Penyusunan Dokumen HACCP"
    ]

    for certificate in certificates:
        st.success(f"✓ {certificate}")


# =========================================================
# CONTACT
# =========================================================

elif page == "💌 Contact":

    st.title("💌 Let's Connect!")

    st.write(
        "Terima kasih sudah mengunjungi portfolio saya. "
        "Jika ingin menghubungi saya, silakan melalui kontak berikut."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📧 Email")

        st.markdown(
            "📩 [annisawidiyastuti24@gmail.com](mailto:annisawidiyastuti24@gmail.com)"
        )

        st.subheader("📍 Location")

        st.write("Bogor, Indonesia")

    with col2:

        st.subheader("🔗 LinkedIn")

        st.markdown(
            "💼 [Annisa Widiyastuti Putri]"
            "(https://www.linkedin.com/in/annisa-widiyastuti-putri-373915300/)"
        )

        st.subheader("🎓 Education")

        st.write("Politeknik AKA Bogor")


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "© 2026 Annisa Widiyastuti Putri • Chemical Analysis Student • Made with ♡"
)
