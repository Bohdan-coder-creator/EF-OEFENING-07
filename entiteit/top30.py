import json
from .liedje import Liedje

class Top30:
    def __init__(self):
        self._collectie = []
        self._laad_top30()

    def _laad_top30(self):
        with open('data/top30.json', 'rt', encoding='utf-8') as file:
            data = json.load(file)
            for item in data['top30']:
                liedje = Liedje(
                    performer=item['performer'],
                    titel=item['titel'],
                    foto=item['foto']
                )
                self._collectie.append(liedje)

    def lijst(self):
        return self._collectie
