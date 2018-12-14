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


#### Klasa HTML

Pole | Wartoœæ
---- | -------
links | Tablica przechowuj¹ca linki do wybranych seriali
com_links | Tablica przechowuj¹ca linki do komentarzy wybranego serialu
record | Tablica surowych rekordów 

Metoda | Parametry | Wartoœæ zwracana | Opis
------ | --------- | ---------------- | ----
Start_extract() | 'name' | Brak | Wyszukuje nazwê serialu podan¹ jako parametr 'name' i zapisuje linki do nich w tablicy 'links'  
extract_data() | Brak parametrów | Brak | Przeszukuje strony html zapisane w tablicy 'links', odszukuje linki do komentarzy i zapisuje je w tablicy 'com_links'
transform_data() | Brak parametrów | Brak | Przeszukuje strony html zapisane w tablicy 'com_links', odnajduje szukane dane i zapisuje je w tablicy 'record'
getRecords() | Brak parametrów | 'record[]' | Zwraca tablicê 'record'


#### Klasy zewnêtrzne 

Klasa | Opis
----- | ----
requests | Pozwala wysy³aæ zapytnia do serverów 
bs4 | Pozwala przeprowadzaæ operacje na plikach html




### Plik mysqlite.py - klasa Database


#### Klasa Database

Pole | Wartoœæ
---- | -------
conn | WskaŸnik do bazy danych 'hd.db'
c | Kursor zmiennej conn wskazuj¹cy na wybran¹ bazê danych
selected_records | Tablica przechowuj¹ca wybrane rekordy


Metoda | Parametry | Wartoœæ zwracana | Opis
------ | --------- | ---------------- | ----
load_data() | 'tuple_data' | Brak | £aduje rekordy podane w tablicy krotek 'tuple_data' do bazy danych 'hd.db'
select() | 'title', 'period', 'username', 'date', 'comment', 'head' | 'chosen_records[]' | Wyszukuje frazy podane w parametrach w rekordach zapsianych w bazie danych 'hd.db' i zwraca wynik w postaci taplicy krotek
update() | 'records' | 'i' | Porównuje rekordy zapisane w bazie danych i aktualizuje je jeœli zosta³y zmienione, zwraca iloœæ sprawdzonych rekordów 'i'
delete_all_records() | Brak parmetrów | Brak | Usuwa ca³¹ zawartoœæ bazy danych 'hd.db'

#### Klasy zewnêtrzne 

Klasa | Opis
----- | ----
sqlite3 | Pozwala manipulowaæ baz¹ danych sqlite




### Plik GUI.py - klasa App


#### Klasa App

Pole | Wartoœæ
---- | -------
main_window | G³ówne okno programu, obiekt klasy 'tkinter'
MY_DATABASE | Obiekt klasy wewnêtrznej 'Database'
My_data_HTML | Obiekt klasy wewnêtrznej 'HTML'
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


