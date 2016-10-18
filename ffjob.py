from app_sql import AppSql
from ff_datatypes import FFNetFandomInfo, FanFicUrl
from FFNetProcess import FFNetProcess
from create_ffbrowse_db import FanFicDB
from fanfic_sql_builder import FanFicSql
from fanfic import FanFic
from fanfic import Author

from epubdb_ficdb_linker import DBLinker

class FFJob(object):
    ffnet_list = []
    appdata_path = 'appdata.db'

    # def create_fandom_info(self, ssql, fan_url, dbPath, url, is_xover, fan_name)
    def create_fandom_info(self, ssql, fan_url, dbPath, is_xover, fan_name):
        # new_fandom = FFNetFandomInfo(0, fan_url, dbPath, url, is_xover, fan_name)
        new_fandom = FFNetFandomInfo()
        new_fandom.FandomName = fan_name
        new_fandom.Fandom_DB_Path = dbPath
        new_fandom.FandomUrl = fan_url
        new_fandom.Is_Xover = is_xover
        self.ffnet_list.append(new_fandom)
        ssql.save_fandom_info(new_fandom)
        return new_fandom

    def create_all_fandoms(self):
        ssql = AppSql()
        ssql.FilePath = 'appdata.db'
        ssql.create_settings_db()
        print("created")
        self.create_fandom_info(ssql, 'anime/Bleach/', 'bleach_ffbrowser.db', False, 'Bleach')
        print("Bleach")
        self.create_fandom_info(ssql, 'anime/Inuyasha/', 'inuyasha_ffbrowser.db', False, 'Inuyasha')
        print("Inuyasha")
        self.create_fandom_info(ssql, 'anime/Guyver/', 'guyver_ffbrowser.db', False, 'Guyver')
        print("Guyver")
        self.create_fandom_info(ssql, 'anime/Ranma/', 'ranma_ffbrowser.db', False, 'Ranma')
        print("Ranma")
        # self.create_fandom_info('anime//', '_ffbrowser.db', '', False, '')
        self.create_fandom_info(ssql, 'book/Dresden-Files/', 'Dresden-Files_ffbrowser.db', False, 'Dresden Files')
        self.create_fandom_info(ssql, 'game/Devil-May-Cry/', 'Devil-May-Cry_ffbrowser.db', False, 'Devil May Cry')
        self.create_fandom_info(ssql, 'game/Halo/', 'Halo_ffbrowser.db', False, 'Halo')
        self.create_fandom_info(ssql, 'Bleach-Crossovers/1758/0/', 'Bleachx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Dresden-Files-Crossovers/2489/0/', 'dresdenx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Fate-stay-night-Crossovers/2746/0/', 'fsnx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Ranma-Crossovers/93/0/', 'r12x_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Gundam-Wing-AC-Crossovers/328/0/', 'gwx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Guyver-Crossovers/473/0/', 'guyverx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Halo-Crossovers/1342/0/', 'halox_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Inuyasha-Crossovers/436/0/', 'inux_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Love-Hina-Crossovers/784/0/', 'lhx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Devil-May-Cry-Crossovers/1337/0/', 'dmcx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'F-E-A-R-Crossovers/2432/0/', 'fearx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'cartoon/Batman-Beyond/', 'bb_ffbrowser.db', False, 'Batman Beyond')
        self.create_fandom_info(ssql, 'Batman-Beyond-Crossovers/718/0/', 'bbx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'anime/Rurouni-Kenshin/', 'rk_ffbrowser.db', False, 'Rurouni Kenshin')
        self.create_fandom_info(ssql, 'Rurouni-Kenshin-Crossovers/355/0/', 'rkx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'book/Lord-of-the-Rings/', 'lotr_ffbrowser.db', False, 'Lord of the Rings')
        self.create_fandom_info(ssql, 'Lord-of-the-Rings-Crossovers/382/0/', 'lotrx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'comic/Star-Wars/', 'sw_c_ffbrowser.db', False, 'Star Wars')
        self.create_fandom_info(ssql, 'Star-Wars-Crossovers/10797/0/', 'swx_c_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'movie/Star-Wars/', 'sw_m_ffbrowser.db', False, 'Star Wars')
        self.create_fandom_info(ssql, 'Star-Wars-Crossovers/8/0/', 'sw_c_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'tv/Dresden-Files/', 'Dresden-Files_tv_ffbrowser.db', False, 'Dresden Files')
        # self.create_fandom_info(ssql, '', '_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Overlord-Crossovers/4473/0/', 'overlord_xover_ffbrowser.db', True, '')
        print('done')
        # self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        # self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        # self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        # self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        # self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        return True

    def load_fandom_info(self):
        ssql = AppSql()
        ssql.FilePath = 'appdata.db'
        fandoms = ssql.get_fandom_list()
        self.ffnet_list = fandoms
        print(str(len(fandoms)) + ' Fandoms loaded')
        return len(self.ffnet_list)

    def create_index_of_fandoms(self):
        for info in self.ffnet_list:
            self.create_index_of_fandom(info)

    def update_index_of_fandoms(self):
        self.load_fandom_info()
        for info in self.ffnet_list:
            self.update_index_of_fandom(info)

    def update_index_of_fandom(self, info):
        print('Updating index: ' + info.Fandom_DB_Path)
        off = FFNetProcess(info.Fandom_DB_Path)
        off.index_archive(info.FandomUrl, info.FandomName, info.Is_Xover)
        print('Updated index: ' + info.Fandom_DB_Path)
        return True

    def get_reindex_targets(self):
        reindex_list = []
        reindex_output_list = []
        else_list = []
        index_list = []
        good_list = []
        ssql = AppSql()
        ssql.FilePath = 'appdata.db'
        fandoms = ssql.get_fandom_list()
        for info in fandoms:
            off = FFNetProcess(info.Fandom_DB_Path)
            fandoms_fic_cnt = off.find_fandom_fic_cnt(info.FandomUrl)
            dbs_fic_cnt = off.get_db_fic_cnt()
            if dbs_fic_cnt == 0:
                to_index = self.print_fandom_reindex(dbs_fic_cnt, fandoms_fic_cnt, info)
                index_list.append(to_index)
                reindex_list.append(info)
            # elif dbs_fic_cnt == 25:
            #     reindex_list.append(info)
            elif fandoms_fic_cnt > dbs_fic_cnt:
                if off.is_oldest_fics_in_db(info):
                    print('DB has oldest fics')
                    update_output = self.print_good_fandominfo(dbs_fic_cnt, fandoms_fic_cnt, info)
                    index_list.append(update_output)
                    print(update_output)
                else:
                    reindex_list.append(info)
                    reindex_info = self.print_fandom_reindex(dbs_fic_cnt, fandoms_fic_cnt, info)
                    reindex_output_list.append(reindex_info)
                    print(reindex_info)
            elif fandoms_fic_cnt < dbs_fic_cnt:
                if off.is_oldest_fics_in_db(info):
                    print('DB has oldest fics')
                    print('--------------DB has more fics then archive ---------------------')
                    else_output = self.print_good_fandominfo(dbs_fic_cnt, fandoms_fic_cnt, info)
                    print(else_output)
                    else_list.append(else_output)
                else:
                    reindex_list.append(info)
                    reindex_info = self.print_fandom_reindex(dbs_fic_cnt, fandoms_fic_cnt, info)
                    reindex_output_list.append(reindex_info)
                    print(reindex_info)
            elif fandoms_fic_cnt == dbs_fic_cnt:
                print('dbfic cnt = fandom fic cnt')
                else_output = self.print_good_fandominfo(dbs_fic_cnt, fandoms_fic_cnt, info)
                print(else_output)
                good_list.append(else_output)
            else:
                print('Else Case_______________________________')
                else_output = self.print_good_fandominfo(dbs_fic_cnt, fandoms_fic_cnt, info)
                print(else_output)
                else_list.append(else_output)
        print('get_reindex_targets done')
        print('Reindex List:')
        for item in reindex_output_list:
            print(item)
        print('Reindex List Done:')
        print('Index List:')
        for item in index_list:
            print(item)
        print('Index List Done: ')
        print('Else List:')
        for item in else_list:
            print(item)
        print('Else List Done:')
        print('Good List:')
        for item in good_list:
            print(item)
        print('Good List Done: ')
        print('')
        return reindex_list

    def print_good_fandominfo(self, db_fic_cnt, fandom_fic_cnt, info):
        target_info = 'FandomId: ' + str(info.FandomId) + ' | FandomUrl: ' + str(
            info.FandomUrl) + ' | Fandom Fic cnt: ' + str(fandom_fic_cnt) + ' |  db fic cnt: ' + str(db_fic_cnt)
        print(target_info)
        return target_info

    def print_fandom_reindex(self, db_fic_cnt, fandom_fic_cnt, info):
        reindex_print_line = 'Db Does not have oldest Fics | '
        target_info = 'FandomId: ' + str(info.FandomId)
        reindex_print_line = reindex_print_line + target_info
        print(target_info)
        target_info = 'FandomUrl: ' + str(info.FandomUrl)
        reindex_print_line = reindex_print_line + " | " + target_info
        print(target_info)
        target_info = 'Fandom Fic cnt: ' + str(fandom_fic_cnt)
        reindex_print_line = reindex_print_line + " | " + target_info
        print(target_info)
        target_info = 'db fic cnt: ' + str(db_fic_cnt)
        reindex_print_line = reindex_print_line + " | " + target_info
        print(target_info)
        return reindex_print_line

    def find_reindex_targets(self):
        ssql = AppSql()
        ssql.FilePath = 'appdata.db'
        fandoms = ssql.get_fandom_list()
        for info in fandoms:
            off = FFNetProcess(info.Fandom_DB_Path)
            fandoms_fic_cnt = off.find_fandom_fic_cnt(info.FandomUrl)
            db_fic_cnt = off.get_db_fic_cnt()
            if fandoms_fic_cnt > db_fic_cnt:
                self.print_fandom_reindex(db_fic_cnt, fandoms_fic_cnt, info)
            else:
                self.print_good_fandominfo(db_fic_cnt, fandoms_fic_cnt, info)
        print('find_reindex_targets done')
        return True

    def create_index_of_fandom(self, info):
        # self.load_fandom_info()
        oDB = FanFicDB(info.Fandom_DB_Path)
        oDB.create_db(info.Fandom_DB_Path)
        off = FFNetProcess(info.Fandom_DB_Path)
        off.index_archive(info.FandomUrl, info.FandomName, info.Is_Xover)
        return True

    def reindex_fandom_by_id(self, Id, starting_page_num):
        print('Reindex Fandom #' + str(Id))
        fandom = self.get_fandom_info_by_id(Id)
        off = FFNetProcess(fandom.Fandom_DB_Path)
        off.reindex_archive(fandom.FandomUrl, fandom.FandomName, fandom.Is_Xover, starting_page_num)
        print('index Fandom #' + str(Id) + ' done')
        return True

    def get_fandom_info_by_id(self, Id):
        ssql = AppSql()
        ssql.FilePath = 'appdata.db'
        fandom = ssql.get_fandom_by_id(Id)
        return fandom

    def testa(self):
        #self.create_ficdb_for_fandom_by_id(30)
        #self.reindex_fandom_by_id(30)
        info_id = 16
        fan_info = self.get_fandom_info_by_id(info_id)
        new_fic = FanFic()
        new_fic.Chapters = 1
        new_fic.Published = '0'
        new_fic.FFNetID = '0'
        new_fic.Rating = 'M'
        new_fic.Status = 'C'
        new_fic.Summary = 'Test'
        new_fic.Title = 'Test'
        new_fic.Url = 'http://www.test.com'
        new_fic.Words = '0'
        ficDb = FanFicSql(fan_info.Fandom_DB_Path)
        ficDb.FilePath = fan_info.Fandom_DB_Path
        #ficDb.save_fic(new_fic)
        new_fic.Chapters = '2'
        new_fic.Words = '999'
        new_fic.Status = "Complete"
        new_fic.Summary = 'update works'
        ficDb.update_fic(new_fic)
        return True

    def test(self):
        #self.create_ficdb_for_fandom_by_id(30)
        #self.reindex_fandom_by_id(30)linker = DBLinker("ffbrowserdb.db")
        linker = DBLinker("ffbrowserdb.db")

        #linker.test()
        linker.test()
        return True

    def create_ficdb_for_fandom_by_id(self, fic_id):
        fandom = self.get_fandom_info_by_id(fic_id)
        ficDB = FanFicDB(fandom.Fandom_DB_Path)
        ficDB.create_db(fandom.Fandom_DB_Path)
        return True
    def remove_dup_fics(self, info):
        print('deduping index: ' + info.Fandom_DB_Path)
        ficDB = FanFicSql(info.Fandom_DB_Path)
        ficDB.FilePath = info.Fandom_DB_Path
        ficDB.delete_duplicate_fics()
        print('Deduped index: ' + info.Fandom_DB_Path)
        return True

    def remove_dup_fics_from_all(self):
        self.load_fandom_info()
        for info in self.ffnet_list:
            self.remove_dup_fics(info)
        print("dedupe of all fandoms complete")
        return True

    def create_ficlink_db(self):
        print('create fic list db')
        ficDB = FanFicSql('fic.db')
        ficDB.create_link_list_db()
        print('created fic list db')
        return True

    def add_fandom_links_to_list(self, info):
        print('starting links import database: ' + info.Fandom_DB_Path)
        ficDB = FanFicSql(info.Fandom_DB_Path)
        ficDB.FilePath = info.Fandom_DB_Path
        ficDB.add_fic_links_to_linkdb()
        print('links imported to database')
        return True

    def add_all_fandoms_to_link_list(self):
        self.load_fandom_info()
        for info in self.ffnet_list:
            self.add_fandom_links_to_list(info)
        print("all links from fandoms complete")
        return True

    def dedup_linkList_db(self):
        self.load_fandom_info()
        print('update linkdb')
        ficDB = FanFicSql(self.ffnet_list[0].Fandom_DB_Path)
        ficDB.delete_dup_ficlinks()

    def update_link_db(self):
        self.load_fandom_info()
        print('update linkdb')
        for info in self.ffnet_list:
            ficDB = FanFicSql(info.Fandom_DB_Path)
            print(info.Fandom_DB_Path)
            ficDB.add_fic_links_to_linkdb()

    def get_epubdb_ficfiles(self):
        linker = DBLinker("ffbrowserdb.db")
        print('adding file-files to table')
        linker.add_file_links_to_linkdb('file.db')
        print('done-adding to table')

    def add_ficFile_table(self):
        print('adding fic_file table')
        linker = DBLinker("ffbrowserdb.db")
        linker.create_file_list_db()
        print('done adding table')

    def set_up_packaged_date_list(self):
        packaged_date_format = "%Y-%m-%d %H:%M:%S"
        select_update_list = 'SELECT Li'
        print('adding data to update list')
        linker = DBLinker("ffbrowserdb.db")
        linker.create_packaged_date_list()
        print('done')
        return True

    def get_update_list(self):
        print('getting update list')
        linker = DBLinker("ffbrowserdb.db")
        url_list = linker.get_update_list()
        for item in url_list:
            print(item[0])

    def load_fanficurls_from_csv(self, sPath):
        fic_file = open(sPath, encoding="utf")
        fic_file_lines = []
        fan_fic_urls = []
        for aline in fic_file.readlines():
            #            values = aline.split()
            aline_list = aline.split(";")
            fic_url = FanFicUrl()
            fic_url.Url = aline_list[0]
            fic_url.Domain = aline_list[1]
            fic_url.FFArchiveFicID = aline_list[2]
            fan_fic_urls.append(fic_url)
        return fan_fic_urls

    def save_fanficurls_to_db(self, url_list):
        linker = DBLinker("ffbrowserdb.db")
        for item in url_list:
            linker.save_fanficurl(item)
    def move_links_from_csv_to_db(self, sPath):
        fan_fic_urls = self.load_fanficurls_from_csv(sPath)
        self.save_fanficurls_to_db(fan_fic_urls)


























