¡Perfecto! Aquí tienes la versión actualizada del proyecto **Conversor de Unidades Inteligente** incluyendo el archivo `agente.py` que actúa como el "cerebro" del asistente, coordinando todas las acciones.

## 📁 Estructura actualizada del proyecto

```
conversor_unidades/
│
├── agente.py               # NUEVO: Agente IA que coordina todo (cerebro del programa)
├── database.py             # Funciones para la base de datos
├── conversiones.py         # Funciones de conversión y fórmulas
├── main.py                 # Programa principal (interfaz con usuario)
├── historial.db            # Base de datos SQLite (se crea sola)
│
└── LEEME.txt               # Descripción del proyecto
```

---

## 🗄️ Base de datos
**`historial.db`** (se genera automáticamente)

---

## 📄 LEEME.txt (actualizado)

```text
========================================
CONVERSOR DE UNIDADES INTELIGENTE
========================================

DESCRIPCIÓN:
Este programa simula un AGENTE DE IA BÁSICO que actúa como asistente
inteligente de conversión de unidades. El agente (agente.py) es el
"cerebro" que coordina todo el programa.

FUNCIONALIDADES:
- Convertir entre diferentes unidades (longitud, masa, volumen)
- Ver la fórmula matemática utilizada en cada conversión
- Guardar automáticamente un historial de todas las conversiones
- El agente toma decisiones y responde como un asistente virtual

NIVEL: Principiante (estudiante de preparatoria)
LENGUAJE: Python (sin programación orientada a objetos)
TECNOLOGÍAS: SQLite, programación estructurada (funciones, if, while)

ESTRUCTURA DEL PROGRAMA:
- agente.py: Agente IA que coordina todo (toma decisiones)
- database.py: Maneja el almacenamiento en base de datos
- conversiones.py: Contiene las fórmulas matemáticas
- main.py: Interfaz con el usuario (menús)

REQUISITOS:
- Tener Python instalado (versión 3.6 o superior)
- No se necesita instalar librerías externas

CÓMO USARLO:
1. Ejecuta el archivo main.py
2. El agente te dará la bienvenida
3. Elige una categoría de conversión
4. Selecciona unidades y valor
5. El agente muestra el resultado y la fórmula
6. Todo queda guardado en historial.db

FÓRMULAS UTILIZADAS:
- Longitud: metros como unidad base (1 km = 1000 m, 1 cm = 0.01 m)
- Masa: kilogramos como unidad base (1 g = 0.001 kg, 1 lb = 0.453592 kg)
- Volumen: litros como unidad base (1 mL = 0.001 L, 1 m³ = 1000 L)

PERSONALIDAD DEL AGENTE:
El agente.py actúa como un asistente virtual amigable que:
- Saluda al usuario
- Explica lo que hace
- Confirma las acciones
- Se despide al final
```

---

## 🐍 Código completo actualizado

### 1. `agente.py` (NUEVO - El cerebro del programa)

