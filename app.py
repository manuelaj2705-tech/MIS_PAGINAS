import streamlit as st

st.set_page_config(page_title="Portafolio IA", layout="wide")

st.markdown("""
<style>
  html, body, [class*="css"], .stApp {
    font-family: Arial, Helvetica, sans-serif !important;
    background-color: #1a1a2e !important;
    color: #e0e0e0 !important;
  }
  #MainMenu, footer, header { visibility: hidden; }

  .block-container {
    padding: 0 !important;
    max-width: 100% !important;
  }

  /* Layout principal */
  .layout {
    display: flex;
    min-height: 100vh;
  }

  /* Sidebar */
  .sidebar {
    width: 220px;
    min-height: 100vh;
    background: #111122;
    border-right: 1px solid #2a2a4a;
    padding: 2.5rem 1.5rem;
    flex-shrink: 0;
  }
  .sidebar h2 {
    font-size: 13px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.4;
    margin-bottom: 1rem;
  }
  .sidebar p {
    font-size: 12px;
    color: #888aaa;
    line-height: 1.7;
  }
  .sidebar-divider {
    border: none;
    border-top: 1px solid #2a2a4a;
    margin: 1.2rem 0;
  }
  .sidebar-nav a {
    display: block;
    font-size: 12px;
    color: #7878aa;
    text-decoration: none;
    padding: 4px 0;
  }
  .sidebar-nav a:hover { color: #ffffff; }

  /* Main */
  .main {
    flex: 1;
    padding: 3rem 3rem 4rem;
  }
  .page-header h1 {
    font-size: 26px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.3;
    margin-bottom: 0.6rem;
  }
  .page-link {
    font-size: 13px;
    color: #888aaa;
    margin-bottom: 2.5rem;
    display: block;
  }
  .page-link a { color: #7b8cff; text-decoration: none; }
  .page-link a:hover { text-decoration: underline; }

  /* Grid */
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
  }

  /* Card */
  .card { display: flex; flex-direction: column; gap: 0.6rem; }
  .card-title {
    font-size: 17px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.3;
  }
  .card-img {
    width: 100%;
    aspect-ratio: 4/3;
    object-fit: cover;
    border: 1px solid #2a2a4a;
    display: block;
  }
  .card-img-placeholder {
    width: 100%;
    aspect-ratio: 4/3;
    background: #222240;
    border: 1px dashed #3a3a6a;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .card-img-placeholder span { font-size: 11px; color: #555577; }
  .card-desc { font-size: 12.5px; color: #9090b0; line-height: 1.6; }
  .card-link { font-size: 12px; color: #9090b0; }
  .card-link a { color: #7b8cff; text-decoration: none; font-weight: 700; }
  .card-link a:hover { text-decoration: underline; }

  @media (max-width: 700px) {
    .layout { flex-direction: column; }
    .sidebar { width: 100%; min-height: auto; }
    .main { padding: 1.5rem 1rem; }
    .grid { grid-template-columns: 1fr; }
  }
</style>
""", unsafe_allow_html=True)

# ── Datos de las apps ──────────────────────────────────────────────────────────
apps = [
    {
        "title": "Vision App",
        "url": "https://visionapp-kprcq5qyohmk25tfgvbqcc.streamlit.app/",
        "img": "img/vision_app.jpg",
        "desc": "Aplicación que usa visión por computadora para analizar imágenes en tiempo real mediante modelos de inteligencia artificial.",
        "label": "Vision App",
    },
    {
        "title": "Chat PDF",
        "url": "https://chatpdf-gzyhln5gmzeasufhkymsrf.streamlit.app/",
        "img": "img/chat_pdf.jpg",
        "desc": "Aplicación RAG que permite cargar un documento PDF y hacerle preguntas directamente usando un modelo de lenguaje.",
        "label": "Chat PDF",
    },
    {
        "title": "Tablero",
        "url": "https://mitablero-37pgfbi27dcveobqybialg.streamlit.app/",
        "img": "img/tablero.jpg",
        "desc": "Dashboard interactivo que visualiza datos en tiempo real con gráficas y métricas para facilitar la toma de decisiones.",
        "label": "Tablero",
    },
    {
        "title": "Reconocimiento Inteligente",
        "url": "https://drawrecog-ockrdwtjmzjkrfmszxkeuk.streamlit.app/",
        "img": "img/draw_recog.jpg",
        "desc": "App que reconoce dibujos trazados a mano usando modelos de clasificación de inteligencia artificial.",
        "label": "Inteligente",
    },
    {
        "title": "Monitor Sensor",
        "url": "https://recepmqtt-6kbfj6gf7btn5mhyilzgdv.streamlit.app/",
        "img": "img/monitor_sensor.jpg",
        "desc": "Monitor de sensores IoT que recibe datos vía protocolo MQTT y los visualiza en tiempo real en un panel de control.",
        "label": "Monitor sensor",
    },
    {
        "title": "Control por Voz",
        "url": "https://ctrlvoice-jwuzn5rmg5bmnkdokphckp.streamlit.app/",
        "img": "img/voice_ctrl.jpg",
        "desc": "Interfaz multimodal que convierte voz a texto y publica los comandos reconocidos en un broker MQTT para controlar dispositivos.",
        "label": "Control por voz",
    },
]

# ── Construir las cards HTML ───────────────────────────────────────────────────
import os
import base64

def img_tag(path, alt):
    """Devuelve <img> embebido en base64 si el archivo existe, si no un placeholder."""
    if os.path.exists(path):
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        ext = path.rsplit(".", 1)[-1].lower()
        mime = "image/jpeg" if ext in ("jpg", "jpeg") else f"image/{ext}"
        return f'<img class="card-img" src="data:{mime};base64,{b64}" alt="{alt}">'
    return f'<div class="card-img-placeholder"><span>{alt}</span></div>'

cards_html = ""
for app in apps:
    img_html = img_tag(app["img"], app["title"])
    cards_html += f"""
    <div class="card">
      <div class="card-title">{app['title']}</div>
      {img_html}
      <p class="card-desc">{app['desc']}</p>
      <div class="card-link">{app['label']}: <a href="{app['url']}" target="_blank">Enlace</a></div>
    </div>
    """

nav_html = ""
for app in apps:
    nav_html += f'<a href="{app["url"]}" target="_blank">{app["title"]}</a>\n'

# ── Render ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="layout">

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <h2>Aplicaciones con Inteligencia Artificial.</h2>
    <hr class="sidebar-divider">
    <p>La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos,
    automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real.</p>
    <hr class="sidebar-divider">
    <nav class="sidebar-nav">
      {nav_html}
    </nav>
  </aside>

  <!-- MAIN -->
  <main class="main">
    <div class="page-header">
      <h1>En el siguiente enlace puedes encontrar páginas y ejercicios prácticos</h1>
    </div>
    <span class="page-link">
      Enlace para páginas y ejercicios:
      <a href="https://visionapp-kprcq5qyohmk25tfgvbqcc.streamlit.app/" target="_blank">Enlace</a>
    </span>

    <div class="grid">
      {cards_html}
    </div>
  </main>

</div>
""", unsafe_allow_html=True)
