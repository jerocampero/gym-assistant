"""
Aplicación web Flask - Asistente de Gimnasio
"""

from flask import Flask, render_template, request, jsonify, send_file
from generador_rutinas import GeneradorRutinas
from generador_pdf import GeneradorPDF
from database import DatabaseManager
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu-clave-secreta-aqui-cambiar-en-produccion'

# Inicializar componentes
generador = GeneradorRutinas()
pdf_gen = GeneradorPDF()
db = DatabaseManager()

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/generar-rutina', methods=['POST'])
def generar_rutina():
    """
    Genera una nueva rutina basándose en el historial
    """
    try:
        # Obtener último entrenamiento
        ultimo = db.obtener_ultimo_entrenamiento()
        ultimo_tipo = ultimo['tipo_rutina'] if ultimo else None
        dias_desde_ultimo = db.calcular_dias_desde_ultimo()
        
        # Generar rutina
        rutina = generador.generar_rutina_completa(ultimo_tipo, dias_desde_ultimo)
        
        # Guardar en base de datos (opcional - se puede hacer al descargar el PDF)
        # db.guardar_entrenamiento(rutina['tipo'], rutina['nombre'])
        
        return jsonify({
            'success': True,
            'rutina': rutina,
            'dias_desde_ultimo': dias_desde_ultimo
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/descargar-pdf', methods=['POST'])
def descargar_pdf():
    """
    Genera y descarga el PDF de la rutina
    """
    try:
        data = request.get_json()
        rutina = data.get('rutina')
        
        if not rutina:
            return jsonify({'success': False, 'error': 'No se proporcionó rutina'}), 400
        
        # Generar PDF
        pdf_buffer = pdf_gen.generar_pdf_rutina(rutina)
        
        # Guardar entrenamiento en base de datos
        ejercicios_nombres = [e['nombre'] for e in rutina.get('principal', [])]
        db.guardar_entrenamiento(
            tipo_rutina=rutina['tipo'],
            nombre_rutina=rutina['nombre'],
            ejercicios=ejercicios_nombres
        )
        
        # Generar nombre de archivo
        fecha_str = datetime.now().strftime("%Y%m%d")
        filename = f"rutina_{rutina['tipo']}_{fecha_str}.pdf"
        
        return send_file(
            pdf_buffer,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=filename
        )
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/historial')
def obtener_historial():
    """
    Obtiene el historial de entrenamientos
    """
    try:
        historial = db.obtener_historial(limite=20)
        return jsonify({
            'success': True,
            'historial': historial
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health')
def health():
    """Endpoint de salud para verificar que la app está funcionando"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    # Crear directorio para templates si no existe
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    # Ejecutar app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
