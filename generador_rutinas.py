"""
Generador de rutinas inteligente
Este módulo decide qué rutina crear basándose en:
- Cuándo fue el último entrenamiento
- Qué grupos musculares se trabajaron
- Rotación para evitar sobreentrenamiento
"""

import random
from datetime import datetime, timedelta
from ejercicios_db import (
    EJERCICIOS_CORE,
    EJERCICIOS_PUSH,
    EJERCICIOS_PULL,
    EJERCICIOS_PIERNAS,
    EJERCICIOS_MOVILIDAD
)

class GeneradorRutinas:
    def __init__(self):
        # Rotación de tipos de entrenamiento
        self.tipos_rotacion = ['push', 'pull', 'piernas']
        
    def decidir_tipo_rutina(self, ultimo_tipo, dias_desde_ultimo):
        """
        Decide qué tipo de rutina hacer hoy
        Si pasaron más de 3 días, puede repetir el mismo tipo
        Si no, rota al siguiente
        """
        if dias_desde_ultimo is None or dias_desde_ultimo >= 3:
            # Si pasó mucho tiempo, elige aleatoriamente
            return random.choice(self.tipos_rotacion)
        
        # Si fue reciente, rota al siguiente tipo
        if ultimo_tipo in self.tipos_rotacion:
            idx = self.tipos_rotacion.index(ultimo_tipo)
            siguiente_idx = (idx + 1) % len(self.tipos_rotacion)
            return self.tipos_rotacion[siguiente_idx]
        
        return random.choice(self.tipos_rotacion)
    
    def generar_rutina_push(self):
        """
        Rutina de empuje: Pecho, Hombros, Tríceps
        """
        rutina = {
            "tipo": "push",
            "nombre": "Día de Empuje (Pecho, Hombros, Tríceps)",
            "descripcion": "Enfoque en movimientos de empuje para tren superior",
            "duracion_estimada": "50-60 minutos",
            "calentamiento": random.sample(EJERCICIOS_MOVILIDAD, 2),
            "core": EJERCICIOS_CORE.copy(),
            "principal": []
        }
        
        # Seleccionar ejercicios de pecho (2 ejercicios)
        ejercicios_pecho = [e for e in EJERCICIOS_PUSH if 'pecho' in e['musculos']]
        rutina["principal"].extend(random.sample(ejercicios_pecho, 2))
        
        # Seleccionar ejercicios de hombros (2 ejercicios)
        ejercicios_hombros = [e for e in EJERCICIOS_PUSH if 'hombros' in e['musculos']]
        rutina["principal"].extend(random.sample(ejercicios_hombros, 2))
        
        # Seleccionar ejercicios de tríceps (1-2 ejercicios)
        ejercicios_triceps = [e for e in EJERCICIOS_PUSH if 'tríceps' in e['musculos'] and 'pecho' not in e['musculos']]
        rutina["principal"].extend(random.sample(ejercicios_triceps, min(2, len(ejercicios_triceps))))
        
        return rutina
    
    def generar_rutina_pull(self):
        """
        Rutina de tracción: Espalda, Bíceps
        """
        rutina = {
            "tipo": "pull",
            "nombre": "Día de Tracción (Espalda, Bíceps)",
            "descripcion": "Enfoque en movimientos de tracción para tren superior",
            "duracion_estimada": "50-60 minutos",
            "calentamiento": random.sample(EJERCICIOS_MOVILIDAD, 2),
            "core": EJERCICIOS_CORE.copy(),
            "principal": []
        }
        
        # Seleccionar ejercicios de espalda (3 ejercicios)
        ejercicios_espalda = [e for e in EJERCICIOS_PULL if 'espalda' in str(e['musculos'])]
        rutina["principal"].extend(random.sample(ejercicios_espalda, min(3, len(ejercicios_espalda))))
        
        # Seleccionar ejercicios de bíceps (2 ejercicios)
        ejercicios_biceps = [e for e in EJERCICIOS_PULL if 'bíceps' in e['musculos'] and 'espalda' not in str(e['musculos'])]
        rutina["principal"].extend(random.sample(ejercicios_biceps, min(2, len(ejercicios_biceps))))
        
        return rutina
    
    def generar_rutina_piernas(self):
        """
        Rutina de piernas completa
        """
        rutina = {
            "tipo": "piernas",
            "nombre": "Día de Piernas",
            "descripcion": "Entrenamiento completo de tren inferior",
            "duracion_estimada": "50-60 minutos",
            "calentamiento": random.sample(EJERCICIOS_MOVILIDAD, 2),
            "core": EJERCICIOS_CORE.copy(),
            "principal": []
        }
        
        # Ejercicio compuesto principal (sentadilla o peso muerto)
        ejercicios_compuestos = [e for e in EJERCICIOS_PIERNAS if e['nombre'] in ['Sentadillas con Barra', 'Peso Muerto Rumano', 'Prensa de Piernas']]
        rutina["principal"].append(random.choice(ejercicios_compuestos))
        
        # Ejercicios accesorios (4-5 ejercicios variados)
        ejercicios_accesorios = [e for e in EJERCICIOS_PIERNAS if e not in rutina["principal"]]
        rutina["principal"].extend(random.sample(ejercicios_accesorios, min(4, len(ejercicios_accesorios))))
        
        return rutina
    
    def generar_rutina_completa(self, ultimo_tipo=None, dias_desde_ultimo=None):
        """
        Genera una rutina completa basándose en el historial
        """
        tipo_hoy = self.decidir_tipo_rutina(ultimo_tipo, dias_desde_ultimo)
        
        if tipo_hoy == 'push':
            return self.generar_rutina_push()
        elif tipo_hoy == 'pull':
            return self.generar_rutina_pull()
        else:
            return self.generar_rutina_piernas()
