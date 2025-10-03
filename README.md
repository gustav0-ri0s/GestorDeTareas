# 📝 Gestor de Tareas en Python

Este proyecto es un **gestor de tareas en consola** desarrollado en **Python** como parte del curso *Algoritmia para el Desarrollo de Programas*.  
Permite a los usuarios **crear, listar, completar y eliminar tareas**, con persistencia de datos mediante un archivo **JSON**.

---

## 🚀 Características principales
- ✅ Programación Orientada a Objetos (POO).  
- ✅ Operaciones **CRUD**: Crear, Leer, Actualizar, Eliminar.  
- ✅ Guardado automático de tareas en archivo `tareas.json`.  
- ✅ Menú interactivo para fácil uso.  
- ✅ Uso de módulos estándar: `json` y `datetime`.  

---

## 📂 Estructura del proyecto
```
GestorTareas/
│-- tareas.py          # Código principal del programa
│-- tareas.json        # Archivo generado automáticamente (persistencia de datos)
│-- README.md          # Documentación del proyecto
```

---

## ⚙️ Requisitos
- Python 3.7 o superior  
- No requiere librerías externas (solo módulos estándar de Python).  

---

## ▶️ Uso
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/GestorTareas.git
   cd GestorTareas
   ```

2. Ejecuta el programa:
   ```bash
   python tareas.py
   ```

3. Interactúa con el menú:
   ```
   --- GESTOR DE TAREAS ---
   1. Agregar tarea
   2. Ver tareas
   3. Completar tarea
   4. Eliminar tarea
   5. Salir
   ```

---

## 📷 Ejemplo de ejecución
```
--- GESTOR DE TAREAS ---
1. Agregar tarea
2. Ver tareas
3. Completar tarea
4. Eliminar tarea
5. Salir
Seleccione una opción: 1
Título: Trabajo Final
Descripción: Implementar aplicación en Python
Prioridad: Alta
Fecha límite: 10-10-2025
```

Resultado al listar:
```
1. [⏳ Pendiente] Trabajo Final | Prioridad: Alta | Vence: 10-10-2025
```

Después de completarla:
```
1. [✅ Completada] Trabajo Final | Prioridad: Alta | Vence: 10-10-2025
```

---

## 📦 Mejoras futuras
- Validación automática de fechas con `datetime`.  
- Ordenar tareas por prioridad o fecha.  
- Interfaz gráfica con Tkinter o PyQt.  
- Integración con bases de datos (SQLite, MySQL).  

---

## 👨‍💻 Autor
Proyecto desarrollado por **Gustavo Rios**  
📧 Contacto: griosq@senati.pe  

---

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo libremente para aprender o mejorar.
