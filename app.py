import os
import io
import re
import base64
from pathlib import Path

import duckdb
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image

# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CareLens AI — Healthcare Intelligence & Analytics Platform",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# 2. LOAD OPENROUTER API KEY
# ============================================================

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    try:
        API_KEY = st.secrets["OPENROUTER_API_KEY"]
    except Exception:
        API_KEY = None

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

TEXT_MODEL = "openrouter/free"
VISION_MODEL = "openrouter/free"

if API_KEY:
    client = OpenAI(
        base_url=OPENROUTER_BASE_URL,
        api_key=API_KEY,
    )
else:
    client = None

# ============================================================
# 3. CUSTOM CSS + ANIMATIONS
# ============================================================

st.markdown(
    """
    <style>
    /* =========================================================
       CARELENS AI — FULL APP MOTION SYSTEM
       ========================================================= */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --navy: #063b73;
        --blue: #0a58a8;
        --cyan: #54d8ff;
        --mint: #79e6b3;
        --green: #164f35;
        --sky: #eaf8ff;
        --white: rgba(255,255,255,.88);
        --line: rgba(10,88,168,.16);
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 8% 12%, rgba(84,216,255,.20), transparent 23%),
            radial-gradient(circle at 92% 8%, rgba(121,230,179,.17), transparent 22%),
            radial-gradient(circle at 50% 100%, rgba(10,88,168,.09), transparent 30%),
            #eaf8ff;
        background-attachment: fixed;
        overflow-x: hidden;
    }

    /* ---------- animated ambient grid ---------- */
    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 0;
        opacity: .22;
        background-image:
            linear-gradient(rgba(10,88,168,.07) 1px, transparent 1px),
            linear-gradient(90deg, rgba(10,88,168,.07) 1px, transparent 1px);
        background-size: 42px 42px;
        mask-image: linear-gradient(to bottom, black, transparent 82%);
        animation: gridMove 18s linear infinite;
    }

    @keyframes gridMove {
        from { transform: translateY(0); }
        to { transform: translateY(42px); }
    }

    .main .block-container {
        position: relative;
        z-index: 1;
        padding-top: 1.2rem;
        padding-bottom: 2.5rem;
        max-width: 1450px;
    }

    h1, h2, h3 {
        color: var(--navy) !important;
        letter-spacing: -.02em;
    }

    /* ---------- floating ambient orbs ---------- */
    .stApp::after {
        content: "";
        position: fixed;
        width: 320px;
        height: 320px;
        right: -100px;
        top: 35%;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(84,216,255,.15), transparent 68%);
        pointer-events: none;
        z-index: 0;
        animation: orbFloat 8s ease-in-out infinite;
    }

    @keyframes orbFloat {
        0%,100% { transform: translate(0,0) scale(1); }
        50% { transform: translate(-45px,55px) scale(1.12); }
    }

    /* ---------- HERO ---------- */
    .app-title {
        position: relative;
        isolation: isolate;
        overflow: hidden;
        padding: 27px 30px 24px;
        margin: 4px 0 24px;
        border-radius: 22px;
        border: 5px solid rgba(10,88,168,.25);
        background:
            linear-gradient(120deg,
                rgba(255,255,255,.92),
                rgba(215,247,255,.90),
                rgba(224,255,241,.88));
        box-shadow:
            0 18px 55px rgba(0,71,130,.13),
            inset 0 1px 0 rgba(255,255,255,.9);
        animation: heroEnter .9s cubic-bezier(.2,.8,.2,1) both,
                   heroBreath 5s ease-in-out 1s infinite;
    }

    .app-title::before {
        content: "";
        position: absolute;
        width: 190px;
        height: 190px;
        border-radius: 50%;
        right: -55px;
        top: -90px;
        background: radial-gradient(circle, rgba(84,216,255,.34), transparent 68%);
        animation: heroOrb 7s ease-in-out infinite;
        z-index: -1;
    }

    .app-title::after {
        content: "";
        position: absolute;
        top: -25%;
        left: -35%;
        width: 22%;
        height: 150%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,.75), transparent);
        transform: skewX(-20deg);
        animation: heroSweep 5.5s ease-in-out infinite;
    }

    .app-title h1 {
        margin: 0;
        font-size: clamp(28px, 3vw, 43px);
        color: var(--navy) !important;
        font-weight: 800;
        position: relative;
        z-index: 2;
    }

    .app-title p {
        margin: 9px 0 0;
        color: red;
        font-size: 20px;
        font-weight: 600;
        position: relative;
        z-index: 2;
    }

    @keyframes heroEnter {
        from { opacity:0; transform: translateY(-24px) scale(.98); }
        to { opacity:1; transform: translateY(0) scale(1); }
    }

    @keyframes heroBreath {
        0%,100% { box-shadow: 0 18px 55px rgba(0,71,130,.13); }
        50% { box-shadow: 0 22px 65px rgba(10,88,168,.20); }
    }

    @keyframes heroOrb {
        0%,100% { transform: translate(0,0) scale(1); }
        50% { transform: translate(-35px,45px) scale(1.35); }
    }

    @keyframes heroSweep {
        0%, 58% { left:-35%; }
        82%,100% { left:120%; }
    }

    /* ---------- status strip ---------- */
    .status-strip {
        display:flex;
        align-items:center;
        justify-items:center;
        gap:10px;
        width:max-content;
        max-width:100%;
        margin: -5px 0 22px 365px;
        padding: 8px 14px;
        border-radius:999px;
        background:rgba(255,255,255,.72);
        border:1px solid rgba(10,88,168,.13);
        box-shadow:0 8px 25px rgba(0,71,130,.08);
        animation: fadeUp .7s .25s both;
    }

    .status-dot {
        width:9px;
        height:9px;
        border-radius:50%;
        background:#2fce75;
        box-shadow:0 0 0 0 rgba(47,206,117,.5);
        animation:pulseDot 1.8s infinite;
    }

    .status-text {
        font-size:12px;
        font-weight:700;
        color:var(--green);
    }

    @keyframes pulseDot {
        0% { box-shadow:0 0 0 0 rgba(47,206,117,.5); }
        70% { box-shadow:0 0 0 9px rgba(47,206,117,0); }
        100% { box-shadow:0 0 0 0 rgba(47,206,117,0); }
    }

    /* ---------- tabs ---------- */
    div[data-baseweb="tab-list"] {
        gap: 8px;
        padding: 7px;
        border-radius: 16px;
        background: rgba(255,255,255,.68);
        border:1px solid rgba(10,88,168,.13);
        box-shadow:0 8px 25px rgba(0,71,130,.07);
        animation: fadeUp .65s .35s both;
    }

    button[data-baseweb="tab"] {
        position:relative;
        border-radius:11px !important;
        padding:10px 16px !important;
        font-weight:700 !important;
        transition: transform .25s ease, background .25s ease, color .25s ease;
    }

    button[data-baseweb="tab"]:hover {
        transform:translateY(-2px);
        background:rgba(84,216,255,.13);
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background:linear-gradient(135deg, #d8f7ff, #e3fff0) !important;
        color:var(--navy) !important;
        box-shadow:0 6px 18px rgba(10,88,168,.10);
    }

    /* ---------- sections ---------- */
    .section-card {
        position:relative;
        overflow:hidden;
        background:rgba(255,255,255,.86);
        backdrop-filter:blur(12px);
        border:1px solid var(--line);
        border-radius:18px;
        padding:19px;
        margin:10px 0;
        box-shadow:0 10px 30px rgba(0,71,130,.08);
        animation: cardEnter .65s cubic-bezier(.2,.8,.2,1) both;
        transition:transform .3s ease, box-shadow .3s ease, border-color .3s ease;
    }

    .section-card::before {
        content:"";
        position:absolute;
        left:-100%;
        top:0;
        width:60%;
        height:2px;
        background:linear-gradient(90deg,transparent,var(--cyan),transparent);
        animation: cardLine 4s ease-in-out infinite;
    }

    .section-card:hover {
        transform:translateY(-4px);
        border-color:rgba(10,88,168,.30);
        box-shadow:0 18px 42px rgba(0,71,130,.13);
    }

    @keyframes cardEnter {
        from { opacity:0; transform:translateY(18px); }
        to { opacity:1; transform:translateY(0); }
    }

    @keyframes cardLine {
        0%,35% { left:-100%; }
        75%,100% { left:140%; }
    }

    /* ---------- insight cards ---------- */
    .insight-card {
        position:relative;
        overflow:hidden;
        background:linear-gradient(135deg, rgba(248,255,242,.96), rgba(239,255,248,.94));
        border-left:6px solid var(--green);
        border-radius:14px;
        padding:15px 18px;
        margin:9px 0;
        box-shadow:0 7px 22px rgba(22,79,53,.07);
        animation: insightIn .6s cubic-bezier(.2,.8,.2,1) both;
        transition:transform .25s ease, box-shadow .25s ease;
    }

    .insight-card::after {
        content:"";
        position:absolute;
        width:80px;
        height:80px;
        right:-25px;
        top:-25px;
        border-radius:50%;
        background:rgba(121,230,179,.15);
        animation: insightOrb 4s ease-in-out infinite;
    }

    .insight-card:hover {
        transform:translateX(6px);
        box-shadow:0 12px 28px rgba(22,79,53,.12);
    }

    @keyframes insightIn {
        from { opacity:0; transform:translateX(-25px); }
        to { opacity:1; transform:translateX(0); }
    }

    @keyframes insightOrb {
        0%,100% { transform:scale(.8); }
        50% { transform:scale(1.35); }
    }

    .warning-card {
        background:linear-gradient(135deg, #fffaf0, #fff8df);
        border-left:6px solid #d89b00;
        border-radius:14px;
        padding:14px 18px;
        margin:10px 0;
        box-shadow:0 8px 25px rgba(216,155,0,.08);
        animation: warningIn .65s both;
    }

    @keyframes warningIn {
        from { opacity:0; transform:scale(.98); }
        to { opacity:1; transform:scale(1); }
    }

    /* ---------- metrics ---------- */
    [data-testid="stMetric"] {
        position:relative;
        overflow:hidden;
        background:rgba(255,255,255,.90);
        backdrop-filter:blur(10px);
        border:1px solid rgba(10,88,168,.15);
        padding:15px;
        border-radius:15px;
        box-shadow:0 8px 25px rgba(0,71,130,.07);
        animation:metricIn .65s cubic-bezier(.2,.8,.2,1) both;
        transition:transform .28s ease, box-shadow .28s ease, border-color .28s ease;
    }

    [data-testid="stMetric"]::before {
        content:"";
        position:absolute;
        width:110px;
        height:110px;
        right:-65px;
        top:-65px;
        border-radius:50%;
        background:radial-gradient(circle, rgba(84,216,255,.24), transparent 68%);
        animation:metricGlow 3.5s ease-in-out infinite;
    }

    [data-testid="stMetric"]:hover {
        transform:translateY(-6px) scale(1.012);
        border-color:rgba(10,88,168,.32);
        box-shadow:0 17px 36px rgba(0,71,130,.15);
    }

    [data-testid="stMetricLabel"] {
        color:var(--green) !important;
        font-weight:700;
    }

    [data-testid="stMetricValue"] {
        color:var(--navy) !important;
        font-weight:800;
    }

    @keyframes metricIn {
        from { opacity:0; transform:translateY(25px) scale(.96); }
        to { opacity:1; transform:translateY(0) scale(1); }
    }

    @keyframes metricGlow {
        0%,100% { transform:scale(.8); opacity:.55; }
        50% { transform:scale(1.3); opacity:1; }
    }

    /* ---------- buttons ---------- */
    .stButton > button {
        position:relative;
        overflow:hidden;
        background:linear-gradient(135deg,#9cff3b,#c6ff82);
        color:blue;
        border-radius:10px;
        border:3px solid black;
        font-weight:bolder;
        min-height:43px;
        padding:8px 18px;
        box-shadow:0 7px 18px rgba(22,51,0,.10);
        transition:transform .2s ease, box-shadow .2s ease, filter .2s ease;
        padding:21px;
        margin:0px 0px 0px 450px;
        width:230px;
        height:30px;
    }

    .stButton > button::after {
        content:"";
        position:absolute;
        top:-50%;
        left:-70%;
        width:35%;
        height:200%;
        transform:rotate(22deg);
        background:rgba(255,255,255,.65);
        animation:buttonShine 4.5s ease-in-out infinite;
    }

    .stButton > button:hover {
        transform:translateY(-3px) scale(1.015);
        box-shadow:0 12px 25px rgba(22,51,0,.17);
        filter:saturate(1.08);
    }

    .stButton > button:active {
        transform:translateY(1px) scale(.985);
    }

    @keyframes buttonShine {
        0%,65% { left:-70%; }
        90%,100% { left:140%; }
    }

    /* ---------- uploaders ---------- */
    [data-testid="stFileUploader"] {
        animation:uploadIn .7s both;
    }

    [data-testid="stFileUploader"] section {
        border:2px dashed rgba(10,88,168,.28) !important;
        border-radius:17px !important;
        background:rgba(255,255,255,.66) !important;
        transition:border-color .3s ease, background .3s ease, transform .3s ease, box-shadow .3s ease;
    }

    [data-testid="stFileUploader"] section:hover {
        border-color:#0a58a8 !important;
        background:rgba(255,255,255,.90) !important;
        transform:translateY(-3px);
        box-shadow:0 13px 32px rgba(0,71,130,.11);
    }

    @keyframes uploadIn {
        from { opacity:0; transform:translateY(15px); }
        to { opacity:1; transform:translateY(0); }
    }

    /* ---------- expanders ---------- */
    details[data-testid="stExpander"] {
        overflow:hidden;
        border:1px solid rgba(10,88,168,.14);
        border-radius:14px;
        margin:9px 0;
        background:rgba(255,255,255,.68);
        animation:fadeUp .55s both;
        transition:border-color .25s ease, box-shadow .25s ease, transform .25s ease;
    }

    details[data-testid="stExpander"]:hover {
        border-color:rgba(10,88,168,.30);
        box-shadow:0 10px 27px rgba(0,71,130,.09);
        transform:translateY(-2px);
    }

    /* ---------- images ---------- */
    [data-testid="stImage"] {
        border-radius:14px;
        overflow:hidden;
        animation:imageEnter .7s both;
        transition:transform .35s ease, filter .35s ease, box-shadow .35s ease;
    }

    [data-testid="stImage"]:hover {
        transform:translateY(-6px) scale(1.012);
        filter:brightness(1.025) saturate(1.04);
        box-shadow:0 18px 38px rgba(0,71,130,.15);
    }

    @keyframes imageEnter {
        from { opacity:0; transform:translateY(22px) scale(.98); }
        to { opacity:1; transform:translateY(0) scale(1); }
    }

    /* ---------- dataframe ---------- */
    [data-testid="stDataFrame"] {
        border-radius:14px;
        overflow:hidden;
        animation:fadeUp .65s both;
        box-shadow:0 8px 25px rgba(0,71,130,.06);
    }

    /* ---------- inputs ---------- */
    [data-baseweb="input"], [data-baseweb="select"] {
        transition:box-shadow .25s ease, transform .25s ease;
    }

    [data-baseweb="input"]:focus-within,
    [data-baseweb="select"]:focus-within {
        box-shadow:0 0 0 3px rgba(84,216,255,.18) !important;
        transform:translateY(-1px);
    }

    /* ---------- sidebar ---------- */
    section[data-testid="stSidebar"] {
        border-right:1px solid rgba(10,88,168,.13);
        background:
            linear-gradient(180deg, rgba(238,250,255,.94), rgba(247,255,250,.94));
    }

    section[data-testid="stSidebar"] > div {
        animation:sidebarIn .7s both;
    }

    @keyframes sidebarIn {
        from { opacity:0; transform:translateX(-14px); }
        to { opacity:1; transform:translateX(0); }
    }

    /* ---------- alerts ---------- */
    [data-testid="stAlert"] {
        border-radius:13px;
        animation:fadeUp .55s both;
    }

    /* ---------- status/loading ---------- */
    [data-testid="stStatusWidget"] {
        border-radius:13px;
        animation:aiPulse 1.7s ease-in-out infinite;
    }

    @keyframes aiPulse {
        0%,100% { box-shadow:0 0 0 rgba(10,88,168,0); }
        50% { box-shadow:0 0 24px rgba(10,88,168,.16); }
    }

    /* ---------- markdown animation ---------- */
    .element-container {
        animation:contentReveal .5s ease both;
    }

    @keyframes contentReveal {
        from { opacity:.65; transform:translateY(4px); }
        to { opacity:1; transform:translateY(0); }
    }

    @keyframes fadeUp {
        from { opacity:0; transform:translateY(13px); }
        to { opacity:1; transform:translateY(0); }
    }

    /* ---------- footer ---------- */
    .carelens-footer {
        text-align:center;
        padding:18px;
        margin-top:22px;
        color:#4d6b5a;
        font-size:13px;
        animation:fadeUp .8s both;
    }

    .carelens-footer .heartbeat {
        display:inline-block;
        animation:heartbeat 1.4s ease-in-out infinite;
    }

    @keyframes heartbeat {
        0%, 35%, 60%, 100% { transform:scale(1); }
        15%, 45% { transform:scale(1.22); }
    }

    /* ---------- reduced motion ---------- */
    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration:.01ms !important;
            animation-iteration-count:1 !important;
            transition-duration:.01ms !important;
            scroll-behavior:auto !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# 4. SESSION STATE
# ============================================================

if "dataframes" not in st.session_state:
    st.session_state.dataframes = {}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "dashboard_results" not in st.session_state:
    st.session_state.dashboard_results = []

# ============================================================
# 5. HELPER FUNCTIONS
# ============================================================

def require_api_key():
    if not API_KEY or not client:
        st.error(
            "OPENROUTER_API_KEY is missing. Add it to your .env file or "
            "Streamlit secrets."
        )
        st.code("OPENROUTER_API_KEY=sk-or-v1-your-key-here")
        return False
    return True


def call_text_ai(prompt, system_prompt=None, temperature=0.2):
    """Call OpenRouter for a normal text request."""
    if not require_api_key():
        return None

    messages = []

    if system_prompt:
        messages.append(
            {
                "role": "system",
                "content": system_prompt,
            }
        )

    messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    try:
        response = client.chat.completions.create(
            model=TEXT_MODEL,
            messages=messages,
            temperature=temperature,
        )

        return response.choices[0].message.content

    except Exception as e:
        st.error(f"AI request failed: {e}")
        return None


def clean_sql(text):
    """Remove Markdown code fences if the AI returns them."""
    if not text:
        return ""

    text = text.strip()
    text = re.sub(r"^```sql\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    return text.strip()


def is_safe_sql(sql):
    """Allow only read-only SELECT queries."""
    if not sql:
        return False

    normalized = re.sub(r"\s+", " ", sql.strip().lower())

    if not normalized.startswith("select"):
        return False

    forbidden = [
        "insert ",
        "update ",
        "delete ",
        "drop ",
        "alter ",
        "create ",
        "truncate ",
        "replace ",
        "merge ",
        "attach ",
        "copy ",
        "export ",
        "install ",
        "load ",
        "pragma ",
        "call ",
    ]

    return not any(word in normalized for word in forbidden)


def dataframe_schema():
    """Create a compact schema description for the AI."""
    if not st.session_state.dataframes:
        return "No datasets have been uploaded."

    sections = []

    for table_name, df in st.session_state.dataframes.items():
        columns = []

        for col in df.columns:
            dtype = str(df[col].dtype)
            columns.append(f"{col} ({dtype})")

        sample = df.head(3).to_dict(orient="records")

        sections.append(
            f"""
TABLE: {table_name}
ROWS: {len(df)}
COLUMNS:
{", ".join(columns)}

SAMPLE ROWS:
{sample}
"""
        )

    return "\n".join(sections)


def execute_sql(sql):
    """Execute read-only SQL against the uploaded dataframes."""
    conn = duckdb.connect(database=":memory:")

    try:
        for table_name, df in st.session_state.dataframes.items():
            conn.register(table_name, df)

        result = conn.execute(sql).df()
        return result

    finally:
        conn.close()


def format_dataframe_for_ai(df, max_rows=100):
    """Convert a result dataframe into compact text."""
    if df is None or df.empty:
        return "The query returned no rows."

    preview = df.head(max_rows)
    return preview.to_string(index=False)


def resize_image_for_ai(image_bytes, max_dimension=1600, quality=85):
    """
    Resize/compress dashboard screenshots so very large screenshots
    don't create unnecessarily large API requests.
    """
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    width, height = image.size
    largest = max(width, height)

    if largest > max_dimension:
        scale = max_dimension / largest
        new_size = (
            max(1, int(width * scale)),
            max(1, int(height * scale)),
        )
        image = image.resize(new_size, Image.LANCZOS)

    output = io.BytesIO()
    image.save(output, format="JPEG", quality=quality, optimize=True)

    return output.getvalue()


def analyze_dashboard_image(image_bytes, filename):
    """Send one Power BI screenshot to a vision-capable OpenRouter model."""
    if not require_api_key():
        return None

    try:
        compressed = resize_image_for_ai(image_bytes)

        encoded = base64.b64encode(compressed).decode("utf-8")
        image_url = f"data:image/jpeg;base64,{encoded}"

        prompt = """
You are a business intelligence analyst reviewing a Power BI healthcare
dashboard screenshot.

Analyze ONLY what is visible in the screenshot.

Give the answer in very simple, easy-to-understand business language.

Your response must contain these sections:

### 1. Dashboard Overview
Explain in 2-3 sentences what the dashboard is showing.

### 2. Important KPIs
List the most important KPI values that are clearly visible.
Do not invent or estimate values.

### 3. Key Insights
Give 4-7 meaningful insights from the charts.
Focus on:
- patient/encounter volume
- costs
- encounter types
- procedures
- unusual peaks or drops
- dominant categories
- important comparisons

### 4. Business Meaning
Explain why the insights matter to a hospital manager or business analyst.

### 5. Recommendations
Give 3-5 practical recommendations based only on the visible data.

### 6. One-Line Summary
Give one strong executive summary sentence.

Important rules:
- Do NOT invent data.
- If a value is unclear, say that it is unclear.
- Do not make medical diagnoses.
- Do not claim causation unless the dashboard actually supports it.
- Clearly distinguish what the chart shows from interpretation.
"""

        content = [
            {
                "type": "text",
                "text": prompt,
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                },
            },
        ]

        response = client.chat.completions.create(
            model=VISION_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content

    except Exception as e:
        st.error(f"Could not analyze {filename}: {e}")
        return None


def combine_dashboard_insights(results):
    """Create one executive summary from multiple screenshot analyses."""
    if not results:
        return None

    combined_text = "\n\n".join(
        [
            f"SCREENSHOT: {filename}\n{analysis}"
            for filename, analysis in results
        ]
    )

    prompt = f"""
You are a senior healthcare BI analyst.

Below are AI analyses of multiple Power BI dashboard screenshots.

Create a concise overall management summary.

Focus on:
1. Most important KPIs
2. Biggest volume trends
3. Biggest cost trends
4. Important encounter/procedure patterns
5. Potential operational concerns
6. 5 practical recommendations

Use simple language.

Do not invent information that is not present in the supplied analyses.

SOURCE ANALYSES:
{combined_text}
"""

    return call_text_ai(
        prompt,
        system_prompt=(
            "You are a healthcare business intelligence analyst. "
            "Be concise, factual and easy to understand."
        ),
        temperature=0.2,
    )


def generate_dataset_summary():
    """Generate an AI summary of all uploaded datasets."""
    if not st.session_state.dataframes:
        return None

    schema = dataframe_schema()

    prompt = f"""
Analyze these uploaded healthcare datasets.

DATASET INFORMATION:
{schema}

Give a simple business-oriented summary with:

1. What data is available
2. Important volume metrics
3. Important cost/revenue metrics if available
4. Interesting patterns
5. Potential data-quality issues
6. 5 useful business questions that can be answered with this data

Do not invent information.
"""

    return call_text_ai(
        prompt,
        system_prompt=(
            "You are a healthcare data analyst. "
            "Explain analytics concepts in simple language."
        ),
    )


def generate_sql(question):
    """Ask AI to convert a natural-language question into DuckDB SQL."""
    schema = dataframe_schema()

    prompt = f"""
You are an expert SQL data analyst.

The user asks:
{question}

Available healthcare tables:
{schema}

Generate ONE read-only DuckDB SQL query.

Rules:
- Return ONLY SQL.
- The query must start with SELECT.
- Do not use INSERT, UPDATE, DELETE, DROP, ALTER, CREATE or other write operations.
- Use only the tables and columns shown above.
- Use DuckDB SQL syntax.
- If the user asks for a percentage, calculate it correctly.
- If the user asks for top/bottom records, use ORDER BY and LIMIT.
- If dates are available, use appropriate date functions.
- Prefer clear column aliases.
"""

    answer = call_text_ai(
        prompt,
        system_prompt=(
            "You generate safe, read-only DuckDB SQL for uploaded healthcare data."
        ),
        temperature=0,
    )

    return clean_sql(answer)


def explain_query_result(question, sql, result_df):
    """Turn SQL output into an easy business explanation."""
    result_text = format_dataframe_for_ai(result_df)

    prompt = f"""
The user asked:

{question}

SQL used:

{sql}

SQL result:

{result_text}

Explain the answer in simple business language.

Include:
- Direct answer
- Important numbers
- What the result means
- One useful business insight

Do not invent values that are not in the result.
"""

    return call_text_ai(
        prompt,
        system_prompt=(
            "You are a business analyst explaining SQL results to a non-technical manager."
        ),
    )


# ============================================================
# 6. HEADER
# ============================================================

st.markdown(
    """
    <div class="app-title">
        <center>
            <h1>🏥 CareLens AI — Healthcare Intelligence & Analytics Platform</h1>
        </center>
        <center>
            <p>
               Upload . Ask . Analyze . Discover Insights
            </p>
        </center>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="status-strip">
        <span class="status-dot"></span>
        <span class="status-text">CareLens AI • Analytics Engine Ready • Healthcare Intelligence Workspace</span>
    </div>
    """,
    unsafe_allow_html=True,
)

if not API_KEY:
    st.warning(
        "⚠️ OpenRouter API key not detected. Add OPENROUTER_API_KEY to your .env file."
    )

# ============================================================
# 7. SIDEBAR
# ============================================================

with st.sidebar:
    st.header("⚙️ Project Controls")

    st.markdown(
        """
        **Recommended healthcare tables**
        - patients
        - encounters
        - procedures
        - payers
        - organizations
        """
    )

    if st.session_state.dataframes:
        st.success(
            f"{len(st.session_state.dataframes)} dataset(s) loaded."
        )

        for table_name, df in st.session_state.dataframes.items():
            st.write(f"• `{table_name}` — {len(df):,} rows")

    st.divider()

    if st.button("🗑️ Clear All Data", use_container_width=True):
        st.session_state.dataframes = {}
        st.session_state.chat_history = []
        st.session_state.dashboard_results = []
        st.rerun()

    st.divider()

    st.markdown(
        """
        **AI models**

        Text: `openrouter/free`

        Vision: `openrouter/free`
        """
    )

# ============================================================
# 8. MAIN TABS
# ============================================================

tab1, tab2, tab3 = st.tabs(
    [
        "📂 Data Upload & Insights",
        "🤖 Ask AI",
        "📊 Power BI Insights",
    ]
)

# ============================================================
# TAB 1 — DATA UPLOAD
# ============================================================

with tab1:
    st.header("📂 Upload Healthcare Files")

    st.markdown(
        """
        """
    )

    uploaded_files = st.file_uploader(
        "Upload one or more CSV files",
        type=["csv"],
        accept_multiple_files=True,
        help="Example: patients.csv, encounters.csv, procedures.csv, payers.csv",
    )

    if uploaded_files:
        for uploaded_file in uploaded_files:
            table_name = Path(uploaded_file.name).stem.lower()

            table_name = re.sub(r"[^a-zA-Z0-9_]", "_", table_name)

            try:
                raw_bytes = uploaded_file.getvalue()

                try:
                    df = pd.read_csv(io.BytesIO(raw_bytes))
                except UnicodeDecodeError:
                    df = pd.read_csv(
                        io.BytesIO(raw_bytes),
                        encoding="latin1",
                    )

                st.session_state.dataframes[table_name] = df

            except Exception as e:
                st.error(
                    f"Could not read {uploaded_file.name}: {e}"
                )

    if st.session_state.dataframes:
        st.subheader("📌 Loaded Datasets")

        for table_name, df in st.session_state.dataframes.items():
            with st.expander(
                f"📄 {table_name} — {len(df):,} rows × {len(df.columns):,} columns",
                expanded=False,
            ):
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Rows", f"{len(df):,}")

                with col2:
                    st.metric("Columns", f"{len(df.columns):,}")

                with col3:
                    st.metric(
                        "Missing Values",
                        f"{int(df.isna().sum().sum()):,}",
                    )

                st.dataframe(
                    df.head(100),
                    use_container_width=True,
                )

        st.divider()

        st.subheader("🤖 AI Dataset Summary")

        if st.button(
            "Generate AI Insights",
            key="generate_dataset_summary",
            use_container_width=True,
        ):
            with st.spinner("Analyzing your healthcare datasets..."):
                summary = generate_dataset_summary()

            if summary:
                st.markdown(
                    f"""
                    <div class="section-card">
                        {summary}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    else:
        st.info(
            "👆 Upload your CSV files to start analyzing the healthcare data."
        )

# ============================================================
# TAB 2 — ASK AI ABOUT DATA
# ============================================================

with tab2:
    st.header("🤖 Ask AI About Your Healthcare Data")

    st.markdown(
        """
        <div class="section-card">
            <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;">
                <div><b>💬 Natural Language</b><br><span class="small-note">Ask a business question</span></div>
                <div style="font-size:24px;">→</div>
                <div><b>🧠 AI</b><br><span class="small-note">Generates SQL</span></div>
                <div style="font-size:24px;">→</div>
                <div><b>🗄️ DuckDB</b><br><span class="small-note">Queries your data</span></div>
                <div style="font-size:24px;">→</div>
                <div><b>📊 Insight</b><br><span class="small-note">Explains the result</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.dataframes:
        st.info(
            "Upload CSV files in the first tab before asking questions."
        )
    else:
        st.markdown(
            """
            Ask questions in normal English. The AI converts your question
            into SQL, runs it against your uploaded data, and explains the result.
            """
        )

        example_questions = [
            "What is the total number of encounters?",
            "Which encounter class has the highest number of encounters?",
            "What is the total claim cost by payer?",
            "Which procedures are performed most frequently?",
            "What is the average encounter cost?",
            "Which year had the highest number of encounters?",
            "What are the top 5 most expensive procedures?",
        ]

        selected_example = st.selectbox(
            "Example question",
            ["-- Select an example --"] + example_questions,
        )

        question = st.text_input(
            "Ask your own question",
            value=(
                ""
                if selected_example == "-- Select an example --"
                else selected_example
            ),
            placeholder="Example: Which payer has the highest total claim cost?",
        )

        if st.button(
            "🔎 Ask AI",
            key="ask_data_ai",
            use_container_width=True,
        ):
            if not question.strip():
                st.warning("Please enter a question.")
            else:
                with st.spinner("Generating SQL and analyzing your data..."):
                    sql = generate_sql(question)

                    if not sql:
                        st.error("The AI could not generate a SQL query.")
                    elif not is_safe_sql(sql):
                        st.error(
                            "The generated query was blocked because it was not "
                            "a safe read-only SELECT query."
                        )
                    else:
                        try:
                            result = execute_sql(sql)

                            explanation = explain_query_result(
                                question,
                                sql,
                                result,
                            )

                            st.session_state.chat_history.append(
                                {
                                    "question": question,
                                    "sql": sql,
                                    "result": result,
                                    "explanation": explanation,
                                }
                            )

                        except Exception as e:
                            st.error(
                                f"SQL execution failed: {e}"
                            )

        if st.session_state.chat_history:
            for item in reversed(st.session_state.chat_history):
                st.markdown("---")

                st.markdown(
                    f"### 👤 Question\n{item['question']}"
                )

                st.markdown("### 🧠 AI Answer")

                if item["explanation"]:
                    st.markdown(
                        f"""
                        <div class="insight-card">
                            {item["explanation"]}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                with st.expander("🔧 View generated SQL"):
                    st.code(
                        item["sql"],
                        language="sql",
                    )

                st.markdown("### 📊 Query Result")

                st.dataframe(
                    item["result"],
                    use_container_width=True,
                )

# ============================================================
# TAB 3 — POWER BI SCREENSHOT ANALYSIS
# ============================================================

with tab3:
    st.header("📊 AI Power BI Dashboard Insights")

    st.markdown(
        """
        <div class="section-card">
            <div style="display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;text-align:center;">
                <span>📤 <b>Upload</b></span>
                <span style="font-size:22px;">→</span>
                <span>👁️ <b>Vision AI</b></span>
                <span style="font-size:22px;">→</span>
                <span>🔎 <b>Detect Trends</b></span>
                <span style="font-size:22px;">→</span>
                <span>💡 <b>Business Insights</b></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        Upload screenshots of your Power BI dashboards. AI will read the
        visible KPIs, charts and trends and explain them in simple business language.
        """
    )

    st.markdown(
        """
        <div class="warning-card">
            <b>🔐 Privacy note:</b>
            Do not upload screenshots containing real patient names, IDs,
            phone numbers, addresses or other sensitive personal information.
            Use anonymized or synthetic healthcare data.
        </div>
        """,
        unsafe_allow_html=True,
    )

    dashboard_files = st.file_uploader(
        "Upload Power BI dashboard screenshots",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
        key="dashboard_upload",
        help="You can upload multiple dashboard screenshots.",
    )

    if dashboard_files:
        st.subheader("🖼️ Uploaded Dashboards")

        cols = st.columns(min(3, len(dashboard_files)))

        for index, file in enumerate(dashboard_files):
            with cols[index % len(cols)]:
                st.image(
                    file,
                    caption=file.name,
                    use_container_width=True,
                )

        st.divider()

        if st.button(
            "👁️ Analyze Dashboard Screenshots",
            key="analyze_dashboards",
            use_container_width=True,
        ):
            results = []

            for dashboard_file in dashboard_files:
                with st.spinner(
                    f"AI is analyzing {dashboard_file.name}..."
                ):
                    analysis = analyze_dashboard_image(
                        dashboard_file.getvalue(),
                        dashboard_file.name,
                    )

                if analysis:
                    results.append(
                        (
                            dashboard_file.name,
                            analysis,
                        )
                    )

            st.session_state.dashboard_results = results

        if st.session_state.dashboard_results:
            st.subheader("🔍 Individual Dashboard Insights")

            for filename, analysis in st.session_state.dashboard_results:
                with st.expander(
                    f"📊 {filename}",
                    expanded=True,
                ):
                    st.markdown(analysis)

            if len(st.session_state.dashboard_results) > 1:
                st.divider()
                st.subheader("🏥 Overall Dashboard Summary")

                if st.button(
                    "Generate Overall Management Summary",
                    key="combine_dashboard_insights",
                    use_container_width=True,
                ):
                    with st.spinner(
                        "Combining insights from all dashboards..."
                    ):
                        overall = combine_dashboard_insights(
                            st.session_state.dashboard_results
                        )

                    if overall:
                        st.markdown(
                            f"""
                            <div class="section-card">
                                {overall}
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

    else:
        st.info(
            "👆 Upload one or more Power BI screenshots to get AI-generated insights."
        )

# ============================================================
# 9. FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div class="carelens-footer">
        <span class="heartbeat">💙</span>
        <b>CareLens AI</b> • Healthcare Intelligence & Analytics
        <br>
        <span>Data → Insights → Decisions</span>
    </div>
    """,
    unsafe_allow_html=True,
)
