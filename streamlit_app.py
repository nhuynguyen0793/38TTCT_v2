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
    header[data-testid="stHeader"],
    footer,
    [data-testid="stToolbar"] { display: none !important; }
    [data-testid="stDecoration"] { display: none !important; }
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: none !important;
    }
    iframe {
        display: block;
        border: 0;
    }
    iframe[title="streamlit_components.v1.html"] {
        width: 100vw !important;
        border: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html_file = "V3_TTCT_Linkdata8.html"
html_path = Path(__file__).with_name(html_file)
if not html_path.exists():
    html_path = Path(__file__).with_name("index.html")
if not html_path.exists():
    st.error("Không tìm thấy file HTML của ứng dụng.")
    st.stop()

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
      window.dispatchEvent(new Event("resize"));
      try {
        if (typeof m1 !== "undefined" && m1) m1.invalidateSize();
        if (typeof m2 !== "undefined" && m2) m2.invalidateSize();
        if (typeof m3 !== "undefined" && m3) m3.invalidateSize();
      } catch (_) {}
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

components.html(html, height=780, scrolling=True)
