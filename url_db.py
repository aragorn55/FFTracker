import sqlite3
from fanfic_sql_builder import FanFicSql
from ff_datatypes import FanFicUrl, UrlInfo, FFDomain


class UrlDB(FanFicSql):
    _FilePath = "Bookmark.db"
    _create_fanficurl = "Create TABLE FanFicUrl(FanFicUrlID INTEGER PRIMARY KEY, FFArchiveID INT, FicUrl TEXT, FFArchiveFicID TEXT);"
    _create_ffarchive = "Create TABLE FFArchive(FFArchiveID INTEGER PRIMARY KEY, FFArchiveDomain TEXT);"
    _create_Bookmark = 'Create TABLE MiscBookmarks(BookmarkID INTEGER PRIMARY KEY, DomainInfoID INT, BookmarkUrl TEXT);'
    _create_domaininfo = "Create TABLE DomainInfo(DomainInfoID INTEGER PRIMARY KEY, DomainUrl TEXT);"

    _select_ffarchive = "SELECT FFArchiveID FROM FFArchive WHERE FFArchive.FFArchiveDomain = ?;"


    _select_domain = "SELECT DomainInfoID FROM DomainInfo WHERE DomainInfo.DomainUrl = ?;"

    insert_fanficurl = "INSERT INTO FanFicUrl(FFArchiveID, FicUrl, FFArchiveFicID) VALUES (?,?,?);"
    insert_ffarchive = "INSERT INTO FFArchive(FFArchiveDomain) VALUES (?);"
    _insert_misc_bookmark = "INSERT INTO MiscBookmarks(DomainInfoID, BookmarkUrl) VALUES (?,?);"
    _insert_domaininfo = "INSERT INTO DomainInfo(DomainUrl) VALUES (?);"

    def create_url_db(self):
        con = sqlite3.connect(self._FilePath)
        cur = con.cursor()
        cur.execute(self._create_fanficurl)
        cur.execute(self._create_ffarchive)
        cur.execute(self._create_Bookmark)
        cur.execute(self._create_domaininfo)
        con.commit()
        con.close()
        return True

    def save_fanficurl(self, f):
        con = sqlite3.connect(self._FilePath)
        cur = con.cursor()

        ffarchiveid = self.save_FFArchive(f.Domain)

        data = (ffarchiveid, f.Url, f.FFArchiveFicID)
        cur.execute(self.insert_fanficurl, data)
        con.commit()
        con.close()
        return True

    def save_misc_bookmark(self, f):
        con = sqlite3.connect(self._FilePath)
        cur = con.cursor()

        domainid = self.save_domain(f.Domain)

        data = (domainid, f.Url)
        cur.execute(self._insert_misc_bookmark, data)
        con.commit()
        con.close()
        return True

    def save_domain(self, newdomain):
        dbpath = self.FilePath

        con = sqlite3.connect(dbpath)

        cur = con.cursor()

        select = self._select_domain
        item = newdomain
        o = (item,)
        cur.execute(select, o)
        con.commit()
        value = cur.fetchall()
        rowid = 0
        if len(value) == 0:
            insert = self._insert_domaininfo
            data = (newdomain,)
            cur.execute(self._insert_domaininfo, data)
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

    def save_FFArchive(self, voAuthor):
        dbpath = self.FilePath

        con = sqlite3.connect(dbpath)

        cur = con.cursor()

        select = self._select_ffarchive
        item = voAuthor
        o = (item,)
        cur.execute(select, o)
        con.commit()
        value = cur.fetchall()
        rowid = 0
        if len(value) == 0:
            insert = self.insert_ffarchive
            data = (voAuthor,)
            cur.execute(self.insert_ffarchive, data)
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



