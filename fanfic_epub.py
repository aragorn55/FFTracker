import os
import ebooklib
import sqlite3
from ebooklib import epub
from fanfic import FanFicEBook
from bs4 import BeautifulSoup
from fic_file_db import FicFileDb
from ebooklib.epub import EpubHtml
#from epub_meta import get_epub_metadata, get_epub_opf_xml, EPubException
from os import scandir, walk
#from yael import SimpleEPUB



class EpubFicTool(object):

    def setup_db(self):
        db = FicFileDb('file.db')
        db.create_db('file.db')


    def get_file_list(self, sPath):
        # The top argument for walk


        # The extension to search for
        exten = '.epub'
        epubs = []
        for dirpath, dirnames, files in os.walk(sPath):
#            print(dirnames)
#            print(dirpath)
#            print(files)
            for name in files:
#                print(name)
                if name.lower().endswith(exten):
                    file_name =  os.path.join(dirpath, name)
                    epubs.append(file_name)

        return  epubs

    def procees_files(self, epub_files):
        fic_list = []
        db = FicFileDb('file.db')
        for file in epub_files:
            try:
                print(file)
                fic =  self.load_fic_file(file)
                fic_list.append(fic)
                print('loaded')
                db.insert_fic(fic)
                print('inserted')
            except:
                print('error')
                pass



    def load_fic_file(self, sPath):
        ebook = epub.read_epub(sPath)
        _items = ebook.items
        _item = _items[2]
        #doc = EpubHtml(_item)
        html = _item.content
        bsObj = BeautifulSoup(html, "html5lib")
        fic = FanFicEBook()
        surls = bsObj.findAll("a")
        href = surls[0]
        storyurl = href['href']
        fic.Url = storyurl
        href = surls[1]
        authorurl = href['href']
        fic.Author.Url = authorurl
        fic.Author.AuthorName =  href.get_text()
        text = bsObj.get_text()
        fic.FilePath = sPath
        fic.Characters.extend(self.get_Characters(text))
        fic.Chapters = self.get_chapters(text)

        fic.Fandoms.extend(self.get_category(text))
        fic.Genres.extend(self.get_genre(text))
        fic.Pairings.extend(self.get_Pairings(text))
        publisher_string = self.get_publisher(text)
        fic.Publisher = publisher_string
        if publisher_string == 'www.fanfiction.net':
            fic.FFNetID = self.get_ffnet_id(fic.Url)

        fic.Packaged = self.get_packaged(text)
        fic.Published = self.get_published(text)
        fic.Updated = self.get_updated(text)
        fic.Rating = self.get_rating(text)
        fic.Relationships.extend(self.get_RelationShips(text))
        fic.Words = self.get_words(text)
        fic.Status = self.get_status(text)
        fic.Summary = self.get_summary(text)

        return fic
#        print(text)



#        for item in _items:
#            print(item.get_content())
#        try:
#            meta = get_epub_metadata(sPath)
#            print(meta)
#        ebook = SimpleEPUB(path=sPath)

#        print('Path: ' + sPath)
#        print('toc' + ebook.resolved_toc)
#        print("Spine")
#        for i_p_spine_item in ebook.resolved_spine:

#            print(i_p_spine_item)
#        print("")
#        print(ebook.description)
#        print(ebook.subjects)

