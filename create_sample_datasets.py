"""
Script alternativo para generar datasets de ejemplo sin descarga de internet
Ejecutar: python create_sample_datasets.py
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Directorio de datos
DATA_DIR = Path(__file__).parent / 'data' / 'samples'
DATA_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 70)
print("🚀 Generando datasets de ejemplo para EDA Automated")
print("=" * 70)


def create_iris_dataset():
    """Crea un dataset similar a Iris"""
    print("\n📊 Creando Iris-like dataset...")
    
    np.random.seed(42)
    
    # Generar datos similares a Iris
    n_samples = 150
    
    # Setosa
    setosa = pd.DataFrame({
        'sepal_length': np.random.normal(5.0, 0.35, 50),
        'sepal_width': np.random.normal(3.4, 0.38, 50),
        'petal_length': np.random.normal(1.5, 0.17, 50),
        'petal_width': np.random.normal(0.2, 0.1, 50),
        'species': ['setosa'] * 50
    })
    
    # Versicolor
    versicolor = pd.DataFrame({
        'sepal_length': np.random.normal(5.9, 0.52, 50),
        'sepal_width': np.random.normal(2.8, 0.31, 50),
        'petal_length': np.random.normal(4.3, 0.47, 50),
        'petal_width': np.random.normal(1.3, 0.2, 50),
        'species': ['versicolor'] * 50
    })
    
    # Virginica
    virginica = pd.DataFrame({
        'sepal_length': np.random.normal(6.6, 0.64, 50),
        'sepal_width': np.random.normal(3.0, 0.32, 50),
        'petal_length': np.random.normal(5.6, 0.55, 50),
        'petal_width': np.random.normal(2.0, 0.27, 50),
        'species': ['virginica'] * 50
    })
    
    df = pd.concat([setosa, versicolor, virginica], ignore_index=True)
    
    # Redondear a 1 decimal
    for col in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:
        df[col] = df[col].round(1)
    
    output_path = DATA_DIR / 'iris.csv'
    df.to_csv(output_path, index=False)
    
    print(f"✅ Iris creado: {output_path}")
    print(f"   Shape: {df.shape}")
    return df


def create_wine_quality_dataset():
    """Crea un dataset similar a Wine Quality"""
    print("\n🍷 Creando Wine Quality-like dataset...")
    
    np.random.seed(42)
    n_samples = 1599
    
    df = pd.DataFrame({
        'fixed_acidity': np.random.uniform(4, 16, n_samples).round(2),
        'volatile_acidity': np.random.uniform(0.1, 1.6, n_samples).round(3),
        'citric_acid': np.random.uniform(0, 1, n_samples).round(2),
        'residual_sugar': np.random.uniform(0.9, 15.5, n_samples).round(2),
        'chlorides': np.random.uniform(0.01, 0.6, n_samples).round(3),
        'free_sulfur_dioxide': np.random.randint(1, 72, n_samples),
        'total_sulfur_dioxide': np.random.randint(6, 289, n_samples),
        'density': np.random.uniform(0.99, 1.01, n_samples).round(4),
        'pH': np.random.uniform(2.7, 4.0, n_samples).round(2),
        'sulphates': np.random.uniform(0.3, 2.0, n_samples).round(2),
        'alcohol': np.random.uniform(8.4, 14.9, n_samples).round(1),
        'quality': np.random.randint(3, 9, n_samples)
    })
    
    output_path = DATA_DIR / 'wine_quality.csv'
    df.to_csv(output_path, index=False)
    
    print(f"✅ Wine Quality creado: {output_path}")
    print(f"   Shape: {df.shape}")
    return df


def create_products_excel():
    """Crea un archivo Excel de productos"""
    print("\n📦 Creando Sample Products Excel...")
    
    np.random.seed(42)
    n_products = 50
    
    categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Home', 'Sports']
    
    df = pd.DataFrame({
        'product_id': range(1, n_products + 1),
        'product_name': [f'Product_{i}' for i in range(1, n_products + 1)],
        'category': np.random.choice(categories, n_products),
        'price': np.random.uniform(10, 500, n_products).round(2),
        'stock': np.random.randint(0, 100, n_products),
        'rating': np.random.uniform(1, 5, n_products).round(1),
        'sales_last_month': np.random.randint(0, 1000, n_products)
    })
    
    output_path = DATA_DIR / 'sample_products.xlsx'
    df.to_excel(output_path, index=False, engine='openpyxl')
    
    print(f"✅ Sample Products creado: {output_path}")
    print(f"   Shape: {df.shape}")
    return df


def create_broken_dataset():
    """Crea un dataset 'broken' para testing"""
    print("\n🔧 Creando Broken Dataset para testing...")
    
    data = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'name': ['Alice', 'Bob', None, 'David', 'Eve', 'Frank', 'Grace', None, 'Ivan', 'Julia'],
        'age': [25, 30, 35, None, 40, 45, 'invalid', 55, 60, 65],
        'salary': [50000, 60000, 70000, 80000, None, 100000, 110000, 120000, None, 140000],
        'constant_column': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'mixed_types': ['text', 123, 'more_text', 456.78, 'text', None, 999, 'text', 'text', 'end']
    }
    
    df = pd.DataFrame(data)
    
    # Agregar duplicados
    df = pd.concat([df, df.iloc[[0, 1]]], ignore_index=True)
    
    output_path = DATA_DIR / 'broken_dataset.csv'
    df.to_csv(output_path, index=False)
    
    print(f"✅ Broken Dataset creado: {output_path}")
    print(f"   Shape: {df.shape}")
    print(f"   Problemas incluidos:")
    print(f"   - Valores faltantes (None/NaN)")
    print(f"   - Tipos mixtos en columnas")
    print(f"   - Columna constante (zero variance)")
    print(f"   - Duplicados (2 filas)")
    print(f"   - Valor inválido en columna numérica")
    return df


def create_sales_dataset():
    """Crea un dataset de ventas más grande"""
    print("\n💰 Creando Sales Dataset...")
    
    np.random.seed(42)
    n_records = 500
    
    # Generar fechas
    dates = pd.date_range('2023-01-01', periods=n_records, freq='D')
    
    df = pd.DataFrame({
        'date': dates,
        'sales_amount': np.random.uniform(100, 10000, n_records).round(2),
        'quantity': np.random.randint(1, 100, n_records),
        'customer_id': np.random.randint(1, 50, n_records),
        'product_category': np.random.choice(['A', 'B', 'C', 'D'], n_records),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n_records),
        'discount': np.random.uniform(0, 0.3, n_records).round(2)
    })
    
    output_path = DATA_DIR / 'sales_data.csv'
    df.to_csv(output_path, index=False)
    
    print(f"✅ Sales Data creado: {output_path}")
    print(f"   Shape: {df.shape}")
    return df


def main():
    """Función principal"""
    try:
        # Crear todos los datasets
        iris = create_iris_dataset()
        wine = create_wine_quality_dataset()
        products = create_products_excel()
        broken = create_broken_dataset()
        sales = create_sales_dataset()
        
        print("\n" + "=" * 70)
        print("✅ TODOS LOS DATASETS CREADOS EXITOSAMENTE")
        print("=" * 70)
        print(f"\n📁 Ubicación: {DATA_DIR.absolute()}")
        print("\n📊 Datasets disponibles:")
        print("   1. iris.csv (150 rows, 5 columns)")
        print("   2. wine_quality.csv (1,599 rows, 12 columns)")
        print("   3. sample_products.xlsx (50 rows, 7 columns)")
        print("   4. broken_dataset.csv (12 rows, 6 columns) - Para testing")
        print("   5. sales_data.csv (500 rows, 7 columns)")
        print("\n🎯 Ahora puedes iniciar la aplicación:")
        print("   cd src")
        print("   streamlit run app.py")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()