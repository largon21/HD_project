from tkinter import *
from tkinter import ttk
from mysqlite import Database
from myhtml import HTML

class App:
    def __init__(self):

        # main window
        self.main_window = Tk()
        self.main_window.title('HD window')
        self.main_window.geometry("1000x600")
        self.My_DATABASE = Database()
        self.My_data_HTML = HTML()

        # configuration row and column
        for i in range(0, 21, 1):
            self.main_window.rowconfigure(i, weight=1)
            self.main_window.columnconfigure(i, weight=1)


    def CreateWidget(self):
        #####LOOK####
        WinColour = 'gray23'
        LefSideColour = 'slate gray'
        ConterButColour = 'thistle4'

        ########## NOTEBOOK ################
        Nbook = ttk.Notebook(self.main_window)
        Nbook.grid(row=1, column=0, columnspan=21, rowspan=19, sticky=NSEW)

        # --------TAB Setting---------
        tab1 = Frame(self.main_window)
        Nbook.add(tab1, text='Setting')
        # configuration row and column
        for i in range(0, 21, 1):
            tab1.rowconfigure(i, weight=1)
            tab1.columnconfigure(i, weight=1)

        ################## Label #################
        label_title = Label(tab1, text='Podaj tytul serialu:')
        label_title.grid(row=0, column=9, columnspan=3, sticky=NSEW)
        ################## ENTRY #################
        self.entry_title = Entry(tab1)
        self.entry_title.grid(row=1, column=8, columnspan=5, sticky=NSEW)

        ################## BUTTONS #################
        # EXTRACT BUTTON
        Extract_Button = Button(tab1, text='Extract', bg=WinColour, command=self.Extract)
        Extract_Button.grid(row=3, column=0, columnspan=7, sticky=NSEW)

        # TRANSFER BUTTON
        Transform_Button = Button(tab1, text='Transform', bg=WinColour, command=self.Transform)
        Transform_Button.grid(row=3, column=7, columnspan=7, sticky=NSEW)

        # LOAD BUTTON
        Load_Button = Button(tab1, text='Load', bg=WinColour, command=self.Load)
        Load_Button.grid(row=3, column=14, columnspan=7, sticky=NSEW)

        # EXTRACT TRANSFER LOAD BUTTON
        ETL_Button = Button(tab1, text='ETL', bg=WinColour, command=self.ETL)
        ETL_Button.grid(row=4, columnspan=21, sticky=NSEW)

        # EXTRACT TRANSFER LOAD BUTTON
        REMOVE_Button = Button(tab1, text='Remove DB', bg='red', command=self.RemoveAllDB)
        REMOVE_Button.grid(row=7, column=9, columnspan=3, sticky=NSEW)

        ###############TEXT FRAME################
        TextFrame = Frame(tab1)
        TextFrame.grid(row=10, columnspan=21, rowspan=4)

        ################### TEXT  - TAB 1#################
        Sbar = Scrollbar(TextFrame)  # SCROLLBAR NEXT TO TEXT BOX
        self.Tbox = Text(TextFrame, height=15, width=80)  # TEXT BOX
        Sbar.pack(side=RIGHT, fill=BOTH, expand=1)  #
        self.Tbox.pack(side=LEFT, fill=BOTH, expand=1)
        Sbar.config(command=self.Tbox.yview)
        self.Tbox.config(yscrollcommand=Sbar.set)



        #############TAB 2 - Database###########
        tab2 = Frame(self.main_window)
        Nbook.add(tab2, text='Database')
        # configuration row and column
        for i in range(0, 21, 1):
            tab2.rowconfigure(i, weight=1)
            tab2.columnconfigure(i, weight=1)

        self.Tview = ttk.Treeview(tab2)  # '''height= 20'''
        self.Tview['columns'] = ['title', 'period', 'username', 'date', 'comment', 'head']

        self.Tview.heading('#0', text='', anchor='w')
        self.Tview.column('#0', stretch=NO, width=5, anchor='w')
        self.Tview.heading('title', text='title')
        self.Tview.heading('period', text='period')
        self.Tview.heading('username', text='username')
        self.Tview.heading('date', text='date')
        self.Tview.heading('comment', text='comment')
        self.Tview.heading('head', text='head')

        # self.Tview.insert("", "end", values=(
        #     'jakis tytul', 'jakis okres', 'jakas nazwa ', 'jakas data', 'komentarzus \n dsd \n fsf', 'czoo'))
        # self.Tview.insert("", "end", values=(
        #     'jakis tytul', 'jakis okres', 'jakas nazwa ', 'jakas data', 'kascaaa \n dsd \n fsf', 'czoo'))

        ################TEXT FRAME#################
        TextFrameDB = Frame(tab2)
        TextFrameDB.grid(row=18, columnspan=21, rowspan=3)

        #######DATABASE TREEVIEW#########
        SbarDB = Scrollbar(TextFrameDB)  # SCROLLBAR NEXT TO TEXT BOX
        self.TboxDB = Text(TextFrameDB, height=10, width=80)  # TEXT BOX
        SbarDB.pack(side=RIGHT, fill=BOTH, expand=1)  #
        self.TboxDB.pack(side=LEFT, fill=BOTH, expand=1)
        SbarDB.config(command=self.TboxDB.yview)
        self.TboxDB.config(yscrollcommand=SbarDB.set)
        TSbar = Scrollbar(tab2)
        TSbar.grid(row=8, columnspan=21, rowspan=10, sticky='NSE')
        self.Tview.grid(row=8, columnspan=20, rowspan=10, sticky=NSEW)
        self.Tview.config(yscrollcommand=TSbar.set)
        TSbar.config(command=self.Tview.yview)

        ############PRESS FUN#############
        self.Tview.bind('<ButtonRelease-1>', self.Show_column)
        self.Tview.config(selectmode='browse')

        ############REFRESH BUTTON############
        self.Refresh_Button=Button(tab2, text='REFRESH', bg=WinColour, command=self.SelectFromDB)
        self.Refresh_Button.grid(row=3, column=8, columnspan=4, sticky=NSEW)

        ###########FILTERS#################
        Label(tab2, text='title: ').grid(row=6, column=1, columnspan=1, sticky=NSEW)
        self.Title_filter=Entry(tab2)
        self.Title_filter.grid(row=6, column=2, columnspan=1, sticky=NSEW)

        Label(tab2, text='period: ').grid(row=6, column=4, columnspan=1, sticky=NSEW)
        self.Period_filter = Entry(tab2)
        self.Period_filter.grid(row=6, column=5, columnspan=1, sticky=NSEW)

        Label(tab2, text='username: ').grid(row=6, column=7, columnspan=1, sticky=NSEW)
        self.User_filter = Entry(tab2)
        self.User_filter.grid(row=6, column=8, columnspan=1, sticky=NSEW)

        Label(tab2, text='date: ').grid(row=6, column=10, columnspan=1, sticky=NSEW)
        self.Date_filter = Entry(tab2)
        self.Date_filter.grid(row=6, column=11, columnspan=1, sticky=NSEW)

        Label(tab2, text='comment: ').grid(row=6, column=13, columnspan=1, sticky=NSEW)
        self.Com_filter = Entry(tab2)
        self.Com_filter.grid(row=6, column=14, columnspan=1, sticky=NSEW)

        Label(tab2, text='head: ').grid(row=6, column=16, columnspan=1, sticky=NSEW)
        self.Head_filter = Entry(tab2)
        self.Head_filter.grid(row=6, column=17, columnspan=1, sticky=NSEW)


    def Show_column(self, event):  #tab2-database database Tabel (Tview : Treeview) - fun
        try:
            self.TboxDB.delete(1.0, END)
            item = self.Tview.selection()[0]
            num_value=self.Tview.identify_column(event.x)
            num_value=int(num_value[-1:])-1

            comment = self.Tview.item(item)['values'][num_value]
            self.TboxDB.insert(END, comment)

        except:
            pass


    def Insert_DB(self, DB): #shows all DB which is send
        try:
            for i in self.Tview.get_children():
                self.Tview.delete(i)

            for title, period, username, date, comment, head in  DB:
                self.Tview.insert("", "end", values=(title, period, username, date, comment, head))
        except:
            pass

    def Start_App(self):
        mainloop()



    def SelectFromDB(self):
        Title=self.Title_filter.get()
        Period=self.Period_filter.get()
        User=self.User_filter.get()
        Date=self.Date_filter.get()
        Com=self.Com_filter.get()
        Head=self.Head_filter.get()

        DATABASE_records = self.My_DATABASE.select(title=Title, period=Period, username=User, date=Date, comment= Com, head=Head)
        self.Insert_DB(DATABASE_records)

    def RemoveAllDB(self):
        self.My_DATABASE.delete_all_records()
        self.Tbox.delete(1.0, END)
        comment='ALL DATABASE HAS BEEN REMOVED!!!'
        self.Tbox.insert(END, comment)

    def Extract(self):
        self.title=self.entry_title.get()

        if self.title:
            self.My_data_HTML.Start_extract(self.title)
            self.My_data_HTML.extract_data()
        self.Tbox.delete(1.0, END)
        comment='Extracted: '+ self.title
        self.Tbox.insert(END, comment)

    def Transform(self):
        self.My_data_HTML.transform_data()
        self.My_data_HTML.showupdata()  # test, print self.data()- list of data
        self.HTML_records = self.My_data_HTML.getRecords()

        self.Tbox.delete(1.0, END)
        comment = 'Transformed: ' + self.title
        self.Tbox.insert(END, comment)

    def Load(self):

        self.DATABASE_records = self.My_DATABASE.select(title=self.title, period='', username='', date='', comment='', head='')

        buffer = [x for x in self.HTML_records if x not in self.DATABASE_records]  # HTML_records.remove(x)
        [print(b) for b in buffer]
        print(len(buffer))

        self.My_DATABASE.load_data(buffer)
        self.Tbox.delete(1.0, END)
        comment = 'Loaded: ' + self.title
        self.Tbox.insert(END, comment)
        self.HTML_records=[]


    def ETL(self):
        pass





test = App()

test.CreateWidget()
# quote = """HAMLET: To be, or not to be--that is the question"""
# test.Insert_statement(quote)

test.Start_App()