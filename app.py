"""C1 scanner operator study; separate from accepted UT replay."""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="BYTE NDT — Scanner C1 — FR / EN",layout="wide",initial_sidebar_state="collapsed")
st.caption("BYTE NDT · SCANNER C1 · OPÉRATEUR / OPERATOR · ÉTUDE 01 / STUDY 01")
p=Path(__file__).parent/"scanner_assets"
@st.cache_data
def document():
    return (p/"00_OUVRIR_SCANNER_C1_OPERATEUR_FR_EN.html").read_text()
components.html(document(),height=1800,scrolling=True)
with st.expander("Version et références / Version and references"):
    st.json((p/"REFERENCE_COMMANDE.json").read_text())
