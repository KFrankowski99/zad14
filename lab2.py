def calculate_chain_length(n):  # Definicja funkcji calculate_chain_length, która przyjmuje jeden argument n, czyli liczbę początkową w ciągu
    count = 1  # Startujemy od liczby początkowej w ciągu 
    while n != 1:
        if n % 2 == 0:  # Jeśli liczba jest parzysta
            n = n // 2
        else:  # Jeśli liczba jest nieparzysta
            n = 3 * n + 1            
        count += 1 # linia 3-8 Rozpoczyna się pętla while, która będzie działać, dopóki wartość n nie osiągnie 1
    return count

najdluzszy_ciag = 0   #Ta zmienna będzie przechowywać długość najdłuższego ciągu
liczba_poczatkowa = 0 # Ta zmienna będzie przechowywać liczbę początkową generującą najdłuższy ciąg.

for i in range(1, 1000000): # Rozpoczyna się pętla for, która iteruje od 1 do 999999. Zmienna i przyjmuje wartości kolejnych liczb początkowych.
    dlugosc_ciagu = calculate_chain_length(i)
    if dlugosc_ciagu > najdluzszy_ciag:
        najdluzszy_ciag = dlugosc_ciagu
        liczba_poczatkowa = i 

print(f"Liczba początkowa {liczba_poczatkowa} generuje najdłuższy ciąg o długości {najdluzszy_ciag}.")
