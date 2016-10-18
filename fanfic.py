class Author(object):
    _AuthorID = 0
    _FFNetID = ""
    _AuthorName = ""
    _Url = ""

    def __init__(self):
        self._FFNetID = ""
        self._AuthorID = 0
        self._AuthorName = ""
        self._Url = ""

    def reset(self):
        self._FFNetID = ""
        self._AuthorID = 0
        self._AuthorName = ""
        self._Url = ""

    @property
    def AuthorID(self):
        return self._AuthorID

    @AuthorID.setter
    def AuthorID(self, vsAuthorID):
        self._AuthorID = vsAuthorID

    @property
    def FFNetID(self):
        return self._FFNetID

    @FFNetID.setter
    def FFNetID(self, vsFFNetID):
        self._FFNetID = vsFFNetID

    @property
    def AuthorName(self):
        return self._AuthorName

    @AuthorName.setter
    def AuthorName(self, vsName):
        self._AuthorName = vsName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, vsUrl):
        self._Url = vsUrl





class FanFic(object):
    _Genres = []
    _FicID = 0
    _FFNetID = ""
    _Chapters = 0
    _Fandoms = []
    _Relationships = []
    _Characters = []
    _Words = 0
    _GenreString = ""
    _Rating = ""
    _Summary = ""
    _CharactersString = ""
    _Updated = ""
    _Published = ""
    _Title = ""
    _Url = ""
    _Status = ''
    _Author = Author()
    _Is_Xover = False
    _FilePath = ""
    _DBPath = ""
    _Tags = []
    _Publisher = ''


    def __init__(self):
        self._Url = ""
        self._Title = ""
        self._Published = ""
        self._Updated = ""
        self._CharactersString = ""
        self._Summary = ""
        self._Rating = ""
        self._GenreString = ""
        self._Words = 0
        self._Characters = []
        self._Relationships = []
        self._Fandoms = []
        self._Chapters = 0
        self._FFNetID = ""
        self._FicID = 0
        self._Status = ''
        self._Genres = []
        self._Author = Author()
        self._Is_Xover = False
        self._FilePath = ''
        self._DBPath = ''

    def reset(self):
        self._Url = ""
        self._Title = ""
        self._Published = ""
        self._Updated = ""
        self._CharactersString = ""
        self._Summary = ""
        self._Rating = ""
        self._GenreString = ""
        self._Words = 0
        self._Characters = []
        self._Relationships = []
        self._Fandoms = []
        self._Chapters = 0
        self._FFNetID = ""
        self._FicID = 0
        self._Genres = []
        self._Author.reset()
        self._Status = ''
        self._Is_Xover = False
        self._FilePath = ''
        self._DBPath = ''

    @property
    def FilePath(self):
        return  self._FilePath

    @FilePath.setter
    def FilePath(self, value):
        self._FilePath = value

    @property
    def DBPath(self):
        return self._DBPath

    @DBPath.setter
    def DBPath(self, value):
        self._DBPath = value


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

    def set_is_xover_numeric(self, isxover):
        if isxover == 1:
            self._Is_Xover = True
        elif isxover == 0:
            self._Is_Xover = False

    def setwords(self, vswords):
        swords = vswords.replace("," "")
        iwords = int(swords)
        self._Words = iwords

    @property
    def Author(self):
        return self._Author

    @Author.setter
    def Author(self, voAuthor):
        self._Author = voAuthor

    @property
    def Updated(self):
        return self._Updated

    @Updated.setter
    def Updated(self, vsUpdated):
        self._Updated = vsUpdated

    @property
    def Characters(self):
        return self._Characters

    @Characters.setter
    def Characters(self, vsCharacters):
        self._Characters = vsCharacters

    @property
    def Rating(self):
        return self._Rating

    @Rating.setter
    def Rating(self, vsRating):
        self._Rating = vsRating

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, vsTitle):
        self._Title = vsTitle

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, vsUrl):
        self._Url = vsUrl

    @property
    def FicID(self):
        return self._FicID

    @FicID.setter
    def FicID(self, ificID):
        self._FicID = ificID

    @property
    def Relationships(self):
        return self._Relationships

    @Relationships.setter
    def Relationships(self, vs_Relationships):
        self._Relationships = vs_Relationships

    @property
    def Fandoms(self):
        return self._Fandoms

    @Fandoms.setter
    def Fandoms(self, vsFandoms):
        self._Fandoms = vsFandoms

    @property
    def Words(self):
        return self._Words

    @Words.setter
    def Words(self, iWord):
        self._Words = iWord

    @property
    def Published(self):
        return self._Published

    @Published.setter
    def Published(self, vsPublished):
        self._Published = vsPublished

    @property
    def Summary(self):
        return self._Summary

    @Summary.setter
    def Summary(self, vsSummary):
        self._Summary = vsSummary

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, vStatus):
        self._Status = vStatus

    @property
    def FFNetID(self):
        return self._FFNetID

    @FFNetID.setter
    def FFNetID(self, vsFFNetID):
        self._FFNetID = vsFFNetID

    @property
    def Genres(self):
        return self._Genres

    @Genres.setter
    def Genres(self, oGenres):
        self._Genres = oGenres

    @property
    def Chapters(self):
        return self._Chapters

    @Chapters.setter
    def Chapters(self, vsChapters):
        self._Chapters = vsChapters

    @property
    def CharactersString(self):
        return self._CharactersString

    @CharactersString.setter
    def CharactersString(self, vsCharacters):
        self._CharactersString = vsCharacters

    def get_date_comparison(self):
        if self._Updated.isnumeric():
            return int(self._Updated)
        elif self._Published.isnumeric():
            return int(self._Published)
        else:
            return 0
    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, vTags):
        self._Tags = vTags

    @property
    def Publisher(self):
        return self._Publisher

    @Publisher.setter
    def Publisher(self, vsPublisher):
        self._Publisher = vsPublisher


class FanFicEBook(FanFic):
    _Packaged = ''
    _Pairings = []

    def __init__(self):
        self._Url = ""
        self._Title = ""
        self._Published = ""
        self._Updated = ""
        self._CharactersString = ""
        self._Summary = ""
        self._Rating = ""
        self._GenreString = ""
        self._Words = 0
        self._Characters = []
        self._Relationships = []
        self._Fandoms = []
        self._Chapters = 0
        self._FFNetID = ""
        self._FicID = 0
        self._Status = ''
        self._Genres = []
        self._Author = Author()
        self._FilePath = ''
        self._Packaged = ''
        self._Tags = []
        self._Pairings = []
        self._Publisher = ''

    def reset(self):

        self._Url = ""
        self._Title = ""
        self._Published = ""
        self._Updated = ""
        self._CharactersString = ""
        self._Summary = ""
        self._Rating = ""
        self._GenreString = ""
        self._Words = 0
        self._Characters = []
        self._Relationships = []
        self._Fandoms = []
        self._Chapters = 0
        self._FFNetID = ""
        self._FicID = 0
        self._Genres = []
        self._Author.reset()
        self._Status = ''
        self._FilePath = ''
        self._Packaged = ''
        self._Tags = []
        self._Pairings = []
        self._Publisher = ''


    @property
    def Packaged(self):
        return self._Packaged

    @Packaged.setter
    def Packaged(self, vsPackaged):
        self._Packaged = vsPackaged


    @property
    def Pairings(self):
        return self._Pairings

    @Pairings.setter
    def Pairings(self, vs_Pairings):
        self._Pairings = vs_Pairings

