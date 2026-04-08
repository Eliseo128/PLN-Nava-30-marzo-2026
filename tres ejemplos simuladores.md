Aquí tienes 3 ejemplos completos, listos para copiar y ejecutar en Python. Están diseñados sin Programación Orientada a Objetos, usando solo funciones, estructuras de control básicas y entrada de datos. Cada uno simula una tarea real de **Procesamiento de Lenguaje Natural (NLP)** a nivel introductorio.

---

### 📚 Ejemplo 1: Chatbot de Biblioteca (Detección de intenciones por palabras clave)
**Concepto NLP:** *Keyword Matching & Text Normalization*. El programa normaliza el texto (minúsculas, sin espacios extra) y busca palabras clave para detectar la "intención" del usuario.

```python
def limpiar_texto(texto):
    """Convierte a minúsculas y elimina espacios al inicio/final."""
    return texto.lower().strip()

def responder_chatbot(texto_usuario):
    """Devuelve una respuesta según palabras clave detectadas."""
    texto = limpiar_texto(texto_usuario)
    
    if "horario" in texto or "abierto" in texto or "hora" in texto:
        return "📚 La biblioteca está abierta de 8:00 a 20:00, de lunes a sábado."
    elif "libro" in texto or "prestamo" in texto or "pedir" in texto:
        return "📖 Puedes solicitar hasta 3 libros por 15 días con tu credencial."
    elif "ayuda" in texto or "contacto" in texto or "correo" in texto:
        return "📧 Escríbenos a ayuda@biblioteca.edu o acude a recepción."
    elif "adios" in texto or "chao" in texto or "salir" in texto:
        return "👋 ¡Hasta luego! Que tengas un excelente día."
    else:
        return "🤔 No entendí bien. Prueba con: 'horario', 'libro' o 'ayuda'."

def menu_chatbot():
    print("=== 🤖 Asistente Virtual de la Biblioteca ===")
    while True:
        print("\n1. 💬 Hablar con el asistente")
        print("2. 📋 Ver comandos que entiendo")
        print("3. 🚪 Salir")
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == "1":
            while True:
                mensaje = input("\n✍️ Escribe tu consulta (o 'salir' para volver al menú): ")
                if limpiar_texto(mensaje) in ["salir", "adios", "chao"]:
                    break
                print("🤖", responder_chatbot(mensaje))
        elif opcion == "2":
            print("\n📌 Palabras clave que detecto:")
            print("  ⏰ Horarios: horario, abierto, hora")
            print("  📚 Préstamos: libro, prestamo, pedir")
            print("  📧 Contacto: ayuda, contacto, correo")
        elif opcion == "3":
            print("👋 ¡Gracias por usar el asistente!")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Ejecutar
if __name__ == "__main__":
    menu_chatbot()
```

---

### 🎭 Ejemplo 2: Detector de Ánimo (Análisis de sentimiento básico)
**Concepto NLP:** *Lexicon-based Sentiment Analysis*. Cuenta palabras positivas y negativas en una frase para determinar si el tono es positivo, negativo o neutral.

```python
def analizar_sentimiento(frase):
    """Cuenta palabras positivas/negativas y devuelve el resultado."""
    palabras = frase.lower().split()
    positivas = ["bien", "genial", "feliz", "amor", "excelente", "increible", "divertido", "gracias", "si", "me encanta"]
    negativas = ["mal", "triste", "odio", "terrible", "aburrido", "no", "peor", "error", "problema", "odio"]
    
    contador_pos = 0
    contador_neg = 0
    
    for p in palabras:
        # Eliminar signos básicos de puntuación pegados a la palabra
        palabra_limpia = p.strip(".,!?;:'\"")
        if palabra_limpia in positivas:
            contador_pos += 1
        elif palabra_limpia in negativas:
            contador_neg += 1
            
    if contador_pos > contador_neg:
        return "😊 POSITIVO", contador_pos, contador_neg
    elif contador_neg > contador_pos:
        return "😟 NEGATIVO", contador_pos, contador_neg
    else:
        return "😐 NEUTRAL", contador_pos, contador_neg

def menu_sentimiento():
    print("=== 🎭 Detector de Sentimiento Básico ===")
    while True:
        print("\n1. ✍️ Analizar una frase")
        print("2. 📖 Ver listas de palabras clave")
        print("3. 🚪 Salir")
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == "1":
            texto = input("\n💬 Escribe una frase corta: ")
            if len(texto.strip()) == 0:
                print("⚠️ Por favor, escribe algo primero.")
                continue
            resultado, pos, neg = analizar_sentimiento(texto)
            print(f"\n📊 Resultado: {resultado}")
            print(f"   Palabras positivas detectadas: {pos}")
            print(f"   Palabras negativas detectadas: {neg}")
        elif opcion == "2":
            print("\n🔍 Diccionario interno del analizador:")
            print("  ✅ Positivas: bien, genial, feliz, amor, excelente, increíble, divertido, gracias, sí, me encanta")
            print("  ❌ Negativas: mal, triste, odio, terrible, aburrido, no, peor, error, problema")
        elif opcion == "3":
            print("👋 ¡Hasta la próxima!")
            break
        else:
            print("⚠️ Opción inválida. Elige 1, 2 o 3.")

# Ejecutar
if __name__ == "__main__":
    menu_sentimiento()
```

