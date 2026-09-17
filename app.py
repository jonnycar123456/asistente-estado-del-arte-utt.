import streamlit as st

# Configuración principal de la aplicación
st.set_page_config(
    page_title="Asistente de Tesis UTT — Posgrado",
    page_icon="🎓",
    layout="wide"
)

# Encabezado principal
st.title("🎓 Asistente de Redacción Científica en LaTeX")
st.caption("Maestría en Ingeniería para la Optimización de Procesos de Manufactura — UTT")

# Definición de pestañas principales para los capítulos de la tesis
tab_estado_arte, tab_marco_teorico = st.tabs([
    "📖 Capítulo 1: Estado del Arte (Sección 1.1)", 
    "📚 Capítulo 2: Marco Teórico (Fundamentación)"
])

# ==============================================================================
# PESTAÑA 1: ESTADO DEL ARTE (SECCIÓN 1.1)
# ==============================================================================
with tab_estado_arte:
    st.header("📖 Generador de Párrafos Tripartitos para el Estado del Arte")
    st.markdown("""
    *Instrucciones:* Completa la ficha con la información de los artículos indexados que analizaste en tu 
    **Matriz de Revisión de Literatura**. El asistente estructurará el párrafo académico bajo la **Fórmula Tripartita** 
    *(Afirmación + Evidencia/KPI + Vacío de Conocimiento/Gap)*.
    """)
    
    col_ea1, col_ea2 = st.columns([1, 1], gap="medium")
    
    with col_ea1:
        st.subheader("📋 Datos del Artículo / Referencia")
        
        tipo_conector_ea = st.selectbox(
            "Enfoque o intención del párrafo:",
            ["Aporte Inicial / Estándar", "Enfoque Complementario", "Enfoque Contrastante"],
            key="tipo_conector_ea"
        )
        
        bib_key_ea = st.text_input("BibTeX Key (ej: Gomez2023_Evaporacion)", "Gomez2023_Evaporacion", key="bib_key_ea")
        autor_ea = st.text_input("Autor(es) y Año (para vista previa)", "Gómez et al. (2023)", key="autor_ea")
        vi_ea = st.text_input("Variable Independiente (VI)", "sistemas de evaporación térmica en lazo cerrado", key="vi_ea")
        vd_ea = st.text_input("Variable Dependiente (VD)", "la concentración de sólidos disueltos totales (TDS)", key="vd_ea")
        metodologia_ea = st.text_input("Metodología / Herramientas", "simulación termodinámica en Aspen Plus a escala banco", key="metodologia_ea")
        resultado_ea = st.text_input("Resultados / KPIs", "una remoción del 98% de contaminantes orgánicos", key="resultado_ea")
        gap_ea = st.text_input("Brecha / Límite (Gap)", "el comportamiento térmico ante flujos continuos con alta variabilidad", key="gap_ea")

    with col_ea2:
        st.subheader("✍️ Salida Generada para capitulo1.tex")

        if tipo_conector_ea == "Aporte Inicial / Estándar":
            latex_ea = f"""% --- Párrafo generado para {bib_key_ea} ---
En lo relativo a la aplicación de {vi_ea}, \\cite{{{bib_key_ea}}} desarrollaron un estudio fundamentado en {metodologia_ea} enfocado en evaluar {vd_ea}. En sus hallazgos, los autores reportaron {resultado_ea}. Sin embargo, un aspecto no considerado en dicha investigación fue {gap_ea}, lo cual demuestra la pertinencia de abordar esta variable dentro del presente trabajo de investigación.
"""
            preview_ea = f"En lo relativo a la aplicación de {vi_ea}, **{autor_ea}** desarrollaron un estudio fundamentado en {metodologia_ea} enfocado en evaluar {vd_ea}. En sus hallazgos, los autores reportaron {resultado_ea}. Sin embargo, un aspecto no considerado en dicha investigación fue {gap_ea}, lo cual demuestra la pertinencia de abordar esta variable dentro del presente trabajo de investigación."

        elif tipo_conector_ea == "Enfoque Complementario":
            latex_ea = f"""% --- Párrafo generado para {bib_key_ea} ---
En esta misma línea de trabajo, \\cite{{{bib_key_ea}}} examinaron la integración de {vi_ea} mediante {metodologia_ea}, orientándose a la optimización de {vd_ea}. Sus resultados evidenciaron {resultado_ea}. A pesar de estos avances, persiste una limitante respecto a {gap_ea}, brecha que se busca cubrir en el desarrollo del presente proyecto.
"""
            preview_ea = f"En esta misma línea de trabajo, **{autor_ea}** examinaron la integración de {vi_ea} mediante {metodologia_ea}, orientándose a la optimización de {vd_ea}. Sus resultados evidenciaron {resultado_ea}. A pesar de estos avances, persiste una limitante respecto a {gap_ea}, brecha que se busca cubrir en el desarrollo del presente proyecto."

        else: # Contrastante
            latex_ea = f"""% --- Párrafo generado para {bib_key_ea} ---
En contraposición a los abordajes tradicionales en {vi_ea}, \\cite{{{bib_key_ea}}} implementaron {metodologia_ea} para analizar su efecto sobre {vd_ea}. Si bien reportaron {resultado_ea}, el estudio omitió evaluar {gap_ea}. Dicha oportunidad de investigación justifica la formulación de la propuesta actual.
"""
            preview_ea = f"En contraposición a los abordajes tradicionales en {vi_ea}, **{autor_ea}** implementaron {metodologia_ea} para analizar su efecto sobre {vd_ea}. Si bien reportaron {resultado_ea}, el estudio omitió evaluar {gap_ea}. Dicha oportunidad de investigación justifica la formulación de la propuesta actual."

        st.markdown("**📖 Vista Previa de Lectura (Texto Plano):**")
        st.info(preview_ea)

        st.markdown("**💻 Código LaTeX:**")
        st.code(latex_ea, language="latex")

        st.download_button(
            label="📥 Descargar párrafo (.tex)",
            data=latex_ea,
            file_name=f"estado_arte_{bib_key_ea}.tex",
            mime="text/x-tex",
            key="btn_download_ea"
        )