#            print(ebook)
#        except:
#            print('fail')
    def get_fandom(self, bsObj):
        title_elements = bsObj.findAll("title")
        title_element = title_elements[0]
        fan = title_element.get_text()
        iend = fan.find(" FanFiction Archive | FanFiction")
        fandom = fan[:iend]
        return fandom

    def get_title(self, bsObj):
        title_elements = bsObj.findAll("title")
        title_element = title_elements[0]
        title = title_element.get_text()
        return title



    def get_ffnet_id(self, url):

        icnt = url.find("/s/")
        iend = url.find('/', icnt + 3 )
        fft = url[icnt + 3:iend]

        #        print('fic ffnetidf: ' + fft)
        return fft

    def get_story_url(self, descString):
        rateCnt = descString.find("Story:")
        if rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            summ = descString[rateCnt + 9:iend]
            return summ
        else:
            return 'Summary'


    def get_href(self, item):
        surl = item.findAll("a", class_='stitle')
        href = surl[0]
        return href

    def get_summary(self, descString):
        rateCnt = descString.find("Summary:")
        if rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            summ = descString[rateCnt + 9:iend]
            return summ
        else:
            return 'Summary'

    def get_category(self, descString):
        summ = ''
        category_list = []
        rateCnt = descString.find("Category:")
        if rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            summ = descString[rateCnt + 10:iend]
            icnt = summ.find(',')
            if icnt > -1:
                categories = summ.split(',')
                for item in categories:
                    item = item.strip()
                    category_list.append(item)
            else:
                summ = summ.strip()
                category_list.append(summ)

            return category_list
        return category_list

    def get_genre(self, descString):
        genre_list = []
        rateCnt = descString.find("Genre:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            genrestring = descString[rateCnt + 7:iend]


            if genrestring.find(",") > -1:
                genres = genrestring.split(",")
                for genre_string in genres:
                    genre_string = genre_string.strip()
                    genre_list.append(genre_string)
            else:
                genre_list.append(genrestring)
            return genre_list
        return genre_list

    def get_rating(self, descString):
        ficRate = ""
        rateCnt = descString.find("Rated:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            rate = descString[rateCnt + 7: iend]

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
        return ficRate

    def get_Characters(self, descString):
        characters_list = []
        rateCnt = descString.find("Characters:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            charstring = descString[rateCnt + 12: iend]
            if charstring.find(",") > -1:
               cstrings = charstring.split(",")
               for cstring in cstrings:
                   character = cstring.strip()
                   characters_list.append(character)
            else:
                charstring = charstring.strip()
                characters_list.append(charstring)
            return characters_list
        return characters_list

    def get_Pairings(self, descString):
        characters_list = []
        rateCnt = descString.find("Pairings:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            charstring = descString[rateCnt + 10: iend]
            characters_list = []

            if charstring.find(",") > -1:
                cstrings = charstring.split(",")
                for cstring in cstrings:
                    character = cstring.strip()
                    characters_list.append(character)
            else:
                charstring = charstring.strip()
                characters_list.append(charstring)
            return characters_list
        return characters_list

    def get_RelationShips(self, descString):
        relationship_list = []
        rateCnt = descString.find("Pairings:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            charstring = descString[rateCnt + 10: iend]
            if charstring.find(",") > -1:
                cstrings = charstring.split(",")
                for cstring in cstrings:
                    relationship_list.append(self.convert_pairing_string_to_list(cstring))
            else:
                relationship_list.append(self.convert_pairing_string_to_list(charstring))
            return relationship_list
        return relationship_list
    def convert_pairing_string_to_list(self, paring_string):
        relationship_list = []
        icnt = paring_string.find('/')
        if icnt > -1:
            pairing_list = paring_string.split('/')
            for item in pairing_list:
                item = item.strip()
                relationship_list.append(item)
        else:
            paring_string = paring_string.strip()
            relationship_list.append(paring_string)
        return relationship_list

    def get_chapters(self, descString):
        iChap = 0
        rateCnt = descString.find("Chapters:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            chapters = descString[rateCnt + 10:iend]
            chapters = chapters.strip()
            iChap = int(chapters)
            return iChap
        return iChap

    def get_words(self, descString):
        iwords =  -1
        rateCnt = descString.find("Words:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            words = descString[rateCnt + 7:iend]
            words = words.strip()
            words = words.replace(',', '')
            iwords = int(words)
            return iwords
        return iwords

    def get_status(self, descString):
        summ = ''
        rateCnt = descString.find("Status:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            summ = descString[rateCnt + 8:iend]
            return summ
        return summ

    def get_published(self, descString):
        summ = ''
        rateCnt = descString.find("Published:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            summ = descString[rateCnt + 11:iend]
            return summ
        return summ

    def get_publisher(self, descString):
        summ = ''
        rateCnt = descString.find("Publisher:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            summ = descString[rateCnt + 11:iend]
            return summ
        return summ

    def get_updated(self, descString):
        summ = ''
        rateCnt = descString.find("Updated:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            summ = descString[rateCnt + 9:iend]
            return summ
        return summ

    def get_packaged(self, descString):
        summ = ''
        rateCnt = descString.find("Packaged:")
        if  rateCnt > -1:
            iend = descString.find('\n', rateCnt)
            summ = descString[rateCnt + 10:iend]
            return summ
        return summ
