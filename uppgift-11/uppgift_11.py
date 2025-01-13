# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text):
    
    words = text.split()
    # Returnera antalet ord
    return len(words)

print(word_count("hello world"))
print(word_count(""))
print(word_count("Python är fantastiskt!"))
