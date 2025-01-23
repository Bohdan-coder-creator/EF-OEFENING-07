class Liedje:
    def __init__(self, performer, titel, foto):
        self._performer = performer
        self._titel = titel
        self._foto = foto

    @property
    def performer(self):
        return self._performer

    @property
    def titel(self):
        return self._titel

    @property
    def foto(self):
        return self._foto

    def __str__(self):
        return f"{self._performer} - {self._titel}"

    def __repr__(self):
        return f"Liedje(performer={self._performer}, titel={self._titel}, foto={self._foto})"
