import sys

class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = dict()

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        t = tuple(filter(lambda k: k.pk == pk, (row for x in self.dict_db.values() for row in x)))
        return t[0] if len(t) > 0 else None

class Record:
    PK = 0

    def __new__(cls, *args, **kwargs):
        cls.PK += 1
        return super().__new__(cls)

    def __init__(self, fio: str, descr: str, old: int):
        self.pk = self.PK
        self.fio = fio
        self.descr = descr
        self.old = old

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in не менять!

path = 'file.txt'

db = DataBase(path)

for line in lst_in:
    v1, v2, v3 = line.split(';')
    record = Record(v1.strip(), v2.strip(), int(v3.strip()))
    db.write(record)