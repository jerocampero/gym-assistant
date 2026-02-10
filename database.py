"""
Base de datos para trackear historial de entrenamientos
"""

import sqlite3
from datetime import datetime
import json

class DatabaseManager:
    def __init__(self, db_path='gym_history.db'):
        self.db_path = db_path
        self._crear_tablas()
    
    def _crear_tablas(self):
        """Crea las tablas necesarias si no existen"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entrenamientos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                tipo_rutina TEXT NOT NULL,
                nombre_rutina TEXT,
                ejercicios_realizados TEXT,
                notas TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def guardar_entrenamiento(self, tipo_rutina, nombre_rutina, ejercicios=None, notas=None):
        """Guarda un nuevo entrenamiento en la base de datos"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        ejercicios_json = json.dumps(ejercicios) if ejercicios else None
        
        cursor.execute('''
            INSERT INTO entrenamientos (tipo_rutina, nombre_rutina, ejercicios_realizados, notas)
            VALUES (?, ?, ?, ?)
        ''', (tipo_rutina, nombre_rutina, ejercicios_json, notas))
        
        conn.commit()
        entrenamiento_id = cursor.lastrowid
        conn.close()
        
        return entrenamiento_id
    
    def obtener_ultimo_entrenamiento(self):
        """Obtiene el último entrenamiento registrado"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, fecha, tipo_rutina, nombre_rutina, ejercicios_realizados, notas
            FROM entrenamientos
            ORDER BY fecha DESC
            LIMIT 1
        ''')
        
        resultado = cursor.fetchone()
        conn.close()
        
        if resultado:
            return {
                'id': resultado[0],
                'fecha': resultado[1],
                'tipo_rutina': resultado[2],
                'nombre_rutina': resultado[3],
                'ejercicios': json.loads(resultado[4]) if resultado[4] else None,
                'notas': resultado[5]
            }
        return None
    
    def obtener_historial(self, limite=10):
        """Obtiene el historial de entrenamientos"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, fecha, tipo_rutina, nombre_rutina
            FROM entrenamientos
            ORDER BY fecha DESC
            LIMIT ?
        ''', (limite,))
        
        resultados = cursor.fetchall()
        conn.close()
        
        historial = []
        for r in resultados:
            historial.append({
                'id': r[0],
                'fecha': r[1],
                'tipo_rutina': r[2],
                'nombre_rutina': r[3]
            })
        
        return historial
    
    def calcular_dias_desde_ultimo(self):
        """Calcula cuántos días pasaron desde el último entrenamiento"""
        ultimo = self.obtener_ultimo_entrenamiento()
        
        if not ultimo:
            return None
        
        fecha_ultimo = datetime.strptime(ultimo['fecha'], '%Y-%m-%d %H:%M:%S')
        dias = (datetime.now() - fecha_ultimo).days
        
        return dias
