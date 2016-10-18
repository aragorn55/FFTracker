from fanfic_epub import EpubFicTool
from fanfic_source import FanFicUpdateTracker
spath = 'C:\\G\\ficfiles\\fanfics'
#ool = EpubFicTool()
#iles = tool.get_file_list(spath)
#tool.setup_db()
#tool.procees_files(files)
tool = FanFicUpdateTracker()
tool.find_fic_references()