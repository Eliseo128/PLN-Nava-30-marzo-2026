Perfecto. Aquí tienes la estructura completa del proyecto **Conversor de Unidades Inteligente**, pensada para un estudiante de preparatoria, sin programación orientada a objetos, con explicaciones claras.

## 📁 Estructura del proyecto

```
conversor_unidades/
│
├── main.py                 # Programa principal (menú y lógica)
├── database.py             # Funciones para la base de datos
├── conversiones.py         # Funciones de conversión y fórmulas
├── historial.db            # Base de datos SQLite (se crea sola)
│
└── LEEME.txt               # Descripción del proyecto
```

---

## 🗄️ Nombre de la base de datos
**`historial.db`**

---

## 📄 LEEME.txt

```text
========================================
CONVERSOR DE UNIDADES INTELIGENTE
========================================

DESCRIPCIÓN:
Este programa es un asistente de conversión de unidades que te permite:
- Convertir entre diferentes unidades (longitud, masa, volumen)
- Ver la fórmula matemática utilizada en cada conversión
- Guardar automáticamente un historial de todas las conversiones

NIVEL: Principiante (estudiante de preparatoria)
LENGUAJE: Python (sin programación orientada a objetos)
TECNOLOGÍAS: SQLite, programación estructurada (funciones, if, while)

REQUISITOS:
- Tener Python instalado (versión 3.6 o superior)
- No se necesita instalar librerías externas (solo se usa sqlite3 que viene con Python)

CÓMO USARLO:
1. Ejecuta el archivo main.py
2. Elige una categoría de conversión (longitud, masa, volumen)
3. Selecciona la unidad de origen y la unidad de destino
4. Ingresa el valor a convertir
5. El programa mostrará el resultado y la fórmula utilizada
6. Todo queda guardado en la base de datos historial.db

FÓRMULAS UTILIZADAS:
- Longitud: Conversión por factor de multiplicación (ej. metros a km: dividir entre 1000)
- Masa: Conversión por factor de multiplicación (ej. kg a g: multiplicar por 1000)
- Volumen: Conversión por factor de multiplicación (ej. litros a ml: multiplicar por 1000)

NOTA PARA ESTUDIANTES:
Este proyecto usa programación estructurada, sin clases ni objetos.
Todas las funciones son independientes y trabajan con datos simples.
```

---

## 🐍 Código completo

### 1. `database.py` (manejo de la base de datos)

```python
import sqlite3
from datetime import datetime

def crear_tabla():
    """Crea la tabla de historial si no existe"""
    conexion = sqlite3.connect("historial.db")
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
    conexion = sqlite3.connect("historial.db")
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

def ver_historial():
    """Muestra las últimas 10 conversiones"""
    conexion = sqlite3.connect("historial.db")
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
        print("\n📭 No hay conversiones guardadas aún.")
        return
    
    print("\n" + "="*70)
    print("📜 HISTORIAL DE CONVERSIONES (últimas 10)")
    print("="*70)
    
    for conv in resultados:
        print(f"\n📅 {conv[0]}")
        print(f"   Categoría: {conv[1]}")
        print(f"   {conv[2]} {conv[3]} → {conv[4]} {conv[5]}")
        print(f"   Fórmula: {conv[6]}")
    
    print("\n" + "="*70)
```

---

### 2. `conversiones.py` (fórmulas y conversiones)

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
        formula = f"Fórmula: {valor} {desde} = {valor} × {_obtener_factor(desde, 'm')} = {en_metros} m, luego a {hasta}"
    elif hasta == "km":
        resultado = en_metros / 1000
        formula = f"Fórmula: {valor} {desde} = {valor} × {_obtener_factor(desde, 'm')} = {en_metros} m, luego ÷ 1000 = {resultado} km"
    elif hasta == "cm":
        resultado = en_metros * 100
        formula = f"Fórmula: {valor} {desde} = {valor} × {_obtener_factor(desde, 'm')} = {en_metros} m, luego × 100 = {resultado} cm"
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
        formula = f"Fórmula: {valor} {desde} = {en_kg} kg"
    elif hasta == "g":
        resultado = en_kg * 1000
        formula = f"Fórmula: {valor} {desde} = {en_kg} kg × 1000 = {resultado} g"
    elif hasta == "lb":
        resultado = en_kg / 0.453592
        formula = f"Fórmula: {valor} {desde} = {en_kg} kg ÷ 0.453592 = {resultado:.4f} lb"
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
        formula = f"Fórmula: {valor} {desde} = {en_litros} L"
    elif hasta == "mL":
        resultado = en_litros * 1000
        formula = f"Fórmula: {valor} {desde} = {en_litros} L × 1000 = {resultado} mL"
    elif hasta == "m3":
        resultado = en_litros / 1000
        formula = f"Fórmula: {valor} {desde} = {en_litros} L ÷ 1000 = {resultado} m³"
    else:
        return None, "Unidad no válida"
    
    return resultado, formula
