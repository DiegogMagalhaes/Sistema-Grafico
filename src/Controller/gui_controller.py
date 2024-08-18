import sys
import copy
from PyQt6 import QtWidgets
from View.main_window import MainWindow
from Model.window import Window

class GUIController():
    view = None
    app = None
    initial_window_dict = {}

    def __init__(self, window):
        self.initial_window = copy.deepcopy(window)

        ##self.initial_window_dict[('window')] = window
        ##self.initial_window = Window(window.xwmin,window.ywmin,window.xwmax,window.ywmax)
        self.initial_window.pontos = copy.deepcopy(window.pontos)
        self.initial_window.retas = copy.deepcopy(window.retas)
        self.initial_window.poligonos = copy.deepcopy(window.poligonos)

    def init_gui(self, window, viewport):
        self.app = QtWidgets.QApplication(sys.argv)
        viewport.transformarCoordenadas(window)
        self.view = MainWindow(viewport, window)
        self.view.onTransformationApplied.connect(lambda type : self.on_transform_window(type))
        self.view.show()
        self.app.exec()


    def update_window(self):
        
        print("teste")
        for p in self.initial_window.pontos:
            print(p.x)

        self.view.window.pontos = copy.deepcopy(self.initial_window.pontos)
        self.view.window.retas = copy.deepcopy(self.initial_window.retas)
        self.view.window.poligonos = copy.deepcopy(self.initial_window.poligonos)

        self.view.viewport.transformarCoordenadas(self.view.window)
        self.view.update()


    def on_transform_window(self,type):
        self.view.window.apply_windows_transformation(type)
        self.update_window()