```python
import database
import conversiones

# Este es el AGENTE DE IA que coordina todo el programa
# El agente toma decisiones y actúa como un asistente virtual

def agente_responder(mensaje, tipo="normal"):
    """El agente responde con diferentes estilos según el tipo de mensaje"""
    if tipo == "saludo":
        print("\n🤖 [AGENTE] ¡Hola! Soy tu asistente inteligente de conversiones.")
        print("🤖 [AGENTE] Estoy aquí para ayudarte a convertir unidades y guardar tu historial.")
        print("🤖 [AGENTE] ¿En qué puedo ayudarte hoy?")
    elif tipo == "error":
        print(f"🤖 [AGENTE] 😅 Lo siento, {mensaje}")
    elif tipo == "exito":
        print(f"🤖 [AGENTE] ✅ ¡Perfecto! {mensaje}")
    elif tipo == "info":
        print(f"🤖 [AGENTE] ℹ️ {mensaje}")
    elif tipo == "despedida":
        print("\n🤖 [AGENTE] ¡Gracias por usar el Conversor de Unidades!")
        print("🤖 [AGENTE] He guardado todas tus conversiones en la base de datos.")
        print("🤖 [AGENTE] ¡Hasta luego! 👋")
    else:
        print(f"🤖 [AGENTE] {mensaje}")

def agente_validar_opcion(opcion, minimo, maximo):
    """El agente valida si la opción elegida es correcta"""
    if opcion < minimo or opcion > maximo:
        agente_responder(f"La opción {opcion} no es válida. Debes elegir entre {minimo} y {maximo}.", "error")
        return False
    return True

def agente_mostrar_menu():
    """El agente muestra el menú principal con su estilo"""
    print("\n" + "="*60)
    print("🤖 AGENTE INTELIGENTE DE CONVERSIONES")
    print("="*60)
    print("📋 OPCIONES DISPONIBLES:")
    print("   1️⃣  Convertir LONGITUD (metros, km, cm)")
    print("   2️⃣  Convertir MASA (kg, gramos, libras)")
    print("   3️⃣  Convertir VOLUMEN (litros, mL, m³)")
    print("   4️⃣  Ver HISTORIAL de conversiones")
    print("   5️⃣  SALIR del programa")
    print("="*60)

def agente_solicitar_datos(categoria):
    """El agente solicita los datos necesarios para la conversión"""
    agente_responder(f"Vamos a convertir {categoria}.", "info")
    print()
    
    # Definir unidades según categoría
    if categoria == "Longitud":
        unidades = ["m", "km", "cm"]
        convertir_func = conversiones.convertir_longitud
    elif categoria == "Masa":
        unidades = ["kg", "g", "lb"]
        convertir_func = conversiones.convertir_masa
    else:  # Volumen
        unidades = ["L", "mL", "m3"]
        convertir_func = conversiones.convertir_volumen
    
    # Mostrar unidades disponibles
    agente_responder(f"Unidades disponibles para {categoria}:")
    for i, unidad in enumerate(unidades, 1):
        print(f"   {i}. {unidad}")
    
    # Obtener unidad de origen
    while True:
        try:
            opcion = int(input("\n🤖 ¿Cuál es la unidad ORIGEN? (elige 1, 2 o 3): "))
            if 1 <= opcion <= len(unidades):
                desde = unidades[opcion - 1]
                break
            else:
                agente_responder(f"Elige un número entre 1 y {len(unidades)}", "error")
        except ValueError:
            agente_responder("Debes ingresar un número válido", "error")
    
    # Obtener unidad de destino
    while True:
        try:
            opcion = int(input("🤖 ¿Cuál es la unidad DESTINO? (elige 1, 2 o 3): "))
            if 1 <= opcion <= len(unidades):
                hasta = unidades[opcion - 1]
                break
            else:
                agente_responder(f"Elige un número entre 1 y {len(unidades)}", "error")
        except ValueError:
            agente_responder("Debes ingresar un número válido", "error")
    
    # Obtener valor a convertir
    while True:
        try:
            valor = float(input(f"🤖 Ingresa el valor en {desde}: "))
            if valor < 0:
                agente_responder("El valor debe ser positivo", "error")
            else:
                break
        except ValueError:
            agente_responder("Debes ingresar un número válido", "error")
    
    return categoria, desde, hasta, valor, convertir_func

def agente_realizar_conversion(categoria, desde, hasta, valor, convertir_func):
    """El agente ejecuta la conversión y muestra el resultado"""
    agente_responder("Procesando tu conversión...", "info")
    
    # Realizar conversión
    resultado, formula = convertir_func(valor, desde, hasta)
    
    if resultado is None:
        agente_responder(f"No se pudo realizar la conversión: {formula}", "error")
        return None, None
    
    # Mostrar resultado con estilo de agente
    print("\n" + "="*60)
    print("🤖 [AGENTE] ¡Aquí está tu resultado!")
    print("="*60)
    print(f"   📊 {valor} {desde} = {resultado} {hasta}")
    print(f"\n   📐 {formula}")
    print("="*60)
    
    agente_responder(f"He convertido {valor} {desde} a {resultado} {hasta}.", "exito")
    
    # Guardar en historial
    database.guardar_conversion(categoria, valor, desde, resultado, hasta, formula)
    agente_responder("Tu conversión ha sido guardada en el historial.", "exito")
    
    return resultado, formula

def agente_mostrar_historial():
    """El agente muestra el historial de conversiones"""
    agente_responder("Consultando tu historial de conversiones...", "info")
    
    conexion = database.obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute('''
        SELECT fecha, categoria, valor_original, unidad_origen,
               valor_convertido, unidad_destino, formula
        FROM conversiones
        ORDER BY id DESC
        LIMIT 10
    ''')
    
    resultados = cursor.fetchall()
    conexion.close()
    
    if not resultados:
        agente_responder("No hay conversiones guardadas todavía. ¡Realiza tu primera conversión!", "info")
        return
    
    print("\n" + "="*60)
    print("🤖 [AGENTE] Aquí están tus últimas 10 conversiones:")
    print("="*60)
    
    for i, conv in enumerate(resultados, 1):
        print(f"\n📌 Conversión #{i}")
        print(f"   📅 Fecha: {conv[0]}")
        print(f"   📂 Categoría: {conv[1]}")
        print(f"   🔄 {conv[2]} {conv[3]} → {conv[4]} {conv[5]}")
        print(f"   📐 Fórmula: {conv[6]}")
    
    print("\n" + "="*60)
    agente_responder("Este es tu historial completo.", "exito")
```

