import attr


@attr.s
class FanFicDbToDb(object):
    _FanFicDbId = -1
    _DBPath = -1
    _FicFileID = -1
    _FicId = -1
    _FanFicArchiveId = ''
    @property
    def FanFicDbId(self):
        return self._FanFicDbId

    @FanFicDbId.setter
    def FanFicDbId(self, voFanFicDbId):
        self._FanFicDbId = voFanFicDbId



    @property
    def FicFileID(self):
        return self._FicFileID

    @FicFileID.setter
    def FicFileID(self, voFicFileID):
        self._FicFileID = voFicFileID



    @property
    def FicId(self):
        return self._FicId

    @FicId.setter
    def FicId(self, voFicId):
        self._FicId = voFicId



    @property
    def FanFicArchiveId(self):
        return self._FanFicArchiveId

    @FanFicArchiveId.setter
    def FanFicArchiveId(self, voFanFicArchiveId):
        self._FanFicArchiveId = voFanFicArchiveId



    @property
    def DBPath(self):
        return self._DBPath

    @DBPath.setter
    def DBPath(self, voDBPath):
        self._DBPath = voDBPath