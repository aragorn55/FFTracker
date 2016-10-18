import sqlite3

from epubdb_ficdb_linker import DBLinker

from epubdb_ficdb_linker import DBLinker
class TestDB(DBLinker):


    def single_use(self):
        select = "select * from FicFileList WHERE FanFicArchiveId = '';"
        dbpath = self._FFnetArchiveLinkDB_Path
        s = ";"
        con = sqlite3.connect(dbpath)
        ficid_list = []
        cur = con.cursor()
        cur.execute(select)
        fic_rows = cur.fetchall()
        file = open("file_list.csv", "w")
        for row in fic_rows:
            srow = str(row[0]) + '; ' + str(row[1]) + '; ' + row[2] + '; ' + row[3] + '; ' + str(row[4]) + '; ' + str(row[5]) + '; ' + row[6] + '; ' + row[7] + '; ' + row[8] + "\n"
            file.write(srow)
        return True
    def fix_file_links_from_cvs(self, filename):
        file = open(filename)
        update_data = []
        _link_list_create = "Create TABLE FicFileList(FicFileListId INTEGER PRIMARY KEY, FicFileID INT, FanFicArchiveId TEXT, Url TEXT, Words INTEGER, Chapters INTEGER, Packaged TEXT, FilePath TEXT, PublisherName TEXT);"
        update_ficfilelist = 'UPDATE FicFileList SET FanFicArchiveId=?, PublisherName=?   WHERE FicFileListId =?;'
        for record in file.readlines():
            fic_properties = record.split(";")
            update = (fic_properties[2], fic_properties[8], fic_properties[0])
            update_data.append(update)
        dbpath = self._FFnetArchiveLinkDB_Path
        s = ";"
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.executemany(update_ficfilelist, update_data)
        con.commit()
        cur.close()
        con.close()
        return True




