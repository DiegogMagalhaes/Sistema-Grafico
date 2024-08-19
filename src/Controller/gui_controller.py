import sys
import copy
from PyQt6 import QtWidgets
from View.main_window import MainWindow
from Model.window import Window, WindowTransformations
from Controller.xml_utils import window_viewport_to_xml

class GUIController():
    view = None
    app = None

    def __init__(self, window):
        self.untransformed_window = copy.deepcopy(window)
        self.untransformed_window.pontos = copy.deepcopy(window.pontos)
        self.untransformed_window.retas = copy.deepcopy(window.retas)
        self.untransformed_window.poligonos = copy.deepcopy(window.poligonos)

    def init_gui(self, window, viewport):
        self.app = QtWidgets.QApplication(sys.argv)
        viewport.transformarCoordenadas(window)
        self.view = MainWindow(viewport, window)
        self.view.onTransformationApplied.connect(lambda type : self.on_transform_window(type))
        self.view.onInsertPonto.connect(lambda p : self.on_insert_point(p))
        self.view.onInsertReta.connect(lambda r: self.on_insert_line(r))
        self.view.onInsertPoligono.connect(lambda pl: self.on_insert_polygon(pl))
        self.view.onExportXml.connect(lambda : self.export_xml())
        self.view.show()
        self.app.exec()

    def copy_window(self, window):
        self.untransformed_window = copy.deepcopy(window)
        self.untransformed_window.pontos = copy.deepcopy(window.pontos)
        self.untransformed_window.retas = copy.deepcopy(window.retas)
        self.untransformed_window.poligonos = copy.deepcopy(window.poligonos)
        self.view.window = window
        self.view.viewport.transformarCoordenadas(window)
        self.view.update()

    def unstransform_window_elements(self):        
        self.view.window.pontos = copy.deepcopy(self.untransformed_window.pontos)
        self.view.window.retas = copy.deepcopy(self.untransformed_window.retas)
        self.view.window.poligonos = copy.deepcopy(self.untransformed_window.poligonos)

    def update_window(self):
        self.unstransform_window_elements()
        self.view.viewport.transformarCoordenadas(self.view.window)
        self.view.update()

    def on_transform_window(self,type):
        self.unstransform_window_elements()
        self.view.window.apply_windows_transformation(type)

        self.untransformed_window.pontos = copy.deepcopy(self.view.window.pontos)
        self.untransformed_window.retas = copy.deepcopy(self.view.window.retas)
        self.untransformed_window.poligonos = copy.deepcopy(self.view.window.poligonos)
            
        if(type == WindowTransformations.RESET):
            self.copy_window(self.view.window)
        else:
            self.update_window()

    def on_insert_point(self, ponto):
        self.untransformed_window.pontos.append(ponto)
        self.update_window()
    
    def on_insert_line(self, reta):
        self.untransformed_window.retas.append(reta)
        self.update_window()

    def on_insert_polygon(self, poligono):
        print("inserindo")
        
        print(len(poligono.pontos))

        for p in poligono.pontos:
            print("ponto")
            print(p.x)
            print(p.y)

        self.untransformed_window.poligonos.append(poligono)
        self.update_window()

    def export_xml(self):
        self.unstransform_window_elements()
        window_viewport_to_xml("saida.xml",self.view.window,self.view.viewport)
        