# import re
# import mechanize
# import requests
# specify the url
from ffjob import FFJob
from chrome_bookmark_reader import ChromeBookmarkParser
from url_tools import UrlTool
#from fanficfare_helper import FanFicFareHelper
# from addventure import Episode
# from addventure import Choice
# from create_be_db import AddventureDB
# from bearchive_process import BEarchive_process
# from be_sql_builder import BeSql
from url_tools import UrlTool
from testdb import TestDB
test_db = TestDB('ffbrowserdb.db')
test_db.fix_file_links_from_cvs("fixed_file_links.csv")
path = r"C:\Users\joshua\AppData\Local\Google\Chrome\User Data\Profile 1\Bookmarks"
sFFpath = "fff_links.csv"
misc = 'misc,csv'
#url_tool = UrlTool()
#urllist = url_tool.load_fanficurls_from_csv(sFFpath)
#url_tool.set_up_db()
#url_tool.save_fanficurls_to_db(urllist)
#helper = FanFicFareHelper()
#urllist = helper.get_urls_from_chrome_bookmark(path)
#helper.get_fanficfare_urls(urllist)
# reader = ChromeBookmarkParser()
# sorter = UrlSorter()
# urllist = reader.simple_get_urls(path)
# #sorter.set_up_db()
# for item in urllist:
#     sorter.sort_url(item)
# sorter.print_sort_results()


# path = "C:\\G\\IDE\\pycharm\\FFBrowser\\bleach2.db"
# oDB = FanFicDB('test.db')
# oDB.create_db('test.db')
# oDB = FanFicDB(path)
# oDB.create_db(path)
# beDB = AddventureDB('be.db')
# beDB.create_db('be.db')
# sbe = 'http://www.bearchive.com/~addventure/game1/docs/441/441552.html'
# betool = BEarchive_process()
# betool.get_be(sbe)
# sUrl = "https://www.fanfiction.net/anime/Bleach/?&srt=1&r=10"
# #"https://m.fanfiction.net/anime/Bleach/?srt=1&t=0&g1=0&g2=0&r=10&lan=1&len=5&s=0&c1=0&c2=0&c3=0&c4=0&_g1=0&_c1=0&_c2=0"
# browser.open(quote_page)
# ficList = []
# oIndex = FFNetIndexer('anime/bleach/')
# oIndex.indexFandom()
# quote_page = 'http://tv.adult-fanfiction.org/story.php?no=600092959'
# off = FFNetProcess(path)
# isxover = False
# off.makeIndex("anime/Bleach/", "Bleach", isxover)
# settings_db_path = 'appdata.db'
# ffDB = FanFicDB(settings_db_path)
# ffDB.create_settings_db(settings_db_path)
# settings = AppSql()
#ojob = FFJob()
# ojob.create_all_fandoms()
#ojob.remove_dup_fics_from_all()
# ojob.reindex_fandom_by_id(2)
# ojob.reindex_fandom_by_id(24)
# ojob.reindex_fandom_by_id(22)
# ojob.reindex_fandom_by_id(26)
# ojob.reindex_fandom_by_id(13)
# ojob.reindex_fandom_by_id(16)
# ojob.reindex_fandom_by_id(23)

# ojob.reindex_fandom_by_id()
# ojob.test()
# ojob.find_reindex_targets()
# targets = ojob.get_reindex_targets()
# for item in targets:
#     print('fandom_id' + str(item.FandomId))
#     print('fandom_url' + item.FandomUrl)
#ojob.update_index_of_fandoms()
# ojob.create_all_fandoms()
# ojob.reindex_fandom_by_id(2)
# ojob.reindex_fandom_by_id(24)
# ojob.reindex_fandom_by_id(22)
# ojob.reindex_fandom_by_id(26)
# ojob.reindex_fandom_by_id(13)
# ojob.reindex_fandom_by_id(16)
#ojob.reindex_fandom_by_id(23, 0)
#ojob.test()
#ojob.set_up_packaged_date_list()
#ojob.get_update_list()
#ojob.create_ficlink_db()
#ojob.add_all_fandoms_to_link_list()
#ojob.add_ficFile_table()
#ojob.get_epubdb_ficfiles()
#ojob.update_link_db()
# ojob.reindex_fandom_by_id()
# ojob.test()
#ojob.find_reindex_targets()

#ojob.update_index_of_fandoms()
# for fic in list:
#    print(fic.FandomId)
#    print(fic.FandomUrl)
# ojob.load_fandom_info()
# ojob.create_index_of_fandoms()
print('done')

#
