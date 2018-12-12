# Hurtownie Danych (Proces ETL - Projekt)

## Dkumentacja techniczna

### Wykorzystane technologie

- Python
- SQLite

### Struktura bazy danych

```sql
CREATE TABLE IF NOT EXISTS stocks(
	title TEXT,	
	period TEXT,
	username TEXT,
	date TEXT,
	comment TEXT,
	head TEXT
);
```

### Opis wykorzystanych klas

#### Plik myhtml.py - klasa HTML

### Klasy wewnêtrzne

Pole | Wartoœæ
---- | -------
links | Tablica przechowywuj¹ca linki do wybranych seriali
com_links | Tablica przechowywuj¹ca linki do komentarzy wybranego serialu
record | Tablica surowych recordów 

Metoda | Parametry | Wartoœæ zwracana | Opis
------ | --------- | ---------------- | ----
Start_extract() | 'name' | Brak | Wyszukuje nazwê serialu podan¹ jako parametr 'name' i zapisuje linki do nich w tablicy 'links'  
extract_data() | Brak parametrów | Brak | Przeszukuje strony html zapisane w tablicy 'links', odszukuje linki do komentarzy i zapisuje je w tablicy 'com_links'
transform_data() | Brak parametrów | Przeszukuje strony html zapisane w tablicy 'com_links', odnajduje szukane dane i zapisuje je w tablicy 'record'
getRecords() | Brak parametrów | 'record[]' | Zwraca tablicê 'record'

### Klasy zewnêtrzne 

Klasa | Opis
----- | ----
requests | Pozwala wysy³aæ zapytnia do serverów 
bs4 | Pozwala przeprowadzaæ operacje na plikach html


#### Plik mysqlite.py - klasa Database

### Klasy wewnêtrzne

Pole | Wartoœæ
---- | -------
conn | WskaŸnik do bazy danych 'hd.db'
c | Cursor zmiennej conn wskazuj¹cy na wybran¹ bazê danych
selected_records | Tablica przechowywuj¹ca wybrane recordy



Metoda | Parametry | Wartoœæ zwracana | Opis
------ | --------- | ---------------- | ----
load_data() | 'tuple_data' | Brak | £aduje recordy podane w tablicy krotek 'tuple_data' do bazy danych 'hd.db'
select() | 'title', 'period', 'username', 'date', 'comment', 'head' | 'chosen_records[]' | Wyszukuje frazy podane w parametrach w rekordach zapsianych w bazie danych 'hd.db' i zwraca wynik w postaci taplicy krotek
update() | 'records' | 'i' | Porównuje rekordy zapisane w bazie danych i aktualizuje je jeœli zosta³y zmienione, zwraca iloœæ sprawdzonych recordów 'i'
delete_all_records() | Brak parmetrów | Brak | Usuwa ca³¹ zawartoœæ bazy danych 'hd.db'

### Klasy zewnêtrzne 

Klasa | Opis
----- | ----
sqlite3 | Pozwala manipulowaæ baz¹ danych sqlite




