Metoda | Parametry | Wartoœæ zwracana | Opis
------ | --------- | ---------------- | ----
CreateWidget | Brak parametrów | Brak | Tworzy widgety na g³ównym oknie programu - 'main_window'
Show_column | 'event' | Brak | Powoduje wyœwietlenie, pola wybranego rekordu w obiekcie 'TboxDB', jako parametr przymuje zdarzenie (klikniêcie lewym przyciskiem myszy)
Insert_DB | 'DB' | Brak | Powoduje wyœwietlenie rekordów podanych jako parametr 'DB' w obiekcie 'Tview'
Start_App | Brak parametrów | Brak | Wywo³uje funkcjê 'mainloop()' klasy tkinter
SelectFromDB | Brak parametrów | Brak | Pobiera wartoœci obiektów 'Title_filter', 'Period_filter', 'User_filter', 'Date_filter', 'Com_filter', 'Head_filter', na podstawie, których wyszukuje rekordy, które s¹ nastêpnie wyœwietlane w obiekcie 'Tview'
CreateCSV | Brak parametrów | Brak | Tworzy plik 'HD.csv', w pliku g³ównym programu, zawieraj¹cy rekordy wyœwietlone w obiekcie  'Tview'
RemoveAllDB | Brak parametrów | Brak | Usuwa ca³¹ zawartoœæ bazy danych 'hd.db'
Extract | Brak parametrów | Brak | Pobiera wartoœæ obiektu 'entry_title' i z tym parametrem wywo³uje funkcje obiektów: 'ProBar.start()', 'ProBar.step()', 'ProBar.stop()', 'My_data_HTML.Start_extract()', 'My_data_HTML.extract_data()' nastêpnie wyœwietla komunikat w obiekcie 'Tbox' 
Transform | Brak parametrów | Brak | Wywo³uje funkcje obiektów: 'ProBar.start()', 'ProBar.step()', 'ProBar.stop()', 'My_data_HTML.transform_data()', 'My_data_HTML.showupdata()', przetworzone rekordy zapisuje w tablicy 'HTML_records', nastepnie wyœwietla komunikat w obiekcie 'Tbox'
Load | Brak parametrów | Brak | Wywo³uje funkcje obiektów: 'ProBar.start()', 'ProBar.step()', 'ProBar.stop()', sprawdza czy pobrane rekordy nie istniej¹ ju¿ w bazie danych a nastêpnie ³aduje tych których nie ma w bazie 'hd.db'
ETL | Brak parametrów | Brak | Wywo³uje fukcje: 'Extract', 'Transform', 'Load', nastepnie wyœwietla komunikat w obiekcie 'Tbox'
Update | Brak parametrów | Brak | Wywo³uje fukcje: 'Extract', 'Transform', pobieraj¹ce i przetwarzaj¹ce aktualne rekordy, nastêpnie sprawdza czy rekordy zosta³y zmienione i uaktualnia je oraz  sprawdza czy istniej¹ nowe komentarze i dodaje je do bazy danych
Thread_Me | 'my_fun' | Brak | Wywo³uje funkcje z podanym parametrem 'my_fun' obiektu 'threading.Thread()', oraz funkcjê 'start()' obiektu klasy threading. Parametr 'my_fun' jest wskaŸnikiem do funkcji. Funcja wywo³uje funcjê, której wskaŸnik jest podany jako parametr w nowym w¹tku.  


#### Klasy zewnêtrzne 

Klasa | Opis
----- | ----
tkinter | Pozwala tworzyæ interface graficzny u¿ytkowanika
pandas | Pozwla manipulowaæ danymi


### Plik main.py 

Zawiera obiekt klasy 'GUI' pozwalaj¹cy uruchomiæ interface graficzny u¿ytkowanika oraz wywo³ania funkcji na tym obiekcie: 'Application' - obiekt klasy 'GUI', 'Application.CreateWidget()' oraz 'Application.Start_App()' 






## Dokumentacja u¿ytkownika


### Instrukcja instalacji

1. Nale¿y pobraæ repozytorium
2. W folderze g³ównym nale¿y otworzyæ podfolder 'dist' i uruchomiæ plik wykonywalny 'main.exe'
3. Opcjonalnie mo¿na utworzyæ skrót folderu 'dist' w wybranej przez siebie lokalizacji.

### Opis programu
Program pozwala pobieraæ komentarze na temat wybranego serialu ze strony 'filmweb.pl'.
Pobrane informacje s¹ zapisywane w postaci rekordów w bazie danych 'sqlite'.
Aby pobraæ opinie o serialu nale¿y wpisaæ jego nazwê w polu opisanym 'Podaj tytu³ serialu', nastêpnie wybraæ przycisk 'Extract', 'Transform', 'Load', lub sam przycisk 'ETL'. Dane 
s¹ pobierane ze strony 'filmweb.pl', (Extract), przetwarzane na odpowiedni format (Transform) i nastêpnie wysy³ane do bazy danych (Load).
Program pozwala równie¿ na aktualizacjê wybranego tytu³u (przycisk 'Update') lub wyczyszczenie ca³ej bazy danych (przycisk 'Remove DB').
Aby przegl¹daæ zawartoœæ bazy danych nale¿y przejœæ do zak³adki 'Database' (lewy górny róg). Po naciœniêciu przycisku 'REFRESH' zostanie wyœwietlona ca³a zawartoœæ bazy danych aby odfiltrowaæ rekordy nale¿y wpisaæ frazê w wybranym polu i ponownie wcisn¹æ przycisk 'REFRESH'.
Przycisk 'Create CSV' s³u¿y do utworzenia pliku csv, który zawiera wyœwietlane rekordy w zak³adce 'Database'. Plik zostanie utworzony w folderze z plikiem 'main.exe'. 


















