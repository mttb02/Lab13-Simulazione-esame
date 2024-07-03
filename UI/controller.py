import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []
        self._anno = None
        self._forma = None

    def fillDD(self):

        self._listYear = self._model.get_years()
        for y in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(key=y, text=y, on_click=self.read_anno))

        self._listShape = self._model.get_shapes()
        for s in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(key=s, text=s, on_click=self.read_forma))

    def read_anno(self, e):
        self._anno = e.control.key
    def read_forma(self, e):
        self._forma = e.control.key


    def handle_graph(self, e):

        self._view.txt_result.controls.clear()
        if self._anno == None or self._forma == None:
            self._view.create_alert("Selezionare anno e forma")
            return

        self._model.crea_grafo(self._anno, self._forma)
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {len(self._model._graph.nodes)} Numero di archi: {len(self._model._graph.edges)}"))
        for n in self._model._graph.nodes:
            temp_neighbors = self._model._graph.neighbors(n)
            temp_tot = 0
            for n1 in temp_neighbors:
                temp_tot += self._model._graph[n][n1]["weight"]
            self._view.txt_result.controls.append(ft.Text(f"Nodo: {n}, somma pesi su archi = {temp_tot}"))
        self._view.btn_path.disabled = False
        self._view.update_page()



    def handle_path(self, e):

        self._model.get_percorso()
        temp_cammino_minimo = self._model.percorso
        temp_lista_costi = self._model.costi
        temp_lista_distanze = self._model.distanze
        self._view.txtOut2.controls.append(ft.Text(f"Peso cammino minimo: {sum(temp_lista_costi)}"))
        for i in range(0, len(temp_cammino_minimo)-2):
            self._view.txtOut2.controls.append(ft.Text(f"{temp_cammino_minimo[i]} --> {temp_cammino_minimo[i+1]}: weight {temp_lista_costi[i+1]} distance {temp_lista_distanze[i+1]}"))
        self._view.update_page()