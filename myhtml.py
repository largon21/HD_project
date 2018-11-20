import requests
from bs4 import BeautifulSoup



class HTML:
    def __init__(self, name):

        self.links = [] #links to websites of series
        self.com_links = []  # links to websites of series
        self.record=[] #data's list of series [title, emission_period , type, comment_head, comment, com_date_time, author, href]

        name = name.lower()
        URLname = name.replace(' ', '+')
        URL = 'https://www.filmweb.pl/serials/search?q={}'.format(URLname)

        numALLresults = 0  # it's necessary to stop 'while'

        while True:
            rhtml = requests.get(URL)  # download ALL website as HTML
            soup = BeautifulSoup(rhtml.text, 'html.parser')  # pulling data out of HTML

            titles = [t.text.lower() for t in soup.find_all('h3', attrs={'class': 'filmPreview__title'})]  # titles of movies, serils, games
            hrefs = [h['href'] for h in soup.find_all('a', href=True, attrs={'class': 'filmPreview__link'}) if h.text]  # links of movies, serials, games
            mix = list(zip(titles, hrefs))

            for title, href in mix:  # search chosen movie
                print(name, href, sep=' ')
                numALLresults += 1
                if title == name:
                    self.links.append((title, href))

            ############################------NEXT PAGE-------##################################
            next_tab = soup.find_all('a', href=True, attrs={'class': 'pagination__link', 'title': 'następna'})  # next page
            if not next_tab:
                break

            URL = 'https://www.filmweb.pl/serials/search' + next_tab[0]['href']
            print(URL, '<-- nastepna strona')

        try:
            quan = soup.find_all('div', attrs={'class': 'search__countResults'})
            num_results = (quan[0].find('span')).text
        except:
            num_results = 0
            print('blad przy odczycie ilosci wynikow')


        print(num_results,'<- odczyt ilosci rezultatow ze strony ||  ', numALLresults, '<- liczona wartosc wszystkich wynikow')
        print(self.links)


    def extract_data(self):
        for t, link in self.links:
            URL_discussion=  'https://www.filmweb.pl{}/discussion'.format(link) #creating link to comments of movie

            while True:
                rhtml=requests.get(URL_discussion)
                soup=BeautifulSoup(rhtml.text, 'html.parser')
                title = t
                emission_period=soup.find('span', attrs={'class': 'halfSize'}).text

                href_tag_soup=soup.find_all('h3', attrs={'class':'s-16'}) #list of tags with href to comment, and heading

                com_href= [h.contents[0]['href'] for h in href_tag_soup]
                title_list = [title for x in com_href]
                eperiod_list = [emission_period for x in com_href]

                self.com_links+=list(zip(title_list, eperiod_list, com_href))

                next_tab = [n for n in soup.find_all('a', href=True, attrs={'class': 'fbtn fbtn-page'}) if n.text=='następna »']  # next page
                print(next_tab, bool(next_tab),len(next_tab), '  <-- next_tab')
                if not next_tab:
                    print('break')
                    break

                URL_discussion = r'https://www.filmweb.pl' + next_tab[0]['href']
                print(URL_discussion, '<-- nastepna strona')

    def transform_data(self):
        for t, period, link in self.com_links:
            URL= 'https://www.filmweb.pl{}'.format(link)
            rhtml = requests.get(URL)
            soup=BeautifulSoup(rhtml.text, 'html.parser')
            try:
                autor=soup.find('a' ,attrs={'class':'pho-47'})['title']
            except:
                autor='brak autora'

            try:
                date_time_com=soup.find('a' ,attrs={'class':'cap'})['title'] #the date whene com was added
            except:
                date_time_com='brak daty i czasu'

            try:
                comment=soup.find('p' ,attrs={'class':'text'}).text
            except:
                comment='brak komentarza'

            try:
                head=soup.find('h1' ,attrs={'class':'inline hdr s-25'}).contents[0].text
            except:
                head='brak tematu'
            # grade=
            record=(t, period, autor, date_time_com, comment, head)
            print(record)
            self.record.append(record)

    def getRecords(self):
        rec=self.record[:]
        return rec


    def showupdata(self):


        print(len(self.com_links))
        print(len(self.record))


