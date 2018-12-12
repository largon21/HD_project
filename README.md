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

### Klasy wewn�trzne

Pole | Warto��
---- | -------
links | Tablica przechowywuj�ca linki do wybranych seriali
com_links | Tablica przechowywuj�ca linki do komentarzy wybranego serialu
record | Tablica surowych record�w 

Metoda | Parametry | Warto�� zwracana | Opis
------ | --------- | ---------------- | ----
Start_extract() | 'name' | Brak | Wyszukuje nazw� serialu podan� jako parametr 'name' i zapisuje linki do nich w tablicy 'links'  
extract_data() | Brak parametr�w | Brak | Przeszukuje strony html zapisane w tablicy 'links', odszukuje linki do komentarzy i zapisuje je w tablicy 'com_links'
transform_data() | Brak parametr�w | Przeszukuje strony html zapisane w tablicy 'com_links', odnajduje szukane dane i zapisuje je w tablicy 'record'
getRecords() | Brak parametr�w | 'record[]' | Zwraca tablic� 'record'

### Klasy zewn�trzne 

Klasa | Opis
----- | ----
requests | Pozwala wysy�a� zapytnia do server�w 
bs4 | Pozwala przeprowadza� operacje na plikach html


#### Plik mysqlite.py - klasa Database

### Klasy wewn�trzne

Pole | Warto��
---- | -------
conn | Wska�nik do bazy danych 'hd.db'
c | Cursor zmiennej conn wskazuj�cy na wybran� baz� danych
selected_records | Tablica przechowywuj�ca wybrane recordy



Metoda | Parametry | Warto�� zwracana | Opis
------ | --------- | ---------------- | ----
load_data() | 'tuple_data' | Brak | �aduje recordy podane w tablicy krotek 'tuple_data' do bazy danych 'hd.db'
select() | 'title', 'period', 'username', 'date', 'comment', 'head' | 'chosen_records[]' | Wyszukuje frazy podane w parametrach w rekordach zapsianych w bazie danych 'hd.db' i zwraca wynik w postaci taplicy krotek
update() | 'records' | 'i' | Por�wnuje rekordy zapisane w bazie danych i aktualizuje je je�li zosta�y zmienione, zwraca ilo�� sprawdzonych record�w 'i'
delete_all_records() | Brak parmetr�w | Brak | Usuwa ca�� zawarto�� bazy danych 'hd.db'

### Klasy zewn�trzne 

Klasa | Opis
----- | ----
sqlite3 | Pozwala manipulowa� baz� danych sqlite




























