import streamlit as st

from auth import (
    sign_up,
    sign_in,
    sign_out,
    get_current_user
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CareLens AI",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOGIN SCREEN
# ============================================================

def authentication_screen():

    # ========================================================
    # CUSTOM CSS
    # ========================================================

    st.markdown(
        """
        <style>

        /* =====================================================
           MAIN PAGE
        ===================================================== */

        .stApp {
            background:
                linear-gradient(
                    135deg,
                    #f8fbff 20%,
                    #eef6ff 45%,
                    #f8fafc 100%
                );

            overflow-x: hidden;
        }


        /* =====================================================
           HIDE DEFAULT STREAMLIT UI
        ===================================================== */

        #MainMenu {
            visibility: hidden;
        }

        header {
            background: transparent !important;
        }

        [data-testid="stHeader"] {
            background: transparent !important;
        }

        footer {
            visibility: hidden;
        }


        /* =====================================================
           MAIN CONTENT
        ===================================================== */

        .block-container {
            max-width: 720px;

            padding-top: 3rem;
            padding-bottom: 3rem;

            position: relative;

            z-index: 10;
        }


        /* =====================================================
           FLOATING CIRCLE 1
        ===================================================== */

        .stApp::before {

            content: "";

            position: fixed;

            width: 300px;
            height: 300px;

            left: -150px;
            top: 8%;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle,
                    rgba(37, 99, 235, 0.18) 0%,
                    rgba(37, 99, 235, 0.09) 35%,
                    rgba(37, 99, 235, 0.03) 60%,
                    transparent 75%
                );

            pointer-events: none;

            z-index: 0;

            animation:
                floatCircleOne 10s ease-in-out infinite;
        }


        /* =====================================================
           FLOATING CIRCLE 2
        ===================================================== */

        .stApp::after {

            content: "";

            position: fixed;

            width: 340px;
            height: 340px;

            right: -170px;
            bottom: 3%;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle,
                    rgba(6, 182, 212, 0.16) 0%,
                    rgba(6, 182, 212, 0.08) 35%,
                    rgba(6, 182, 212, 0.03) 60%,
                    transparent 75%
                );

            pointer-events: none;

            z-index: 0;

            animation:
                floatCircleTwo 13s ease-in-out infinite;
        }


        /* =====================================================
           EXTRA FLOATING CIRCLE
        ===================================================== */

        .brand-container::before {

            content: "";

            position: fixed;

            width: 120px;
            height: 120px;

            right: 16%;
            top: 10%;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle,
                    rgba(99, 102, 241, 0.12),
                    transparent 70%
                );

            pointer-events: none;

            z-index: -1;

            animation:
                floatCircleThree 8s ease-in-out infinite;
        }


        /* =====================================================
           EXTRA FLOATING CIRCLE
        ===================================================== */

        .brand-container::after {

            content: "";

            position: fixed;

            width: 90px;
            height: 90px;

            left: 18%;
            bottom: 12%;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle,
                    rgba(14, 165, 233, 0.11),
                    transparent 70%
                );

            pointer-events: none;

            z-index: -1;

            animation:
                floatCircleFour 11s ease-in-out infinite;
        }


        /* =====================================================
           FLOAT ANIMATIONS
        ===================================================== */

        @keyframes floatCircleOne {

            0%, 100% {
                transform:
                    translate(0px, 0px)
                    scale(1);
            }

            50% {
                transform:
                    translate(35px, -25px)
                    scale(1.04);
            }
        }


        @keyframes floatCircleTwo {

            0%, 100% {
                transform:
                    translate(0px, 0px)
                    scale(1);
            }

            50% {
                transform:
                    translate(-35px, 25px)
                    scale(1.05);
            }
        }


        @keyframes floatCircleThree {

            0%, 100% {
                transform:
                    translate(0px, 0px);
            }

            50% {
                transform:
                    translate(-20px, 25px);
            }
        }


        @keyframes floatCircleFour {

            0%, 100% {
                transform:
                    translate(0px, 0px);
            }

            50% {
                transform:
                    translate(20px, -20px);
            }
        }


        /* =====================================================
           BRAND
        ===================================================== */

        .brand-container {

            text-align: center;

            
            margin-bottom: 30px;

            position: relative;

            z-index: 20;
        }


        /* =====================================================
           LOGO
        ===================================================== */

        .logo {

            width: 68px;
            height: 68px;

            margin:
                0 auto 14px auto;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 18px;

            background:
                linear-gradient(
                    135deg,
                    #2563eb,
                    #0891b2
                );

            color: white;

            font-size: 31px;

            box-shadow:
                0 12px 28px
                rgba(37, 99, 235, 0.22);

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;
        }


        .logo:hover {

            transform:
                translateY(-4px)
                rotate(-2deg)
                scale(1.05);

            box-shadow:
                0 16px 34px
                rgba(37, 99, 235, 0.30);
        }


        /* =====================================================
           BRAND TITLE
        ===================================================== */

        .brand-title {

            margin: 0;

            font-size: 34px;

            font-weight: 800;

            letter-spacing: -1px;

            background:
                linear-gradient(
                    90deg,
                    #1d4ed8,
                    #0891b2
                );

            -webkit-background-clip: text;

            -webkit-text-fill-color: transparent;
        }


        .brand-subtitle {

            margin-top: 7px;

            color: #64748b;

            font-size: 14px;
        }


        /* =====================================================
           FORM CARD
        ===================================================== */

        div[data-testid="stForm"] {

            background:
                rgba(255, 255, 255, 0.95);

            border:
                1px solid #e2e8f0;

            border-radius: 18px;

            padding: 26px;

            box-shadow:
                0 12px 35px
                rgba(15, 23, 42, 0.08);

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;
        }


        div[data-testid="stForm"]:hover {

            transform:
                translateY(-3px);

            box-shadow:
                0 18px 45px
                rgba(15, 23, 42, 0.11);
        }


        /* =====================================================
           INPUTS
        ===================================================== */

        div[data-baseweb="input"] {

            border-radius: 9px !important;

            border:
                1px solid #cbd5e1 !important;

            background:
                #ffffff !important;

            transition:
                border-color 0.2s ease,
                box-shadow 0.2s ease;
        }


        div[data-baseweb="input"]:hover {

            border-color:
                #94a3b8 !important;
        }


        div[data-baseweb="input"]:focus-within {

            border-color:
                #2563eb !important;

            box-shadow:
                0 0 0 3px
                rgba(37, 99, 235, 0.10);
        }


        /* =====================================================
           SUBMIT BUTTON
        ===================================================== */

        .stFormSubmitButton button {

            background:
                linear-gradient(
                    90deg,
                    #2563eb,
                    #0891b2
                ) !important;

            color:
                white !important;

            border:
                none !important;

            border-radius:
                9px !important;

            font-weight:
                600 !important;

            min-height:
                44px;

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease,
                filter 0.2s ease !important;
        }


        .stFormSubmitButton button:hover {

            transform:
                translateY(-2px);

            filter:
                brightness(1.04);

            box-shadow:
                0 9px 22px
                rgba(37, 99, 235, 0.25);
        }


        .stFormSubmitButton button:active {

            transform:
                translateY(0);
        }


        /* =====================================================
           TABS
        ===================================================== */

        button[data-baseweb="tab"] {

            font-weight:
                600;

            color:
                #475569;

            transition:
                color 0.2s ease;
        }


        button[data-baseweb="tab"]:hover {

            color:
                #2563eb;
        }


        /* =====================================================
           SECURITY BOX
        ===================================================== */

        .info-box {

            margin-top:
                22px;

            padding:
                15px 17px;

            background:
                rgba(239, 246, 255, 0.92);

            border:
                1px solid #dbeafe;

            border-radius:
                11px;

            color:
                #334155;

            font-size:
                13px;

            line-height:
                1.5;

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;
        }


        .info-box:hover {

            transform:
                translateY(-2px);

            box-shadow:
                0 7px 20px
                rgba(37, 99, 235, 0.08);
        }


        /* =====================================================
           FEATURE BADGES
        ===================================================== */

        .features {

            display:
                flex;

            justify-content:
                center;

            gap:
                8px;

            flex-wrap:
                wrap;

            margin-top:
                20px;

            position:
                relative;

            z-index:
                20;
        }


        .feature {

            padding:
                7px 12px;

            border-radius:
                20px;

            background:
                rgba(255, 255, 255, 0.90);

            border:
                1px solid #e2e8f0;

            color:
                #64748b;

            font-size:
                11px;

            transition:
                transform 0.2s ease,
                color 0.2s ease,
                border-color 0.2s ease,
                box-shadow 0.2s ease;
        }


        .feature:hover {

            transform:
                translateY(-4px);

            color:
                #2563eb;

            border-color:
                #bfdbfe;

            box-shadow:
                0 7px 18px
                rgba(37, 99, 235, 0.10);
        }


        /* =====================================================
           FOOTER
        ===================================================== */

        .login-footer {

            text-align:
                center;

            margin-top:
                22px;

            color:
                #94a3b8;

            font-size:
                11px;
        }


        /* =====================================================
           SIDEBAR
        ===================================================== */

        section[data-testid="stSidebar"] {

            background:
                #ffffff;

            border-right:
                1px solid #e2e8f0;
        }


        /* Sidebar content */

        section[data-testid="stSidebar"] > div {

            padding-top:
                1.5rem;
        }


        /* Keep sidebar contents within the available sidebar width. */
        section[data-testid="stSidebar"] {
            box-sizing: border-box;
            min-width: 0;
            overflow-x: hidden;
        }

        section[data-testid="stSidebar"] [data-testid="stButton"] {
            min-width: 0;
            max-width: 100%;
            box-sizing: border-box;
        }

        section[data-testid="stSidebar"] [data-testid="stButton"] > button {
            width: 100%;
            max-width: 100%;
            min-width: 0;
            box-sizing: border-box;
            white-space: normal;
            overflow-wrap: anywhere;
        }

        /* =====================================================
           SIDEBAR LOGOUT AREA
        ===================================================== */

        .logout-title {

            color:
                #64748b;

            font-size:
                13px;

            font-weight:
                600;

            margin-bottom:
                8px;
                
        }


        /* =====================================================
           LOGOUT BUTTON
        ===================================================== */

        .logout-button button {

            background:
                #fee2e2 !important;

            color:
                #b91c1c !important;

            border:
                1px solid #fecaca !important;

            border-radius:
                8px !important;

            font-weight:
                600 !important; 

            transition:
                background 0.2s ease,
                border-color 0.2s ease,
                transform 0.2s ease !important;
        }


        .logout-button button:hover {

            background:
                #fecaca !important;

            border-color:
                #fca5a5 !important;

            transform:
                translateY(-1px);
        }


        /* =====================================================
           CLEAR DATA BUTTON
        ===================================================== */

        .clear-button button {

            background:
                #f8fafc !important;

            color:
                #475569 !important;

            border:
                1px solid #cbd5e1 !important;

            border-radius:
                8px !important;

            font-weight:
                500 !important;

            transition:
                background 0.2s ease,
                border-color 0.2s ease,
                transform 0.2s ease !important;
        }


        .clear-button button:hover {

            background:
                #f1f5f9 !important;

            border-color:
                #94a3b8 !important;

            transform:
                translateY(-1px);
        }


        /* =====================================================
           MOBILE
        ===================================================== */

        @media (max-width: 768px) {

            .block-container {

                padding-top:
                    2rem;

                padding-left:
                    1rem;

                padding-right:
                    1rem;
            }


            .brand-title {

                font-size:
                    29px;
            }


            .stApp::before {

                width:
                    190px;

                height:
                    190px;

                left:
                    -110px;
            }


            .stApp::after {

                width:
                    210px;

                height:
                    210px;

                right:
                    -120px;
            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # BRAND
    # ========================================================

    st.title("🩺 CareLens AI")
    st.caption("Healthcare Intelligence & Analytics Platform")

    # ========================================================
    # LOGIN / SIGNUP TABS
    # ========================================================

    login_tab, signup_tab = st.tabs(
        [
            "🔐 Login",
            "Create Account"
        ]
    )


    # ========================================================
    # LOGIN
    # ========================================================

    with login_tab:

        st.markdown("### Welcome back")

        st.caption(
            "Sign in to access your healthcare analytics workspace."
        )

        with st.form("login_form"):

            email = st.text_input(
                "Email",
                placeholder="you@example.com"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            login_button = st.form_submit_button(
                "Sign In",
                use_container_width=True
            )

            if login_button:

                if not email.strip():

                    st.error(
                        "Please enter your email."
                    )

                elif not password:

                    st.error(
                        "Please enter your password."
                    )

                else:

                    try:

                        success = sign_in(
                            email.strip(),
                            password
                        )

                        if success:

                            st.success(
                                "Login successful."
                            )

                            st.rerun()

                        else:

                            st.error(
                                "Invalid email or password."
                            )

                    except Exception:

                        st.error(
                            "Login failed. Please check your credentials and try again."
                        )


    # ========================================================
    # SIGNUP
    # ========================================================

    with signup_tab:

        st.markdown("### Create your account")

        st.caption(
            "Create an account to start exploring healthcare data with AI."
        )

        with st.form("signup_form"):

            signup_email = st.text_input(
                "Email",
                placeholder="you@example.com",
                key="signup_email"
            )

            signup_password = st.text_input(
                "Password",
                type="password",
                placeholder="Minimum 8 characters",
                key="signup_password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                placeholder="Re-enter your password",
                key="confirm_password"
            )

            signup_button = st.form_submit_button(
                "Create Account",
                use_container_width=True
            )

            if signup_button:

                if not signup_email.strip():

                    st.error(
                        "Please enter your email."
                    )

                elif not signup_password:

                    st.error(
                        "Please enter a password."
                    )

                elif len(signup_password) < 8:

                    st.error(
                        "Password must contain at least 8 characters."
                    )

                elif signup_password != confirm_password:

                    st.error(
                        "Passwords do not match."
                    )

                else:

                    try:

                        sign_up(
                            signup_email.strip(),
                            signup_password
                        )

                        st.success(
                            "Account created successfully. "
                            "Check your email if verification is enabled."
                        )

                    except Exception:

                        st.error(
                            "Unable to create account. "
                            "The email may already be registered."
                        )


    # ========================================================
    # SECURITY INFORMATION
    # ========================================================

    st.markdown(
        """
        <div class="info-box">

            🔒 Secure workspace

            Your uploaded data remains isolated within your
            current session. Sensitive information is checked
            before AI analysis.

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # FEATURES
    # ========================================================
    

    

# ============================================================
# CHECK AUTHENTICATION
# ============================================================

current_user = get_current_user()


if not current_user:

    authentication_screen()

    st.stop()


# ============================================================
# GLOBAL SIDEBAR LAYOUT FIX (applies after login too)
st.markdown(
    """
    <style>
    /* Keep sidebar content inside its own width without creating a horizontal bar. */
    /* Do not set the sidebar section width/position: Streamlit must control
       its native collapse animation and let the main page reclaim the space. */
    section[data-testid="stSidebar"] {
        min-width: 0 !important;
    }

    [data-testid="stSidebar"] > div,
    [data-testid="stSidebarContent"],
    [data-testid="stSidebarUserContent"],
    [data-testid="stSidebarUserContent"] > div,
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"],
    [data-testid="stSidebar"] [data-testid="stElementContainer"],
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        box-sizing: border-box !important;
        min-width: 0 !important;
        max-width: 100% !important;
    }

    [data-testid="stSidebarContent"],
    [data-testid="stSidebarUserContent"],
    [data-testid="stSidebarUserContent"] > div {
        overflow-x: hidden !important;
    }

    /* Ensure long email addresses/captions wrap instead of widening the sidebar. */
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        overflow-wrap: anywhere !important;
        word-break: break-word !important;
    }

    /* Both action buttons use the same width and stay aligned to the sidebar edges. */
    [data-testid="stSidebar"] [data-testid="stButton"],
    [data-testid="stSidebar"] [data-testid="stButton"] > div {
        display: block !important;
        width: 100% !important;
        min-width: 0 !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    [data-testid="stSidebar"] [data-testid="stButton"] button {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        min-width: 0 !important;
        max-width: 100% !important;
        margin: 0 !important;
        padding: 0.55rem 0.65rem !important;
        box-sizing: border-box !important;
        white-space: normal !important;
        overflow-wrap: anywhere !important;
        line-height: 1.25 !important;
    }

    /* Hide only horizontal scrollbar tracks; vertical scrolling remains available. */
    [data-testid="stSidebar"] * {
        scrollbar-width: thin;
    }
    [data-testid="stSidebar"] *::-webkit-scrollbar:horizontal {
        height: 0 !important;
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# LOGGED-IN USER SIDEBAR
# ============================================================

with st.sidebar:

    # ========================================================
    # BRAND
    # ========================================================

    st.markdown(
        "## 🩺 CareLens AI"
    )

    st.caption(
        "Healthcare Intelligence Platform"
    )

    st.divider()


    # ========================================================
    # ACCOUNT
    # ========================================================

    st.markdown(
        "### 👤 Account"
    )

    st.write(
        current_user["email"]
    )

    st.divider()


    # ========================================================
    # SESSION INFORMATION
    # ========================================================

    st.markdown(
        "### 📁 Session"
    )

    st.caption(
        "Your uploaded data is stored only in the current session."
    )

    st.divider()


    # ========================================================
    # CLEAR SESSION DATA
    # ========================================================

    st.markdown(
        '<div class="logout-title">Data Management</div>',
        unsafe_allow_html=True
    )

    clear_data_clicked = st.button(
        "🗑️ Clear Session Data",
        use_container_width=True,
        key="clear_session_data"
    )


    if clear_data_clicked:

        data_keys = [
            "dataframes",
            "uploaded_files",
            "uploaded_filenames",
            "chat_history",
            "dashboard_results",
            "db_conn",
            "sensitive_columns",
            "sensitive_columns_by_table"
        ]

        for key in data_keys:

            st.session_state.pop(
                key,
                None
            )

        st.success(
            "Session data cleared."
        )

        st.rerun()


    # ========================================================
    # LOGOUT SECTION
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="logout-title">Account</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # LOGOUT BUTTON
    # ========================================================

    logout_clicked = st.button(
        "🚪 Logout",
        use_container_width=True,
        key="logout_button",
        
    )


    if logout_clicked:

        # ----------------------------------------------------
        # SIGN OUT
        # ----------------------------------------------------

        sign_out()


        # ----------------------------------------------------
        # CLEAR ALL USER SESSION DATA
        # ----------------------------------------------------

        keys_to_clear = [

            "auth_user",

            "dataframes",

            "uploaded_files",

            "uploaded_filenames",

            "chat_history",

            "dashboard_results",

            "db_conn",

            "sensitive_columns",

            "sensitive_columns_by_table"

        ]


        for key in keys_to_clear:

            st.session_state.pop(
                key,
                None
            )


        # ----------------------------------------------------
        # RETURN TO LOGIN
        # ----------------------------------------------------

        st.rerun()


    st.caption(
        "🔐 Logging out clears your session data."
    )

# ----------------------------------------------

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
client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=API_KEY) if API_KEY else None

# ============================================================
# 3. CUSTOM CSS
# ============================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    :root{--navy:#063b73;--blue:#0a58a8;--cyan:#54d8ff;--mint:#79e6b3;--green:#164f35;--line:rgba(10,88,168,.16)}
    html,body,[class*="css"]{font-family:'Inter',sans-serif}
    .stApp{background:radial-gradient(circle at 8% 12%,rgba(84,216,255,.20),transparent 23%),radial-gradient(circle at 92% 8%,rgba(121,230,179,.17),transparent 22%),#eaf8ff;background-attachment:fixed;overflow-x:hidden}
    .stApp::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.18;background-image:linear-gradient(rgba(10,88,168,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(10,88,168,.07) 1px,transparent 1px);background-size:42px 42px;mask-image:linear-gradient(to bottom,black,transparent 82%);animation:gridMove 18s linear infinite}
    @keyframes gridMove{to{transform:translateY(42px)}}
    .main .block-container{position:relative;z-index:1;padding-top:1.2rem;padding-bottom:2.5rem;max-width:1450px}
    h1,h2,h3{color:var(--navy)!important;letter-spacing:-.02em}
    .app-title{position:relative;isolation:isolate;overflow:hidden;padding:27px 30px 24px;margin:4px 0 24px;border-radius:22px;border:2px solid rgba(10,88,168,.25);background:linear-gradient(120deg,rgba(255,255,255,.94),rgba(215,247,255,.92),rgba(224,255,241,.90));box-shadow:0 18px 55px rgba(0,71,130,.13);animation:fadeUp .7s ease both}
    .app-title h1{margin:0;font-size:clamp(26px,3vw,42px);font-weight:800;color:var(--navy)!important}
    .app-title p{margin:9px 0 0;color:red;font-size:18px;font-weight:600}
    .status-strip{display:flex;align-items:center;gap:10px;max-width:100%;width:fit-content;margin:0 auto 22px;padding:8px 14px;border-radius:999px;background:rgba(255,255,255,.78);border:1px solid rgba(10,88,168,.13);box-shadow:0 8px 25px rgba(0,71,130,.08)}
    .status-dot{width:9px;height:9px;flex:0 0 9px;border-radius:50%;background:#2fce75;animation:pulseDot 1.8s infinite}
    .status-text{font-size:12px;font-weight:700;color:var(--green)}
    @keyframes pulseDot{70%{box-shadow:0 0 0 9px rgba(47,206,117,0)}0%,100%{box-shadow:0 0 0 0 rgba(47,206,117,.4)}}
    div[data-baseweb="tab-list"]{gap:8px;padding:7px;border-radius:16px;background:rgba(255,255,255,.75);border:1px solid var(--line)}
    button[data-baseweb="tab"]{border-radius:11px!important;padding:10px 16px!important;font-weight:700!important;white-space:normal}
    button[data-baseweb="tab"][aria-selected="true"]{background:linear-gradient(135deg,#d8f7ff,#e3fff0)!important;color:var(--navy)!important}
    .section-card{background:rgba(255,255,255,.88);border:1px solid var(--line);border-radius:18px;padding:19px;margin:10px 0;box-shadow:0 10px 30px rgba(0,71,130,.08)}
    /* Animated workflow panels */
    .workflow-shell{position:relative;overflow:hidden;margin:12px 0 20px;padding:20px;border:3px dashed red;border-radius:22px;background:linear-gradient(135deg,rgba(255,255,255,.96),rgba(226,248,255,.92) 52%,rgba(230,255,242,.94));box-shadow:0 14px 34px rgba(0,71,130,.09)}
    .workflow-shell:before{content:"";position:absolute;width:220px;height:220px;right:-90px;top:-120px;border-radius:50%;background:radial-gradient(circle,rgba(84,216,255,.23),transparent 70%);pointer-events:none}
    .workflow-heading{position:relative;display:flex;align-items:center;gap:10px;margin:0 0 15px;color:#063b73;font-size:15px;font-weight:800;letter-spacing:.01em}
    .workflow-heading-icon{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:11px;background:linear-gradient(135deg,#d8f7ff,#dcffeb);box-shadow:0 5px 12px rgba(0,71,130,.08);font-size:18px}
    .workflow-track{position:relative;display:grid;grid-template-columns:minmax(0,1fr) 26px minmax(0,1fr) 26px minmax(0,1fr) 26px minmax(0,1fr);align-items:stretch;gap:7px}
    .workflow-step{position:relative;min-width:0;min-height:128px;padding:15px 12px 13px;border:1px solid rgba(10,88,168,.15);border-radius:16px;background:rgba(255,255,255,.88);box-shadow:0 7px 18px rgba(0,71,130,.06);animation:workflowEnter .6s cubic-bezier(.2,.8,.2,1) both;transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}
    .workflow-step:nth-child(1){animation-delay:.04s}.workflow-step:nth-child(3){animation-delay:.12s}.workflow-step:nth-child(5){animation-delay:.20s}.workflow-step:nth-child(7){animation-delay:.28s}
    .workflow-step:hover{transform:translateY(-5px);border-color:rgba(10,88,168,.38);box-shadow:0 14px 27px rgba(0,71,130,.13)}
    .workflow-step-top{display:flex;align-items:center;gap:9px;margin-bottom:9px}
    .workflow-icon{display:inline-flex;align-items:center;justify-content:center;flex:0 0 39px;width:39px;height:39px;border-radius:13px;background:linear-gradient(135deg,#d9f6ff,#e0ffed);font-size:21px;box-shadow:inset 0 0 0 1px rgba(10,88,168,.07)}
    .workflow-number{margin-left:auto;color:#6b91a9;font-size:10px;font-weight:800;letter-spacing:.08em}
    .workflow-step-title{color:#063b73;font-size:13px;line-height:1.35;font-weight:800}
    .workflow-step-desc{color:#547083;font-size:11px;line-height:1.45;margin-top:5px}
    .workflow-arrow{display:flex;align-items:center;justify-content:center;color:#1486b8;font-size:24px;font-weight:800;animation:arrowPulse 1.8s ease-in-out infinite}
    .workflow-footer{display:flex;align-items:center;gap:8px;margin-top:13px;color:#456b60;font-size:11px;font-weight:600}
    .workflow-footer-dot{width:7px;height:7px;flex:0 0 7px;border-radius:50%;background:#36c987;box-shadow:0 0 0 4px rgba(54,201,135,.12);animation:pulseDot 1.8s infinite}
    @keyframes workflowEnter{from{opacity:0;transform:translateY(12px) scale(.985)}to{opacity:1;transform:translateY(0) scale(1)}}
    @keyframes arrowPulse{0%,100%{opacity:.55;transform:translateX(0)}50%{opacity:1;transform:translateX(3px)}}
    @media(max-width:850px){.workflow-track{grid-template-columns:1fr 22px 1fr;gap:8px}.workflow-step{min-height:120px}.workflow-arrow:nth-child(6){display:none}}
    @media(max-width:520px){.workflow-shell{padding:14px}.workflow-track{grid-template-columns:1fr;gap:9px}.workflow-step{min-height:0;padding:13px}.workflow-arrow{height:15px;transform:rotate(90deg);font-size:19px}.workflow-arrow:nth-child(6){display:flex}.workflow-step-desc{font-size:12px}}
    .insight-card{background:linear-gradient(135deg,rgba(248,255,242,.96),rgba(239,255,248,.94));border-left:5px solid var(--green);border-radius:14px;padding:15px 18px;margin:9px 0}
    .warning-card{background:linear-gradient(135deg,#fffaf0,#fff8df);border-left:5px solid #d89b00;border-radius:14px;padding:14px 18px;margin:10px 0}
    [data-testid="stMetric"]{background:rgba(255,255,255,.9);border:1px solid var(--line);padding:15px;border-radius:15px;box-shadow:0 8px 25px rgba(0,71,130,.07)}
    [data-testid="stMetricLabel"]{color:var(--green)!important;font-weight:700}[data-testid="stMetricValue"]{color:var(--navy)!important;font-weight:800}
    /* Interactive buttons: gradient, lift, shine and press feedback */
    .stButton>button,.stDownloadButton>button,[data-testid="stFormSubmitButton"] button{
        position:relative;isolation:isolate;overflow:hidden;width:100%;min-height:45px;
        border:1px solid rgba(6,59,115,.35);border-radius:12px;font-weight:750;
        white-space:normal;overflow-wrap:anywhere;color:#063b73;
        background:#8BFFCD;
        box-shadow:0 4px 12px rgba(0,71,130,.08);
        transition:transform .22s cubic-bezier(.2,.8,.2,1),box-shadow .22s ease,border-color .22s ease,background-position .35s ease;
        background-size:180% 100%;background-position:0% 50%;
    }
    .stButton>button::before,.stDownloadButton>button::before,[data-testid="stFormSubmitButton"] button::before{
        content:"";position:absolute;top:-40%;left:-70%;width:42%;height:180%;
        transform:skewX(-22deg);background:linear-gradient(90deg,transparent,rgba(255,255,255,.85),transparent);
        transition:left .55s ease;z-index:-1;pointer-events:none;
    }
    .stButton>button:hover,.stDownloadButton>button:hover,[data-testid="stFormSubmitButton"] button:hover{
        transform:translateY(-3px) scale(1.01);background-position:100% 50%;
        border-color:rgba(10,88,168,.65);box-shadow:0 11px 25px rgba(0,71,130,.17),0 0 0 3px rgba(84,216,255,.12);
        color:#042d59;
    }
    .stButton>button:hover::before,.stDownloadButton>button:hover::before,[data-testid="stFormSubmitButton"] button:hover::before{left:135%}
    .stButton>button:active,.stDownloadButton>button:active,[data-testid="stFormSubmitButton"] button:active{
        transform:translateY(0) scale(.975);box-shadow:0 2px 6px rgba(0,71,130,.12);transition-duration:.08s;
    }
    .stButton>button:focus-visible,.stDownloadButton>button:focus-visible,[data-testid="stFormSubmitButton"] button:focus-visible{
        outline:3px solid rgba(10,88,168,.4);outline-offset:3px;
    }
    .stButton>button:disabled,.stDownloadButton>button:disabled,[data-testid="stFormSubmitButton"] button:disabled{
        opacity:.58;cursor:not-allowed;transform:none;box-shadow:none;
    }
    .section-card,.insight-card,.warning-card{animation:fadeUp .45s ease both;transition:transform .22s ease,box-shadow .22s ease}
    .section-card:hover{transform:translateY(-2px);box-shadow:0 14px 34px rgba(0,71,130,.11)}
    div[data-baseweb="tab"]{transition:transform .18s ease,box-shadow .18s ease}
    button[data-baseweb="tab"]:hover{transform:translateY(-1px)}
    [data-testid="stFileUploader"] section{border:2px dashed rgba(10,88,168,.28)!important;border-radius:17px!important;background:rgba(255,255,255,.66)!important}
    details[data-testid="stExpander"]{border:1px solid var(--line);border-radius:14px;margin:9px 0;background:rgba(255,255,255,.72)}
    [data-testid="stDataFrame"]{border-radius:14px;overflow:hidden;box-shadow:0 8px 25px rgba(0,71,130,.06)}
    [data-baseweb="input"],[data-baseweb="select"]{min-width:0}
    section[data-testid="stSidebar"]{border-right:1px solid var(--line);background:linear-gradient(180deg,rgba(238,250,255,.97),rgba(247,255,250,.97))}
    section[data-testid="stSidebar"] button{width:100%;margin:0;min-height:42px}
    .carelens-footer{text-align:center;padding:18px;margin-top:22px;color:#4d6b5a;font-size:13px}
    .pii-hero{position:relative;overflow:hidden;padding:22px;border-radius:22px;border:1px solid rgba(10,88,168,.18);background:linear-gradient(125deg,rgba(255,255,255,.96),rgba(224,246,255,.95),rgba(226,255,239,.94));box-shadow:0 14px 34px rgba(0,71,130,.09);animation:fadeUp .55s ease both;margin:8px 0 18px}
    .pii-hero-title{font-size:22px;font-weight:800;color:#063b73;margin-bottom:6px}
    .pii-hero-copy{font-size:13px;line-height:1.6;color:#456579;max-width:850px}
    .pii-chip{display:inline-block;padding:6px 10px;margin:5px 5px 0 0;border-radius:999px;background:rgba(255,255,255,.85);border:1px solid rgba(10,88,168,.15);color:#164f35;font-size:11px;font-weight:700}
    .pii-risk-high{color:#9f2424;font-weight:800}.pii-risk-medium{color:#946200;font-weight:800}.pii-risk-low{color:#176b45;font-weight:800}
    @keyframes fadeUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
    @media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}}
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# 4. SESSION STATE
# ============================================================
for key, default in {
    "dataframes": {},
    "chat_history": [],
    "dashboard_results": [],
    "dataset_summary": None,
    "overall_dashboard_summary": None,
    "pii_scan_results": None,
    "pii_scan_timestamp": None,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ============================================================
# 5. HELPERS: API + RESPONSE FORMATTING
# ============================================================
def require_api_key():
    if not API_KEY or client is None:
        st.error("OPENROUTER_API_KEY is missing. Add it to your .env file or Streamlit secrets.")
        st.code("OPENROUTER_API_KEY=your_openrouter_api_key")
        return False
    return True


def render_ai_markdown(content, container=None):
    """Render AI output as Markdown, not raw HTML, so headings/lists/tables format correctly."""
    if not content or not str(content).strip():
        st.info("No response was returned. Please try again.", icon="ℹ️")
        return
    target = container if container is not None else st
    target.markdown(str(content).strip())


def call_text_ai(prompt, system_prompt=None, temperature=0.2):
    if not require_api_key():
        return None
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    try:
        response = client.chat.completions.create(
            model=TEXT_MODEL,
            messages=messages,
            temperature=temperature,
        )
        content = response.choices[0].message.content
        if isinstance(content, list):
            content = "\n".join(str(part.get("text", "")) for part in content if isinstance(part, dict))
        return str(content).strip() if content else None
    except Exception as exc:
        st.error(f"AI request failed: {exc}")
        return None


def clean_sql(text):
    if not text:
        return ""
    text = text.strip()
    text = re.sub(r"^```(?:sql)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip().rstrip(";") + ";"


def is_safe_sql(sql):
    """Allow a single read-only SELECT/WITH query; reject multiple statements and write operations."""
    if not sql:
        return False
    normalized = sql.strip().lower()
    normalized = re.sub(r"--.*?$|/\*.*?\*/", "", normalized, flags=re.MULTILINE | re.DOTALL).strip()
    if not (normalized.startswith("select ") or normalized.startswith("with ")):
        return False
    # Permit only one statement (one trailing semicolon is okay).
    if ";" in normalized.rstrip(";"):
        return False
    forbidden = r"\b(insert|update|delete|drop|alter|create|truncate|replace|merge|attach|copy|export|install|load|pragma|call|execute|vacuum|detach|import|set|reset)\b"
    return re.search(forbidden, normalized) is None


def dataframe_schema():
    if not st.session_state.dataframes:
        return "No datasets have been uploaded."
    sections = []
    for table_name, df in st.session_state.dataframes.items():
        columns = ", ".join(f'"{col}" ({df[col].dtype})' for col in df.columns)
        sample = df.head(3).to_dict(orient="records")
        sections.append(f"TABLE: {table_name}\nROWS: {len(df)}\nCOLUMNS: {columns}\nSAMPLE ROWS: {sample}")
    return "\n\n".join(sections)


def execute_sql(sql):
    conn = duckdb.connect(database=":memory:")
    try:
        for table_name, df in st.session_state.dataframes.items():
            conn.register(table_name, df)
        return conn.execute(sql).df()
    finally:
        conn.close()


def format_dataframe_for_ai(df, max_rows=100):
    if df is None or df.empty:
        return "The query returned no rows."
    return df.head(max_rows).to_string(index=False)


def resize_image_for_ai(image_bytes, max_dimension=1600, quality=85):
    with Image.open(io.BytesIO(image_bytes)) as source:
        image = source.convert("RGB")
    width, height = image.size
    largest = max(width, height)
    if largest > max_dimension:
        scale = max_dimension / largest
        image = image.resize((max(1, int(width * scale)), max(1, int(height * scale))), Image.LANCZOS)
    output = io.BytesIO()
    image.save(output, format="JPEG", quality=quality, optimize=True)
    return output.getvalue()


# ============================================================
# PRIVACY HELPERS: HEURISTIC PII DETECTION AND SANITIZATION
# ============================================================
PII_COLUMN_RULES = {
    "Full name / name": ("name", "patient_name", "first_name", "last_name", "full_name", "given_name", "family_name"),
    "Email address": ("email", "e_mail"),
    "Phone number": ("phone", "mobile", "telephone", "contact_number", "cell_number"),
    "Home / mailing address": ("address", "street", "postal_address"),
    "Date of birth": ("dob", "birth_date", "date_of_birth", "birthdate"),
    "Patient / medical record ID": ("patient_id", "patientid", "mrn", "medical_record", "record_id", "member_id", "subscriber_id"),
    "Government / insurance identifier": ("ssn", "social_security", "national_id", "insurance_id", "policy_number"),
    "Postal code": ("zip_code", "zipcode", "postal_code", "postcode"),
}
PII_PATTERNS = {
    "Email address": re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"),
    "US Social Security number": re.compile(r"\b(?!000|666|9\d\d)\d{3}[- ]?(?!00)\d{2}[- ]?(?!0000)\d{4}\b"),
    "Phone number (possible)": re.compile(r"(?<!\w)(?:\+?\d{1,3}[ .-]?)?(?:\(?\d{3,5}\)?[ .-]?)\d{3,4}[ .-]?\d{3,4}(?!\w)"),
}


def _normalized_column_name(value):
    return re.sub(r"[^a-z0-9]+", "_", str(value).strip().lower()).strip("_")


def _column_pii_categories(column_name):
    normalized = _normalized_column_name(column_name)
    found = []
    for category, tokens in PII_COLUMN_RULES.items():
        for token in tokens:
            if normalized == token or normalized.endswith("_" + token) or normalized.startswith(token + "_") or token in normalized:
                found.append(category)
                break
    return found


def scan_dataframe_for_pii(table_name, df):
    """Return metadata-only findings; never include the matched sensitive values."""
    findings = []
    for column in df.columns:
        series = df[column]
        column_categories = _column_pii_categories(column)
        nonempty = series.notna() & series.astype(str).str.strip().ne("") & ~series.astype(str).str.fullmatch(r"(?i)\[REDACTED\]")
        if column_categories and int(nonempty.sum()) > 0:
            for category in column_categories:
                findings.append({
                    "Dataset": table_name, "Column": str(column), "Detected category": category,
                    "Potential matches": int(nonempty.sum()), "Detection method": "Column name",
                    "Risk": "High" if category in {"Full name / name", "Date of birth", "Patient / medical record ID", "Government / insurance identifier"} else "Medium",
                })
        # Content-based checks catch PII even when column names are generic.
        for category, pattern in PII_PATTERNS.items():
            # Phone-like patterns are noisy, so only scan them in contact-like columns.
            normalized = _normalized_column_name(column)
            if category == "Phone number (possible)" and not any(x in normalized for x in ("phone", "mobile", "contact", "telephone", "tel")):
                continue
            try:
                matches = series.dropna().astype(str).map(lambda value: bool(pattern.search(value)))
                count = int(matches.sum())
            except Exception:
                count = 0
            if count:
                findings.append({
                    "Dataset": table_name, "Column": str(column), "Detected category": category,
                    "Potential matches": count, "Detection method": "Value pattern",
                    "Risk": "High" if category == "US Social Security number" else "Medium",
                })
    return findings


def scan_all_datasets_for_pii(dataframes):
    findings = []
    for table_name, df in dataframes.items():
        findings.extend(scan_dataframe_for_pii(table_name, df))
    return pd.DataFrame(findings, columns=["Dataset", "Column", "Detected category", "Potential matches", "Detection method", "Risk"])


def sanitize_dataframe(df):
    """Mask identified PII in a copy. This is heuristic and should be reviewed before sharing."""
    cleaned = df.copy(deep=True)
    for column in cleaned.columns:
        categories = _column_pii_categories(column)
        if categories:
            cleaned[column] = cleaned[column].map(lambda value: "[REDACTED]" if pd.notna(value) and str(value).strip() else value)
            continue
        normalized = _normalized_column_name(column)
        for category, pattern in PII_PATTERNS.items():
            if category == "Phone number (possible)" and not any(x in normalized for x in ("phone", "mobile", "contact", "telephone", "tel")):
                continue
            cleaned[column] = cleaned[column].map(
                lambda value, pat=pattern: pat.sub("[REDACTED]", str(value)) if pd.notna(value) else value
            )
    return cleaned

# ============================================================
# 6. AI TASKS WITH EXPLICIT OUTPUT FORMATS
# ============================================================
def generate_dataset_summary():
    if not st.session_state.dataframes:
        return None
    prompt = f"""
Analyze the uploaded healthcare datasets using ONLY the dataset information below.

DATASET INFORMATION:
{dataframe_schema()}

Return a polished Markdown report using exactly this structure:
# Healthcare Dataset Overview
## 1. Executive Summary
Write 2-4 concise sentences describing what is available.
## 2. Dataset Inventory
Use a Markdown table with: Table, Rows, Columns, Main data fields.
## 3. Key Metrics
List metrics that can be verified from the supplied information. If values cannot be calculated from the sample/schema, say so instead of guessing.
## 4. Potential Data-Quality Checks
Use bullets and distinguish observed issues from checks that should be performed.
## 5. Business Insights
Provide useful observations only when supported by the data provided.
## 6. Recommended Business Questions
List five questions that could be answered by querying the uploaded tables.
## 7. Suggested Next Steps
Give 3-5 actionable steps.
Do not invent statistics, claim medical conclusions, or expose patient-level information. Use simple business language. Use valid Markdown tables and bullets.
"""
    return call_text_ai(prompt, "You are a careful healthcare data analyst. Return clean Markdown only; never wrap the whole response in a code fence. Never fabricate values.")


def generate_sql(question):
    prompt = f"""
User's business question: {question}

Available tables and schemas:
{dataframe_schema()}

Generate ONE read-only DuckDB SQL query. Return SQL only, without Markdown fences or explanation.
Rules: query only the listed tables and columns; use valid DuckDB syntax; SELECT or WITH only; no multiple statements; no write operations. Use clear aliases. Do not guess column names.
"""
    answer = call_text_ai(prompt, "You generate safe, read-only DuckDB SQL. Return only one query.", temperature=0)
    return clean_sql(answer)


def explain_query_result(question, sql, result_df):
    prompt = f"""
Explain this SQL result in a concise, professional Markdown report.

USER QUESTION: {question}
SQL QUERY: {sql}
RESULT DATA:
{format_dataframe_for_ai(result_df)}

Use this exact structure:
### Answer
Answer the question directly using the result.
### Key Findings
- List the most important numbers or comparisons.
### Business Interpretation
Explain what the result means in simple language.
### Suggested Follow-up
Give one useful next question or analysis.
Only report values present in the result. If the result is empty, clearly say that no matching rows were returned. Do not imply causation.
"""
    return call_text_ai(prompt, "You are a business analyst explaining query results. Return well-structured Markdown, no HTML.")


def analyze_dashboard_image(image_bytes, filename):
    if not require_api_key():
        return None
    try:
        encoded = base64.b64encode(resize_image_for_ai(image_bytes)).decode("utf-8")
        prompt = """
You are a business intelligence analyst reviewing a Power BI healthcare dashboard screenshot.
Analyze ONLY what is visible. Do not invent, estimate, or infer unreadable numbers. Do not make medical diagnoses.
Return a professional Markdown report with these sections:
# Dashboard Analysis
## 1. Dashboard Overview
Explain in 2-3 sentences what is shown.
## 2. Visible KPIs
Use a Markdown table with KPI, visible value, and brief meaning. If no value is readable, say so.
## 3. Key Insights
Give 4-7 numbered insights grounded in visible charts. Note the chart/category when possible.
## 4. Business Implications
Explain why the observed patterns may matter to a hospital manager or analyst. Distinguish observation from interpretation.
## 5. Recommendations
Give 3-5 practical, data-grounded recommendations. Label any suggestion that needs more data to validate.
## 6. Executive Summary
End with one concise sentence.
"""
        response = client.chat.completions.create(
            model=VISION_MODEL,
            messages=[{"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded}"}},
            ]}],
            temperature=0.2,
        )
        content = response.choices[0].message.content
        if isinstance(content, list):
            content = "\n".join(str(part.get("text", "")) for part in content if isinstance(part, dict))
        return str(content).strip() if content else None
    except Exception as exc:
        st.error(f"Could not analyze {filename}: {exc}")
        return None


def combine_dashboard_insights(results):
    if not results:
        return None
    combined_text = "\n\n".join(f"SCREENSHOT: {name}\n{analysis}" for name, analysis in results)
    prompt = f"""
Create a concise executive report from these dashboard analyses. Use ONLY information present below.

SOURCE ANALYSES:
{combined_text}

Use this Markdown structure:
# Healthcare Dashboard — Executive Summary
## 1. Overall Summary
## 2. Most Important KPIs
Use a table where comparable values are available.
## 3. Cross-Dashboard Patterns
## 4. Operational Questions to Investigate
## 5. Recommended Actions
List five prioritized actions.
## 6. Management Takeaway
Do not invent values or combine metrics that are not comparable. Mention when source dashboards are unclear or incomplete.
"""
    return call_text_ai(prompt, "You are a senior healthcare BI analyst. Return clear Markdown, no HTML, and do not fabricate information.")

# ============================================================
# 7. HEADER
# ============================================================
st.markdown(
    '<div class="app-title"><center><h1>🏥 CareLens AI — Healthcare Intelligence & Analytics Platform</h1><p>Upload · Ask · Analyze · Discover Insights</p></center></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="status-strip"><span class="status-dot"></span><span class="status-text">CareLens AI · Analytics Engine Ready · Healthcare Intelligence Workspace</span></div>',
    unsafe_allow_html=True,
)
if not API_KEY:
    st.warning("OpenRouter API key not detected. Add OPENROUTER_API_KEY to your .env file or Streamlit secrets.")

# ============================================================
# 8. SIDEBAR
# ============================================================
with st.sidebar:
    st.header("⚙️ Project Controls")
    st.markdown("**Recommended healthcare tables**\n- patients\n- encounters\n- procedures\n- payers\n- organizations")
    if st.session_state.dataframes:
        st.success(f"{len(st.session_state.dataframes)} dataset(s) loaded.")
        for table_name, df in st.session_state.dataframes.items():
            st.write(f"• `{table_name}` — {len(df):,} rows")
    st.divider()
    if st.button("🗑️ Clear All Data", use_container_width=True):
        st.session_state.dataframes = {}
        st.session_state.chat_history = []
        st.session_state.dashboard_results = []
        st.session_state.dataset_summary = None
        st.session_state.overall_dashboard_summary = None
        st.session_state.pii_scan_results = None
        st.session_state.pii_scan_timestamp = None
        st.rerun()
    st.divider()
    st.markdown("**AI models**\n\nText: `openrouter/free`\n\nVision: `openrouter/free`")

# ============================================================
# 9. MAIN TABS
# ============================================================
tab1, tab2, tab3, tab4 = st.tabs(["📂 Data Upload & Insights", "🤖 Ask AI", "🔐 Privacy & PII Scanner", "📊 Power BI Insights"])

# ============================================================
# TAB 1 — DATA UPLOAD & DATASET INSIGHTS
# ============================================================
with tab1:
    st.header("📂 Upload Healthcare Files")
    st.caption("Upload CSV datasets to preview the data, inspect quality, and generate a structured AI report.")
    uploaded_files = st.file_uploader(
        "Upload one or more CSV files", type=["csv"], accept_multiple_files=True,
        help="Example: patients.csv, encounters.csv, procedures.csv, payers.csv",
        key="healthcare_csv_upload",
    )
    if uploaded_files:
        for uploaded_file in uploaded_files:
            table_name = re.sub(r"[^a-zA-Z0-9_]", "_", Path(uploaded_file.name).stem.lower())
            if not table_name or table_name[0].isdigit():
                table_name = f"table_{table_name}"
            try:
                raw_bytes = uploaded_file.getvalue()
                try:
                    df = pd.read_csv(io.BytesIO(raw_bytes))
                except UnicodeDecodeError:
                    df = pd.read_csv(io.BytesIO(raw_bytes), encoding="latin1")
                st.session_state.dataframes[table_name] = df
            except Exception as exc:
                st.error(f"Could not read {uploaded_file.name}: {exc}")
    if st.session_state.dataframes:
        st.subheader("📌 Loaded Datasets")
        for table_name, df in st.session_state.dataframes.items():
            with st.expander(f"📄 {table_name} — {len(df):,} rows × {len(df.columns):,} columns"):
                c1, c2, c3 = st.columns(3)
                c1.metric("Rows", f"{len(df):,}")
                c2.metric("Columns", f"{len(df.columns):,}")
                c3.metric("Missing Values", f"{int(df.isna().sum().sum()):,}")
                st.dataframe(df.head(100), use_container_width=True)
                if not df.empty:
                    quality = pd.DataFrame({
                        "Column": df.columns.astype(str),
                        "Data Type": [str(dtype) for dtype in df.dtypes],
                        "Missing Values": [int(v) for v in df.isna().sum().values],
                        "Missing %": [round(float(v) / len(df) * 100, 2) for v in df.isna().sum().values],
                        "Unique Values": [int(df[col].nunique(dropna=True)) for col in df.columns],
                    })
                    with st.expander("View column-level data quality"):
                        st.dataframe(quality, use_container_width=True, hide_index=True)
        st.divider()
        st.subheader("🤖 AI Dataset Summary")
        if st.button("Generate AI Insights", key="generate_dataset_summary", use_container_width=True):
            with st.spinner("Analyzing your healthcare datasets..."):
                st.session_state.dataset_summary = generate_dataset_summary()
        if st.session_state.dataset_summary:
            with st.container(border=True):
                render_ai_markdown(st.session_state.dataset_summary)
    else:
        st.info("👆 Upload your CSV files to start analyzing healthcare data.")

# ============================================================
# TAB 2 — ASK AI ABOUT DATA
# ============================================================
with tab2:
    st.header("🤖 Ask AI About Your Healthcare Data")
    with st.container(border=True):
        st.markdown(
            """
            <div class="workflow-shell">
              <div class="workflow-heading"><span class="workflow-heading-icon">✨</span> From your question to actionable insights</div>
              <div class="workflow-track">
                <div class="workflow-step"><div class="workflow-step-top"><span class="workflow-icon">💬</span><span class="workflow-number">STEP 01</span></div><div class="workflow-step-title">Ask in plain English</div><div class="workflow-step-desc">Describe the healthcare question you want answered.</div></div>
                <div class="workflow-arrow" aria-hidden="true">›</div>
                <div class="workflow-step"><div class="workflow-step-top"><span class="workflow-icon">🧠</span><span class="workflow-number">STEP 02</span></div><div class="workflow-step-title">AI writes the SQL</div><div class="workflow-step-desc">Your question is translated into a read-only query.</div></div>
                <div class="workflow-arrow" aria-hidden="true">›</div>
                <div class="workflow-step"><div class="workflow-step-top"><span class="workflow-icon">🗄️</span><span class="workflow-number">STEP 03</span></div><div class="workflow-step-title">DuckDB analyzes data</div><div class="workflow-step-desc">The query runs against your uploaded CSV tables.</div></div>
                <div class="workflow-arrow" aria-hidden="true">›</div>
                <div class="workflow-step"><div class="workflow-step-top"><span class="workflow-icon">📊</span><span class="workflow-number">STEP 04</span></div><div class="workflow-step-title">Understand the result</div><div class="workflow-step-desc">Get a structured answer with findings and next steps.</div></div>
              </div>
              <div class="workflow-footer"><span class="workflow-footer-dot"></span> Ask a question, explore the result, and use the findings to guide your next analysis.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    if not st.session_state.dataframes:
        st.info("Upload CSV files in the first tab before asking questions.")
    else:
        st.write("Ask a question in plain English. CareLens AI generates a read-only SQL query, runs it on your uploaded datasets, and explains the result.")
        example_questions = [
            "What is the total number of encounters?",
            "Which encounter class has the highest number of encounters?",
            "What is the total claim cost by payer?",
            "Which procedures are performed most frequently?",
            "What is the average encounter cost?",
            "Which year had the highest number of encounters?",
            "What are the top 5 most expensive procedures?",
        ]
        selected_example = st.selectbox("Example question", ["-- Select an example --"] + example_questions)
        question = st.text_input(
            "Ask your own question",
            value="" if selected_example == "-- Select an example --" else selected_example,
            placeholder="Example: Which payer has the highest total claim cost?",
            key="data_question_input",
        )
        if st.button("🔎 Ask AI", key="ask_data_ai", use_container_width=True):
            if not question.strip():
                st.warning("Please enter a question.")
            else:
                with st.spinner("Generating SQL and analyzing your data..."):
                    sql = generate_sql(question)
                    if not sql:
                        st.error("The AI could not generate a SQL query. Please try rephrasing the question.")
                    elif not is_safe_sql(sql):
                        st.error("The generated query was blocked because it was not a safe, single read-only query.")
                    else:
                        try:
                            result = execute_sql(sql)
                            explanation = explain_query_result(question, sql, result)
                            st.session_state.chat_history.append({
                                "question": question,
                                "sql": sql,
                                "result": result,
                                "explanation": explanation,
                            })
                        except Exception as exc:
                            st.error(f"SQL execution failed: {exc}")
        if st.session_state.chat_history:
            st.subheader("💡 Analysis History")
            for index, item in enumerate(reversed(st.session_state.chat_history), start=1):
                with st.container(border=True):
                    st.markdown(f"### {index}. {item['question']}")
                    st.markdown("#### 🧠 AI Answer")
                    render_ai_markdown(item.get("explanation"))
                    with st.expander("🔧 View generated SQL"):
                        st.code(item["sql"], language="sql")
                    with st.expander("📊 View query result", expanded=True):
                        result_df = item["result"]
                        if result_df is None or result_df.empty:
                            st.info("The query returned no rows.")
                        else:
                            st.dataframe(result_df, use_container_width=True, hide_index=True)
                            st.download_button(
                                "⬇️ Download query result as CSV",
                                data=result_df.to_csv(index=False).encode("utf-8-sig"),
                                file_name=f"carelens_query_result_{index}.csv",
                                mime="text/csv",
                                key=f"download_query_result_{index}",
                            )

# ============================================================
# TAB 3 — PRIVACY & PII SCANNER
# ============================================================
with tab3:
    st.markdown(
        """
        <div class="pii-hero">
          <div class="pii-hero-title">🔐 Privacy & PII Scanner</div>
          <div class="pii-hero-copy">Check uploaded healthcare CSV datasets for potential personal identifiers before using AI analysis. The scanner checks column names and common value patterns locally and does not display matched values.</div>
          <span class="pii-chip">Local CSV scan</span><span class="pii-chip">No values shown in report</span><span class="pii-chip">Sanitized CSV export</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.warning("PII detection is heuristic, not a guarantee. It may miss sensitive information or flag ordinary data. Review results before sharing data. This scanner does not OCR or certify screenshots.")

    if not st.session_state.dataframes:
        st.info("Upload CSV files in **Data Upload & Insights** before scanning for PII.")
    else:
        left, right = st.columns([1, 1])
        with left:
            st.metric("Datasets to scan", len(st.session_state.dataframes))
        with right:
            st.metric("Rows in loaded datasets", f"{sum(len(df) for df in st.session_state.dataframes.values()):,}")

        scan_col, export_col = st.columns(2)
        with scan_col:
            if st.button("🔎 Scan datasets for PII", key="run_pii_scan", use_container_width=True):
                with st.spinner("Scanning column names and common patterns locally..."):
                    st.session_state.pii_scan_results = scan_all_datasets_for_pii(st.session_state.dataframes)
                    st.session_state.pii_scan_timestamp = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")
        with export_col:
            if st.button("🛡️ Sanitize active datasets", key="sanitize_pii_datasets", use_container_width=True):
                findings = scan_all_datasets_for_pii(st.session_state.dataframes)
                if findings.empty:
                    st.info("No likely PII patterns were detected. This does not prove the data is anonymous.")
                else:
                    st.session_state.dataframes = {
                        name: sanitize_dataframe(df) for name, df in st.session_state.dataframes.items()
                    }
                    st.session_state.chat_history = []
                    st.session_state.dataset_summary = None
                    st.session_state.pii_scan_results = scan_all_datasets_for_pii(st.session_state.dataframes)
                    st.session_state.pii_scan_timestamp = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")
                    st.success("Sanitization applied to the active in-memory datasets. Previous AI summaries and query history were cleared.")
                    st.warning("The active datasets have been replaced with masked copies for this session. Re-upload the original CSVs to restore the original values.")
                    st.rerun()

        if st.session_state.pii_scan_results is not None:
            findings = st.session_state.pii_scan_results
            st.caption(f"Last scan: {st.session_state.pii_scan_timestamp or 'Unknown'} · Sensitive values are intentionally not shown.")
            if findings.empty:
                st.success("No likely PII patterns were detected by the current checks.")
                st.caption("A clean scan is not proof that a dataset contains no personal or sensitive information.")
            else:
                total_matches = int(findings["Potential matches"].sum())
                high_risk = int((findings["Risk"] == "High").sum())
                m1, m2, m3 = st.columns(3)
                m1.metric("Flagged columns / findings", len(findings))
                m2.metric("Potential matches", f"{total_matches:,}")
                m3.metric("High-risk findings", high_risk)
                st.dataframe(findings, use_container_width=True, hide_index=True)
                st.download_button(
                    "⬇️ Download PII scan report (metadata only)",
                    data=findings.to_csv(index=False).encode("utf-8-sig"),
                    file_name="carelens_pii_scan_report.csv",
                    mime="text/csv",
                    key="download_pii_report",
                    use_container_width=True,
                )
                st.markdown("#### Download sanitized copies")
                st.caption("This export masks columns identified by their names and replaces detected email / SSN / contact patterns. It does not modify the active datasets unless you click **Sanitize active datasets**.")
                sanitized_files = {
                    name: sanitize_dataframe(df) for name, df in st.session_state.dataframes.items()
                }
                for table_name, sanitized_df in sanitized_files.items():
                    st.download_button(
                        f"⬇️ Download sanitized {table_name}.csv",
                        data=sanitized_df.to_csv(index=False).encode("utf-8-sig"),
                        file_name=f"{table_name}_sanitized.csv",
                        mime="text/csv",
                        key=f"download_sanitized_{table_name}",
                        use_container_width=True,
                    )

# ============================================================
# TAB 4 — POWER BI SCREENSHOT ANALYSIS
# ============================================================
with tab4:
    st.header("📊 AI Power BI Dashboard Insights")
    with st.container(border=True):
        st.markdown(
            """
            <div class="workflow-shell">
              <div class="workflow-heading"><span class="workflow-heading-icon">🪄</span> Turn dashboard visuals into business direction</div>
              <div class="workflow-track">
                <div class="workflow-step"><div class="workflow-step-top"><span class="workflow-icon">📤</span><span class="workflow-number">STEP 01</span></div><div class="workflow-step-title">Upload a screenshot</div><div class="workflow-step-desc">Share a clear image of your Power BI dashboard.</div></div>
                <div class="workflow-arrow" aria-hidden="true">›</div>
                <div class="workflow-step"><div class="workflow-step-top"><span class="workflow-icon">👁️</span><span class="workflow-number">STEP 02</span></div><div class="workflow-step-title">Vision AI reviews charts</div><div class="workflow-step-desc">AI identifies readable KPIs, labels, and visible patterns.</div></div>
                <div class="workflow-arrow" aria-hidden="true">›</div>
                <div class="workflow-step"><div class="workflow-step-top"><span class="workflow-icon">🔎</span><span class="workflow-number">STEP 03</span></div><div class="workflow-step-title">Explore key insights</div><div class="workflow-step-desc">Review observations and what they may mean operationally.</div></div>
                <div class="workflow-arrow" aria-hidden="true">›</div>
                <div class="workflow-step"><div class="workflow-step-top"><span class="workflow-icon">💡</span><span class="workflow-number">STEP 04</span></div><div class="workflow-step-title">Plan next actions</div><div class="workflow-step-desc">Get practical recommendations and questions to investigate.</div></div>
              </div>
              <div class="workflow-footer"><span class="workflow-footer-dot"></span> Insights are based on visible dashboard content; unreadable values are not guessed.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.write("Upload Power BI dashboard screenshots. AI will summarize readable KPIs and visible patterns in a structured report.")
    st.markdown('<div class="warning-card"><b>🔐 Privacy note:</b> Do not upload screenshots containing real patient names, IDs, phone numbers, addresses, or other sensitive information. Use anonymized or synthetic data.</div>', unsafe_allow_html=True)
    dashboard_files = st.file_uploader(
        "Upload Power BI dashboard screenshots", type=["png", "jpg", "jpeg"],
        accept_multiple_files=True, key="dashboard_upload",
        help="You can upload multiple dashboard screenshots.",
    )
    if dashboard_files:
        st.subheader("🖼️ Uploaded Dashboards")
        cols = st.columns(min(3, len(dashboard_files)))
        for index, file in enumerate(dashboard_files):
            with cols[index % len(cols)]:
                st.image(file, caption=file.name, use_container_width=True)
        if st.button("👁️ Analyze Dashboard Screenshots", key="analyze_dashboards", use_container_width=True):
            results = []
            for dashboard_file in dashboard_files:
                with st.spinner(f"AI is analyzing {dashboard_file.name}..."):
                    analysis = analyze_dashboard_image(dashboard_file.getvalue(), dashboard_file.name)
                if analysis:
                    results.append((dashboard_file.name, analysis))
            st.session_state.dashboard_results = results
            st.session_state.overall_dashboard_summary = None
        if st.session_state.dashboard_results:
            st.subheader("🔍 Individual Dashboard Insights")
            for filename, analysis in st.session_state.dashboard_results:
                with st.expander(f"📊 {filename}", expanded=True):
                    render_ai_markdown(analysis)
            if len(st.session_state.dashboard_results) > 1:
                st.divider()
                st.subheader("🏥 Overall Dashboard Summary")
                if st.button("Generate Overall Management Summary", key="combine_dashboard_insights", use_container_width=True):
                    with st.spinner("Combining insights from all dashboards..."):
                        st.session_state.overall_dashboard_summary = combine_dashboard_insights(st.session_state.dashboard_results)
                if st.session_state.overall_dashboard_summary:
                    with st.container(border=True):
                        render_ai_markdown(st.session_state.overall_dashboard_summary)
    else:
        st.info("👆 Upload one or more Power BI screenshots to get AI-generated insights.")

# ============================================================
# 10. FOOTER
# ============================================================
st.markdown("---")
st.markdown(
    '<div class="carelens-footer">💙 <b>CareLens AI</b> · Healthcare Intelligence & Analytics<br>Data → Insights → Decisions</div>',
    unsafe_allow_html=True,
)




