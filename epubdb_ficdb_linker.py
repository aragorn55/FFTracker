from fanfic_sql_builder import FanFicSql
import sqlite3
from fanfic import FanFic
from fanfic import Author
import datetime
import calendar
from ff_datatypes import UrlInfo, FFDomain


class DBLinker(FanFicSql):
    _url_db_path = "url.db"

    _create_url_info = "Create TABLE UrlInfo(UrlInfoID INTEGER PRIMARY KEY, DomainInfoID INT, Url TEXT);"
    _create_domain = "Create TABLE DomainInfo(DomainInfoID INTEGER PRIMARY KEY, DomainUrl TEXT);"
    _FicLinkCreate = "CREATE TABLE FicDbLink(FicDbLinkID INTEGER PRIMARY KEY, FicFileID INTEGER, FicId INTEGER, FanFicArchiveId TEXT, DBPath TEXT);"
    _FicCreate = "CREATE TABLE FicFile(FicId INTEGER PRIMARY KEY, FFNetID TEXT, Url TEXT, Title TEXT, AuthorId INTEGER, Updated TEXT, Published TEXT, Rating TEXT, Words INTEGER, Chapters INTEGER, Summary TEXT, Status TEXT, Packaged TEXT, FilePath TEXT);"

    _link_list_create = "Create TABLE LinkList(LinkListId INTEGER PRIMARY KEY, FicID INT, FanFicArchiveId TEXT, Url TEXT, Updated TEXT, Published TEXT, Words INTEGER, Chapters INTEGER, Archive TEXT, Fandom_DB_Path TEXT);"
    _link_list_create = "Create TABLE FicFileList(FicFileListId INTEGER PRIMARY KEY, FicFileID INT, FanFicArchiveId TEXT, Url TEXT, Words INTEGER, Chapters INTEGER, Packaged TEXT, FilePath TEXT, PublisherName TEXT);"
    create_fic_file_links = "Create TABLE FicFileLinks(FicFileLinkID INTEGER PRIMARY KEY, FicFileListId INT, LinkListId INT);"


    _insert_file_link = ''
    _insertFicLink = 'INSERT INTO FicDbLink(FicFileID, FicId, FanFicArchiveId, DBPath) VALUES (?,?,?,?);'
    _insert_url = "INSERT INTO UrlInfo(DomainInfoID, Url) VALUES (?,?);"
    _insert_domain = "INSERT INTO DomainInfo(DomainUrl) VALUES (?);"

    _select_domain = "SELECT DomainInfoID FROM DomainInfo WHERE DomainInfo.DomainUrl = ?;"
    _select_ficlink_by_archive_id = 'SELECT * from FicDbLink WHERE FicDbLink.FanFicArchiveId = ?;'

    select_ficfileList = 'SELECT FicFile.FicId, FicFile.FFNetID, FicFile.Url, FicFile.Words, FicFile.Chapters, FicFile.Packaged, FicFile.FilePath, Publisher.PublisherName FROM FicFile, FicPublisher, Publisher WHERE FicFile.FicId = FicPublisher.FicID AND FicPublisher.PublisherID = Publisher.PublisherId'
    insert_filelinks = 'INSERT INTO FicFileList(FicFileID, FanFicArchiveId, Url, Words, Chapters, Packaged, FilePath, PublisherName ) VALUES (?,?,?,?,?,?,?,?);'
    # ----------------------------- Bookmark FanFicUrl
    _create_fanficurl = "Create TABLE FanFicUrl(FanFicUrlID INTEGER PRIMARY KEY, FFArchiveID INT, FicUrl TEXT, FFArchiveFicID TEXT);"
    _create_ffarchive = "Create TABLE FFArchive(FFArchiveID INTEGER PRIMARY KEY, FFArchiveDomain TEXT);"


    _select_ffarchiveid = "SELECT FFArchiveID FROM FFArchive WHERE FFArchive.FFArchiveDomain = ?;"


    insert_fanficurl = "INSERT INTO FanFicUrl(FFArchiveID, FicUrl, FFArchiveFicID) VALUES (?,?,?);"
    insert_ffarchive = "INSERT INTO FFArchive(FFArchiveDomain) VALUES (?);"

    def create_file_list_db(self):

        con = sqlite3.connect(self._FFnetArchiveLinkDB_Path)
        cur = con.cursor()
        cur.execute(self._link_list_create)
        con.commit()
        con.close()
        return True

    def add_file_links_to_linkdb(self, epub_db_path):
        dbpath = self.FilePath

