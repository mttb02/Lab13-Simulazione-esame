from dataclasses import dataclass


@dataclass
class State:
    _id: str
    _name: str
    _capital: str
    _lat: float
    _lng: float
    _area: float
    _population: str
    _neighbors: str

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def capital(self):
        return self._capital

    @property
    def lat(self):
        return self._lat

    @property
    def lng(self):
        return self._lng

    @property
    def area(self):
        return self._area

    @property
    def population(self):
        return self._population

    @property
    def neighbors(self):
        return self._neighbors

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return f"{self._name}"
