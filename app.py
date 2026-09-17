import streamlit as st

st.set_page_config(
    page_title="Generador Estado del Arte - UTT", layout="wide"
)

st.title("🎓 Asistente de Redacción Científica: Estado del Arte")
st.caption(
    "Plantilla en LaTeX — Maestría en Ingeniería UTT (Basado en Fórmula Tripartita)"
)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Datos de la Referencia (Google Sheet)")
    bib_key = st.text_input("BibTeX Key", "Gomez2023_Evaporacion")
    autor = st.text_input("Autor(es) y Año", "Gómez et al. (2023)")
    vi = st.text_input(
        "Variable Independiente (VI)",
        "sistemas de evaporación térmica en lazo cerrado",
    )
    vd = st.text_input(
        "Variable Dependiente (VD)",
        "la concentración de sólidos disueltos totales (TDS)",
    )
    metodologia = st.text_input(
        "Metodología / Herramientas",
        "simulación termodinámica en Aspen Plus a escala banco",
    )
    resultado = st.text_input(
        "Resultados / KPIs",
        "una remoción del 98% de contaminantes orgánicos",
    )
    gap = st.text_input(
        "Brecha / Límite (Gap)",
        "el comportamiento térmico ante flujos continuos con alta variabilidad",
    )

with col2:
    st.subheader("✍️ Salida Generada para capitulo1.tex")

    parrafo_latex = f"""% --- Párrafo generado para {bib_key} ---
En lo relativo a la aplicación de {vi}, \\cite{{{bib_key}}} desarrollaron un estudio fundamentado en {metodologia} enfocado en evaluar {vd}. En sus hallazgos, los autores reportaron {resultado}. Sin embargo, un aspecto no considerado en dicha investigación fue {gap}, lo cual demuestra la pertinencia de abordar esta variable dentro del presente trabajo de investigación.
"""

    st.code(parrafo_latex, language="latex")

    st.subheader("💡 Conectores Transicionales")
    st.markdown(
        """
    - **Para contrastar:** *En contraposición a los hallazgos de \\cite{...}...*
    - **Para complementar:** *En esta misma línea de trabajo, \\cite{...} demostraron que...*
    - **Para sintetizar el Gap:** *A partir de estas evidencias, se deduce que...*
    """
    )