#        '(FicId, FFNetID, Url, Title, AuthorId, Updated, Published, Rating, Words, Chapters, Summary, Status, Packaged, FilePath)'


        fic_list = []
        select_link_list_by_id = 'SELECT * FROM FicFile WHERE FFNetID = ? AND Fandom_DB_Path = ?'
        select_fic = self._select_fic_by_ffnet_id


        con = sqlite3.connect(epub_db_path)
        cur = con.cursor()
        linkdb_path = self._FFnetArchiveLinkDB_Path
        cur.execute(self.select_ficfileList)
        link_rows = cur.fetchall()
        linkdb = sqlite3.connect(linkdb_path)
        link_cur = linkdb.cursor()
        icnt = 0
        prrocessed = 0
        print('total fics in db: ' + str(len(link_rows)))
        link_cur.executemany(self.insert_filelinks, link_rows)
        linkdb.commit()
        linkdb.close()
        return True

    def link_files_to_fics(self):
        insert_fic_file_links = "INSERT INTO FicFileLinks(FicFileListId, LinkListId) VALUES (?,?);"


        con = sqlite3.connect(self._FFnetArchiveLinkDB_Path)
        cur = con.cursor()
        #cur.execute()
        ficfiles = self.get_ficfilelist_list()
        dblinking = []
        for ficfile in ficfiles:
            ficsIDs = self.get_fic_ids_by_ffnetID(ficfile.FFNetID)
            ficlink_list = []
            for fic_id in ficsIDs:
                fic_link = (ficfile.FicID, fic_id)
                cur.execute(insert_fic_file_links, fic_link)
                con.commit()
        return True

    def test(self):
        con = sqlite3.connect(self._FFnetArchiveLinkDB_Path)
        cur = con.cursor()
        create_fic_file_links = "Create TABLE FicFileLinks(FicFileLinkID INTEGER PRIMARY KEY, FicFileListId INT, LinkListId INT);"
        cur.execute(create_fic_file_links)
        con.commit()





    def get_fic_ids_by_ffnetID(self, ffnetid):
        _select_ficid_by_ffnetid = 'SELECT LinkList.LinkListId from LinkList WHERE LinkList.FanFicArchiveId = ?;'

        dbpath = self._FFnetArchiveLinkDB_Path

        con = sqlite3.connect(dbpath)
        ficid_list = []
        cur = con.cursor()
        select_fic = _select_ficid_by_ffnetid
        cur.execute(select_fic, (ffnetid,))
        fic_rows = cur.fetchall()
        for row in fic_rows:
            ficid_list.append(row[0])
        return ficid_list


    def convert_row_to_ficfile(self, fic_row):
        fic = FanFic()
        fic.FicID =fic_row[0]
        fic.FFNetID = fic_row[2]



        return fic

    def get_ficfilelist_list(self):
        select_ficfileList = "SELECT * FROM FicFileList "
        dbpath = self._FFnetArchiveLinkDB_Path

        con = sqlite3.connect(dbpath)
        fics = []
        cur = con.cursor()
        select_fic = select_ficfileList
        cur.execute(select_fic)
        fic_rows = cur.fetchall()
        for row in fic_rows:
            fics.append(self.convert_row_to_ficfile(row))
        return fics

    def create_packaged_date_list(self):
        packaged_date_format = "%Y-%m-%d %H:%M:%S"
        select_update_list = 'SELECT FicFileLinks.FicFileLinkID, FicFileList.Packaged, LinkList.Url From FicFileLinks, FicFileList, LinkList WHERE FicFileLinks.FicFileListId = FicFileList.FicFileListId AND FicFileLinks.LinkListId = LinkList.LinkListId'
        select_ficid_by_ffnetid = 'SELECT LinkList.LinkListId from LinkList WHERE LinkList.FanFicArchiveId = ?;'
        _FicCreate = "CREATE TABLE FicFile(FicId INTEGER PRIMARY KEY, FFNetID TEXT, Url TEXT, Title TEXT, AuthorId INTEGER, Updated TEXT, Published TEXT, Rating TEXT, Words INTEGER, Chapters INTEGER, Summary TEXT, Status TEXT, Packaged TEXT, FilePath TEXT);"
        create_fic_file_links = "Create TABLE FicFileLinks(FicFileLinkID INTEGER PRIMARY KEY, FicFileListId INT, LinkListId INT);"
        _link_list_create = "Create TABLE LinkList(LinkListId INTEGER PRIMARY KEY, FicID INT, FanFicArchiveId TEXT, Url TEXT, Updated TEXT, Published TEXT, Words INTEGER, Chapters INTEGER, Archive TEXT, Fandom_DB_Path TEXT);"

        ficfile_list_create = "Create TABLE FicFileList(FicFileListId INTEGER PRIMARY KEY, FicFileID INT, FanFicArchiveId TEXT, Url TEXT, Words INTEGER, Chapters INTEGER, Packaged TEXT, FilePath TEXT, PublisherName TEXT);"
        new_rows = []
        insert_update_list = 'INSERT INTO UpdateList(FicFileListId, PackagedTime, Url) VALUES (?,?,?)'
        create_update_list = 'Create TABLE UpdateList(UpdateListId INTEGER PRIMARY KEY, FicFileListId INT, PackagedTime TEXT, Url TEXT);'
        dbpath = self._FFnetArchiveLinkDB_Path

        con = sqlite3.connect(dbpath)
        fics = []
        cur = con.cursor()
        select_fic = select_update_list
        cur.execute(select_fic)
        fic_rows = cur.fetchall()
        print('update_list count: ' + str(len(fic_rows)))
        icnt = 0
        for row in fic_rows:
            new_time = self.convert_packaged_date_to_unix(row[1])
            print('converted time: ' +  str(new_time))
            new_row = (row[0], new_time, row[2])
            cur.execute(insert_update_list, new_row)
            con.commit()
            icnt += 1
            print('updated count: ' + str(icnt))

    def convert_packaged_date_to_unix(self, date):
        packaged_date_format = "%Y-%m-%d %H:%M:%S"
        date = datetime.datetime.strptime(date, packaged_date_format)
        time_stamp = calendar.timegm(date.utctimetuple())
        return time_stamp

    def test_two(self):
        dbpath = self._FFnetArchiveLinkDB_Path
        create_update_list = 'Create TABLE UpdateList(UpdateListId INTEGER PRIMARY KEY, FicFileListId INT, PackagedTime TEXT, Url TEXT);'
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute(create_update_list)
        con.commit()
        return True

    def get_update_list(self):
        select_update_urls = 'select Distinct LinkList.Url FROM LinkList, UpdateList, FicFileLinks WHERE UpdateList.FicFileListId = FicFileLinks.FicFileListId AND FicFileLinks.LinkListId = LinkList.LinkListId AND Cast(UpdateList.PackagedTime AS INT) <  CAST (LinkList.Updated AS INT);'

