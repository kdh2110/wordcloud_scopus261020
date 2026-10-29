from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="연구 키프레이즈 · 논문 탐색",
    layout="wide",
)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
st.iframe(html, height="content", alt="워드클라우드 및 논문 탐색")
