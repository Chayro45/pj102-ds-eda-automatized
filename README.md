# 📊 EDA Automated - Sistema de Análisis Exploratorio de Datos

Sistema automatizado para realizar análisis exploratorio de datos (EDA) que genera reportes completos de cualquier dataset.

## 🎯 Fase Actual: FASE 1 - Setup + Upload Básico

### ✅ Funcionalidades Implementadas
- ✅ Carga de datasets (CSV y Excel)
- ✅ Validación automática de archivos
- ✅ Detección automática de encoding y separadores
- ✅ Preview de datos con información básica
- ✅ Interfaz Streamlit con tema oscuro
- ✅ Manejo de errores robusto

---

## 🚀 Setup del Proyecto

### 1. Crear Entorno Virtual

**En Windows:**
```bash
cd eda-automated
python -m venv env
env\Scripts\activate
```

**En Mac/Linux:**
```bash
cd eda-automated
python3 -m venv env
source env/bin/activate
```

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Generar Datasets de Prueba

```bash
python create_sample_datasets.py
```

---

## 🎮 Uso de la Aplicación

### Iniciar la Aplicación

```bash
cd src
streamlit run app.py
```

La aplicación se abrirá automáticamente en: `http://localhost:8501`

### Flujo de Uso

1. **Upload Dataset:**
   - Arrastra un archivo CSV o Excel a la zona de upload
   - O haz clic para seleccionar desde tu computadora
   
2. **Validación Automática:**
   - El sistema detecta formato, encoding y separadores
   - Valida tamaño (<50MB) y estructura
   
3. **Preview:**
   - Ve las primeras filas de tu dataset
   - Revisa información básica (shape, tipos de datos, memoria)
   - Identifica valores faltantes y duplicados

4. **Cargar Nuevo Dataset:**
   - Usa el botón "Cargar nuevo dataset" en el sidebar

---

## 📁 Estructura del Proyecto

```
eda-automated/
├── src/
│   ├── app.py                    # Aplicación Streamlit principal
│   └── utils/
│       ├── __init__.py
│       ├── config.py             # Configuración y constantes
│       └── file_handler.py       # Lógica de carga de archivos
├── data/
│   └── samples/                  # Datasets de prueba
├── outputs/                      # Reportes generados (futuro)
├── notebooks/                    # Notebooks Jupyter
├── .streamlit/
│   └── config.toml              # Configuración tema oscuro
├── requirements.txt              # Dependencias Python
├── create_sample_datasets.py     # Script generador de datos
├── test_phase1.py               # Script de testing
├── .gitignore
└── README.md
```

---

## 🧪 Testing

### Test Automático

```bash
python test_phase1.py
```

### Tests Manuales Recomendados

1. **Upload CSV:** `data/samples/iris.csv`
2. **Upload Excel:** `data/samples/sample_products.xlsx`
3. **Dataset Grande:** `data/samples/wine_quality.csv`
4. **Manejo Errores:** `data/samples/broken_dataset.csv`

---

## 🛠️ Troubleshooting

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "Cannot load Excel file"
```bash
pip install openpyxl --upgrade
```

### Puerto ocupado
```bash
streamlit run app.py --server.port 8502
```

---

## 📋 Próximas Fases

- ⏳ **Fase 2:** Análisis básico (estadísticas descriptivas)
- ⏳ **Fase 3:** Visualizaciones (histogramas, correlaciones)
- ⏳ **Fase 4:** Features avanzados (outliers, insights)
- ⏳ **Fase 5:** Export y deployment (PDF, Docker)

---

## 📝 Decisiones Técnicas

### ¿Por qué Streamlit?
- Setup rápido para prototipos
- UI profesional sin HTML/CSS
- Hot reload durante desarrollo
- Deploy sencillo

### ¿Por qué detectar encoding automáticamente?
- CSV pueden venir en diferentes encodings
- Evita errores de lectura
- Mejora UX

---

## 👨‍💻 Autor

Data Scientist Portfolio Project

**Status:** ✅ Fase 1 Completada

---

## 📜 Licencia

Proyecto educativo y de portafolio.