#        select_update_urls = 'SELECT LinkList.URL FROM LinkList WHERE LinkList.LinkListId = ?;'
        dbpath = self._FFnetArchiveLinkDB_Path
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute(select_update_urls)
        url_list = cur.fetchall()
        return url_list



    def create_url_db(self):
        con = sqlite3.connect(self._url_db_path)
        cur = con.cursor()
        cur.execute(self._create_url_info)
        cur.execute(self._create_domain)
        con.commit()
        con.close()
        return True

    def save_urlinfo(self, new_info):
        con = sqlite3.connect(self._url_db_path)
        cur = con.cursor()

        cur.execute(self._select_domain, (new_info.Domain,))
        row = cur.fetchall()[0][0]
        data = (row, new_info.Url)
        cur.execute(self._insert_url, data)
        con.commit()
        con.close()
        return True

    def save_domain(self, new_domain):
        con = sqlite3.connect(self._url_db_path)
        cur = con.cursor()
        data = (new_domain.DomainUrl,)
        cur.execute(self._select_domain, data)
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute(self._insert_domain, data)
            con.commit()
        con.close()
        return True

    #------------------------ FanFicUrl

    def save_fanficurl(self, f):
        con = sqlite3.connect(self._FilePath)
        cur = con.cursor()

        ffarchiveid = self.save_FFArchive(f.Domain)

        data = (ffarchiveid, f.Url, f.FFArchiveFicID)
        cur.execute(self.insert_fanficurl, data)
        con.commit()
        con.close()
        return True



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
