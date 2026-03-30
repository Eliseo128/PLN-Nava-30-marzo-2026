# Asistente Virtual: Capitales de Países

class AsistentCapitales:
    """Clase para gestionar consultas sobre capitales de países."""
    
    def __init__(self):
        """Inicializa el diccionario de capitales."""
        self.capitales = {
            'Francia': 'París',
            'Alemania': 'Berlín',
            'Japón': 'Tokio',
            'Italia': 'Roma',
            'Brasil': 'Brasilia',
            'India': 'Nueva Delhi',
            'Sudáfrica': 'Pretoria',
            'Canadá': 'Ottawa',
            'Australia': 'Canberra',
            'Reino Unido': 'Londres'
        }
    
    def tokenizar(self, texto):
        """
        Divide el texto en palabras de forma simple.
        
        Args:
            texto (str): El texto a tokenizar
            
        Returns:
            list: Lista de palabras
        """
        # Convertir a minúsculas y dividir por espacios
        palabras = texto.lower().split()
        # Remover caracteres especiales
        palabras_limpias = []
        for palabra in palabras:
            palabra_limpia = ''.join(c for c in palabra if c.isalnum() or c == ' ')
            if palabra_limpia:
                palabras_limpias.append(palabra_limpia)
        return palabras_limpias
    
    def obtener_capital(self, pais):
        """
        Obtiene la capital de un país.
        
        Args:
            pais (str): Nombre del país
            
        Returns:
            str: La capital del país o un mensaje de error
        """
        return self.capitales.get(pais, "Lo siento, no sé la capital de ese país.")
    
    def buscar_pais(self, pregunta):
        """
        Busca un país en la pregunta del usuario.
        
        Args:
            pregunta (str): La pregunta del usuario
            
        Returns:
            str: El país encontrado o vacío si no hay coincidencia
        """
        palabras = self.tokenizar(pregunta)
        for palabra in palabras:
            # Capitalizar primera letra para coincidir con el diccionario
            palabra_capitalizada = palabra.capitalize()
            if palabra_capitalizada in self.capitales:
                return palabra_capitalizada
        return ''
    
    def ejecutar(self):
        """Inicia el asistente interactivo."""
        print("¡Bienvenido al Asistente de Capitales!")
        while True:
            pregunta = input("Pregúntame sobre capitales de países (o escribe 'salir' para terminar): ")
            if pregunta.lower() == 'salir':
                print("¡Hasta luego!")
                break
            
            pais = self.buscar_pais(pregunta)
            if pais:
                capital = self.obtener_capital(pais)
                print(f'La capital de {pais} es {capital}.')
            else:
                print("Lo siento, no encontré un país en tu pregunta.")


if __name__ == '__main__':
    asistente = AsistentCapitales()
    asistente.ejecutar()
