"""
Script de testing para validar Fase 1
Ejecutar desde la raíz del proyecto: python test_phase1.py
"""

import sys
import os
from pathlib import Path

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

print("=" * 70)
print("🧪 TESTING FASE 1 - EDA Automated")
print("=" * 70)

# Test 1: Imports
print("\n[1/6] Testing imports...")
try:
    from utils import FileHandler, get_dataframe_info
    from utils.config import MAX_FILE_SIZE_MB, SUPPORTED_EXTENSIONS
    import pandas as pd
    import streamlit as st
    print("✅ Todos los imports exitosos")
except Exception as e:
    print(f"❌ Error en imports: {e}")
    sys.exit(1)

# Test 2: Estructura de directorios
print("\n[2/6] Verificando estructura de directorios...")
required_dirs = [
    'src/utils',
    'data/samples',
    'outputs',
    'notebooks',
    '.streamlit'
]

all_exist = True
for dir_path in required_dirs:
    full_path = Path(__file__).parent / dir_path
    if full_path.exists():
        print(f"  ✅ {dir_path}")
    else:
        print(f"  ⚠️  {dir_path} - NO EXISTE (crear si es necesario)")
        all_exist = False

# Test 3: Archivos críticos
print("\n[3/6] Verificando archivos críticos...")
required_files = [
    'requirements.txt',
    'src/app.py',
    'src/utils/file_handler.py',
    'src/utils/config.py',
    '.streamlit/config.toml'
]

all_exist = True
for file_path in required_files:
    full_path = Path(__file__).parent / file_path
    if full_path.exists():
        print(f"  ✅ {file_path}")
    else:
        print(f"  ❌ {file_path} - NO EXISTE")
        all_exist = False

if not all_exist:
    print("❌ Archivos críticos faltan!")
    sys.exit(1)

# Test 4: FileHandler functionality
print("\n[4/6] Testing FileHandler...")
try:
    # Test validación de extensión
    assert FileHandler.validate_file_extension("test.csv") == True
    assert FileHandler.validate_file_extension("test.xlsx") == True
    assert FileHandler.validate_file_extension("test.txt") == False
    print("  ✅ Validación de extensiones funciona")
    
    # Test get_dataframe_info
    df_test = pd.DataFrame({
        'A': [1, 2, 3, None],
        'B': ['a', 'b', 'c', 'd']
    })
    info = get_dataframe_info(df_test)
    assert 'shape' in info
    assert 'memory_usage_mb' in info
    assert 'missing_values' in info
    print("  ✅ get_dataframe_info funciona")
    
    print("✅ FileHandler funcionando correctamente")
except Exception as e:
    print(f"❌ Error en FileHandler: {e}")
    sys.exit(1)

# Test 5: Datasets
print("\n[5/6] Verificando datasets de prueba...")
data_dir = Path(__file__).parent / 'data' / 'samples'

if not data_dir.exists():
    print(f"⚠️  Directorio {data_dir} no existe")
    print("   Ejecuta: python create_sample_datasets.py")
else:
    datasets = list(data_dir.glob('*.csv')) + list(data_dir.glob('*.xlsx'))
    
    if len(datasets) == 0:
        print("⚠️  No hay datasets en data/samples/")
        print("   Ejecuta: python create_sample_datasets.py")
    else:
        print(f"  ✅ {len(datasets)} datasets encontrados:")
        for ds in datasets:
            size = ds.stat().st_size / 1024  # KB
            print(f"     - {ds.name} ({size:.1f} KB)")

# Test 6: Configuración Streamlit
print("\n[6/6] Verificando configuración Streamlit...")
config_file = Path(__file__).parent / '.streamlit' / 'config.toml'
if config_file.exists():
    with open(config_file) as f:
        content = f.read()
        if 'backgroundColor' in content and '0E1117' in content:
            print("  ✅ Tema oscuro configurado")
        else:
            print("  ⚠️  Configuración de tema incompleta")
else:
    print("  ❌ config.toml no existe")

# Resumen final
print("\n" + "=" * 70)
print("📊 RESUMEN DE TESTING")
print("=" * 70)
print("\n✅ FASE 1 LISTA PARA USAR\n")
print("Próximos pasos:")
print("  1. Descarga datasets (si no lo hiciste):")
print("     python create_sample_datasets.py")
print("")
print("  2. Inicia la aplicación:")
print("     cd src")
print("     streamlit run app.py")
print("")
print("  3. Prueba con los datasets en data/samples/")
print("")
print("💡 Si todo funciona, estás listo para Fase 2!")
print("=" * 70)