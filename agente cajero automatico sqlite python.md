# 🏦 Simulador de Cajero Básico en Python + SQLite
Proyecto diseñado para estudiantes de preparatoria. Código limpio, comentado y listo para ejecutarse en VS Code.

---

## 📁 Estructura de Carpetas y Archivos
Crea una carpeta llamada `cajero_simulador` y dentro de ella estos 3 archivos:
```
cajero_simulador/
│
├── database.py      # Manejo de la base de datos SQLite
├── main.py          # Agente / Interfaz del cajero
└── README.md        # Instrucciones (opcional)
```
*(No necesitas instalar nada extra. SQLite ya viene incluido en Python)*

---

## 💻 1. `database.py`
Maneja toda la lógica de la base de datos. Separar esto del código principal es una **buena práctica** que te ayudará a entender arquitectura modular.

```python
import sqlite3

# Nombre del archivo de base de datos (se crea automáticamente)
NOMBRE_DB = "cuenta.db"

def conectar():
    """Abre una conexión a la base de datos y la devuelve."""
    conn = sqlite3.connect(NOMBRE_DB)
    # Permite acceder a las columnas por nombre (ej: cuenta["saldo"])
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_db():
    """Crea la tabla 'cuentas' si aún no existe."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cuentas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titular TEXT NOT NULL,
            saldo REAL DEFAULT 0.0,
            pin TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def registrar_cuenta(titular, saldo_inicial, pin):
    """Guarda una nueva cuenta y devuelve su ID."""
    conn = conectar()
    cursor = conn.cursor()
    try:
        # El uso de "?" evita inyecciones SQL (seguridad básica)
        cursor.execute(
            "INSERT INTO cuentas (titular, saldo, pin) VALUES (?, ?, ?)",
            (titular, saldo_inicial, pin)
        )
        conn.commit()
        return cursor.lastrowid  # Devuelve el ID generado automáticamente
    except sqlite3.Error as e:
        print(f"❌ Error al crear cuenta: {e}")
        return None
    finally:
        conn.close()

def verificar_cuenta(id_cuenta, pin):
    """Busca si el ID y PIN coinciden. Devuelve los datos o None."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cuentas WHERE id = ? AND pin = ?", (id_cuenta, pin))
    cuenta = cursor.fetchone()
    conn.close()
    return cuenta

def actualizar_saldo(id_cuenta, nuevo_saldo):
    """Modifica el saldo de una cuenta existente."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE cuentas SET saldo = ? WHERE id = ?", (nuevo_saldo, id_cuenta))
    conn.commit()
    conn.close()

def obtener_cuenta(id_cuenta):
    """Devuelve los datos actuales de una cuenta por su ID."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cuentas WHERE id = ?", (id_cuenta,))
    cuenta = cursor.fetchone()
    conn.close()
    return cuenta
```

---

## 💻 2. `main.py`
Este es el **agente principal**. Controla el flujo, muestra el menú y llama a las funciones de la base de datos.

