class UrlInfo(object):
    _URL = ""
    _Domain = ""
    _Path = ""

    @property
    def Url(self):
        return self._URL

    @Url.setter
    def Url(self, value):
        self._URL = value

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, value):
        self._Domain = value


class FanFicUrl(UrlInfo):
    _FicID = 0
    _FFArchiveFicID = ""
    _Rating = ""
    _Summary = ""
    _Updated = ""
    _Publisher = ""
    _Title = ""
#    _Url = ""
    _FicPath = ""
    _DBFicPath = ""


    def __init__(self):
        self._FicID = 0
        self._FFArchiveFicID = ""
        self._Rating = ""
        self._Summary = ""
        self._Updated = ""
        self._Publisher = ""
        self._Title = ""
        self._Url = ""
        self._FicPath = ""
        self._DBFicPath = ""

    def reset(self):
        self._FicID = 0
        self._FFArchiveFicID = ""
        self._Rating = ""
        self._Summary = ""
        self._Updated = ""
        self._Publisher = ""
        self._Title = ""
        self._Url = ""
        self._FicPath = ""
        self._DBFicPath = ""

    @property
    def FicPath(self):
        return self._FicPath

    @FicPath.setter
    def FicPath(self, value):
        self._FicPath = value

    @property
    def DBFicPath(self):
        return self._DBFicPath

    @DBFicPath.setter
    def DBFicPath(self, value):
        self._DBFicPath = value

    @property
    def Updated(self):
        return self._Updated

    @Updated.setter
    def Updated(self, vsUpdated):
        self._Updated = vsUpdated

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, vsTitle):
        self._Title = vsTitle

    # @property
    # def Url(self):
    #     return self._Url
    #
    # @Url.setter
    # def Url(self, vsUrl):
    #     self._Url = vsUrl

    @property
    def FicID(self):
        return self._FicID

    @FicID.setter
    def FicID(self, ificID):
        self._FicID = ificID

    @property
    def Publisher(self):
        return self._Publisher

    @Publisher.setter
    def Publisher(self, vsPublisher):
        self._Publisher = vsPublisher

    @property
    def FFArchiveFicID(self):
        return self._FFArchiveFicID

    @FFArchiveFicID.setter
    def FFArchiveFicID(self, vsFFArchiveFicID):
        self._FFArchiveFicID = vsFFArchiveFicID

    def get_date_comparison(self):
        if self._Updated.isnumeric():
            return int(self._Updated)
        elif self._Publisher.isnumeric():
            return int(self._Publisher)
        else:
            return 0


class FFDomain(object):
    _DomainUrl = ""
    _DomainCount = 0
    @property
    def DomainUrl(self):
        return self._DomainUrl

    @DomainUrl.setter
    def DomainUrl(self, value):
        self._DomainUrl = value

    @property
    def DomainCount(self):
        return self._DomainCount

    @DomainCount.setter
    def DomainCount(self, value):
        self._DomainCount = value


class FFNetFandomInfo(object):
    _Is_Xover = False
    #    Url = attr.ib()
    _FandomName = ''
    _Fandom_DB_Path = ''
    _FandomUrl = ''
    _FandomId = -1

    @property
    def FandomName(self):
        return self._FandomName

    @FandomName.setter
    def FandomName(self, voFandomName):
        self._FandomName = voFandomName

    @property
    def Fandom_DB_Path(self):
        return self._Fandom_DB_Path

    @Fandom_DB_Path.setter
    def Fandom_DB_Path(self, voFandom_DB_Path):
        self._Fandom_DB_Path = voFandom_DB_Path

    @property
    def FandomUrl(self):
        return self._FandomUrl

    @FandomUrl.setter
    def FandomUrl(self, voFandomUrl):
        self._FandomUrl = voFandomUrl

    @property
    def FandomId(self):
        return self._FandomId

    @FandomId.setter
    def FandomId(self, voFandomId):
        self._FandomId = voFandomId

    @property
    def Is_Xover(self):
        return self._Is_Xover

    @Is_Xover.setter
    def Is_Xover(self, voIs_Xover):
        self._Is_Xover = voIs_Xover

    def get_is_xover_numeric(self):
        if self.Is_Xover:
            return 1
        else:
            return 0

    def __init__(self):
        self._Is_Xover = False
        self._FandomUrl = ''
        self._Fandom_DB_Path = ''
        self._FandomName = ''
        self._FandomId = 0

    def set_is_xover_numeric(self, isxover):
        if isxover == 1:
            self._Is_Xover = True
        elif isxover == 0:
            self._Is_Xover = False


class FanFicFareData(object):
    _FicURL = ''
    _FanFicFareID = ''
    _ArchiveID = ''
    _ArchiveDomain = ''
    @property
    def FicUrl(self):
        return self._FicUrl

    @FicUrl.setter
    def FicUrl(self, value):
        self._FicUrl = value

    @property
    def ArchiveDomain(self):
        return self._ArchiveDomain

    @ArchiveDomain.setter
    def ArchiveDomain(self, value):
        self._ArchiveDomain = value

    @property
    def ArchiveID(self):
        return self._ArchiveID

    @ArchiveID.setter
    def ArchiveID(self, value):
        self._ArchiveID = value

    @property
    def FanFicFareID(self):
        return self._FanFicFareID

    @FanFicFareID.setter
    def FanFicFareID(self, value):
        self._FanFicFareID = value