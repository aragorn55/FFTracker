import json, sys, os, re

class ChromeBookmarkParser(object):
    def print_urls(self, file_path):

        with open (file_path, encoding="utf") as f:
            caca = json.load(f)
        bookmarks = caca['roots']['other']['children'][0]['children'][1]['children']
        for obj in bookmarks:
            print(obj['url'])

    def simple_get_urls(self, file_path):
        print(file_path)
        bookmark_file = open(file_path, encoding="utf")
        bookmark_lines = []
        bookmark_urls = []
        for aline in bookmark_file.readlines():
#            values = aline.split()
            bookmark_lines.append(aline)
        print(str(len(bookmark_lines)))
        for bk_line in bookmark_lines:
            icnt = bk_line.find('"url": "')
            if icnt > -1:
                iend = bk_line.rfind('"')
                bk_line = bk_line[icnt + 8:iend ]
                bookmark_urls.append(bk_line)
                print(bk_line)

        return bookmark_urls