---

### 2. `database.py` (actualizado para trabajar con el agente)

```python
import sqlite3
from datetime import datetime

def obtener_conexion():
    """Obtiene la conexión a la base de datos"""
    return sqlite3.connect("historial.db")

def crear_tabla():
    """Crea la tabla de historial si no existe"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversiones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            categoria TEXT,
            valor_original REAL,
            unidad_origen TEXT,
            valor_convertido REAL,
            unidad_destino TEXT,
            formula TEXT
        )
    ''')
    
    conexion.commit()
    conexion.close()

def guardar_conversion(categoria, valor_original, unidad_origen, 
                       valor_convertido, unidad_destino, formula):
    """Guarda una conversión en el historial"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO conversiones (fecha, categoria, valor_original, 
                                  unidad_origen, valor_convertido, 
                                  unidad_destino, formula)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (fecha_actual, categoria, valor_original, unidad_origen,
          valor_convertido, unidad_destino, formula))
    
    conexion.commit()
    conexion.close()
```

---

### 3. `conversiones.py` (sin cambios, pero se incluye completo)

```python
def convertir_longitud(valor, desde, hasta):
    """Convierte entre metros (m), kilómetros (km), centímetros (cm)"""
    # Primero convertimos todo a metros
    if desde == "m":
        en_metros = valor
    elif desde == "km":
        en_metros = valor * 1000
    elif desde == "cm":
        en_metros = valor / 100
    else:
        return None, "Unidad no válida"
    
    # Luego convertimos de metros a la unidad destino
    if hasta == "m":
        resultado = en_metros
        formula = f"{valor} {desde} = {valor} × {_obtener_factor(desde, 'm')} = {en_metros} m"
    elif hasta == "km":
        resultado = en_metros / 1000
        formula = f"{valor} {desde} = {valor} × {_obtener_factor(desde, 'm')} = {en_metros} m, luego ÷ 1000 = {resultado} km"
    elif hasta == "cm":
        resultado = en_metros * 100
        formula = f"{valor} {desde} = {valor} × {_obtener_factor(desde, 'm')} = {en_metros} m, luego × 100 = {resultado} cm"
    else:
        return None, "Unidad no válida"
    
    return resultado, formula

def _obtener_factor(origen, destino_en_metros):
    """Factor de conversión a metros (uso interno)"""
    factores = {"m": 1, "km": 1000, "cm": 0.01}
    return factores.get(origen, 1)

def convertir_masa(valor, desde, hasta):
    """Convierte entre kilogramos (kg), gramos (g), libras (lb)"""
    # Primero convertimos todo a kilogramos
    if desde == "kg":
        en_kg = valor
    elif desde == "g":
        en_kg = valor / 1000
    elif desde == "lb":
        en_kg = valor * 0.453592
    else:
        return None, "Unidad no válida"
    
    # Luego convertimos de kg a la unidad destino
    if hasta == "kg":
        resultado = en_kg
        formula = f"{valor} {desde} = {en_kg} kg"
    elif hasta == "g":
        resultado = en_kg * 1000
        formula = f"{valor} {desde} = {en_kg} kg × 1000 = {resultado} g"
    elif hasta == "lb":
        resultado = en_kg / 0.453592
        formula = f"{valor} {desde} = {en_kg} kg ÷ 0.453592 = {resultado:.4f} lb"
    else:
        return None, "Unidad no válida"
    
    return resultado, formula

def convertir_volumen(valor, desde, hasta):
    """Convierte entre litros (L), mililitros (mL), metros cúbicos (m³)"""
    # Primero convertimos todo a litros
    if desde == "L":
        en_litros = valor
    elif desde == "mL":
        en_litros = valor / 1000
    elif desde == "m3":
        en_litros = valor * 1000
    else:
        return None, "Unidad no válida"
    
    # Luego convertimos de litros a la unidad destino
    if hasta == "L":
        resultado = en_litros
        formula = f"{valor} {desde} = {en_litros} L"
    elif hasta == "mL":
        resultado = en_litros * 1000
        formula = f"{valor} {desde} = {en_litros} L × 1000 = {resultado} mL"
    elif hasta == "m3":
        resultado = en_litros / 1000
        formula = f"{valor} {desde} = {en_litros} L ÷ 1000 = {resultado} m³"
    else:
        return None, "Unidad no válida"
    
    return resultado, formula
```

