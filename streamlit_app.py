from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="HCA - Trung tâm Chính trị",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] { background: #060a14; }
    [data-testid="stHeader"] { height: 0; }
    [data-testid="stToolbar"] { display: none !important; }
    [data-testid="stDecoration"] { display: none !important; }
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: none !important;
        width: 100vw !important;
        height: 100vh !important;
        height: 100dvh !important;
        overflow: hidden !important;
    }
    iframe[title="streamlit_components.v1.html"] {
        position: fixed !important;
        inset: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        height: 100dvh !important;
        border: 0 !important;
        z-index: 999 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")

html = html.replace(
    "<head>",
    """<head>
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <style>
      html, body { width: 100% !important; height: 100% !important; min-height: 100% !important; }
    </style>""",
    1,
)

resize_script = """
<script>
  (function () {
    function resize() {
      var height = window.innerHeight;
      window.parent.postMessage({
        isStreamlitMessage: true,
        type: "streamlit:setFrameHeight",
        height: height
      }, "*");
      window.parent.postMessage({
        type: "streamlit:setFrameHeight",
        height: height
      }, "*");
    }
    window.addEventListener("load", resize);
    window.addEventListener("resize", resize);
    document.addEventListener("DOMContentLoaded", resize);
    setTimeout(resize, 100);
    setTimeout(resize, 500);
  })();
</script>
"""
html = html.replace("</body>", resize_script + "\n</body>", 1)

components.html(html, height=900, scrolling=False)
