import time
from urllib.request import urlopen

from bs4 import BeautifulSoup

from FFNetProcess import FFNetProcess
from FanfictionNetUrlBuilder import FanfictionNetUrlBuilder
from fanfic_sql_builder import FanFicSql


# specify the url

class FFnetUpdate(FFNetProcess):
    _last_date = ''

    def update_index(self, ffnet_url, fandom_name, isXover):
        oDB = FanFicSql(self._Path)
        #        ffNetFile = open(self._Path, 'a')

        self._is_xover = isXover
        self._Fandom = fandom_name
        oUrl = FanfictionNetUrlBuilder(ffnet_url, "http://", "www.fanfiction.net/")
        # cnt = 810
        cnt = 3
        sUrl = oUrl.generate_page_url(1)
        html = urlopen(sUrl)
        bsObj = BeautifulSoup(html, "html5lib")
        icnt = self.get_fandom_length(bsObj)
        icnt2 = 0
        for x in range(icnt):
            i = x + 1
            sUrl = oUrl.generate_page_url(i)
            try:
                html = urlopen(sUrl)
            except:
                time.sleep(60)
                html = urlopen(sUrl)
            bsObj = BeautifulSoup(html, "html5lib")
            _icnt = self.get_fandom_length(bsObj)
            if _icnt > 0:
                icnt2 = _icnt
            self.get_fic_from_page(bsObj)
            print(str(i))
            # time.sleep(6)
            time.sleep(5)
        if icnt2 > icnt:
            for a in range(icnt, icnt2):
                ii = a + 1
                sUrl = oUrl.generate_page_url(0, ii)
                html = urlopen(sUrl)
                bsObj = BeautifulSoup(html, "html5lib")
                self.get_fic_from_page(bsObj)
                print(str(ii))
                time.sleep(5)
