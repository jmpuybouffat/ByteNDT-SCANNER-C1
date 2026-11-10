"""C1 scanner operator study; separate from accepted UT replay."""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="BYTE NDT — Scanner C1 — FR / EN",layout="wide",initial_sidebar_state="collapsed")
st.caption("BYTE NDT · SCANNER C1 · OPÉRATEUR / OPERATOR · ÉTUDE 04 / STUDY 04 — BÂTI + CARTOGRAPHIE C1 / BASE + C1 CARTOGRAPHY")
st.info("Concept retenu : deux coques moulées sur aérofoil et plateforme, slot intégré et eau dans sa lèvre supérieure. La vue sur colonnettes ci-dessous est une étude antérieure à remplacer. / Selected concept: two shells fitted to airfoil and platform, integrated slot and water supply in its upper lip. The stand-off-supported view below is an earlier study to be replaced.")
p=Path(__file__).parent/"scanner_assets"
# Read the release document directly: never retain an older geometry in cache.
def document():
    return (p/"00_OUVRIR_SCANNER_C1_OPERATEUR_FR_EN.html").read_text()
with st.expander("Procédure opérateur et couplage / Operator procedure and coupling", expanded=True):
    procedure_language = st.radio("Langue de la procédure / Procedure language", ["Français", "English"], horizontal=True)
    if procedure_language == "Français":
        st.markdown("**Positionnement validé → étalonnage sur référence → tirs et parcours → contrôle du film d’eau et du couplage → scan et rapport.**")
        st.write("Vérifier la formation et la continuité du film d’eau sous le sabot avant le départ et pendant tout le parcours. Surveiller en complément le signal acoustique de référence. En cas de perte : signaler, arrêter, enregistrer et reprendre la zone selon la procédure approuvée.")
        st.caption("Projet C1-PROC-DRAFT-02. Seuils à établir avec la référence et l’instrumentation réelle. Le rejeu actuel ne mesure pas le couplage physique.")
    else:
        st.markdown("**Validated positioning → reference calibration → firing laws and path → water-film and acoustic-coupling checks → scan and report.**")
        st.write("Check water-film formation and continuity beneath the wedge before starting and throughout travel. Also monitor the acoustic reference signal. On loss: flag, stop, record and re-examine the affected zone under the approved procedure.")
        st.caption("Draft C1-PROC-DRAFT-02. Establish thresholds with the reference and actual instrumentation. The current replay does not measure physical coupling.")
    procedure = Path(__file__).parent / "documentation" / "PROCEDURE_EXAMEN_C1_FR_EN.md"
    st.download_button("Procédure complète FR/EN / Full FR/EN procedure", procedure.read_text(), file_name=procedure.name, mime="text/markdown")
components.html(document(),height=2350,scrolling=True)
with st.expander("Version et références / Version and references"):
    st.json((p/"REFERENCE_COMMANDE.json").read_text())

st.link_button("Dossier maquette et fichiers CAO / Mock-up and CAD files", "https://github.com/jmpuybouffat/ByteNDT-SCANNER-C1/tree/main/maquette_etude")
st.link_button("Notice du bâti / Base guide", "https://github.com/jmpuybouffat/ByteNDT-SCANNER-C1/blob/main/documentation/NOTICE_BATI_C1_FR_EN.md")

st.link_button("Procédure d’examen — projet FR/EN / Draft examination procedure", "https://github.com/jmpuybouffat/ByteNDT-SCANNER-C1/blob/main/documentation/PROCEDURE_EXAMEN_C1_FR_EN.md")

st.link_button("Concept coques et alimentation en eau / Shell and water-supply concept", "https://github.com/jmpuybouffat/ByteNDT-SCANNER-C1/blob/main/documentation/CONCEPT_COQUES_C1_FR_EN.md")
