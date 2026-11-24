# =============================================================================
# TABLERO INTERACTIVO: HISTORIA DE LA MINERÍA ILEGAL EN COLOMBIA
# Desarrollado para la clase de Economía
# =============================================================================
import streamlit as st
import pandas as pd
# Configuración de página de Streamlit
st.set_page_config(
    page_title="Minería Ilegal en Colombia - Tablero Educativo",
    layout="wide",
    initial_sidebar_state="expanded"
)
# =============================================================================
# SECCIÓN: MENÚ LATERAL DE NAVEGACIÓN
# =============================================================================
with st.sidebar:
    st.header("⛏️ Minería e Historia")
    opcion_menu = st.radio(
        "Seleccione un módulo pedagógico:",
        [
            "1. Introducción y Conceptos",
            "2. El Triángulo de Galtung y Minería",
            "3. Línea de Tiempo: Ciclos del Oro y Gemas",
            "4. Base de Datos Comparativa",
            "5. ¿Por qué se repite la historia?"
        ]
    )
    st.write("---")
    st.info("💡 *Consejo para la clase:* Analicen cómo las bonanzas económicas interactúan con la debilidad estatal para perpetuar la informalidad y el daño ambiental.")
# =============================================================================
# SECCIÓN: CONTROL DE PÁGINAS (LÓGICA CONDICIONAL)
# =============================================================================

# -----------------------------------------------------------------------------
# MÓDULO 1: INTRODUCCIÓN
# -----------------------------------------------------------------------------
if opcion_menu == "1. Introducción y Conceptos":
    st.title("Minería Ilegal e Informal en Colombia")
    st.subheader("Perspectiva Histórica, Social y Económica")
    st.markdown("""
    Este tablero digital interactivo analiza la evolución histórica de la explotación de recursos minerales en Colombia,
    conectando las realidades económicas del oro, esmeraldas y carbón con los impactos socioambientales y el conflicto armado.

    ### Objetivos del Aprendizaje:
    - **Comprender** la transición de la minería de la época colonial a la era de las retroexcavadoras modernas.
    - **Analizar** el impacto de la minería ilegal sobre los ecosistemas y la salud comunitaria (mercurio, deforestación).
    - **Evaluar** la relación histórica entre los recursos naturales de alto valor y la financiación de grupos armados.
    """)

# -----------------------------------------------------------------------------
# MÓDULO 2: EL TRIÁNGULO DE GALTUNG (ADAPTADO A MINERÍA)
# -----------------------------------------------------------------------------
elif opcion_menu == "2. El Triángulo de Galtung y Minería":
    st.title("🔺 El Triángulo de Galtung aplicado a la Minería Ilegal")
    st.write("Analiza las tres dimensiones de la violencia en el contexto de la explotación de minerales en Colombia.")

    col1, col2, col3 = st.columns(3)
    with col1:
        boton_directa = st.button("💥 Violencia Directa", use_container_width=True)
    with col2:
        boton_estructural = st.button("🏗️ Violencia Estructural", use_container_width=True)
    with col3:
        boton_cultural = st.button("🧠 Violencia Cultural", use_container_width=True)
    st.write("---")

    if boton_directa:
        st.error("### Violencia Directa\nEnfrentamientos armados por el control de las minas, extorsiones o \"vacunas\" a mineros, masacres, desplazamiento forzado de comunidades étnicas y rurales, y financiamiento directo de insurgencias o bandas criminales.")
    elif boton_estructural:
        st.warning("### Violencia Estructural\nFalta de oportunidades en regiones remotas, ausencia de mecanismos ágiles de formalización para mineros tradicionales y exclusión económica que empuja a comunidades al sustento informal sin garantías de salud ni seguridad.")
    elif boton_cultural:
        st.info("### Violencia Cultural\nLa normalización del contrabando de oro arraigada desde la Colonia, la justificación del daño ambiental como \"único medio de supervivencia\" y la legitimación social de las economías subterráneas en zonas con nula presencia del Estado.")
    else:
        st.caption("👈 Haz clic en cualquiera de los tres botones de arriba para desplegar el análisis conceptual de la minería.")

