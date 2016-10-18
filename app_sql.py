import sqlite3

from ff_datatypes import FFNetFandomInfo


class AppSql(object):
    # _FandomInfo_create = "CREATE TABLE FFNetFandomInfo(FandomInfoId INTEGER PRIMARY KEY, FandomName TEXT,
    # FandomUrl TEXT,
    #  Fandom_DB_Path TEXT, Url TEXT, Is_Xover BIT );"
    _FandomInfo_create = "CREATE TABLE FFNetFandomInfo(FandomInfoId INTEGER PRIMARY KEY, FandomName TEXT, " \
                         "FandomUrl TEXT, Fandom_DB_Path TEXT, Is_Xover BOOLEAN);"
    _FilePath = ''
    # _insert_fandom_info = 'INSERT INTO FFNetFandomInfo(FandomName, FandomUrl, Fandom_DB_Path, Url, Is_Xover)
    #  VALUES (?,?,?,?,?);'
    _insert_fandom_info = 'INSERT INTO FFNetFandomInfo(FandomName, FandomUrl, Fandom_DB_Path, Is_Xover) ' \
                          'VALUES (?,?,?,?);'
    _select_fandominfo_by_ID = 'SELECT * from FFNetFandomInfo WHERE FFNetFandomInfo.FandomInfoId = ?'
    _select_Id_by_Name = 'SELECT FFNetFandomInfo.FandomInfoId from FFNetFandomInfo WHERE FandomName.FandomName = ?;'
    _select_fic_by_FicID = 'SELECT * from FFNetFandomInfo WHERE FFNetFandomInfo.FandomInfoId = ?'
    _select_all_fandom_info = 'SELECT * from FFNetFandomInfo'


    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, vspath):
        self._FilePath = vspath

    def create_settings_db(self):
        dbpath = self.FilePath
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute(self._FandomInfo_create)
        con.commit()
        con.close()

    def save_fandom_info(self, f):
        # f = FFNetFandomInfo()
        dbpath = self.FilePath
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        data = (f.FandomName, f.FandomUrl, f.Fandom_DB_Path, f.get_is_xover_numeric())
        cur.execute(self._insert_fandom_info, data)
        con.commit()

    def get_fandom_list(self):
        dbpath = self.FilePath
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        select = self._select_all_fandom_info
        fandom_list = []

        cur.execute(select)
        con.commit()
        values = cur.fetchall()
        for row in values:
            fandom = self.get_fandom_from_row(row)
            fandom_list.append(fandom)
        return fandom_list

    def get_fandom_from_row(self, row):
        ooo = FFNetFandomInfo()
        ooo.FandomId = row[0]
        ooo.FandomName = row[1]
        ooo.FandomUrl = row[2]
        ooo.Fandom_DB_Path = row[3]
        # ooo.Url = row['Url']
        ooo.set_is_xover_numeric(row[4])
        return ooo

    def get_fandom_by_id(self, Id):
        dbpath = self.FilePath
        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        select = self._select_fandominfo_by_ID
        data = (Id,)
        cur.execute(select, data)
        con.commit()
        values = cur.fetchall()
        row = values[0]
        fandom = self.get_fandom_from_row(row)
        return fandom
