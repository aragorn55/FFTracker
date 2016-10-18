import sqlite3

from fanfic import Author, FanFicEBook
#from fanfic import FanFic
from fic_file import FanFicEBook
from fic_link import FanFicDbToDb
class FicFileDb(object):
    _Path = 'ffbrowse.db'  # name of the sqlite database file


    _fandomcreate = "CREATE TABLE Fandom(FandomId INTEGER PRIMARY KEY , FandomName TEXT);"
    _PairingsCreate = "CREATE TABLE Pairings(PairingsId INTEGER PRIMARY KEY , PairingsName TEXT);"
    _GenreCreate = "Create TABLE Genre(GenreId INTEGER PRIMARY KEY, GenreName TEXT);"
    _FicGenresCreate = "Create TABLE FicGenre(FicGenreId INTEGER PRIMARY KEY,FicID INT, GenreID INT);"
    _PublisherCreate = "Create TABLE Publisher(PublisherId INTEGER PRIMARY KEY, PublisherName TEXT);"
    _FicPublishersCreate = "Create TABLE FicPublisher(FicPublisherId INTEGER PRIMARY KEY,FicID INT, PublisherID INT);"
    _FicPairingsCreate = "Create TABLE FicPairings(FicPairingsId INTEGER PRIMARY KEY,FicID INT, PairingsID INT);"
    _FicFandomCreate = "Create TABLE FicFandom(FicFandomId INTEGER PRIMARY KEY,FicID INT, FandomId INT);"
    _CharacterCreate = "CREATE TABLE Character(CharacterId INTEGER PRIMARY KEY,CharacterName TEXT);"
    _RelationshipCreate = "CREATE TABLE Relationship(FicId INT, RelationShipNumber INT, CharacterId INT);"
    _FicCreate = "CREATE TABLE FicFile(FicId INTEGER PRIMARY KEY, FFNetID TEXT, Url TEXT, Title TEXT, AuthorId INTEGER, Updated TEXT, Published TEXT, Rating TEXT, Words INTEGER, Chapters INTEGER, Summary TEXT, Status TEXT, Packaged TEXT, FilePath TEXT);"
    _FicCharactersCreate = "Create TABLE FicCharacter(FicCharacterId INTEGER PRIMARY KEY,FicID INT, CharacterID INT);"
    _AuthorCreate = "CREATE TABLE Author(AuthorId INTEGER PRIMARY KEY, FFNetID TEXT, AuthorName TEXT, Url TEXT);"
    _database_exists = "SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = ?;"
    _insert_fic = 'INSERT INTO FicFile(FFNetID, Url, Title, AuthorId, Updated, Published, Rating, Words, Chapters, Summary, Status, Packaged, FilePath) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);'
    _cnt_fanfics = 'SELECT COUNT(DISTINCT FFNetID) FROM FanFic;'
    _insert_author = "INSERT INTO Author(FFNetID, AuthorName, Url) VALUES (?,?,?);"
    _select_AuthorId = 'SELECT Author.AuthorId from Author WHERE Author.Url = ?;'
    _select_Author_from_id = 'SELECT * from Author WHERE Author.AuthorId = ?;'
    _insert_relationship = 'INSERT INTO Relationship(FicId, RelationShipNumber, CharacterId) VALUES (?,?,?);'
    _select_FandomId = 'SELECT Fandom.FandomId from Fandom WHERE Fandom.FandomName = ?;'
    _select_CharacterId = 'SELECT Character.CharacterId from Character WHERE Character.CharacterName = ?;'
    _select_GenreId = 'SELECT Genre.GenreId from Genre WHERE Genre.GenreName = ?;'
    _select_fic_by_ffnet_id = 'SELECT * from FicFile WHERE FicFile.FFNetID = ?;'
    _insert_Genre = 'INSERT INTO Genre(GenreName) VALUES (?);'
    _insert_Character = 'INSERT INTO Character(CharacterName) VALUES (?);'
    _insert_Fandom = 'INSERT INTO Fandom(FandomName) VALUES (?);'
    _insert_FicGenre = 'INSERT INTO FicGenre(FicID, GenreID) VALUES (?,?);'
    _insert_FicFandom = 'INSERT INTO FicFandom(FicID, FandomID) VALUES (?,?);'
    _insert_FicCharacter = 'INSERT INTO FicCharacter(FicID, CharacterID) VALUES (?,?);'
    _select_published_date = 'SELECT FicFile.Published from FicFile;'
    _select_newest_published = 'select Max(FicFile.Published) from FicFile;'
    _select_newest_updated = 'select Max(FicFile.Updated) from FicFile'
    _delete_FicGenre = 'DELETE FROM FicGenre WHERE FicGenre.FicID = ?;'
    _delete_FanFic = 'DELETE FROM FicFile WHERE FicFile.FicID = ?;'
    _delete_FicFandom = 'DELETE FROM FicFandom WHERE FicFandom.FicID = ?;'
    _delete_FicCharacter = 'DELETE FROM FicCharacter WHERE FicCharacter.FicID = ?;'
    _select_PublisherId = 'SELECT Publisher.PublisherId from Publisher WHERE Publisher.PublisherName = ?;'
    _insert_Publisher = 'INSERT INTO Publisher(PublisherName) VALUES (?);'
    _insert_FicPublisher = 'INSERT INTO FicPublisher(FicID, PublisherID) VALUES (?,?);'
    _delete_FicPublisher = 'DELETE FROM FicPublisher WHERE FicPublisher.FicID = ?;'
    _select_PairingsId = 'SELECT Pairings.PairingsId from Pairings WHERE Pairings.PairingsName = ?;'
    _insert_Pairings = 'INSERT INTO Pairings(PairingsName) VALUES (?);'
    _insert_FicPairings = 'INSERT INTO FicPairings(FicID, PairingsID) VALUES (?,?);'
    _delete_FicPairings = 'DELETE FROM FicPairings WHERE FicPairings.FicID = ?;'
    _select_ficfiles_by_publisher = "SELECT FicFile.FicId,  FicFile.FFNetID,  FicFile.Url,  FicFile.FilePath FROM FicFile, FicPublisher, Publisher WHERE FicFile.FicId = FicPublisher.FicID AND FicPublisher.PublisherID = Publisher.PublisherId AND  Publisher.PublisherName = ?"
    _FicLinkCreate = "CREATE TABLE FicDbLink(FicDbLinkID INTEGER PRIMARY KEY, FicFileID INTEGER, FicId INTEGER, FanFicArchiveId TEXT, DBPath TEXT);"
    _insertFicLink = 'INSERT INTO FicDbLink(FicFileID, FicId, FanFicArchiveId, DBPath) VALUES (?,?,?,?);'
    _select_ficlink_by_ffnet_id = 'SELECT * from FicDbLink WHERE FicDbLink.FanFicArchiveId = ?;'
    def __init__(self, path):
        self._Path = path

    def create_db(self, path):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute(self._fandomcreate)
        cur.execute(self._AuthorCreate)
        cur.execute(self._GenreCreate)
        cur.execute(self._CharacterCreate)
        cur.execute(self._FicCreate)
        cur.execute(self._FicGenresCreate)
        cur.execute(self._FicFandomCreate)
        cur.execute(self._RelationshipCreate)
        cur.execute(self._FicCharactersCreate)
        cur.execute(self._PairingsCreate)
        cur.execute(self._FicPairingsCreate)
        cur.execute(self._PublisherCreate)
        cur.execute(self._FicPublishersCreate)
        cur.execute(self._FicLinkCreate)


        # cur.execute(self._database_exists, ('',))
        # cur.execute(self._database_exists, ('',))
        # cur.execute(self._database_exists, ('',))
        # cur.execute(self._database_exists, ('',))

        con.commit()
        con.close()

    def test_table(self, cur, table):
        cur.execute(self._database_exists, (table,))
        a_row = cur.fetchone()
        if int(a_row[0]) == 0:
            return False
        else:
            return True

    def set_path(self, path):
        self._Path = path

    def save_fic_link(self, fic_link):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        select = self._select_ficlink_by_ffnet_id
        item = fic_link.FanFicArchiveId
        o = (item,)
        cur.execute(select, o)
        con.commit()
        value = cur.fetchall()
        rowid = 0
        if len(value) == 0:
            data = (fic_link.FicFileID, fic_link.FicId, fic_link.FanFicArchiveId, fic_link.DBPath)
            cur.execute(self._insertFicLink, data)
            con.commit()
            ficid = cur.lastrowid
            return ficid

        else:
            row = value[0]
            rowid = row[0]
            rowid = int(rowid)
            return rowid
        return rowid

    def delete_fic(self, fic):
        fic = FanFicEBook()
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        delete_fic = self._delete_FanFic
        delete_char = self._delete_FicCharacter
        delete_fan = self._delete_FicFandom
        delete_genre = self._delete_FicGenre
        delete_Publisher = self._delete_FicPublisher
        delete_Pairings = self._delete_FicPairings
        cur.execute(delete_fic, (fic.FicID,))
        cur.execute(delete_char, (fic.FicID,))
        cur.execute(delete_fan, (fic.FicID,))
        cur.execute(delete_genre, (fic.FicID,))
        cur.execute(delete_Publisher, (fic.FicID,))
        cur.execute(delete_Pairings, (fic.FicID,))

        con.commit()

    def get_fanfic_cnt(self):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        cur.execute(self._cnt_fanfics)
        fic_cnt = cur.fetchall()[0][0]
        return fic_cnt

    def get_newest_date(self):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        cur.execute(self._select_newest_published)
        new_pubs = cur.fetchall()
        cur.execute(self._select_newest_updated)
        new_ups = cur.fetchall()
        ipub = self.convert_rows_to_int(new_pubs)
        iup = self.convert_rows_to_int(new_ups)
        if ipub > iup:
            return ipub
        else:
            return iup

    def convert_rows_to_int(self, row_list):
        row = row_list[0]
        col = row[0]
        if col is None:
            return 0

        elif col.isnumeric():
            return int(col)
        else:
            return 0

    def get_fic_by_ffnetID(self, ffnetid):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        select_fic = self._select_fic_by_ffnet_id
        cur.execute(select_fic, ffnetid)
        fic_row = cur.fetchone()
        fic = self.convert_row_to_fic(fic_row)
        fic.Author = self.get_author_by_id(fic_row[4])
        return fic

    def get_fics_by_publisher(self, publisher):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        select_fic = self._select_ficfiles_by_publisher
        data = (publisher,)
        cur.execute(select_fic, data)
        fic_rows = cur.fetchall()
        ficfiles = []
        for row in fic_rows:
            fic = FanFicEBook()
            fic.FicID = row[0]
            fic.FFNetID = row[1]
            fic.Url = row[2]
            fic.FilePath = row[3]
            ficfiles.append(fic)

        return ficfiles

    def is_fic_in_Db(self, fic):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        select_fic = self._select_fic_by_ffnet_id

        cur.execute(select_fic, (fic.FFNetID,))
        rows = cur.fetchall()
        if len(rows) == 0:
            return False
        else:
            return True

    def get_author_by_id(self, vId):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        select_a = self._select_Author_from_id
        cur.execute(select_a, (vId,))
        a_row = cur.fetchone()
        oAuthor = Author()
        oAuthor.AuthorID = a_row['AuthorId']
        oAuthor.FFNetID = a_row['FFNetID']
        oAuthor.AuthorName = a_row['AuthorName']
        oAuthor.Url = a_row['Url']
        return oAuthor



    def convert_row_to_fic(self, item):
        fic = FanFicEBook()
        fic.FicId = item[0]
        fic.FFNetID = item[1]
        fic.Url = item[2]
        fic.Title = item[3]
        fic.Author.AuthorID = item[4]
        fic.Updated = str(item[4])
        fic.Published = str(item[5])
        fic.Rating = item[6]
        fic.Words = item[7]
        fic.Chapters = item[8]
        fic.Summary = item[9]
        fic.Status = item[10]
        fic.Packaged = item[11]
        fic.FilePath = item[12]
        return fic

    def __init__(self, path):
        self._Path = path

    def save_author(self, voAuthor):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()

        select = self._select_AuthorId
        item = voAuthor.Url
        o = (item,)
        cur.execute(select, o)
        con.commit()
        value = cur.fetchall()
        rowid = 0
        if len(value) == 0:
            data = (voAuthor.FFNetID, voAuthor.AuthorName, voAuthor.Url)
            cur.execute(self._insert_author, data)
            # cur.execute(insert, o)
            con.commit()
            rowid = cur.lastrowid
            return rowid
        else:
            row = value[0]
            rowid = row[0]
            rowid = int(rowid)
            return rowid
        return rowid

    def insert_fic(self, f):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()

        f.Author.AuthorID = self.save_author(f.Author)
        data = (
        f.FFNetID, f.Url, f.Title, f.Author.AuthorID, f.Updated, f.Published, f.Rating, f.Words, f.Chapters, f.Summary,
        f.Status, f.Packaged, f.FilePath)
        cur.execute(self._insert_fic, data)
        con.commit()
        ficid = cur.lastrowid
        if len(f.Genres) > 0:
            self.save_FicGenre(f.Genres, ficid)
        self.save_FicFandom(f.Fandoms, ficid)
        if len(f.Characters) > 0:
            self.save_FicCharacter(f.Characters, ficid)
        self.save_FicPublisher(f.Publisher, ficid)
        if len(f.Pairings) > 0:
            self.save_FicPairings(f.Pairings, ficid)
        if len(f.Relationships) > 0:
            self.save_relationships(f.Relationships, ficid)
        return ficid

    def save_FicPairings(self, Pairingss, ficId):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        Pairings_ids = self.save_Pairingss(Pairingss)
        for x in range(len(Pairings_ids)):
            Pairings_id = Pairings_ids[x]
            Pairings_id = int(Pairings_id)
            Pairingstupal = (ficId, Pairings_id)
            # cur.execute(self._insert_FicPairings, Pairingstupal)
            cur.execute(self._insert_FicPairings, Pairingstupal)
            con.commit()

    def save_Pairingss(self, voList):
        PairingsId_list = []
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        for x in range(len(voList)):
            select = self._select_PairingsId
            item = voList[x]
            o = (item,)
            cur.execute(select, o)
            con.commit()
            value = cur.fetchall()
            rowid = 0
            if len(value) == 0:
                insert = self._insert_Pairings
                cur.execute(insert, o)
                con.commit()
                rowid = cur.lastrowid
                PairingsId_list.append(rowid)
            else:
                row = value[0]
                rowid = row[0]
                rowid = int(rowid)
                PairingsId_list.append(rowid)
        return PairingsId_list

    def save_FicPublisher(self, Publisher, ficId):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        Publisher_id = self.save_Publisher(Publisher)
        Publishertupal = (ficId, Publisher_id)
        cur.execute(self._insert_FicPublisher, Publishertupal)
        con.commit()


    def save_Publisher(self, voList):


        con = sqlite3.connect(self._Path)
        cur = con.cursor()

        select = self._select_PublisherId
        publisher_id = -1
        o = (voList,)
        cur.execute(select, o)
        con.commit()
        value = cur.fetchall()
        rowid = 0
        if len(value) == 0:
            insert = self._insert_Publisher
            cur.execute(insert, o)
            con.commit()
            rowid = cur.lastrowid
            return rowid
        else:
            row = value[0]
            rowid = row[0]
            rowid = int(rowid)
            return rowid

    def save_FicGenre(self, genres, ficId):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        genre_ids = self.save_Genres(genres)
        for x in range(len(genre_ids)):
            genre_id = genre_ids[x]
            genre_id = int(genre_id)
            genretupal = (ficId, genre_id)
            # cur.execute(self._insert_FicGenre, genretupal)
            cur.execute(self._insert_FicGenre, genretupal)
            con.commit()

    def save_FicCharacter(self, characters, ficId):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        CharacterIds = self.save_Characters(characters)
        for x in range(len(CharacterIds)):
            CharacterId = CharacterIds[x]
            # cur.execute(self._insert_FicCharacter, characterTupal)
            cur.execute(self._insert_FicCharacter, (ficId, int(CharacterId)))
            con.commit()

    def save_FicFandom(self, fandoms, ficId):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        fandom_ids = self.save_Fandoms(fandoms)
        for x in range(len(fandom_ids)):
            fandom_id = fandom_ids[x]
            # cur.execute(self._insert_FicFandom, Fandomtupal)
            cur.execute(self._insert_FicFandom, (ficId, int(fandom_id)))
            con.commit()

    def save_Genres(self, voList):
        GenreId_list = []
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        for x in range(len(voList)):
            select = self._select_GenreId
            item = voList[x]
            o = (item,)
            cur.execute(select, o)
            con.commit()
            value = cur.fetchall()
            rowid = 0
            if len(value) == 0:
                insert = self._insert_Genre
                cur.execute(insert, o)
                con.commit()
                rowid = cur.lastrowid
                GenreId_list.append(rowid)
            else:
                row = value[0]
                rowid = row[0]
                rowid = int(rowid)
                GenreId_list.append(rowid)
        return GenreId_list

    def save_Fandoms(self, voList):
        FandomId_list = []
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        for x in range(len(voList)):
            select = self._select_FandomId
            item = voList[x]
            o = (item,)
            cur.execute(select, o)
            con.commit()
            value = cur.fetchall()
            rowid = 0
            if len(value) == 0:
                insert = self._insert_Fandom
                cur.execute(insert, o)
                con.commit()
                rowid = cur.lastrowid
                FandomId_list.append(rowid)
            else:
                row = value[0]
                rowid = row[0]
                rowid = int(rowid)
                FandomId_list.append(rowid)

        return FandomId_list

    def save_Characters(self, voList):
        CharacterId_list = []
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        for x in range(len(voList)):
            select = self._select_CharacterId
            item = voList[x]
            o = (item,)
            cur.execute(select, o)
            con.commit()
            value = cur.fetchall()
            rowid = 0
            if len(value) == 0:
                insert = self._insert_Character
                cur.execute(insert, o)
                con.commit()
                rowid = cur.lastrowid
                CharacterId_list.append(rowid)
            else:
                row = value[0]
                rowid = row[0]
                rowid = int(rowid)
                CharacterId_list.append(rowid)

        return CharacterId_list

    def save_relationships(self, voList, ficid):
        charId_list = []
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        for i in range(len(voList)):
            charIds = self.save_Characters(voList[i])

            for x in range(len(charIds)):
                charId = charIds[x]
                data = (ficid, i, charId)
                cur.execute(self._insert_relationship, data)
                con.commit()

        return charId_list

    def set_path(self, path):
        self._Path = path
