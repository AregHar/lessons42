import sqlite3

from storage.persistence import Persistence


class SQLitePersistence(Persistence):
    def __init__(self,db="file:sqlite.db?mode=rwc"):
        self._sqlite = sqlite3.connect(db, uri=True)
        self._cur = self._sqlite.cursor()

    def write(self, key: str, data: str) -> None:
        self._cur.execute("create table '%s' (value text)" % key)
        self._cur.execute("insert into '%s' values('%s')" % (key, data))
        self._sqlite.commit()
        self._cur.close()
        self._sqlite.close()

    def read(self, key: str) -> str:
        self._cur.execute("select value from '%s'" % key)
        value = self._cur.fetchone()[0]
        self._sqlite.commit()
        self._sqlite.close()
        return value