# -----------------------------------------------------------------------------
# MÓDULO 3: LÍNEA DE TIEMPO HISTÓRICA
# -----------------------------------------------------------------------------
elif opcion_menu == "3. Línea de Tiempo: Ciclos del Oro y Gemas":
    st.title("⏳ Evolución Histórica de la Minería en Colombia")
    periodo = st.select_slider(
        "Arrastra el marcador para navegar por los periodos históricos clave:",
        options=[
            "1500-1810: Colonia",
            "1810-1950: República",
            "1970-1990: Esmeraldas",
            "1990-2000: Guerrilla y Paramilitares",
            "2001-2012: Boom del Oro",
            "2013-2019: Convenio Minamata",
            "2020-Hoy: Amazonía y Delito"
        ]
    )
    st.write("---")

    if "Colonia" in periodo:
        st.subheader("Colonia: Oro, contrabando y esclavitud")
        st.markdown("**Contexto:** La Corona cobraba el \"quinto real\" sobre el oro; evadirlo con contrabando fue común en Antioquia, Chocó y Popayán.\n- **Social:** Explotación y esclavización de indígenas y africanos.\n- **Económico:** Evasión de impuestos y salida sistemática de riqueza.\n- **Ambiental:** Primeros desvíos de ríos y minería de aluvión en el Pacífico.")
    elif "República" in periodo:
        st.subheader("República: Informalidad y minería artesanal")
        st.markdown("**Contexto:** Persisten el barequeo y la minería de aluvión sin un control estatal efectivo en Chocó, Antioquia y Cauca.\n- **Económico:** Economía informal generalizada y baja captación fiscal estatal.\n- **Ambiental:** Sedimentación paulatina de los ríos y pérdida de cauces naturales.\n- **Social:** Comunidades rurales altamente dependientes de una actividad sin garantías.")
    elif "Esmeraldas" in periodo:
        st.subheader("Esmeraldas y primeras economías ilegales")
        st.markdown("**Contexto:** La \"guerra verde\" en Boyacá y Cundinamarca desata violencia extrema por el control de minas de esmeraldas.\n- **Violencia:** Disputas armadas entre clanes por el control de minas y rutas.\n- **Social:** Desplazamiento y férreo control territorial ejercido por actores ilegales.\n- **Económico:** Dinámicas iniciales de lavado de dinero y surgimiento de economías paralelas.")
    elif "Guerrilla" in periodo:
        st.subheader("Financiación de grupos armados")
        st.markdown("**Contexto:** En el sur de Bolívar, Bajo Cauca y Pacífico, las guerrillas y paramilitares cobran \"vacunas\" y se disputan el oro.\n- **Violencia:** Extorsiones sistemáticas, masacres y disputas de fronteras invisibles.\n- **Social:** Desplazamiento forzado de comunidades étnicas y campesinas.\n- **Ambiental:** Expansión descontrolada de dragas en los principales ríos.")
    elif "Boom" in periodo:
        st.subheader("Boom del oro y retroexcavadoras")
        st.markdown("**Contexto:** El alza internacional del precio del oro y la llegada de maquinaria pesada multiplican la minería ilegal. El Estado responde con el Decreto 2235 de 2012 (destrucción de maquinaria).\n- **Ambiental:** Deforestación masiva, destrucción de cauces y pérdida irreparable de suelos.\n- **Salud:** Contaminación severa con mercurio en peces y agua de consumo.\n- **Violencia:** Consolidación de bandas criminales y grupos armados en zonas mineras.")
    elif "Minamata" in periodo:
        st.subheader("Mercurio, Minamata y Río Atrato")
        st.markdown("**Contexto:** Se aprueba la Ley 1658 de 2013 para eliminar el mercurio. En 2016, la Sentencia T-622 declara al río Atrato sujeto de derechos. En 2018 se ratifica el Convenio de Minamata (Ley 1892).\n- **Salud:** Intoxicaciones masivas por mercurio en el Pacífico y el Bajo Cauca.\n- **Ambiental:** Contaminación crítica de grandes cuencas fluviales.\n- **Social:** Conflictos con comunidades étnicas por la defensa de sus territorios ancestrales.")
    elif "Amazonía" in periodo:
        st.subheader("Amazonía, dragas y delitos ambientales")
        st.markdown("**Contexto:** La minería se expande a ríos amazónicos y parques naturales. La Ley 2111 de 2021 tipifica los delitos ambientales con mayor rigor.\n- **Ambiental:** Deforestación y dragado ilegal en áreas de alta biodiversidad protegida.\n- **Violencia:** Estructuras transnacionales y disidencias se financian con el oro.\n- **Económico:** El oro ilegal se blanquea y se mezcla en los circuitos de exportación formal.")

