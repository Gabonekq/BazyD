# BazyDanych

## Aplikacja "Twoje zdrowie" na potrzeby projektu studenckiego
W rozwiązaniu skupiono się na aspekcie zdrowotnym. Użytkownik może sprawdzić czy wyniki 
jego badań mieszczą się w normie. W ułatwieniu wprowadzania tych danych, może otworzyć plik PDF otrzymany w laboratorium.
Dodatkowo jest w stanie zapisywać swoje treningi, ich czas 
i ilość powtórzeń/serii. W razie potrzeby, dane można także usunąć.

### Funkcje
- Logowanie
- Odczyt z pliku .db
- Zapis do pliku .db
- Dodanie rekordów do bazy
- Aktualizacja istniejących rekordów w tabelach
- Otwieranie plików PDF
  

### Technologia

- Python Tkinter
- Visual Studio Code

# 💻 Uruchomienie: 
- home i report -> python app.py
- pozostałe pliki -> python (nazwa pliku)

## Instalacja

Użyj [pip](https://pip.pypa.io/en/stable/) w celu zainstalowania bibliotek:
- aplikację buduje tkinter:
```bash
pip install tkinter
```
- bazy danych używają sqlite3:
```bash
pip install sqlite3
```
- pliki PDF można oglądać dzięki pyPDF2
```bash
pip install pyPDF2
```

⭐W przypadku braku pozostałych bibliotek należy działać analogicznie jak w powyższych przypadkach