```python
from database import inicializar_db, registrar_cuenta, verificar_cuenta, actualizar_saldo, obtener_cuenta
import sys

def limpiar_pantalla():
    """Limpia la consola para que se vea más ordenado."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_numero(mensaje):
    """Valida que el usuario escriba un número válido."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("⚠️ Por favor, ingresa solo números (ej: 50.00)")

def crear_cuenta():
    print("\n📝 === REGISTRAR NUEVA CUENTA === 📝")
    titular = input("👤 Nombre del titular: ").strip()
    if not titular:
        print("❌ El nombre no puede estar vacío.")
        return

    saldo = pedir_numero("💰 Saldo inicial (ej. 0.00): ")
    if saldo < 0:
        print("❌ El saldo no puede ser negativo.")
        return

    pin = input("🔒 Crea un PIN de 4 dígitos: ").strip()
    if len(pin) != 4 or not pin.isdigit():
        print("❌ El PIN debe ser exactamente 4 números.")
        return

    id_cuenta = registrar_cuenta(titular, saldo, pin)
    if id_cuenta:
        print(f"✅ ¡Cuenta creada con éxito! Tu ID es: {id_cuenta}")
        print("📌 ¡Anótalo! Lo necesitarás para entrar.")

def iniciar_sesion():
    print("\n🔑 === INICIAR SESIÓN === 🔑")
    try:
        id_cuenta = int(input("🆔 Ingresa tu ID de cuenta: "))
        pin = input("🔒 Ingresa tu PIN: ").strip()
    except ValueError:
        print("❌ El ID debe ser un número.")
        return

    cuenta = verificar_cuenta(id_cuenta, pin)
    if cuenta:
        print(f"\n👋 ¡Bienvenido/a, {cuenta['titular']}!")
        menu_usuario(id_cuenta)
    else:
        print("❌ ID o PIN incorrectos. Intenta de nuevo.")

def menu_usuario(id_cuenta):
    """Menú exclusivo para usuarios autenticados."""
    while True:
        print("\n🏦 === MENÚ DE USUARIO === 🏦")
        print("1. 💵 Consultar saldo")
        print("2. 📥 Depositar dinero")
        print("3. 📤 Retirar dinero")
        print("4. 🚪 Cerrar sesión")

        opcion = input("\n👉 Elige una opción (1-4): ").strip()
        cuenta = obtener_cuenta(id_cuenta)  # Datos frescos de la DB

        if opcion == "1":
            print(f"💳 Tu saldo actual es: ${cuenta['saldo']:.2f}")
        elif opcion == "2":
            monto = pedir_numero("📥 ¿Cuánto deseas depositar? $")
            if monto <= 0:
                print("❌ El monto debe ser mayor a 0.")
            else:
                nuevo_saldo = cuenta['saldo'] + monto
                actualizar_saldo(id_cuenta, nuevo_saldo)
                print(f"✅ Depósito exitoso. Nuevo saldo: ${nuevo_saldo:.2f}")
        elif opcion == "3":
            monto = pedir_numero("📤 ¿Cuánto deseas retirar? $")
            if monto <= 0:
                print("❌ El monto debe ser mayor a 0.")
            elif monto > cuenta['saldo']:
                print("❌ Fondos insuficientes. 💸")
            else:
                nuevo_saldo = cuenta['saldo'] - monto
                actualizar_saldo(id_cuenta, nuevo_saldo)
                print(f"✅ Retiro exitoso. Nuevo saldo: ${nuevo_saldo:.2f}")
        elif opcion == "4":
            print("👋 Sesión cerrada correctamente.")
            break
        else:
            print("⚠️ Opción no válida. Elige entre 1 y 4.")

def main():
    """Punto de entrada del programa."""
    inicializar_db()  # Prepara la BD al arrancar
    limpiar_pantalla()

    while True:
        print("\n🏦 === SIMULADOR DE CAJERO === 🏦")
        print("1. 🆕 Crear cuenta nueva")
        print("2. 🔑 Iniciar sesión")
        print("3. 🚪 Salir del programa")

        opcion = input("\n👉 Elige una opción (1-3): ").strip()

        if opcion == "1":
            crear_cuenta()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("\n✨ ¡Gracias por usar el simulador! Hasta pronto. ✨")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
```

---

## 🛠️ Cómo ejecutarlo en VS Code (Paso a paso)

1. **Abre VS Code** → `File > Open Folder` → Selecciona la carpeta `cajero_simulador`.
2. **Instala la extensión de Python** (si no la tienes):
   - Ve al ícono de extensiones (🔲 izquierda) → busca `Python` (de Microsoft) → `Install`.
3. **Ejecuta el programa**:
   - Abre la terminal integrada: `` Ctrl + ` `` (o `View > Terminal`)
   - Escribe: `python main.py` (o `python3 main.py` en Mac/Linux)
   - ¡Listo! El menú aparecerá en la terminal.

💡 *Tip VS Code*: Puedes hacer clic derecho en `main.py` y seleccionar `Run Python File in Terminal`.

---

## 📚 Guía Didáctica (Conceptos Clave)

| Concepto | ¿Qué es? | ¿Por qué lo usamos aquí? |
|----------|----------|--------------------------|
| `sqlite3` | Motor de base de datos ligero incluido en Python | No requiere servidor, perfecto para practicar |
| `?` en SQL | Parámetros seguros | Evita que un usuario malintencionado inyecte código SQL |
| `row_factory = sqlite3.Row` | Configura la conexión | Permite usar `cuenta["saldo"]` en lugar de `cuenta[2]` |
| `try / except / finally` | Manejo de errores | Garantiza que la conexión se cierre incluso si hay fallos |
| `cursor.lastrowid` | ID autogenerado | Devuelve el número de la cuenta recién creada |

🔍 **Nota de seguridad**: En un cajero real, el PIN **nunca** se guarda como texto plano. Se cifra (hash). Para este nivel escolar, guardarlo como texto es aceptable para entender el flujo, pero es un buen tema para investigar después.

---

## 🚀 Retos para Seguir Aprendiendo
1. 📜 Agrega un historial de movimientos (`CREATE TABLE movimientos ...`).
2. 🔄 Implementa `UNIQUE` en el campo `titular` para evitar cuentas duplicadas.
3. 🎨 Usa la librería `rich` o `colorama` para dar colores al menú.
4. 📦 Empaquétalo con `pyinstaller` para crear un `.exe` ejecutable sin Python.

¿Quieres que te explique cómo agregar el historial de transacciones o cómo añadir colores al menú? 😊