```

---

### 3. `main.py` (programa principal)

```python
import database
import conversiones

def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("🔄 CONVERSOR DE UNIDADES INTELIGENTE")
    print("="*50)
    print("1️⃣  Conversiones de LONGITUD (m, km, cm)")
    print("2️⃣  Conversiones de MASA (kg, g, lb)")
    print("3️⃣  Conversiones de VOLUMEN (L, mL, m³)")
    print("4️⃣  Ver historial de conversiones")
    print("5️⃣  Salir")
    print("="*50)

def mostrar_menu_unidades(categoria, unidades):
    """Muestra las opciones de unidades disponibles"""
    print(f"\n📏 Unidades disponibles para {categoria}:")
    for i, unidad in enumerate(unidades, 1):
        print(f"   {i}. {unidad}")

def obtener_opcion_unidad(unidades):
    """Obtiene la unidad seleccionada por el usuario"""
    while True:
        try:
            opcion = int(input("Selecciona una opción: "))
            if 1 <= opcion <= len(unidades):
                return unidades[opcion - 1]
            else:
                print(f"❌ Opción inválida. Elige entre 1 y {len(unidades)}")
        except ValueError:
            print("❌ Por favor, ingresa un número válido")

def realizar_conversion():
    """Flujo principal para realizar una conversión"""
    print("\n📐 ¿Qué tipo de conversión deseas hacer?")
    print("1. Longitud (metros, kilómetros, centímetros)")
    print("2. Masa (kilogramos, gramos, libras)")
    print("3. Volumen (litros, mililitros, metros cúbicos)")
    
    try:
        opcion_cat = int(input("\nElige una opción (1-3): "))
    except ValueError:
        print("❌ Opción inválida")
        return
    
    # Configurar según la categoría elegida
    if opcion_cat == 1:
        categoria = "Longitud"
        unidades = ["m", "km", "cm"]
        convertir_func = conversiones.convertir_longitud
    elif opcion_cat == 2:
        categoria = "Masa"
        unidades = ["kg", "g", "lb"]
        convertir_func = conversiones.convertir_masa
    elif opcion_cat == 3:
        categoria = "Volumen"
        unidades = ["L", "mL", "m3"]
        convertir_func = conversiones.convertir_volumen
    else:
        print("❌ Opción inválida")
        return
    
    # Seleccionar unidad de origen
    print(f"\n📌 {categoria} - UNIDAD DE ORIGEN")
    mostrar_menu_unidades(categoria, unidades)
    desde = obtener_opcion_unidad(unidades)
    
    # Seleccionar unidad de destino
    print(f"\n📌 {categoria} - UNIDAD DE DESTINO")
    mostrar_menu_unidades(categoria, unidades)
    hasta = obtener_opcion_unidad(unidades)
    
    # Ingresar valor
    try:
        valor = float(input(f"\n🔢 Ingresa el valor en {desde}: "))
    except ValueError:
        print("❌ Valor inválido")
        return
    
    # Realizar conversión
    resultado, formula = convertir_func(valor, desde, hasta)
    
    if resultado is None:
        print(f"❌ Error: {formula}")
        return
    
    # Mostrar resultado
    print("\n" + "="*50)
    print("✅ RESULTADO DE LA CONVERSIÓN")
    print("="*50)
    print(f"📊 {valor} {desde} = {resultado} {hasta}")
    print(f"\n📐 {formula}")
    print("="*50)
    
    # Guardar en historial
    database.guardar_conversion(categoria, valor, desde, resultado, hasta, formula)
    print("\n💾 Conversión guardada en el historial")

def main():
    """Función principal del programa"""
    # Crear la tabla de la base de datos al iniciar
    database.crear_tabla()
    
    print("\n🚀 ¡Bienvenido al Conversor de Unidades Inteligente!")
    print("Este programa te ayudará a convertir unidades y guardará tu historial.")
    
    while True:
        mostrar_menu_principal()
        opcion = input("\n👉 ¿Qué deseas hacer? (1-5): ")
        
        if opcion == "1" or opcion == "2" or opcion == "3":
            realizar_conversion()
            input("\nPresiona Enter para continuar...")
        elif opcion == "4":
            database.ver_historial()
            input("\nPresiona Enter para continuar...")
        elif opcion == "5":
            print("\n👋 ¡Gracias por usar el Conversor de Unidades!")
            print("📁 Tu historial se guardó en 'historial.db'")
            break
        else:
            print("❌ Opción no válida. Por favor elige 1, 2, 3, 4 o 5.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
```

---

## ▶️ Cómo ejecutarlo

1. Crea una carpeta llamada `conversor_unidades`
2. Dentro, crea los 4 archivos: `main.py`, `database.py`, `conversiones.py` y `LEEME.txt`
3. Abre una terminal en esa carpeta
4. Ejecuta: `python main.py`

¡El programa creará automáticamente la base de datos `historial.db` la primera vez que lo ejecutes!
