from app_sql import AppSql
from fanfic import FanFic
from fanfic_sql_builder import FanFicSql
from fic_file_db import FicFileDb
from fic_link import FanFicDbToDb
import sys,os
sys.path.append(os.path.realpath('..'))

class FanFicUpdateTracker(object):

    def find_fic_references(self):
        ssql = AppSql()
        ssql._spath = 'appdata.db'
        #fandoms = ssql.get_fandom_list()

        #appdb = 'appdata.db'
        fic_list = []
        db = FicFileDb('file.db')
        epub_files = db.get_fics_by_publisher('www.fanfiction.net')
        for file in epub_files:
            print(file.FilePath)
            self.create_link_for_fic_file(file)
        print('done')



    def create_link_for_fic_file(self, fic_file):


        db = FicFileDb('file.db')
        spath = self.get_FFbrowser_db_path('appdata.db')
        ssql = AppSql()
        ssql.FilePath = spath
        fandoms = ssql.get_fandom_list()
        for f in fandoms:

            dbPath = self.get_FFbrowser_db_path(f.Fandom_DB_Path)
            fanfic_db = FanFicSql(dbPath)
            if fanfic_db.is_fic_in_Db(fic_file.FFNetID):
                fanfic = fanfic_db.get_fic_by_ffnetID(fic_file.FFNetID)
                fic_link = FanFicDbToDb()
                fic_link.FicFileID = fic_file.FicID
                fic_link.FicId = fanfic.FicID
                fic_link.FanFicArchiveId = fic_file.FFNetID
                fic_link.DBPath = f.Fandom_DB_Path
                db.save_fic_link(fic_link)
        print("")
        print("Fanfic Not found in FicDBs: " + fic_file.FFNetID)
        print("FicID:" + str(fic_file.FicID))
        print("Fic File Path: " + fic_file.FilePath)
        print("--------------------------------------------------")


    def get_FFbrowser_db_path(self, filename):
        ffbrowser = "C:\\G\\IDE\\pycharm\\FFBrowser"
        fullname = os.path.join(ffbrowser, filename)
        return filename


