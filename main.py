from myhtml import HTML
from mysqlite import Database

series_title = input('Nazwa filmu: ')

data_from_HTML = HTML(series_title)
data_from_HTML.extract_data()
data_from_HTML.transform_data()

data_from_HTML.showupdata()   #test, print self.data()- list of data

HTML_records = data_from_HTML.getRecords()

My_DATABASE = Database()

DATABASE_records= My_DATABASE.select(title=series_title, period='', username='', date='', comment='', head='')

buffer=[x for x in HTML_records if x not in DATABASE_records] #HTML_records.remove(x)
[print(b) for b in buffer]
print(len(buffer))

My_DATABASE.load_data(buffer)


yes_no = 'no' # input('Czy usunac wszystkie recordy?')
if yes_no == 'yes':
    My_DATABASE.delete_all_records()
    print('Dane zostaly usuniete')
else:
    print('Dane zostaly zachowane')

# My_DATABASE.show_database()