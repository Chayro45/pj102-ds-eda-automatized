"""
EDA Automated - Aplicación principal Streamlit
Fase 1: Setup + Upload básico
"""

import streamlit as st
import pandas as pd
from utils import FileHandler, get_dataframe_info
from utils.config import (
    MAX_FILE_SIZE_MB,
    SUPPORTED_EXTENSIONS,
    PREVIEW_ROWS,
    MSG_FILE_TOO_LARGE,
    MSG_UPLOAD_SUCCESS
)


# Configuración de la página
st.set_page_config(
    page_title="EDA Automated",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("📊 EDA Automated - Análisis Exploratorio de Datos")
st.markdown("### Sistema automatizado de análisis exploratorio de datos")
st.markdown("---")


def init_session_state():
    """Inicializa el estado de la sesión"""
    if 'df' not in st.session_state:
        st.session_state.df = None
    if 'metadata' not in st.session_state:
        st.session_state.metadata = None
    if 'file_loaded' not in st.session_state:
        st.session_state.file_loaded = False


def display_sidebar():
    """Muestra el sidebar con controles"""
    with st.sidebar:
        st.header("⚙️ Configuración")
        
        st.markdown(f"""
        **Formatos soportados:**
        - {', '.join([f"{ext.upper()}" for ext in SUPPORTED_EXTENSIONS.keys()])}
        
        **Límite de tamaño:** {MAX_FILE_SIZE_MB}MB
        """)
        
        st.markdown("---")
        
        if st.session_state.file_loaded:
            st.success("✅ Dataset cargado")
            if st.button("🔄 Cargar nuevo dataset"):
                st.session_state.df = None
                st.session_state.metadata = None
                st.session_state.file_loaded = False
                st.rerun()
        else:
            st.info("📁 Esperando archivo...")


def display_upload_section():
    """Muestra la sección de carga de archivos"""
    st.header("📁 Cargar Dataset")
    
    uploaded_file = st.file_uploader(
        "Arrastra tu archivo aquí o haz clic para seleccionar",
        type=list(SUPPORTED_EXTENSIONS.keys()),
        help=f"Tamaño máximo: {MAX_FILE_SIZE_MB}MB"
    )
    
    if uploaded_file is not None:
        with st.spinner("⏳ Cargando y validando archivo..."):
            df, metadata, error = FileHandler.load_file(uploaded_file)
            
            if error:
                st.error(f"❌ {error}")
                return
            
            # Guardar en session state
            st.session_state.df = df
            st.session_state.metadata = metadata
            st.session_state.file_loaded = True
            
            st.success(MSG_UPLOAD_SUCCESS)
            st.rerun()


def display_dataset_info():
    """Muestra información básica del dataset"""
    if not st.session_state.file_loaded:
        return
    
    df = st.session_state.df
    metadata = st.session_state.metadata
    
    st.header("📋 Información del Dataset")
    
    # Metadata en columnas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Filas", f"{metadata['rows']:,}")
    with col2:
        st.metric("Columnas", metadata['columns'])
    with col3:
        st.metric("Tamaño", f"{metadata['file_size_mb']} MB")
    with col4:
        st.metric("Formato", metadata['extension'].upper())
    
    # Información adicional
    with st.expander("🔍 Detalles técnicos"):
        info_df = get_dataframe_info(df)
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("**Uso de memoria:**")
            st.text(f"{info_df['memory_usage_mb']} MB")
            
            st.markdown("**Duplicados:**")
            st.text(f"{info_df['duplicates']} filas")
        
        with col_b:
            if metadata['extension'] == 'csv':
                st.markdown("**Encoding:**")
                st.text(metadata.get('encoding', 'N/A'))
                
                st.markdown("**Separador:**")
                st.text(repr(metadata.get('separator', ',')))


def display_preview():
    """Muestra preview del dataset"""
    if not st.session_state.file_loaded:
        return
    
    df = st.session_state.df
    
    st.header("👀 Preview de Datos")
    
    # Controles de preview
    col1, col2 = st.columns([1, 4])
    
    with col1:
        num_rows = st.number_input(
            "Filas a mostrar",
            min_value=5,
            max_value=100,
            value=PREVIEW_ROWS,
            step=5
        )
    
    # Mostrar preview
    st.dataframe(
        df.head(num_rows),
        use_container_width=True,
        height=400
    )
    
    # Información de columnas
    with st.expander("📊 Tipos de datos"):
        dtypes_df = pd.DataFrame({
            'Columna': df.columns,
            'Tipo': df.dtypes.values,
            'No Nulos': df.count().values,
            '% Nulos': ((df.isnull().sum() / len(df)) * 100).round(2).values
        })
        
        st.dataframe(
            dtypes_df,
            use_container_width=True,
            hide_index=True
        )


def main():
    """Función principal"""
    init_session_state()
    display_sidebar()
    
    if not st.session_state.file_loaded:
        # Mostrar sección de upload
        display_upload_section()
        
        # Instrucciones
        st.markdown("---")
        st.markdown("""
        ### 📖 Cómo usar
        
        1. **Sube tu dataset** en formato CSV o Excel
        2. El sistema automáticamente:
           - Detectará el formato y encoding
           - Validará la estructura
           - Cargará los datos
        3. **Revisa el preview** para confirmar que todo está correcto
        
        #### 🎯 Próximas fases
        - ✅ Fase 1: Upload y validación (actual)
        - ⏳ Fase 2: Estadísticas descriptivas
        - ⏳ Fase 3: Visualizaciones
        - ⏳ Fase 4: Features avanzados
        - ⏳ Fase 5: Export y deployment
        """)
    else:
        # Mostrar información y preview
        display_dataset_info()
        st.markdown("---")
        display_preview()


if __name__ == "__main__":
    main()