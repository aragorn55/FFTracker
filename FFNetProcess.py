import logging
import time
from urllib.request import urlopen

from bs4 import BeautifulSoup

from FanfictionNetUrlBuilder import FanfictionNetUrlBuilder
from fanfic import Author
from fanfic import FanFic
from fanfic_sql_builder import FanFicSql


# specify the url


class FFNetProcess(object):
    _Path = "ffnetindex.txt"
    _Fandom = ""
    logging.basicConfig(filename='ffprocess.log', level=logging.DEBUG)
    _is_xover = False

    def __init__(self, path):
        self._Path = path

    def get_db_fic_cnt(self):
        oDB = FanFicSql(self._Path)
        oDB.FilePath = self._Path
        db_fic_cnt = oDB.get_fanfic_cnt()
        return db_fic_cnt

    def is_oldest_fics_in_db(self, info):
        logging.debug('find-cnt')

        oDB = FanFicSql(self._Path)
        oDB.FilePath = self._Path
        logging.debug('DB: ' + self._Path)
        oUrl = FanfictionNetUrlBuilder(info.FandomUrl, "http://", "www.fanfiction.net/")
        # cnt = 810
        fic_cnt = 0
        sUrl = oUrl.generate_page_url(1)
        logging.debug('surl: ' + sUrl)
        try:
            html = urlopen(sUrl)
        except:
            print('sleep')
            time.sleep(60)
            try:
                html = urlopen(sUrl)
            except:
                logging.CRITICAL("html = urlopen(sUrl) failed" + sUrl)
                print("ERROR")
                return fic_cnt
        bsObj = BeautifulSoup(html, "html5lib")
        icnt = self.get_fandom_length(bsObj)
        sUrl = oUrl.generate_page_url(icnt)
        html = urlopen(sUrl)
        bsObj = BeautifulSoup(html, "html5lib")
        fics = self.get_fic_from_page(bsObj)
        for fic in fics:
            if not oDB.is_fic_in_Db(fic.FFNetID):
                return False
        return True

    def get_fandom_length(self, bsObj):
        center_element = bsObj.findAll("center")
        if len(center_element) == 0:
            logging.warning(bsObj.prettify(formatter="minimal"))
        else:
            for center in center_element:
                ce = center.findAll("a")
                page_cnt = 0
                for x in range(len(ce)):
                    descript = ce[x].get_text()
                    if descript == 'Last':
                        page_num = ce[x].get('href')
                        page_cnt = int(page_num[page_num.find("&p=") + 3:])
                        return page_cnt

        return 1

    def find_fandom_fic_cnt(self, ffnet_url):
        logging.debug('find-cnt')

        oDB = FanFicSql(self._Path)
        oDB.FilePath = self._Path
        logging.debug('DB: ' + self._Path)
        oUrl = FanfictionNetUrlBuilder(ffnet_url, "http://", "www.fanfiction.net/")
        # cnt = 810
        fic_cnt = 0
        sUrl = oUrl.generate_page_url(1)
        logging.debug('surl: ' + sUrl)
        try:
            html = urlopen(sUrl)
        except:
            print('sleep')
            time.sleep(60)
            try:
                html = urlopen(sUrl)
            except:
                logging.CRITICAL("html = urlopen(sUrl) failed" + sUrl)
                print("ERROR")
                return fic_cnt
        bsObj = BeautifulSoup(html, "html5lib")
        icnt = self.get_fandom_length(bsObj)
        sUrl = oUrl.generate_page_url(icnt)
        try:
            html = urlopen(sUrl)
        except:
            print('sleep')
            time.sleep(60)
            try:
                html = urlopen(sUrl)
            except:
                logging.CRITICAL("html = urlopen(sUrl) failed" + sUrl)
                print("ERROR")
                return fic_cnt
        bsObj = BeautifulSoup(html, "html5lib")
        nameList = bsObj.findAll("div", class_='z-list zhover zpointer ')
        last_pg_cnt = len(nameList)
        if icnt == 1:
            return last_pg_cnt
        else:
            icnt -= 1

            fic_cnt = icnt * 25
            fic_cnt += last_pg_cnt
            return fic_cnt

    def index_archive(self, ffnet_url, fandom_name, isXover):
        logging.debug('')
        self._is_xover = isXover
        self._Fandom = fandom_name
        oDB = FanFicSql(self._Path)
        oDB.FilePath = self._Path
        logging.debug('DB: ' + self._Path)
        last_index_date = oDB.get_newest_date()
        logging.debug('lastDate: ' + str(last_index_date))
        oUrl = FanfictionNetUrlBuilder(ffnet_url, "http://", "www.fanfiction.net/")
        # cnt = 810
        cnt = 3
        fic_cnt = 0
        sUrl = oUrl.generate_page_url(1)
        logging.debug('surl: ' + sUrl)
        html = urlopen(sUrl)
        bsObj = BeautifulSoup(html, "html5lib")
        if not isXover:
            self._Fandom = self.get_fandom(bsObj)
            print('fandom: ' + self._Fandom)
            logging.debug('Fandom: ' + self._Fandom)
        icnt = self.get_fandom_length(bsObj)
        logging.debug('Length: ' + str(icnt))
        icnt2 = 0
        last_fic_index_date = 0
        for x in range(icnt):
            if last_fic_index_date > last_index_date or last_fic_index_date == 0:
                sUrl = oUrl.generate_page_url(x)
                logging.debug('surl: ' + sUrl)
                try:
                    html = urlopen(sUrl)
                except:
                    print('sleep')
                    time.sleep(60)
                    try:
                        html = urlopen(sUrl)
                    except:
                        logging.CRITICAL("html = urlopen(sUrl) failed" + sUrl)
                        print("ERROR")
                        return fic_cnt

                bsObj = BeautifulSoup(html, "html5lib")
                try:
                    _icnt = self.get_fandom_length(bsObj)
                except:
                    pass
                logging.debug('Length: ' + str(_icnt))
                if _icnt > 0:
                    icnt2 = _icnt
                fic_list = []
                fic_list = self.get_fic_from_page(bsObj)
                fic_cnt += len(fic_list)
                print('Fic count this run is: ' +  str(fic_cnt))
                self.save_fic_list(fic_list)
                logging.debug('fic count: ' + str(fic_cnt))
                last_fic = fic_list[len(fic_list) - 1]
                last_fic_index_date = last_fic.get_date_comparison()
                print('page_num : ' + str(x))
                # time.sleep(6)
                time.sleep(5)
            else:
                return fic_cnt
            # time.sleep(6)
        if icnt2 > icnt:
            for a in range(icnt, icnt2):
                if last_fic_index_date > last_index_date:
                    sUrl = oUrl.generate_page_url(a)
                    html = urlopen(sUrl)
                    bsObj = BeautifulSoup(html, "html5lib")
                    fic_list = self.get_fic_from_page(bsObj)
                    fic_cnt += len(fic_list)
                    self.save_fic_list(fic_list)
                    last_fic = fic_list[len(fic_list) - 1]
                    last_fic_index_date = last_fic.get_date_comparison()
                    print('page_num: ' + str(a))
                    time.sleep(5)
                else:
                    return fic_cnt
        return fic_cnt

    def reindex_archive(self, ffnet_url, fandom_name, isXover, start_page_num):
        logging.debug('')
        self._is_xover = isXover
        self._Fandom = fandom_name
        oDB = FanFicSql(self._Path)
        oDB.FilePath = self._Path
        logging.debug('DB: ' + self._Path)

        logging.debug('lastDate: ' + str(0))
        oUrl = FanfictionNetUrlBuilder(ffnet_url, "http://", "www.fanfiction.net/")
        # cnt = 810
        cnt = 3
        fic_cnt = 0
        sUrl = oUrl.generate_page_url(1)
        logging.debug('surl: ' + sUrl)
        html = urlopen(sUrl)
        bsObj = BeautifulSoup(html, "html5lib")
        if not isXover:
            self._Fandom = self.get_fandom(bsObj)
            print('fandom: ' + self._Fandom)
            logging.debug('Fandom: ' + self._Fandom)
        icnt = self.get_fandom_length(bsObj)
        logging.debug('Length: ' + str(icnt))
        icnt2 = 0
        for x in range(start_page_num, icnt):

            sUrl = oUrl.generate_page_url(x)
            logging.debug('surl: ' + sUrl)
            try:
                html = urlopen(sUrl)
            except:
                print('sleep')
                time.sleep(60)
                try:
                    html = urlopen(sUrl)
                except:
                    logging.CRITICAL("html = urlopen(sUrl) failed" + sUrl)
                    print("ERROR")
                    return fic_cnt

            bsObj = BeautifulSoup(html, "html5lib")
            try:
                _icnt = self.get_fandom_length(bsObj)
            except:
                pass
            logging.debug('Length: ' + str(_icnt))
            if _icnt > 0:
                icnt2 = _icnt
            fic_list = self.get_fic_from_page(bsObj)
            fic_cnt += len(fic_list)
            self.save_fic_list(fic_list)
            logging.debug('fic count: ' + str(fic_cnt))
            print('page_num : ' + str(x))
            # time.sleep(6)
            time.sleep(5)
        if icnt2 > icnt:
            for a in range(icnt, icnt2):
                sUrl = oUrl.generate_page_url(a)
                html = urlopen(sUrl)
                bsObj = BeautifulSoup(html, "html5lib")
                fic_list = self.get_fic_from_page(bsObj)
                fic_cnt += len(fic_list)
                self.save_fic_list(fic_list)
                print('page_num: ' + str(a))
                time.sleep(5)
        return fic_cnt

    def get_fandom(self, bsObj):
        title_elements = bsObj.findAll("title")
        title_element = title_elements[0]
        fan = title_element.get_text()
        iend = fan.find(" FanFiction Archive | FanFiction")
        fandom = fan[:iend]
        return fandom

    def save_fic_list(self, ficList):
        oDB = FanFicSql(self._Path)
        oDB.FilePath = self._Path
        #        ffNetFile = open(self._Path, 'a')
        for x in range(len(ficList)):
            item = ficList[x]
            oDB.save_fic(item)
        #            output = item.toFile()
        #            ffNetFile.write(output)
        #            ffNetFile.write("\r\n")
        #        ffNetFile.close()

    def getCharacterListFromString(self, item):
        charList = item.split(",")
        return charList

    def get_fic_from_page(self, bsObj):
        nameList = bsObj.findAll("div", class_='z-list zhover zpointer ')
        date = ""
        ficList = []
        # browser.open(quote_page)

        for x in range(len(nameList)):
            item = nameList[x]
            ofic = FanFic()
            ofic = self.get_fic(item, )
            ficList.append(ofic)

        return ficList

    def get_xoverfandoms(self, descString):
        fandomstring = ""
        fandom_list = []
        istart = descString.rfind("Crossover - ")
        iend = descString.rfind(" - Rated:")
        fandomstring = descString[istart + 12: iend]
        isplit = fandomstring.count(" & ")
        if isplit > 1:
            fandom_list.append(fandomstring)
        else:
            fandom_list = fandomstring.split(" & ")
        return fandom_list

    def get_fic(self, item):
        descString = ''
        description = ''
        ofic = FanFic()
        ofic.reset()
        ofic.Author = self.get_author(item)
        href = self.get_href(item)
        ofic.Url = self.get_story_url(href)
        ofic.FFNetID = self.get_ffnet_id(href)
        ofic.Title = self.get_title(href)

        print('fic url: ' + ofic.Url)
        description = item.findAll("div", class_='z-indent z-padtop')
        descString = self.get_title(description[0])
        if self._is_xover:
            ofic.Fandoms.extend(self.get_xoverfandoms(descString))
        else:
            ofic.Fandoms.append(self._Fandom)
        ofic.Summary = self.get_summary(descString)
        ofic.Rating = self.get_rating(descString)
        ofic.Genres.extend(self.get_genre(descString))
        ofic.Chapters = self.get_chapters(descString)
        ofic.Words = self.get_words(descString)
        ofic.Status = self.get_status(descString)
        charstring = self.get_characterstring(descString)
        #         print('fic charstring: ' + charstring)
        ofic.Characters.extend(self.get_Characters(charstring))
        #        print('fic char_num: ' + str(len(ofic.Characters)))
        ofic.Relationships.extend(self.get_RelationShips(charstring))
        ofic.CharactersString = charstring
        meta = item.findAll("div", class_='z-padtop2 xgray')
        metastring = self.get_title(meta[0])
        dates = meta[0].findAll("span")
        if len(dates) > 1:
            date1 = dates[0]
            updated = date1['data-xutime']
            date2 = dates[1]

            published = date2['data-xutime']
            ofic.Published = published
            ofic.Updated = updated
            date = updated
        #            print('fic updated: ' + updated)
        #            print('fic pub: ' + published)
        else:
            date1 = dates[0]
            published = date1['data-xutime']
            ofic.Published = published
            date = published
        #            print('fic pub: ' + published)
        return ofic

    def get_title(self, href):
        title = href.get_text()
        return title

    def get_status(self, href):
        icnt = href.rfind('- Complete')
        if icnt > -1:
            return 'Complete'
        else:
            return 'In-Progress'
        return title

    def get_ffnet_id(self, href):
        ffnet = href['href']
        iend = ffnet.find("/", 3)
        fft = ffnet[3:iend]
        #        print('fic ffnetidf: ' + fft)
        return fft

    def get_story_url(self, href):
        storyurl = "http://www.fanfiction.net"
        storyurl = storyurl + href['href']
        return storyurl

    def get_author(self, item):
        surls = item.findAll("a")
        _author = Author()
        ffneturl = "http://www.fanfiction.net"
        for x in range(len(surls)):
            href = surls[x]
            url = href['href']
            if url.find('/u/') == 0:
                author_list = url.split('/')
                if len(author_list) == 4:
                    # first = author_list[0]
                    # type = author_list[1]
                    ffnetid = author_list[2]
                    a_name = author_list[3]
                    _author.FFNetID = ffnetid
                    _author.AuthorName = a_name
                    _author.Url = ffneturl + url
                elif len(author_list) == 3:
                    ffnetid = author_list[2]
                    _author.FFNetID = ffnetid
                    _author.Url = ffneturl + url
                else:
                    _author.Url = ffneturl + url
                return _author
        _author.FFNetID = '0'
        _author.AuthorID = '0'
        return _author

    def get_href(self, item):
        surl = item.findAll("a", class_='stitle')
        href = surl[0]
        return href

    def get_summary(self, descString):
        rateCnt = descString.rfind("Rated: ")
        summ = descString[0:rateCnt]
        return summ

    def get_genre(self, descString):
        genrestring = ""
        genre_list = []
        istart = descString.rfind("English - ")
        iend = descString.rfind("Chapters:")
        genrestring = descString[istart + 10: iend]
        # print('fic genrestring: ' + genrestring)
        if genrestring.find(" - ") > -1:
            genrestring = genrestring[0:genrestring.find(" - ")]
            if genrestring.find("/") > -1:
                genre_list = genrestring.split("/")
            else:
                genre_list.append(genrestring)
        return genre_list

    def get_rating(self, descString):
        rateCnt = descString.rfind("Rated: ")
        rate = descString[rateCnt + 7: rateCnt + 8]
        ficRate = ""
        if rate[0:1] == "K":
            if rate[1:2] == "+":
                ficRate = "K+"
            else:
                ficRate = "K"
        elif rate[0:1] == "T":
            ficRate = "T"
        else:
            ficRate = "M"
        return ficRate

    def get_Characters(self, descString):
        if descString.count("[") > 0:
            d = descString.replace('[', ',')
            descString = d.replace(']', ',')
        dd = descString.split(',')
        chars = []
        for item in dd:
            if len(item) > 2:

                item = item.strip()
                #                print('fic character: ' + item)
                chars.append(item)
            elif len(item) == 0 or item.isspace():
                item
            else:
                chars.append(item)
        return chars

    def get_RelationShips(self, descString):
        charstring = ""
        char_strings = []
        rels = []
        relation = []
        front = ''
        back = ''
        leftcnt = descString.count("[")
        for x in range(leftcnt):
            icnt = descString.find("[")
            iend = descString.find("]")
            char_strings.append(descString[:icnt])
            rels.append(descString[icnt:iend])
            descString = descString[iend:]
        for x in range(len(rels)):
            r_string = rels[x]
            r_string = r_string.replace('[', '')
            r_string = r_string.replace(']', '')
            r = self.get_Characters(r_string)
            relation.append(r)
        return relation

    def get_characterstring(self, descString):
        icnt = descString.rfind("Published: ")
        icnt = descString.find("-", icnt)
        if icnt == -1:
            return ""
        iend = descString.rfind("- Complete", icnt + 1)
        if iend == -1:
            iend = len(descString)
            characterstring = descString[icnt + 2:]
            return characterstring
        else:
            characterstring = descString[icnt + 2: iend - 1]
            return characterstring

    def get_chapters(self, descString):
        icnt = descString.rfind("Chapters: ")
        iend = descString.find("-", icnt)
        chapters = descString[icnt + 10: iend - 1]
        chapters = chapters.strip()
        iChap = int(chapters)
        return iChap

    def get_words(self, descString):
        icnt = descString.rfind("Words: ")
        iend = descString.find("-", icnt)
        words = descString[icnt + 7: iend - 1]
        words = words.strip()
        words = words.replace(',', '')
        words = int(words)
        return words