---

### 🔍 Ejemplo 3: Analizador de Frecuencia (Limpieza y conteo de palabras)
**Concepto NLP:** *Text Cleaning & Tokenization*. Elimina signos de puntuación, normaliza el texto y cuenta cuántas veces aparece cada palabra. Es la base de tareas como extracción de temas o nubes de palabras.

```python
def limpiar_texto(texto):
    """Elimina signos de puntuación y pasa todo a minúsculas."""
    import string
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    return texto.lower().strip()

def contar_frecuencia(texto):
    """Devuelve un diccionario con las palabras y sus repeticiones."""
    texto_limpio = limpiar_texto(texto)
    palabras = texto_limpio.split()
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia, len(palabras)

def menu_frecuencia():
    print("=== 📝 Analizador de Frecuencia de Palabras ===")
    while True:
        print("\n1. 📄 Ingresar y analizar un texto")
        print("2. 🧹 ¿Cómo funciona la limpieza NLP?")
        print("3. 🚪 Salir")
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == "1":
            texto = input("\n✍️ Escribe un párrafo corto: ")
            if len(texto.strip()) < 3:
                print("⚠️ El texto es muy corto. Intenta con al menos 3 palabras.")
                continue
                
            frec, total = contar_frecuencia(texto)
            print(f"\n📊 Total de palabras procesadas: {total}")
            print("🔢 Frecuencia de cada palabra:")
            for palabra, veces in frec.items():
                print(f"   '{palabra}': {veces} veces")
        elif opcion == "2":
            print("\n🛠️ Pasos que aplicamos automáticamente:")
            print("  1️⃣ Normalización: Todo a minúsculas")
            print("  2️⃣ Limpieza: Eliminamos . , ! ? ; : ( ) etc.")
            print("  3️⃣ Tokenización: Separamos el texto en palabras individuales")
            print("  4️⃣ Conteo: Registramos cuántas veces aparece cada palabra")
        elif opcion == "3":
            print("👋 ¡Fin del análisis! Sigue practicando NLP.")
            break
        else:
            print("⚠️ Opción no válida. Elige 1, 2 o 3.")

# Ejecutar
if __name__ == "__main__":
    menu_frecuencia()
```

---

### 💡 Consejos pedagógicos para usar estos ejemplos en clase:
1. **Simulación guiada:** Pide a los estudiantes que ejecuten un ejemplo, anoten qué palabras usan y luego modifiquen las listas de palabras clave (`positivas`, `negativas`, o las del chatbot) para ver cómo cambia el comportamiento.
2. **Extensión progresiva:** Una vez dominen la estructura `while` + menú, pídeles que agreguen:
   - Una opción 4 en el Ejemplo 2 que muestre el porcentaje de sentimiento `(positivas / total) * 100`.
   - En el Ejemplo 3, que filtre palabras de menos de 3 letras (artículos, preposiciones).
3. **Conexión con NLP real:** Explica que aunque esto es básico, los modelos actuales usan los mismos principios: normalización → tokenización → extracción de características → respuesta. La diferencia es que usan matemáticas y redes neuronales en lugar de listas manuales.
4. **Depuración interactiva:** Usa `print()` estratégicos para mostrar variables intermedias (ej. `print("Texto limpio:", limpiar_texto(texto))`) y ayuda a los estudiantes a visualizar el flujo de datos.

Todos los ejemplos son autocontenidos, no requieren instalación de librerías externas y cumplen estrictamente con programación estructurada básica. ¡Listos para el aula! 🚀
