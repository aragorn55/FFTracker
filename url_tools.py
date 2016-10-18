from ff_datatypes import UrlInfo, FFDomain, FanFicUrl
from url_db import UrlDB
from epubdb_ficdb_linker import DBLinker

class UrlTool(object):
    _url_info_list = []
    _domain_list = []



    def get_url_info(self, surl):
        new_info = UrlInfo()
        new_info.Url = surl
        icnt = surl.find("://")
        sdomain = surl[icnt + 3:]
        iend = sdomain.find("/")
        sdomain = sdomain[:iend]
        new_info.Domain = sdomain
        return new_info

    def set_up_db(self):
        oLinker = UrlDB('BookmarkDB.db')
        oLinker.create_url_db()
        return True



    def load_misc_bookmarks(self, sPath):
        fic_file = open(sPath, encoding="utf")
        fic_file_lines = []
        fan_fic_urls = []
        for aline in fic_file.readlines():
            #            values = aline.split()
            new_info = self.get_url_info(aline)

            fan_fic_urls.append(new_info)
        return fan_fic_urls

    def save_url_info_list(self, info_list):
        linker = UrlDB("BookmarkDB.db")
        for item in info_list:
            linker.save_misc_bookmark(item)







