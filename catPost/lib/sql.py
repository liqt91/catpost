

class AutoCloseCursorConnection(object):
    _cursor = None
    _conn = None

    def __init__(self, conn):
        self._conn = conn

    def __getattr__(self, key):
        return getattr(self._conn, key)

    def cursor(self, *args, **kwargs):
        self._cursor = self._conn.cursor(*args, **kwargs)
        return self._cursor

    def close(self):
        if self._cursor:
            self._cursor.close()
        self._conn.close()