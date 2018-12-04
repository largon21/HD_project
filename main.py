# from myhtml import HTML
# from mysqlite import Database
# from GUI import *
x=input('Podaj nazwe: ')
print(bool(x))

# data_from_HTML = HTML() #<----objekt
#
# data_from_HTML.Start_extract()
# data_from_HTML.extract_data()
# data_from_HTML.transform_data()
#
# data_from_HTML.showupdata()   #test, print self.data()- list of data
#
# HTML_records = data_from_HTML.getRecords()
#
# My_DATABASE = Database()
#
# DATABASE_records= My_DATABASE.select(title=series_title, period='', username='', date='', comment='', head='')
#
# buffer=[x for x in HTML_records if x not in DATABASE_records] #HTML_records.remove(x)
# [print(b) for b in buffer]
# print(len(buffer))
#
# My_DATABASE.load_data(buffer)
#
#
#
#
# # My_DATABASE.show_database()
#
# test = App()
#
# test.CreateWidget()
# # quote = """HAMLET: To be, or not to be--that is the question"""
# # test.Insert_statement(quote)
# # test.Insert_DB(DATABASE_records)
# test.Start_App()