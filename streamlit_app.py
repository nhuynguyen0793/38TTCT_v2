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
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        display: none !important;
    }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
        width: 100% !important;
        height: 100vh !important;
        height: 100dvh !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    [data-testid="stMain"], [data-testid="stMainBlockContainer"] {
        width: 100% !important;
        height: 100vh !important;
        height: 100dvh !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: none !important;
        overflow: hidden !important;
    }
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: none !important;
        width: 100vw !important;
        height: 100vh !important;
        height: 100dvh !important;
        overflow: hidden !important;
    }
    iframe {
        display: block;
        border: 0 !important;
    }
    iframe[title="streamlit_components.v1.html"] {
        position: fixed !important;
        inset: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        height: 100dvh !important;
        z-index: 999 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html_candidates = (
    "index.html",
    "V3_TTCT_Linkdata8.html",
)
html_path = next(
    (Path(__file__).with_name(name) for name in html_candidates if (Path(__file__).with_name(name)).exists()),
    None,
)

if html_path is None:
    st.error("Không tìm thấy file HTML của ứng dụng.")
    st.stop()

html = html_path.read_text(encoding="utf-8")

if "<head>" in html:
    html = html.replace(
        "<head>",
        """<head>
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <style>
      html, body {
        width: 100% !important;
        height: 100% !important;
        min-height: 100% !important;
      }
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

if "</body>" in html:
    html = html.replace("</body>", resize_script + "\n</body>", 1)

components.html(html, height=900, scrolling=False)
