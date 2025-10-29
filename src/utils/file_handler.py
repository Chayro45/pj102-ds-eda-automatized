"""
Módulo para manejo de carga y validación de archivos
"""

import pandas as pd
import chardet
from io import BytesIO
from typing import Tuple, Optional
from .config import (
    MAX_FILE_SIZE_BYTES,
    CSV_ENCODINGS,
    CSV_SEPARATORS,
    SUPPORTED_EXTENSIONS
)


class FileHandler:
    """Maneja la carga y validación de datasets"""
    
    @staticmethod
    def validate_file_size(file) -> bool:
        """
        Valida que el tamaño del archivo esté dentro del límite
        
        Args:
            file: Archivo subido (UploadedFile de Streamlit)
            
        Returns:
            bool: True si es válido, False si excede el límite
        """
        return file.size <= MAX_FILE_SIZE_BYTES
    
    @staticmethod
    def validate_file_extension(filename: str) -> bool:
        """
        Valida que la extensión del archivo sea soportada
        
        Args:
            filename: Nombre del archivo
            
        Returns:
            bool: True si es soportado, False si no
        """
        extension = filename.split('.')[-1].lower()
        return extension in SUPPORTED_EXTENSIONS
    
    @staticmethod
    def detect_encoding(file_bytes: bytes) -> str:
        """
        Detecta el encoding de un archivo
        
        Args:
            file_bytes: Bytes del archivo
            
        Returns:
            str: Encoding detectado
        """
        result = chardet.detect(file_bytes)
        detected_encoding = result['encoding']
        
        # Si no detecta o tiene baja confianza, usar utf-8
        if not detected_encoding or result['confidence'] < 0.7:
            return 'utf-8'
        
        return detected_encoding
    
    @staticmethod
    def detect_csv_separator(file_bytes: bytes, encoding: str) -> str:
        """
        Detecta el separador de un archivo CSV
        
        Args:
            file_bytes: Bytes del archivo
            encoding: Encoding del archivo
            
        Returns:
            str: Separador detectado
        """
        # Leer las primeras líneas
        sample = file_bytes[:1024].decode(encoding, errors='ignore')
        
        # Contar ocurrencias de cada separador
        separator_counts = {sep: sample.count(sep) for sep in CSV_SEPARATORS}
        
        # Retornar el más frecuente
        return max(separator_counts, key=separator_counts.get)
    
    @staticmethod
    def load_csv(file, encoding: Optional[str] = None) -> Tuple[pd.DataFrame, dict]:
        """
        Carga un archivo CSV
        
        Args:
            file: Archivo subido
            encoding: Encoding a usar (opcional)
            
        Returns:
            Tuple[pd.DataFrame, dict]: DataFrame y metadata
        """
        file_bytes = file.read()
        file.seek(0)  # Reset pointer
        
        # Detectar encoding si no se proporciona
        if encoding is None:
            encoding = FileHandler.detect_encoding(file_bytes)
        
        # Detectar separador
        separator = FileHandler.detect_csv_separator(file_bytes, encoding)
        
        # Intentar cargar con diferentes encodings
        for enc in [encoding] + CSV_ENCODINGS:
            try:
                df = pd.read_csv(
                    BytesIO(file_bytes),
                    sep=separator,
                    encoding=enc,
                    low_memory=False
                )
                
                metadata = {
                    'encoding': enc,
                    'separator': separator,
                    'rows': len(df),
                    'columns': len(df.columns),
                    'file_size_mb': round(file.size / (1024 * 1024), 2)
                }
                
                return df, metadata
                
            except Exception as e:
                continue
        
        raise ValueError(f"No se pudo cargar el archivo CSV con ningún encoding")
    
    @staticmethod
    def load_excel(file) -> Tuple[pd.DataFrame, dict]:
        """
        Carga un archivo Excel
        
        Args:
            file: Archivo subido
            
        Returns:
            Tuple[pd.DataFrame, dict]: DataFrame y metadata
        """
        df = pd.read_excel(file, engine='openpyxl')
        
        metadata = {
            'rows': len(df),
            'columns': len(df.columns),
            'file_size_mb': round(file.size / (1024 * 1024), 2)
        }
        
        return df, metadata
    
    @staticmethod
    def load_file(file) -> Tuple[Optional[pd.DataFrame], Optional[dict], Optional[str]]:
        """
        Carga un archivo (CSV o Excel) automáticamente
        
        Args:
            file: Archivo subido (UploadedFile de Streamlit)
            
        Returns:
            Tuple[Optional[pd.DataFrame], Optional[dict], Optional[str]]: 
                DataFrame, metadata, y mensaje de error (None si todo OK)
        """
        # Validar tamaño
        if not FileHandler.validate_file_size(file):
            return None, None, "El archivo excede el límite de tamaño"
        
        # Validar extensión
        if not FileHandler.validate_file_extension(file.name):
            return None, None, f"Formato no soportado. Use: {', '.join(SUPPORTED_EXTENSIONS.keys())}"
        
        try:
            extension = file.name.split('.')[-1].lower()
            
            if extension == 'csv':
                df, metadata = FileHandler.load_csv(file)
            elif extension == 'xlsx':
                df, metadata = FileHandler.load_excel(file)
            else:
                return None, None, "Formato no reconocido"
            
            # Agregar metadata adicional
            metadata['filename'] = file.name
            metadata['extension'] = extension
            
            return df, metadata, None
            
        except Exception as e:
            return None, None, f"Error al cargar archivo: {str(e)}"


def get_dataframe_info(df: pd.DataFrame) -> dict:
    """
    Obtiene información básica del DataFrame
    
    Args:
        df: DataFrame de pandas
        
    Returns:
        dict: Información del DataFrame
    """
    info = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'memory_usage_mb': round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2),
        'missing_values': df.isnull().sum().to_dict(),
        'duplicates': df.duplicated().sum()
    }
    
    return info