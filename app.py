import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Generador Estado del Arte - UTT",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Asistente de Redacción Científica: Estado del Arte")
st.caption("Plantilla en LaTeX — Maestría en Ingeniería UTT (Basado en Fórmula Tripartita)")

# Estructura en 2 columnas
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.subheader("📋 Datos de la Referencia")
    
    # Selección de estilo de conector para variar la redacción
    tipo_conector = st.selectbox(
        "Tipo de conector / Párrafo:",
        ["Aporte Inicial / Estándar", "En foque Complementario", "Enfoque Contrastante"]
    )
    
    bib_key = st.text_input("BibTeX Key (ej: Gomez2023)", "Gomez2023_Evaporacion")
    autor = st.text_input("Autor(es) y Año (opcional para vista previa)", "Gómez et al. (2023)")
    vi = st.text_input("Variable Independiente (VI)", "sistemas de evaporación térmica en lazo cerrado")
    vd = st.text_input("Variable Dependiente (VD)", "la concentración de sólidos disueltos totales (TDS)")
    metodologia = st.text_input("Metodología / Herramientas", "simulación termodinámica en Aspen Plus a escala banco")
    resultado = st.text_input("Resultados / KPIs", "una remoción del 98% de contaminantes orgánicos")
    gap = st.text_input("Brecha / Límite (Gap)", "el comportamiento térmico ante flujos continuos con alta variabilidad")

with col2:
    st.subheader("✍️ Salida Generada para capitulo1.tex")

    # Selección del patrón de redacción según el tipo de conector
    if tipo_conector == "Aporte Inicial / Estándar":
        plantilla_latex = f"""% --- Párrafo generado para {bib_key} ---
En lo relativo a la aplicación de {vi}, \\cite{{{bib_key}}} desarrollaron un estudio fundamentado en {metodologia} enfocado en evaluar {vd}. En sus hallazgos, los autores reportaron {resultado}. Sin embargo, un aspecto no considerado en dicha investigación fue {gap}, lo cual demuestra la pertinencia de abordar esta variable dentro del presente trabajo de investigación.
"""
        plantilla_preview = f"En lo relativo a la aplicación de {vi}, **{autor}** desarrollaron un estudio fundamentado en {metodologia} enfocado en evaluar {vd}. En sus hallazgos, los autores reportaron {resultado}. Sin embargo, un aspecto no considerado en dicha investigación fue {gap}, lo cual demuestra la pertinencia de abordar esta variable dentro del presente trabajo de investigación."

    elif tipo_conector == "Enfoque Complementario":
        plantilla_latex = f"""% --- Párrafo generado para {bib_key} ---
En esta misma línea de trabajo, \\cite{{{bib_key}}} examinaron la integración de {vi} mediante {metodologia}, orientándose a la optimización de {vd}. Sus resultados evidenciaron {resultado}. A pesar de estos avances, persiste una limitante respecto a {gap}, brecha que se busca cubrir en el desarrollo del presente proyecto.
"""
        plantilla_preview = f"En esta misma línea de trabajo, **{autor}** examinaron la integración de {vi} mediante {metodologia}, orientándose a la optimización de {vd}. Sus resultados evidenciaron {resultado}. A pesar de estos avances, persiste una limitante respecto a {gap}, brecha que se busca cubrir en el desarrollo del presente proyecto."

    else:  # Contrastante
        plantilla_latex = f"""% --- Párrafo generado para {bib_key} ---
En contraposición a los abordajes tradicionales en {vi}, \\cite{{{bib_key}}} implementaron {metodologia} para analizar su efecto sobre {vd}. Si bien reportaron {resultado}, el estudio omitió evaluar {gap}. Dicha oportunidad de investigación justifica la formulación de la propuesta actual.
"""
        plantilla_preview = f"En contraposición a los abordajes tradicionales en {vi}, **{autor}** implementaron {metodologia} para analizar su efecto sobre {vd}. Si bien reportaron {resultado}, el estudio omitió evaluar {gap}. Dicha oportunidad de investigación justifica la formulación de la propuesta actual."

    # Mostrar vista previa de lectura
    st.markdown("**📖 Vista Previa de Redacción (Texto Plano):**")
    st.info(plantilla_preview)

    # Mostrar código LaTeX
    st.markdown("**💻 Código LaTeX:**")
    st.code(plantilla_latex, language="latex")

    # Botón de descarga directa
    st.download_button(
        label="📥 Descargar fragmento (.tex)",
        data=plantilla_latex,
        file_name=f"parrafo_{bib_key}.tex",
        mime="text/x-tex"
    )

    st.markdown("---")
    st.subheader("💡 Conectores Transicionales Útiles")
    st.markdown(
        """
    * **Para contrastar:** *En contraposición a los hallazgos de `\\cite{...}`...*
    * **Para complementar:** *En esta misma línea de trabajo, `\\cite{...}` demostraron que...*
    * **Para sintetizar el Gap:** *A partir de estas evidencias, se deduce que...*
    """
    )