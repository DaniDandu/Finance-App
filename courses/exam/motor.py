# -număr cilindri (int)
# -număr supape (int)
# -putere maximă - cp (int)
# -tip carburant (string)
# -tip injecţie (string)
# -catalizator (string)
# -sistem de alimentare (string)

class Motor:
    def __init__(self, nr_cilindri: int, nr_supape: int, putere_max: int, tip_carburant: str,
                 tip_injectie: str, catalizator: str, sistem_alimentare: str):
        self.set_nr_cilindri(nr_cilindri)
        self.__nr_supape = nr_supape
        self.set_putere_max(putere_max)
        self.__tip_carburant = tip_carburant
        self.__tip_injectie = tip_injectie
        self.set_catalizator(catalizator)
        self.__sistem_alimentare = sistem_alimentare

    def get_nr_cilindri(self) -> int:
        return self.__nr_cilindri

    def set_nr_cilindri(self, value: int):
        self.__nr_cilindri = value

    def get_putere_max(self) -> int:
        return self.__putere_max

    def set_putere_max(self, value: int):
        self.__putere_max = value

    def get_catalizator(self) -> str:
        return self.__catalizator

    def set_catalizator(self, value: str):
        self.__catalizator = value
