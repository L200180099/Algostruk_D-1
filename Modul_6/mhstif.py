class MhsTIF(object):
    def __init__(self,nama,nim,tinggal,us):
        self.nama = nama
        self.nim = nim
        self.tinggal = tinggal
        self.us = us
    def __str__(self):
        return str(self.nama," ",self.nim," ",self.tinggal)
