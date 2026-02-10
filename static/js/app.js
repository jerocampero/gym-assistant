// Estado de la aplicación
let rutinaActual = null;

// Elementos del DOM
const btnGenerar = document.getElementById('btn-generar');
const btnDescargarPDF = document.getElementById('btn-descargar-pdf');
const btnNuevaRutina = document.getElementById('btn-nueva-rutina');
const welcomeSection = document.getElementById('welcome-section');
const rutinaSection = document.getElementById('rutina-section');
const loadingSection = document.getElementById('loading');
const historialContainer = document.getElementById('historial-container');

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    cargarHistorial();
    btnGenerar.addEventListener('click', generarRutina);
    btnDescargarPDF.addEventListener('click', descargarPDF);
    btnNuevaRutina.addEventListener('click', nuevaRutina);
});

// Función para generar rutina
async function generarRutina() {
    try {
        // Mostrar loading
        mostrarSeccion('loading');
        
        // Llamar al API
        const response = await fetch('/api/generar-rutina', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) {
            throw new Error('Error al generar rutina');
        }
        
        const data = await response.json();
        
        if (data.success) {
            rutinaActual = data.rutina;
            mostrarRutina(data.rutina, data.dias_desde_ultimo);
        } else {
            throw new Error(data.error || 'Error desconocido');
        }
        
    } catch (error) {
        console.error('Error:', error);
        alert('Hubo un error al generar la rutina. Por favor, intentá de nuevo.');
        mostrarSeccion('welcome');
    }
}

// Función para mostrar la rutina generada
function mostrarRutina(rutina, diasDesdeUltimo) {
    // Actualizar header
    document.getElementById('rutina-nombre').textContent = rutina.nombre;
    document.getElementById('rutina-descripcion').textContent = rutina.descripcion;
    document.getElementById('rutina-duracion').textContent = rutina.duracion_estimada;
    
    // Mostrar calentamiento
    const calentamientoContainer = document.getElementById('ejercicios-calentamiento');
    calentamientoContainer.innerHTML = '';
    rutina.calentamiento.forEach(ejercicio => {
        calentamientoContainer.appendChild(crearEjercicioElement(ejercicio));
    });
    
    // Mostrar core
    const coreContainer = document.getElementById('ejercicios-core');
    coreContainer.innerHTML = '';
    rutina.core.forEach(ejercicio => {
        coreContainer.appendChild(crearEjercicioElement(ejercicio));
    });
    
    // Mostrar principales
    const principalesContainer = document.getElementById('ejercicios-principales');
    principalesContainer.innerHTML = '';
    rutina.principal.forEach(ejercicio => {
        principalesContainer.appendChild(crearEjercicioElement(ejercicio));
    });
    
    // Mostrar sección de rutina
    mostrarSeccion('rutina');
}

// Función para crear elemento de ejercicio
function crearEjercicioElement(ejercicio) {
    const div = document.createElement('div');
    div.className = 'ejercicio-item';
    
    const nombre = document.createElement('div');
    nombre.className = 'ejercicio-nombre';
    nombre.textContent = ejercicio.nombre;
    
    const detalles = document.createElement('div');
    detalles.className = 'ejercicio-detalles';
    detalles.innerHTML = `<strong>Series:</strong> ${ejercicio.series} | <strong>Reps:</strong> ${ejercicio.reps}`;
    
    if (ejercicio.equipamiento) {
        detalles.innerHTML += ` | <strong>Equipamiento:</strong> ${ejercicio.equipamiento}`;
    }
    
    const musculos = document.createElement('div');
    musculos.className = 'ejercicio-musculos';
    if (ejercicio.musculos && ejercicio.musculos.length > 0) {
        musculos.textContent = `Músculos: ${ejercicio.musculos.join(', ')}`;
    }
    
    div.appendChild(nombre);
    div.appendChild(detalles);
    if (ejercicio.musculos && ejercicio.musculos.length > 0) {
        div.appendChild(musculos);
    }
    
    return div;
}

// Función para descargar PDF
async function descargarPDF() {
    if (!rutinaActual) {
        alert('No hay rutina para descargar');
        return;
    }
    
    try {
        btnDescargarPDF.disabled = true;
        btnDescargarPDF.textContent = '⏳ Generando PDF...';
        
        const response = await fetch('/api/descargar-pdf', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                rutina: rutinaActual
            })
        });
        
        if (!response.ok) {
            throw new Error('Error al generar PDF');
        }
        
        // Descargar el archivo
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        
        const fecha = new Date().toISOString().split('T')[0];
        a.download = `rutina_${rutinaActual.tipo}_${fecha}.pdf`;
        
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
        
        // Recargar historial
        cargarHistorial();
        
    } catch (error) {
        console.error('Error:', error);
        alert('Hubo un error al generar el PDF. Por favor, intentá de nuevo.');
    } finally {
        btnDescargarPDF.disabled = false;
        btnDescargarPDF.textContent = '📄 Descargar PDF';
    }
}

// Función para generar nueva rutina
function nuevaRutina() {
    mostrarSeccion('welcome');
    rutinaActual = null;
}

// Función para cargar historial
async function cargarHistorial() {
    try {
        const response = await fetch('/api/historial');
        const data = await response.json();
        
        if (data.success && data.historial.length > 0) {
            historialContainer.innerHTML = '';
            data.historial.forEach(item => {
                const div = document.createElement('div');
                div.className = 'historial-item';
                
                const tipo = document.createElement('span');
                tipo.className = 'historial-tipo';
                tipo.textContent = item.nombre_rutina || item.tipo_rutina;
                
                const fecha = document.createElement('span');
                fecha.className = 'historial-fecha';
                fecha.textContent = formatearFecha(item.fecha);
                
                div.appendChild(tipo);
                div.appendChild(fecha);
                historialContainer.appendChild(div);
            });
        } else {
            historialContainer.innerHTML = '<p class="text-muted">Aún no tenés entrenamientos registrados</p>';
        }
    } catch (error) {
        console.error('Error cargando historial:', error);
        historialContainer.innerHTML = '<p class="text-muted">Error al cargar historial</p>';
    }
}

// Función para formatear fecha
function formatearFecha(fechaStr) {
    const fecha = new Date(fechaStr);
    const ahora = new Date();
    const diff = Math.floor((ahora - fecha) / (1000 * 60 * 60 * 24));
    
    if (diff === 0) {
        return 'Hoy';
    } else if (diff === 1) {
        return 'Ayer';
    } else if (diff < 7) {
        return `Hace ${diff} días`;
    } else {
        return fecha.toLocaleDateString('es-AR', { 
            day: 'numeric', 
            month: 'short',
            year: 'numeric'
        });
    }
}

// Función para mostrar secciones
function mostrarSeccion(seccion) {
    welcomeSection.style.display = 'none';
    rutinaSection.style.display = 'none';
    loadingSection.style.display = 'none';
    
    switch(seccion) {
        case 'welcome':
            welcomeSection.style.display = 'block';
            break;
        case 'rutina':
            rutinaSection.style.display = 'block';
            break;
        case 'loading':
            loadingSection.style.display = 'block';
            break;
    }
}