---

### 4. `main.py` (simplificado - ahora usa al agente)

```python
import database
import agente

def main():
    """Función principal - el programa usa al agente como coordinador"""
    
    # El agente prepara la base de datos
    database.crear_tabla()
    
    # El agente saluda al usuario
    agente.agente_responder("", "saludo")
    
    # Bucle principal del programa
    while True:
        # El agente muestra el menú
        agente.agente_mostrar_menu()
        
        # El usuario elige una opción
        try:
            opcion = int(input("\n🤖 ¿Qué deseas hacer? (1-5): "))
        except ValueError:
            agente.agente_responder("Por favor, ingresa un número válido (1-5)", "error")
            continue
        
        # El agente procesa la opción
        if opcion == 1:
            # Conversión de longitud
            categoria, desde, hasta, valor, convertir_func = agente.agente_solicitar_datos("Longitud")
            agente.agente_realizar_conversion(categoria, desde, hasta, valor, convertir_func)
            input("\n🤖 Presiona Enter para continuar...")
            
        elif opcion == 2:
            # Conversión de masa
            categoria, desde, hasta, valor, convertir_func = agente.agente_solicitar_datos("Masa")
            agente.agente_realizar_conversion(categoria, desde, hasta, valor, convertir_func)
            input("\n🤖 Presiona Enter para continuar...")
            
        elif opcion == 3:
            # Conversión de volumen
            categoria, desde, hasta, valor, convertir_func = agente.agente_solicitar_datos("Volumen")
            agente.agente_realizar_conversion(categoria, desde, hasta, valor, convertir_func)
            input("\n🤖 Presiona Enter para continuar...")
            
        elif opcion == 4:
            # Ver historial
            agente.agente_mostrar_historial()
            input("\n🤖 Presiona Enter para continuar...")
            
        elif opcion == 5:
            # Salir - el agente se despide
            agente.agente_responder("", "despedida")
            break
            
        else:
            agente.agente_responder(f"La opción {opcion} no es válida. Elige entre 1 y 5.", "error")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
```

---

## ▶️ Cómo ejecutarlo

1. **Crea la carpeta del proyecto:**
   ```
   conversor_unidades/
   ```

2. **Guarda los 5 archivos dentro de la carpeta:**
   - `agente.py` (el cerebro)
   - `database.py` (la memoria)
   - `conversiones.py` (las fórmulas)
   - `main.py` (la interfaz)
   - `LEEME.txt` (la documentación)

3. **Abre una terminal en la carpeta `conversor_unidades`**

4. **Ejecuta el programa:**
   ```bash
   python main.py
   ```

---

## 🎯 ¿Qué hace cada archivo?

| Archivo | Rol | Función |
|---------|-----|---------|
| **agente.py** | 🤖 El cerebro | Toma decisiones, se comunica con el usuario, coordina todo |
| **main.py** | 🎮 El controlador | Solo inicia el programa y llama al agente |
| **database.py** | 💾 La memoria | Guarda y recupera datos de la base de datos |
| **conversiones.py** | 📐 Las matemáticas | Contiene todas las fórmulas de conversión |
| **historial.db** | 🗄️ Datos | Base de datos SQLite (se crea sola) |

---

## 🌟 Características del agente

El `agente.py` simula un asistente de IA porque:

1. **Saluda al usuario** de manera amigable
2. **Explica lo que hace** antes de cada acción
3. **Valida las entradas** y da mensajes de error claros
4. **Confirma las acciones exitosas**
5. **Mantiene una personalidad consistente** (usa emojis y un estilo de diálogo)
6. **Se despide** al finalizar el programa

¡Así tienes un proyecto completo con un agente IA simulado, ideal para un estudiante de preparatoria! 🚀
