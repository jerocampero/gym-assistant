"""
Script de prueba para verificar que todo funciona
"""

from generador_rutinas import GeneradorRutinas
import json

print("=" * 60)
print("PRUEBA DEL GENERADOR DE RUTINAS")
print("=" * 60)

generador = GeneradorRutinas()

# Test 1: Generar rutina sin historial previo
print("\n1. Generando primera rutina (sin historial)...")
rutina1 = generador.generar_rutina_completa(ultimo_tipo=None, dias_desde_ultimo=None)
print(f"   ✓ Tipo: {rutina1['tipo']}")
print(f"   ✓ Nombre: {rutina1['nombre']}")
print(f"   ✓ Calentamiento: {len(rutina1['calentamiento'])} ejercicios")
print(f"   ✓ Core: {len(rutina1['core'])} ejercicios")
print(f"   ✓ Principales: {len(rutina1['principal'])} ejercicios")

# Test 2: Generar rutina con rotación (días recientes)
print("\n2. Generando segunda rutina (1 día después de PUSH)...")
rutina2 = generador.generar_rutina_completa(ultimo_tipo='push', dias_desde_ultimo=1)
print(f"   ✓ Tipo: {rutina2['tipo']}")
print(f"   ✓ Debería ser diferente a 'push': {rutina2['tipo'] != 'push'}")

# Test 3: Generar rutina después de varios días
print("\n3. Generando tercera rutina (5 días después)...")
rutina3 = generador.generar_rutina_completa(ultimo_tipo='pull', dias_desde_ultimo=5)
print(f"   ✓ Tipo: {rutina3['tipo']}")

# Test 4: Verificar que los ejercicios de core están presentes
print("\n4. Verificando ejercicios de CORE...")
ejercicios_core_esperados = [
    "Deadbug con Pesa",
    "Sit-ups con Pesa (Copa)",
    "Plank Pull-Through",
    "Halo (Kettlebell o Mancuerna)",
    "Toe Touches (Toque de pies)",
    "Russian Twists (Giros rusos)"
]
core_nombres = [e['nombre'] for e in rutina1['core']]
print(f"   ✓ Ejercicios de core encontrados: {len(core_nombres)}")
for nombre in ejercicios_core_esperados:
    presente = nombre in core_nombres
    print(f"   {'✓' if presente else '✗'} {nombre}: {'Presente' if presente else 'Falta'}")

# Test 5: Verificar estructura completa
print("\n5. Verificando estructura de la rutina...")
keys_requeridas = ['tipo', 'nombre', 'descripcion', 'duracion_estimada', 'calentamiento', 'core', 'principal']
for key in keys_requeridas:
    presente = key in rutina1
    print(f"   {'✓' if presente else '✗'} {key}: {'Presente' if presente else 'Falta'}")

# Test 6: Mostrar ejemplo de ejercicio completo
print("\n6. Ejemplo de ejercicio completo:")
if rutina1['principal']:
    ej = rutina1['principal'][0]
    print(f"   Nombre: {ej['nombre']}")
    print(f"   Series: {ej['series']}")
    print(f"   Reps: {ej['reps']}")
    print(f"   Músculos: {', '.join(ej['musculos'])}")
    print(f"   Equipamiento: {ej.get('equipamiento', 'N/A')}")
    print(f"   Imagen: {ej.get('imagen_url', 'N/A')[:50]}...")

print("\n" + "=" * 60)
print("TODAS LAS PRUEBAS COMPLETADAS ✓")
print("=" * 60)

# Mostrar rutina completa en JSON (útil para debug)
print("\n\nRutina completa (JSON):")
print(json.dumps({
    'tipo': rutina1['tipo'],
    'nombre': rutina1['nombre'],
    'cantidad_ejercicios': {
        'calentamiento': len(rutina1['calentamiento']),
        'core': len(rutina1['core']),
        'principales': len(rutina1['principal'])
    }
}, indent=2, ensure_ascii=False))