# -----------------------------------------------------------------------------
# MÓDULO 4: BASE DE DATOS COMPARATIVA
# -----------------------------------------------------------------------------
elif opcion_menu == "4. Base de Datos Comparativa":
    st.title("📊 Indicadores del Impacto de la Minería por Periodo")
    st.write("Matriz histórica comparativa de los efectos socioeconómicos y ambientales de la explotación minera:")

    datos_mineria = {
        "Periodo": ["Colonia (1500-1810)", "República (1810-1950)", "Economías Ilegales (1970-2000)", "Boom y Regulación (2001-Presente)"],
        "Impuesto / Captación": ["Quinto Real (Frecuente evasión)", "Baja captación fiscal", "Nulo (Lavado y extorsión)", "Regalías vs. Pérdida por Ilegalidad"],
        "Impacto Ambiental": ["Desvío local de ríos de aluvión", "Sedimentación de ríos en Cauca", "Uso descontrolado de dragas", "Deforestación crítica y mercurio"],
        "Población Afectada": ["Indígenas y esclavizados", "Comunidades tradicionales", "Campesinos desplazados", "Comunidades étnicas (Atrato/Amazonía)"]
    }

    df = pd.DataFrame(datos_mineria)
    st.dataframe(df, use_container_width=True)

    st.markdown("""
    💡 *Preguntas para el debate:*
    - Analice cómo los mecanismos de evasión tributaria (desde el Quinto Real hasta el lavado de activos actual) afectan la capacidad del Estado para invertir en el desarrollo de estas regiones.
    """)

# -----------------------------------------------------------------------------
# MÓDULO 5: ¿POR QUÉ SE RECOGE ESTE CICLO EN LA HISTORIA?
# -----------------------------------------------------------------------------
elif opcion_menu == "5. ¿Por qué se repite la historia?":
    st.title("🤔 Las Razones del Ciclo de Repetición")
    st.write("Analicemos los 5 factores estructurantes que perpetúan la minería ilegal en Colombia:")

    st.markdown("""
    1. **Ciclo de Bonanza:** Cada vez que el precio internacional del oro o metales preciosos sube, se incrementa exponencialmente el incentivo para la explotación ilegal y la introducción de maquinaria pesada.
    2. **Debilidad Estatal en Zonas Remotas:** La ausencia de instituciones fuertes en las regiones periféricas crea vacíos de poder que son rápidamente copados por actores criminales o armados.
    3. **Financiación de Actores Armados:** Los recursos de alto valor y fácil transporte (históricamente las esmeraldas y hoy el oro) sustituyen o complementan al narcotráfico como motor de guerra.
    4. **Daño Ambiental Acumulado:** Las regiones afectadas siguen siendo las mismas a lo largo de siglos (Chocó, Antioquia, Bolívar y Cauca), concentrando la degradación de suelos y ríos.
    5. **Informalidad Histórica:** La gran masa de mineros ancestrales y tradicionales carece de herramientas de capacitación, recursos y facilidades burocráticas para lograr una formalización efectiva.
    """)
