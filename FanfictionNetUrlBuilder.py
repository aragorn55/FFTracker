class FanfictionNetUrlBuilder(object):
    """description of class"""
    _http = "http://"

    _https = "https://"
    _sFFarchive = "m.fanfiction.net/"
    _protocol = ""

    _sFandomX = "Fate-stay-night-Crossovers/2746/0/"
    _fandom_url = "anime/Fate-stay-night/"

    def __init__(self, fandom_url, protocol, sFFarchive):
        self._fandom_url = fandom_url
        self._sFFarchive = sFFarchive
        self._protocol = protocol

    def GenerateUrl(self, minwords, pagenum):
        sUrl = ""
        sUrl = self.baseGenerateUrl(minwords, pagenum)
        return sUrl

    def baseGenerateUrl(self, minwords, pagenum):

        sUrl = ""

        sortid = self.get_srt_SorterID()
        censorid = self.get_r_CensorID()
        length = self.get_len_LengthID(minwords)

        languageid = self.get_lan_LanguageID()
        pageId = self.get_p_Page_num(pagenum)

        sUrl = self._protocol + self._sFFarchive + self._fandom_url
        surl = sUrl + "?" + sortid + languageid + censorid + length + pageId
        return surl

    def generate_page_url(self, pagenum):
        sUrl = ''
        sUrl = self._protocol + self._sFFarchive + self._fandom_url
        surl = sUrl + "?" + self.get_srt_SorterID() + self.get_g1_genreID1() + self.get_g2_GenreID2() \
               + self.get_e_g1_exclude_genreid1() + self.get_lan_LanguageID() + self.get_r_CensorID() \
               + self.get_len_LengthID(0) + self.get_t_timerange() + self.get_s_statusid() \
               + self.get_c1_characterid1() + self.get_c2_characterid2() + self.get_c3_characterid3() \
               + self.get_c4_characterid4() + self.get_e_c1_exclude_characterid1() \
               + self.get_e_c2_exclude_characterid2() + self.get_v1_VerseID1() + self.get_e_v1_exclude_verseid1()
        # + self  + self + self + self + self
        if pagenum > 1:
            surl += self.get_p_Page_num(pagenum)

        return surl

    def get_p_Page_num(self, pagenumber):
        if pagenumber > 1:
            pagenumber += 1
            sval = "&p=" + str(pagenumber)
            return sval
        return ""

    def get_srt_SorterID(self):
        sval = "&srt=" + "1"
        return sval

    def get_len_LengthID(self, words):
        if words == 0:
            sval = "&len=" + "0"
            return sval
        if words == -1:
            sval = "&len=" + "11"
            return sval
        if words == -5:
            sval = "&len=" + "51"
            return sval
        if words == 1:
            sval = "&len=" + "1"
            return sval
        if words == 5:
            sval = "&len=" + "5"
            return sval
        if words == 10:
            sval = "&len=" + "10"
            return sval
        if words == 20:
            sval = "&len=" + "20"
            return sval
        if words == 40:
            sval = "&len=" + "40"
            return sval
        if words == 60:
            sval = "&len=" + "60"
            return sval
        if words == 100:
            sval = "&len=" + "100"
            return sval

        sval2 = "&len=" + "0"
        return sval2

    def get_r_CensorID(self):
        sval = "&r=" + "10"
        return sval

    def get_lan_LanguageID(self):
        sval = "&lan=" + "1"
        return sval

    def get_v2_VerseID2(self):
        s = "&v2=0"
        return s

    def get_v1_VerseID1(self):
        s = "&v1=0"
        return s

    def get_e_v1_exclude_verseid1(self):
        s = "&_v1=0"
        return s

    def get_e_c1_exclude_characterid1(self):
        s = "&_c1=0"
        return s

    def get_e_c2_exclude_characterid2(self):
        s = "&_c2=0"
        return s

    def get_c4_characterid4(self):
        s = "&c4=0"
        return s

    def get_c3_characterid3(self):
        s = "&c3=0"
        return s

    def get_c2_characterid2(self):
        s = "&c2=0"
        return s

    def get_c1_characterid1(self):
        s = "&c1=0"
        return s

    def get_s_statusid(self):
        s = "&s=0"
        return s

    def get_t_timerange(self):
        s = "&t=0"
        return s

    def get_e_g1_exclude_genreid1(self):
        s = "&_g1=0"
        return s

    def get_g1_genreID1(self):
        s = "&g1=0"
        return s

    def get_g2_GenreID2(self):
        s = "&g2=0"
        return s
