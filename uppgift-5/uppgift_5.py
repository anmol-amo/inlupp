# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(numbers):
    """
    Skriv beskrivning här.
    """
    



num_list = [1, 2, 3, 4]
runs = 0
odds = []

for n in num_list:
    if n % 2 == 0:

        odds.append(n)
        runs += 1
        if runs == 5:
            break
print(odds)