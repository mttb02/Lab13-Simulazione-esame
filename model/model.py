import copy

from database.DAO import DAO
import networkx as nx
from geopy import distance
class Model:
    def __init__(self):
        self._stati = {}
        self._graph = nx.Graph()

        self.percorso = []
        self.distanze = []
        self.costi = []

    def get_years(self):
        return DAO.get_all_years()

    def get_shapes(self):
        return DAO.get_all_shapes()

    def crea_grafo(self, year, shape):
        temp_stati = DAO.get_all_states()
        for s in temp_stati:
            self._stati[s.id] = s
        self._graph.add_nodes_from(self._stati.keys(), weight=0)

        temp_relazioni = DAO.get_all_rel()
        self._graph.add_edges_from(temp_relazioni)

        temp_pesi = DAO.get_frequenze(year, shape)
        for e in self._graph.edges:
            if e[0] not in temp_pesi:
                temp_pesi[e[0]] = 0
            if e[1] not in temp_pesi:
                temp_pesi[e[1]] = 0
            print(temp_pesi[e[0]] + temp_pesi[e[1]])
            self._graph.add_edge(e[0], e[1], weight=temp_pesi[e[0]] + temp_pesi[e[1]])

    def get_percorso(self):
        temp_percorso = []
        temp_distanze = []
        temp_costi = []

        for n in self._graph.nodes:
            temp_percorso.append(n)
            temp_distanze.append(0)
            temp_costi.append(0)
            self.ricorsione(n, self._graph.copy(), temp_percorso, temp_distanze, temp_costi)
            temp_percorso.remove(n)
            temp_distanze.remove(0)
            temp_costi.remove(0)


    def ricorsione(self, n, grafo, temp_percorso, temp_distanze, temp_costi):
        if len(list(grafo.neighbors(n))) == 0:
            if sum(temp_distanze) > sum(self.distanze):
                self.distanze = copy.deepcopy(temp_distanze)
                self.percorso = copy.deepcopy(temp_percorso)
                self.costi = copy.deepcopy(temp_costi)
        else:
            for n1 in grafo.neighbors(n):
                if grafo[n][n1]["weight"] > temp_costi[len(temp_costi)-1]:
                    temp_percorso.append(n1)
                    temp_distanze.append(float(distance.geodesic((self._stati[n].lat, self._stati[n].lng), (self._stati[n1].lat, self._stati[n1].lng)).km))
                    temp_costi.append(float(grafo[n][n1]["weight"]))
                    temp_grafo = grafo.copy()
                    temp_grafo.remove_node(n)
                    self.ricorsione(n1, temp_grafo, temp_percorso, temp_distanze, temp_costi)
                    temp_percorso.remove(n1)
                    temp_distanze.remove(distance.geodesic((self._stati[n].lat, self._stati[n].lng), (self._stati[n1].lat, self._stati[n1].lng)).km)
                    temp_costi.remove(grafo[n][n1]["weight"])
                else:
                    if sum(temp_distanze) > sum(self.distanze):
                        self.distanze = copy.deepcopy(temp_distanze)
                        self.percorso = copy.deepcopy(temp_percorso)
                        self.costi = copy.deepcopy(temp_costi)





