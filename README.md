# 💪 Asistente de Gimnasio

Aplicación web personalizada para generar rutinas de gimnasio inteligentes basadas en tu historial de entrenamientos.

## 🎯 Características

- **Rutinas Personalizadas**: Genera rutinas que rotan entre tren superior (push/pull) y tren inferior
- **Core Siempre Presente**: Tus ejercicios de abdominales favoritos en cada sesión
- **Rotación Inteligente**: Evita entrenar los mismos grupos musculares consecutivamente
- **PDFs con Imágenes**: Descarga rutinas en PDF con imágenes demostrativas de cada ejercicio
- **Historial de Entrenamientos**: Trackea todos tus entrenamientos
- **Interfaz Simple**: Diseño limpio y fácil de usar

## 🚀 Instalación Local

### Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

2. **Ejecutar la aplicación**
```bash
python app.py
```

3. **Abrir en el navegador**
```
http://localhost:5000
```

## 📱 Cómo Usar

1. **Abrir la app** en tu navegador
2. **Click en "Generar Rutina de Hoy"** - La app decide automáticamente qué tipo de rutina hacer basándose en tu último entrenamiento
3. **Revisar la rutina** - Verás calentamiento, core y ejercicios principales
4. **Descargar PDF** - Guarda el PDF en tu teléfono para llevarlo al gym
5. **¡A entrenar!** 💪

## 🔧 Configuración

### Personalizar Ejercicios

Editá `ejercicios_db.py` para:
- Agregar nuevos ejercicios
- Modificar series/repeticiones
- Cambiar URLs de imágenes
- Adaptar a tu equipamiento

### Modificar Rotación

Editá `generador_rutinas.py` para cambiar:
- Tipos de rutinas
- Cantidad de ejercicios por grupo muscular
- Lógica de rotación

## 🌐 Deployment en Render (Gratis)

### Paso 1: Crear cuenta en Render
1. Andá a [render.com](https://render.com)
2. Registrate con tu cuenta de GitHub

### Paso 2: Subir código a GitHub
1. Creá un repositorio en GitHub
2. Subí todos los archivos del proyecto:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <tu-repo-url>
git push -u origin main
```

### Paso 3: Deploy en Render
1. En Render, click en "New +" → "Web Service"
2. Conectá tu repositorio de GitHub
3. Configuración:
   - **Name**: gym-assistant (o el que quieras)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Plan**: Free

4. Click "Create Web Service"

¡Listo! En unos minutos tendrás tu app online 24/7 gratis.

## 📊 Estructura del Proyecto

```
gym-assistant/
├── app.py                 # Aplicación Flask principal
├── ejercicios_db.py       # Base de datos de ejercicios
├── generador_rutinas.py   # Lógica de generación de rutinas
├── generador_pdf.py       # Generador de PDFs
├── database.py            # Manejo de base de datos SQLite
├── requirements.txt       # Dependencias Python
├── templates/
│   └── index.html        # Interfaz web
├── static/
│   ├── css/
│   │   └── style.css     # Estilos
│   └── js/
│       └── app.js        # Lógica frontend
└── gym_history.db        # Base de datos (se crea automáticamente)
```

## 🎨 Personalización

### Cambiar Colores
Editá `static/css/style.css` y modificá:
- Gradiente principal: `background: linear-gradient(...)`
- Color de botones: `.btn-primary { background: ... }`

### Agregar Más Tipos de Rutinas
1. Agregá ejercicios en `ejercicios_db.py`
2. Creá nueva función en `generador_rutinas.py`
3. Agregá el tipo a la rotación

## 🐛 Troubleshooting

**Error: ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**Error al descargar imágenes**
- Verificá tu conexión a internet
- Las URLs de imágenes pueden cambiar, actualizalas en `ejercicios_db.py`

**La base de datos no se crea**
- Verificá permisos de escritura en el directorio
- La base de datos se crea automáticamente al primer uso

## 🔜 Próximas Mejoras

- [ ] Agregar temporizador para descansos entre series
- [ ] Exportar rutina a Google Calendar
- [ ] Gráficos de progreso
- [ ] Sistema de logros y streaks
- [ ] Integración con Strava/Apple Health

## 📝 Notas

- La app usa imágenes de ejercicios de fuentes públicas (Inspire USA Foundation)
- Los PDFs incluyen las imágenes descargadas en tiempo real
- El historial se guarda localmente en SQLite

## 🤝 Contribuciones

Este proyecto fue creado específicamente para tus necesidades. Podés modificarlo como quieras.

---

**¡Buen entrenamiento! 💪🔥**
