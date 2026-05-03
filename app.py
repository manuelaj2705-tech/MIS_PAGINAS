import streamlit as st
import os
import base64

st.set_page_config(page_title="Portafolio IA", layout="wide")

# ── CSS global ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
html, body, [class*="css"], .stApp {
  font-family: Arial, Helvetica, sans-serif !important;
  background-color: #1a1a2e !important;
  color: #e0e0e0 !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] {
  background-color: #111122 !important;
  border-right: 1px solid #2a2a4a !important;
}
section[data-testid="stSidebar"] * {
  font-family: Arial, Helvetica, sans-serif !important;
  color: #9090b0 !important;
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] strong {
  color: #ffffff !important;
  font-size: 13px !important;
  font-weight: 700 !important;
}
section[data-testid="stSidebar"] a {
  color: #7878aa !important;
  text-decoration: none !important;
  font-size: 12px !important;
  display: block;
  padding: 3px 0;
}
section[data-testid="stSidebar"] a:hover { color: #ffffff !important; }
section[data-testid="stSidebar"] hr {
  border-color: #2a2a4a !important;
  margin: 0.8rem 0 !important;
}
.card-title {
  font-size: 17px;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 6px;
}
.card-desc {
  font-size: 12.5px;
  color: #9090b0;
  line-height: 1.6;
  margin: 6px 0;
}
.card-link {
  font-size: 12px;
  color: #9090b0;
}
.card-link a {
  color: #7b8cff !important;
  font-weight: 700;
  text-decoration: none;
}
.page-title {
  font-size: 26px;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.3;
  margin-bottom: 8px;
}
.page-subtitle {
  font-size: 13px;
  color: #888aaa;
  margin-bottom: 2rem;
}
.page-subtitle a { color: #7b8cff; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ── Datos ──────────────────────────────────────────────────────────────────────
apps = [
    {
        "title": "Vision App",
        "url": "https://visionapp-kprcq5qyohmk25tfgvbqcc.streamlit.app/",
        "img": "vision_app.jpg.png",
        "desc": "Analiza imágenes en tiempo real usando visión por computadora e inteligencia artificial.",
        "label": "Vision App",
    },
    {
        "title": "Chat PDF",
        "url": "https://chatpdf-gzyhln5gmzeasufhkymsrf.streamlit.app/",
        "img": "Chatbot.png",
        "desc": "Carga un PDF y hazle preguntas directamente usando un modelo de lenguaje (RAG).",
        "label": "Chat PDF",
    },
    {
        "title": "Tablero",
        "url": "https://mitablero-37pgfbi27dcveobqybialg.streamlit.app/",
        "img": "Tablero.png",
        "desc": "Dashboard interactivo con gráficas y métricas en tiempo real para toma de decisiones.",
        "label": "Tablero",
    },
    {
        "title": "Reconocimiento Inteligente",
        "url": "Corazon.png",
        "img": "img/draw_recog.jpg",
        "desc": "Reconoce dibujos trazados a mano usando modelos de clasificación con IA.",
        "label": "Inteligente",
    },
    {
        "title": "Monitor Sensor",
        "url": "https://recepmqtt-6kbfj6gf7btn5mhyilzgdv.streamlit.app/",
        "img": "img/monitor_sensor.jpg",
        "desc": "Monitor IoT que recibe datos de sensores vía MQTT y los visualiza en tiempo real.",
        "label": "Monitor sensor",
    },
    {
        "title": "Control por Voz",
        "url": "https://ctrlvoice-jwuzn5rmg5bmnkdokphckp.streamlit.app/",
        "img": "img/voice_ctrl.jpg",
        "desc": "Convierte voz a texto y publica comandos vía MQTT para controlar dispositivos.",
        "label": "Control por voz",
    },
]

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("**Aplicaciones con Inteligencia Artificial.**")
    st.markdown("---")
    st.markdown(
        "<p style='font-size:12px;color:#888aaa;line-height:1.7;'>"
        "La inteligencia artificial permite mejorar la toma de decisiones "
        "con el uso de datos, automatizar tareas rutinarias y proporcionar "
        "análisis avanzados en tiempo real.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    for app in apps:
        st.markdown(
            f'<a href="{app["url"]}" target="_blank">{app["title"]}</a>',
            unsafe_allow_html=True,
        )

# ── Encabezado ─────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="page-title">En el siguiente enlace puedes encontrar páginas y ejercicios prácticos</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="page-subtitle">Enlace para páginas y ejercicios: '
    '<a href="https://visionapp-kprcq5qyohmk25tfgvbqcc.streamlit.app/" target="_blank">Enlace</a></div>',
    unsafe_allow_html=True,
)

# ── Helper: imagen en base64 o placeholder ─────────────────────────────────────
def render_image(path, alt):
    if os.path.exists(path):
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        ext = path.rsplit(".", 1)[-1].lower()
        mime = "image/jpeg" if ext in ("jpg", "jpeg") else f"image/{ext}"
        st.markdown(
            f'<img src="data:{mime};base64,{b64}" alt="{alt}" '
            f'style="width:100%;aspect-ratio:4/3;object-fit:cover;'
            f'border:1px solid #2a2a4a;display:block;">',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div style="width:100%;aspect-ratio:4/3;background:#222240;'
            f'border:1px dashed #3a3a6a;display:flex;align-items:center;'
            f'justify-content:center;">'
            f'<span style="font-size:11px;color:#555577;">{alt}</span></div>',
            unsafe_allow_html=True,
        )

# ── Grid 3 columnas ────────────────────────────────────────────────────────────
rows = [apps[i:i+3] for i in range(0, len(apps), 3)]

for row in rows:
    cols = st.columns(3, gap="large")
    for col, app in zip(cols, row):
        with col:
            st.markdown(f'<div class="card-title">{app["title"]}</div>', unsafe_allow_html=True)
            render_image(app["img"], app["title"])
            st.markdown(f'<p class="card-desc">{app["desc"]}</p>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="card-link">{app["label"]}: '
                f'<a href="{app["url"]}" target="_blank">Enlace</a></div>',
                unsafe_allow_html=True,
            )
    st.markdown("<br>", unsafe_allow_html=True)