# ==============================================================================
# PESTAÑA 2: MARCO TEÓRICO (CAPÍTULO 2)
# ==============================================================================
with tab_marco_teorico:
    st.header("📚 Generador de Subsecciones para el Capítulo 2 (Marco Teórico)")
    st.markdown("""
    *Instrucciones:* Selecciona qué sección del **Capítulo 2** deseas redactar[cite: 2]. Recuerda que el Marco Teórico 
    sustenta cuantitativa y científicamente las variables principales de tu proyecto de posgrado[cite: 2].
    """)
    
    col_mt1, col_mt2 = st.columns([1, 1], gap="medium")
    
    with col_mt1:
        st.subheader("⚙️ Configuración del Fundamento Teórico")
        
        tipo_seccion_mt = st.selectbox(
            "Selecciona la sección del Capítulo 2 a redactar:",
            [
                "2.1 Fundamentación de la Variable Independiente (VI)",
                "2.2 Fundamentación de la Variable Dependiente (VD)",
                "2.3 Intersección Teórica (Mecanismo Causal)"
            ],
            key="tipo_seccion_mt"
        )
        
        bib_key_mt = st.text_input("BibTeX Key de la Fuente Teórica (Libro/Norma/Artículo)", "Smith2019_Termodinamica", key="bib_key_mt")
        autor_mt = st.text_input("Autor o Entidad Emisora", "Smith & Van Ness (2019)", key="autor_mt")
        concepto_mt = st.text_input("Concepto, Ley, Modelo o Ecuación Principal", "Ley de Raoult y Balance de Masa", key="concepto_mt")
        
        definicion_mt = st.text_area(
            "Principio, Ley Físico-Matemática o Definición Teórica:",
            "Establece que en una solución ideal, la presión parcial de vapor de cada componente es proporcional a su fracción molar en la fase líquida.",
            key="definicion_mt"
        )
        
        aplicacion_mt = st.text_input(
            "¿Cómo se aplica o modela en tu proyecto de tesis?",
            "dimensionar el comportamiento térmico en la columna de separación de fases",
            key="aplicacion_mt"
        )

    with col_mt2:
        st.subheader("✍️ Salida Generada para capitulo2.tex")
        
        if "2.1" in tipo_seccion_mt:
            latex_mt = f"""% --- Subsección 2.1: Sustento de la VI ---
\\subsection{{{concepto_mt}}}
\\label{{sec:vi_{bib_key_mt}}}

El sustento técnico y teórico de la Variable Independiente se fundamenta en {concepto_mt}. De acuerdo con \\cite{{{bib_key_mt}}}, este principio se define formalmente como:

\\begin{{quote}}
``{definicion_mt}''
\\end{{quote}}

En el desarrollo de la presente tesis, la formulación matemática de este modelo permite {aplicacion_mt}, garantizando la precisión operativa de la propuesta tecnológica.
"""
            preview_mt = f"El sustento técnico de la Variable Independiente se fundamenta en **{concepto_mt}**. De acuerdo con **{autor_mt}**, este principio establece que: '{definicion_mt}'. En esta investigación, dicho modelo permite {aplicacion_mt}."

        elif "2.2" in tipo_seccion_mt:
            latex_mt = f"""% --- Subsección 2.2: Sustento de la VD ---
\\subsection{{{concepto_mt}}}
\\label{{sec:vd_{bib_key_mt}}}

Para la evaluación cuantitativa de la Variable Dependiente, se adopta como estándar de referencia {concepto_mt}. Como exponen \\cite{{{bib_key_mt}}}, la métrica principal queda expresada como:

\\begin{{quote}}
``{definicion_mt}''
\\end{{quote}}

La integración de este indicador formaliza la medición de desempeño en el proyecto, permitiendo {aplicacion_mt} bajo criterios normativos e industriales comparables.
"""
            preview_mt = f"Para la evaluación cuantitativa de la Variable Dependiente, se adopta como estándar **{concepto_mt}**. Como exponen **{autor_mt}**, la métrica establece que: '{definicion_mt}'. Este indicador se aplica para {aplicacion_mt}."

        else: # 2.3 Intersección Teórica
            latex_mt = f"""% --- Subsección 2.3: Intersección Teórica ---
\\subsection{{Mecanismo Causal: {concepto_mt}}}
\\label{{sec:interseccion_{bib_key_mt}}}

La relación de causa-efecto entre las variables de estudio se explica a través de {concepto_mt}. Según los fundamentos consolidados por \\cite{{{bib_key_mt}}}, el mecanismo de interacción sostiene que:

\\begin{{quote}}
``{definicion_mt}''
\\end{{quote}}

Este postulado teórico demuestra que la modificación controlada de la Variable Independiente impactará directamente sobre la Variable Dependiente, justificando la viabilidad científica de {aplicacion_mt}.
"""
            preview_mt = f"La relación de causa-efecto entre las variables se explica a través de **{concepto_mt}**. Según **{autor_mt}**: '{definicion_mt}'. Este postulado demuestra que al modificar la causa se impactará directamente la Variable Dependiente, logrando {aplicacion_mt}."

        st.markdown("**📖 Vista Previa de Lectura (Texto Plano):**")
        st.info(preview_mt)

        st.markdown("**💻 Código LaTeX:**")
        st.code(latex_mt, language="latex")

        st.download_button(
            label="📥 Descargar subsección (.tex)",
            data=latex_mt,
            file_name=f"marco_teorico_{bib_key_mt}.tex",
            mime="text/x-tex",
            key="btn_download_mt"
        )

# Pie de página informativo
st.markdown("---")
st.caption("💡 *Tip para los alumnos:* Una vez descargados los archivos `.tex`, recuerden subirlos a su carpeta de proyecto en Overleaf o VS Code e incluirlos mediante la sintaxis `\\input{nombre_archivo.tex}`.")