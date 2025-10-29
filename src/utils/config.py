"""
Configuración y constantes del proyecto EDA Automated
"""

# Límites de archivos
MAX_FILE_SIZE_MB = 50
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

# Tipos de archivo soportados
SUPPORTED_EXTENSIONS = {
    'csv': 'CSV (Comma Separated Values)',
    'xlsx': 'Excel (XLSX)',
}

# Configuración de lectura CSV
CSV_ENCODINGS = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
CSV_SEPARATORS = [',', ';', '\t', '|']

# Configuración de preview
PREVIEW_ROWS = 10

# Mensajes
MSG_FILE_TOO_LARGE = f"⚠️ El archivo excede el límite de {MAX_FILE_SIZE_MB}MB"
MSG_UNSUPPORTED_FORMAT = "⚠️ Formato de archivo no soportado"
MSG_UPLOAD_SUCCESS = "✅ Archivo cargado exitosamente"
MSG_UPLOAD_ERROR = "❌ Error al cargar el archivo"

# Tema Streamlit (oscuro)
THEME_CONFIG = {
    "primaryColor": "#FF4B4B",
    "backgroundColor": "#0E1117",
    "secondaryBackgroundColor": "#262730",
    "textColor": "#FAFAFA",
    "font": "sans serif"
}