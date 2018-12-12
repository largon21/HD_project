import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('hd.db')
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS stocks(title TEXT, period TEXT, username TEXT, date TEXT, comment TEXT, head TEXT)')
        self.selected_records=[]

    def load_data(self, tuple_data):

        for  t, e_p, u, d_a, com ,h_c in tuple_data:
            self.c.execute("INSERT INTO stocks VALUES (?,?,?,?,?,?)", (t, e_p, u, d_a, com, h_c)) #"INSERT INTO stuffToPlot (title, period, username, date, comment, head) VALUES (?,?,?,?,?,?)"
            self.conn.commit()

    def select(self, title, period, username, date, comment, head):
        selected_values=''
        searched_phrases=[]
        if title != '' : selected_values += "title=? "; searched_phrases.append(title)
        if period != '': selected_values += "period=? "; searched_phrases.append(period)
        if username != '': selected_values += "username=? "; searched_phrases.append(username)
        if date != '': selected_values += "date=? "; searched_phrases.append(date)
        if comment != '' : selected_values += "comment=? "; searched_phrases.append(comment)
        if head != '' : selected_values += "head=? "; searched_phrases.append(head)

        if len(selected_values):
            selected_values=selected_values[:-1].replace(" ", " AND ")
            self.c.execute("SELECT * from stocks WHERE {}".format(selected_values), tuple(searched_phrases))
            self.selected_records = self.c.fetchall()
        else :
            self.c.execute("SELECT * from stocks", tuple(searched_phrases))
            self.selected_records = self.c.fetchall()


        chosen_records = self.selected_records[:]
        return chosen_records

    def update(self, records):
        i=0
        for title, period, username, date, comment, head in records:
            searched_phrase=comment, head, title, period, username, date
            self.c.execute("UPDATE stocks SET comment=?, head=? WHERE title=? AND period=? AND username=? AND date=?", tuple(searched_phrase))
            self.conn.commit()
            i+=1

        return i
        # title
        # period
        # username
        # date
        # comment
        # head





    def delete_all_records(self):
        self.c.execute('DELETE from stocks')
        self.conn.commit()

    # def show_database(self):
    #     [print(record) for record in self.c.execute('SELECT * from stocks')]

    def __del__(self):
        self.c.close()
        self.conn.close()
        print('__del__()')