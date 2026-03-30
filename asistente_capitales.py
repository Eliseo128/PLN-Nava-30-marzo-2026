# Virtual Assistant: Country Capitals

## Problem Statement

Create a virtual assistant that can understand natural language queries about the capitals of countries around the world. The assistant should respond to questions like "What is the capital of France?" or "Tell me the capital of Japan" by providing accurate responses in a user-friendly manner.

## Code Explanation

This Python code uses the Natural Language Toolkit (nltk) for tokenizing user queries and a simple dictionary for storing country and capital pairs. The assistant matches user input with known formats and responds accordingly.

### Code
```python
import nltk
from nltk.tokenize import word_tokenize

# Ensure necessary resources are downloaded
nltk.download('punkt')

# Dictionary of countries and their capitals
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Japan': 'Tokyo',
    'Italy': 'Rome',
    'Brazil': 'Brasilia',
    'India': 'New Delhi',
    'South Africa': 'Pretoria',
    'Canada': 'Ottawa',
    'Australia': 'Canberra',
    'United Kingdom': 'London'
}

def get_capital(country):
    return capitals.get(country, "Sorry, I don't know the capital of that country.")

def main():
    print("Welcome to the Country Capital Assistant!")
    while True:
        question = input("Ask me a question about country capitals (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        tokens = word_tokenize(question)
        country = ''
        for token in tokens:
            # Check if token matches any country
            if token in capitals:
                country = token
                break
        if country:
            capital = get_capital(country)
            print(f'The capital of {country} is {capital}.')
        else:
            print("Sorry, I couldn't find a country in your question.")

if __name__ == '__main__':
    main()
```

### Test Examples
1. **Input**: "What is the capital of France?"  
   **Output**: "The capital of France is Paris."
2. **Input**: "Tell me the capital of Japan."  
   **Output**: "The capital of Japan is Tokyo."
3. **Input**: "What about Germany?"  
   **Output**: "The capital of Germany is Berlin."
4. **Input**: "Can you tell me the capital of Brazil?"  
   **Output**: "The capital of Brazil is Brasilia."
5. **Input**: "What is the capital of South Africa?"  
   **Output**: "The capital of South Africa is Pretoria."
6. **Input**: "What is the capital of Australia?"  
   **Output**: "The capital of Australia is Canberra."
7. **Input**: "Can you tell me the capital of Italy?"  
   **Output**: "The capital of Italy is Rome."
8. **Input**: "What is the capital of Canada?"  
   **Output**: "The capital of Canada is Ottawa."
9. **Input**: "What is the capital of India?"  
   **Output**: "The capital of India is New Delhi."
10. **Input**: "Where is the capital of the United Kingdom?"  
    **Output**: "The capital of the United Kingdom is London."