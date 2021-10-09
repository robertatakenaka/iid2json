class BaseDocument:

    def __init__(self):
        self._records = None

    @property
    def i_record(self):
        try:
            return self._records.get("i")[0]
        except (KeyError, IndexError):
            return

    @property
    def o_record(self):
        try:
            return self._records.get("o")[0]
        except (KeyError, IndexError):
            return

    @property
    def h_record(self):
        try:
            return self._records.get("h")[0]
        except (KeyError, IndexError):
            return

    @property
    def c_records(self):
        return self._records.get("c")

    @property
    def p_records(self):
        return self._records.get("p")

    def set_records(self, records):
        self._records = {}
        for record in records:
            self._records.setdefault(record.rec_type, [])
            self._records[record.rec_type].append(record)
