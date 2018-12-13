# Hurtownie Danych (Proces ETL - Projekt)

## Dokumentacja techniczna



## Wykorzystane technologie

- Python
- SQLite



## Struktura bazy danych

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



## Opis wykorzystanych klas




### Plik myhtml.py - klasa HTML


#### Klasy wewn�trzne

Pole | Warto��
---- | -------
links | Tablica przechowywuj�ca linki do wybranych seriali
com_links | Tablica przechowywuj�ca linki do komentarzy wybranego serialu
record | Tablica surowych record�w 

Metoda | Parametry | Warto�� zwracana | Opis
------ | --------- | ---------------- | ----
Start_extract() | 'name' | Brak | Wyszukuje nazw� serialu podan� jako parametr 'name' i zapisuje linki do nich w tablicy 'links'  
extract_data() | Brak parametr�w | Brak | Przeszukuje strony html zapisane w tablicy 'links', odszukuje linki do komentarzy i zapisuje je w tablicy 'com_links'
transform_data() | Brak parametr�w | Brak | Przeszukuje strony html zapisane w tablicy 'com_links', odnajduje szukane dane i zapisuje je w tablicy 'record'
getRecords() | Brak parametr�w | 'record[]' | Zwraca tablic� 'record'


#### Klasy zewn�trzne 

Klasa | Opis
----- | ----
requests | Pozwala wysy�a� zapytnia do server�w 
bs4 | Pozwala przeprowadza� operacje na plikach html




### Plik mysqlite.py - klasa Database


#### Klasy wewn�trzne

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

#### Klasy zewn�trzne 

Klasa | Opis
----- | ----
sqlite3 | Pozwala manipulowa� baz� danych sqlite




### Plik GUI.py - klasa App


#### Klasy wewn�trzne

Pole | Warto��
---- | -------
main_window | G��wne okno programu, obiekt klasy 'tkinter'
MY_DATABASE | Obiekt klasy wewn�trznej 'Database'
My_data_HTML | Obiekt klasy wewn�trznej 'HTML'
entry_title | Obiekt klasy 'tkinter.Entry'
Tbox | Obiekt klasy 'tkinter.Text'
ProBar | Obiekt klasy 'tkinter.Progressbar'
Tview | Obiekt klasy 'tkinter.Treeview'
TboxDB | Obiekt klasy 'tkinter.Text'
Refresh_Button | Obiekt klasy 'tkinter.Button'
Title_filter | Obiekt klasy 'tkinter.Entry'
Period_filter | Obiekt klasy 'tkinter.Entry'
User_filter | Obiekt klasy 'tkinter.Entry'
Date_filter | Obiekt klasy 'tkinter.Entry'
Com_filter | Obiekt klasy 'tkinter.Entry'
Head_filter | Obiekt klasy 'tkinter.Entry'


Metoda | Parametry | Warto�� zwracana | Opis
------ | --------- | ---------------- | ----
CreateWidget | Brak parametr�w | Brak | Tworzy widgety na g��wnym oknie programu - 'main_window'
Show_column | 'event' | Brak | Powoduje wy�wietlenie, pola wybranego rekordu w obiekcie 'TboxDB', jako parametr przymuje zdarzenie (klikni�cie prawym przyciskiem myszy)
Insert_DB | 'DB' | Brak | Powoduje wy�wietlenie rekord�w podanych jako parametr 'DB' w obiekcie 'Tview'
Start_App | Brak parametr�w | Brak | Wywo�uje funkcj� 'mainloop()' klasy tkinter
SelectFromDB | Brak parametr�w | Brak | Pobiera warto�ci obiekt�w 'Title_filter', 'Period_filter', 'User_filter', 'Date_filter', 'Com_filter', 'Head_filter', na podstawie, kt�rych wyszukuje rekordy, kt�re s� nast�pnie wy�wietlane w obiekcie 'Tview'
CreateCSV | Brak parametr�w | Brak | Tworzy plik 'HD.csv', w pliku g��wnym programu, zawieraj�cy rekordy wy�wietlone w obiekcie  'Tview'
RemoveAllDB | Brak parametr�w | Brak | Usuwa ca�� zawarto�� bazy danych 'hd.db'
Extract | Brak parametr�w | Brak | Pobiera warto�� obiektu 'entry_title' i z tym parametrem wywo�uje funkcje obiekt�w: 'ProBar.start()', 'ProBar.step()', 'ProBar.stop()', 'My_data_HTML.Start_extract()', 'My_data_HTML.extract_data()' nast�pnie wy�wietla komunikat w obiekcie 'Tbox' 
Transform | Brak parametr�w | Brak | Wywo�uje funkcje obiekt�w: 'ProBar.start()', 'ProBar.step()', 'ProBar.stop()', 'My_data_HTML.transform_data()', 'My_data_HTML.showupdata()', przetworzone rekordy zapisuje w tablicy 'HTML_records', nastepnie wy�wietla komunikat w obiekcie 'Tbox'
Load | Brak parametr�w | Brak | Wywo�uje funkcje obiekt�w: 'ProBar.start()', 'ProBar.step()', 'ProBar.stop()', sprawdza czy pobrane rekordy nie istniej� ju� w bazie danych a nast�pnie �aduje tych kt�rych nie ma w bazie 'hd.db'
ETL | Brak parametr�w | Brak | Wywo�uje fukcje: 'Extract', 'Transform', 'Load', nastepnie wy�wietla komunikat w obiekcie 'Tbox'
Update | Brak parametr�w | Brak | Wywo�uje fukcje: 'Extract', 'Transform', pobieraj�ce i przetwarzaj�ce aktualne rekordy, nast�pnie sprawdza czy rekordy zosta�y zmienione i uaktualnia je oraz  sprawdza czy istniej� nowe komentarze i dodaje je do bazy danych
Thread_Me | 'my_fun' | Brak | Wywo�uje funkcje z podanym parametrem 'my_fun' obiektu 'threading.Thread()', oraz funkcj� 'start()' obiektu klasy threading. Parametr 'my_fun' jest wska�nikiem do funkcji. Funcja wywo�uje funcj�, kt�rej wska�nik jest podany jako parametr w nowym w�tku.  


#### Klasy zewn�trzne 

Klasa | Opis
----- | ----
tkinter | Pozwala tworzy� interface graficzny u�ytkowanika
pandas | Pozwla manipulowa� danymi


### Plik main.py 

Zawiera obiekt klasy 'GUI' pozwalaj�cy uruchomi� interface graficzny u�ytkowanika oraz wywo�ania funkcji na tym obiekcie: 'Application' - obiekt klasy 'GUI', 'Application.CreateWidget()' oraz 'Application.Start_App()' 






## Dokumentacja u�ytkownika


### Instrukcja instalacji

1. Nale�y pobra� repozytorium
2. W folderze g��wnym nale�y otworzy� podfolder 'dist' i uruchomi� plik wykonywalny 'main.exe'
3. Opcjonalnie mo�na utworzy� skr�t folderu w wybranej przez siebie lokalizacji.



















