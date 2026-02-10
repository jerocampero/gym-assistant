"""
Generador de PDFs
Crea PDFs profesionales con imágenes de ejercicios
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from io import BytesIO
import requests
from PIL import Image as PILImage
from datetime import datetime

class GeneradorPDF:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Configurar estilos personalizados para el PDF"""
        # Título principal
        self.styles.add(ParagraphStyle(
            name='TituloPrincipal',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#2C3E50'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Subtítulo
        self.styles.add(ParagraphStyle(
            name='Subtitulo',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#34495E'),
            spaceAfter=12,
            spaceBefore=20,
            fontName='Helvetica-Bold'
        ))
        
        # Texto normal
        self.styles.add(ParagraphStyle(
            name='TextoNormal',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=colors.HexColor('#2C3E50'),
            spaceAfter=12
        ))
        
        # Nombre de ejercicio
        self.styles.add(ParagraphStyle(
            name='NombreEjercicio',
            parent=self.styles['Heading3'],
            fontSize=13,
            textColor=colors.HexColor('#16A085'),
            spaceAfter=6,
            fontName='Helvetica-Bold'
        ))
    
    def _descargar_imagen(self, url, max_width=2*inch, max_height=1.5*inch):
        """
        Descarga una imagen desde URL y la redimensiona
        """
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                img_data = BytesIO(response.content)
                pil_img = PILImage.open(img_data)
                
                # Redimensionar manteniendo aspect ratio
                pil_img.thumbnail((int(max_width * 2), int(max_height * 2)), PILImage.Resampling.LANCZOS)
                
                # Guardar en BytesIO
                output = BytesIO()
                pil_img.save(output, format='PNG')
                output.seek(0)
                
                return Image(output, width=max_width, height=max_height)
            else:
                return None
        except Exception as e:
            print(f"Error descargando imagen {url}: {e}")
            return None
    
    def _crear_seccion_ejercicio(self, ejercicio, mostrar_imagen=True):
        """
        Crea una sección para un ejercicio individual
        """
        elementos = []
        
        # Nombre del ejercicio
        nombre = Paragraph(f"<b>{ejercicio['nombre']}</b>", self.styles['NombreEjercicio'])
        elementos.append(nombre)
        
        # Detalles del ejercicio
        detalles = f"<b>Series:</b> {ejercicio['series']} | <b>Repeticiones:</b> {ejercicio['reps']}"
        if ejercicio.get('equipamiento'):
            detalles += f" | <b>Equipamiento:</b> {ejercicio['equipamiento']}"
        
        detalles_p = Paragraph(detalles, self.styles['TextoNormal'])
        elementos.append(detalles_p)
        
        # Imagen del ejercicio
        if mostrar_imagen and ejercicio.get('imagen_url'):
            img = self._descargar_imagen(ejercicio['imagen_url'])
            if img:
                elementos.append(Spacer(1, 0.1*inch))
                elementos.append(img)
        
        elementos.append(Spacer(1, 0.2*inch))
        
        return elementos
    
    def generar_pdf_rutina(self, rutina, fecha=None):
        """
        Genera un PDF completo de la rutina
        """
        if fecha is None:
            fecha = datetime.now()
        
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter,
                              rightMargin=0.75*inch, leftMargin=0.75*inch,
                              topMargin=0.75*inch, bottomMargin=0.75*inch)
        
        elementos = []
        
        # Encabezado
        titulo = Paragraph(f"<b>Rutina de Gimnasio</b>", self.styles['TituloPrincipal'])
        elementos.append(titulo)
        
        fecha_str = fecha.strftime("%d de %B, %Y")
        fecha_p = Paragraph(f"<i>Generado el {fecha_str}</i>", self.styles['TextoNormal'])
        elementos.append(fecha_p)
        elementos.append(Spacer(1, 0.3*inch))
        
        # Información de la rutina
        info = f"<b>{rutina['nombre']}</b><br/>{rutina['descripcion']}<br/>Duración estimada: {rutina['duracion_estimada']}"
        info_p = Paragraph(info, self.styles['TextoNormal'])
        elementos.append(info_p)
        elementos.append(Spacer(1, 0.3*inch))
        
        # Calentamiento
        elementos.append(Paragraph("<b>CALENTAMIENTO Y MOVILIDAD</b>", self.styles['Subtitulo']))
        for ejercicio in rutina.get('calentamiento', []):
            elementos.extend(self._crear_seccion_ejercicio(ejercicio, mostrar_imagen=True))
        
        elementos.append(Spacer(1, 0.2*inch))
        
        # Core (siempre presente)
        elementos.append(Paragraph("<b>ENTRENAMIENTO DE CORE</b>", self.styles['Subtitulo']))
        nota_core = Paragraph("<i>Estos ejercicios son parte fundamental de tu rutina y se realizan en cada sesión</i>", 
                             self.styles['TextoNormal'])
        elementos.append(nota_core)
        elementos.append(Spacer(1, 0.1*inch))
        
        for ejercicio in rutina.get('core', []):
            elementos.extend(self._crear_seccion_ejercicio(ejercicio, mostrar_imagen=True))
        
        elementos.append(Spacer(1, 0.2*inch))
        
        # Ejercicios principales
        elementos.append(Paragraph("<b>EJERCICIOS PRINCIPALES</b>", self.styles['Subtitulo']))
        for ejercicio in rutina.get('principal', []):
            elementos.extend(self._crear_seccion_ejercicio(ejercicio, mostrar_imagen=True))
        
        # Notas finales
        elementos.append(Spacer(1, 0.3*inch))
        elementos.append(Paragraph("<b>NOTAS IMPORTANTES:</b>", self.styles['Subtitulo']))
        
        notas = """
        • Asegurate de hacer un calentamiento adecuado antes de empezar<br/>
        • Mantené buena forma en todos los ejercicios, calidad sobre cantidad<br/>
        • Descansá 60-90 segundos entre series para ejercicios principales<br/>
        • Descansá 30-45 segundos entre series de core<br/>
        • Mantenete hidratado durante toda la sesión<br/>
        • Si algún ejercicio causa dolor (no fatiga muscular), consultá con un profesional
        """
        
        notas_p = Paragraph(notas, self.styles['TextoNormal'])
        elementos.append(notas_p)
        
        # Construir PDF
        doc.build(elementos)
        
        buffer.seek(0)
        return buffer
