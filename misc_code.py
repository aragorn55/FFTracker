import os
import re

from ff_datatypes import FanFicUrl, UrlInfo, FFDomain
from fanfic import FanFic
from fanfic_sql_builder import FanFicSql
from url_tools import UrlTool
from url_db import UrlDB
class CFanfic(FanFic):
    """description of class"""

    def toFile(self, ofic):
        chars = ",".join(ofic.Characters)
        fan = ",".join(ofic.Fandoms)
        rela = ""
        for item in ofic.Relationships:
            rela = rela + "[" + ",".join(item) + "]"

        output = ofic.Url + "; " + ofic.Title + "; " + ofic.Updated + "; " + ofic.Published + "; " \
                 + str(ofic.Chapters) + "; " + str(ofic.Words) + "; " + ofic.Summary + "; " + fan + "; " \
                 + ofic.Rating + "; " + chars + "; " + rela + "; " + ofic.GenreString
        return output

    def insert_to_db(self, path):
        oDB = FanFicSql(path)


class FanFicUrlTool(object):
    def fanfic_dot_net_normalize(self, surl):
        if surl.find("https://") > -1:
            ff_url = "http://" + surl[7:]

    def update_fff_domain_sources(self, fff_path):
        fff_domains = []
        py_sources = self.get_fff_file_list(fff_path)
        for py_class in py_sources:
            print("to do")
            #fff_domains.extend(self.get_domains_from_class(py_class))



    def get_fff_file_list(self, sPath):
            # The top argument for walk


            # The extension to search for
            exten = '.py'
            pyfile = []
            for dirpath, dirnames, files in os.walk(sPath):
                #            print(dirnames)
                #            print(dirpath)
                #            print(files)
                for name in files:
                    #                print(name)
                    if name.lower().endswith(exten):
                        file_name = os.path.join(dirpath, name)
                        pyfile.append(file_name)

            return pyfile


    def validateURL(self, vsUrl, site_pattern):
#        return re.match(self.getSiteURLPattern(), self.url)
        return re.match(site_pattern, vsUrl)

class  MiscCode(object):
    _url_info_list = []
    _domain_list = []
    def sort_url(self, surl):
        url_tool = UrlTool()
        url_info = url_tool.get_url_info(surl)
        for domain in self._domain_list:
            if domain.DomainUrl == url_info.Domain:
                domain.DomainCount += 1
                self._url_info_list.append(url_info)
                return True
        new_domain = FFDomain()
        new_domain.DomainUrl = url_info.Domain
        new_domain.DomainCount += 1
        self._domain_list.append(new_domain)
        return True

    def print_sort_results(self):
        oLinker = UrlDB('url.db')

        for item in self._domain_list:
            oLinker.save_domain(item)
            #            db.save_domain(item)
            print("Domain url: " + item.DomainUrl)
            print("url count: " + str(item.DomainCount))

        for url_item in self._url_info_list:
            oLinker.save_urlinfo(url_item)
            #            db.save_urlinfo(url_item)

        print("done")

class FFnetUrlTool(FanFicUrlTool):
    def fix_chapter_count(self, sUrl):
        url_list = sUrl.split('/')
        fixed_url = 'http://www.fanfiction.net/s/' + url_list[4] +'/1/'
        if len(url_list) > 6:
         fixed_url += url_list[6]





class FFnetFicUrl(FanFicUrl):

    def __init__(self, vsUrl):
        self.load_url(vsUrl)


    def load_url(self, vsurl):
        self.Publisher = 'www.fanfiction.net'
        url_list = vsurl.split('/')
        self.FFArchiveFicID = url_list[4]
        if len(url_list) > 6:
            self.FicPath = url_list[6]
        else:
            self.FicPath = ''
        self.Url = 'http://www.fanfiction.net/s/' + self.FFArchiveFicID + '/1/' + self.FicPath
        self.Domain = 'www.fanfiction.net'

