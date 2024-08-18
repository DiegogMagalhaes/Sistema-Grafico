import sys
from PyQt6 import QtWidgets
from Controller.xml_utils import xmt_to_window_viewport, window_viewport_to_xml
from View.main_window import MainWindow
from Controller.gui_controller import GUIController

##Le o arquivo xml e preenche window e viewport
window, viewport = xmt_to_window_viewport("entrada.xml")

##Transforma as coordenadas dos objetos da window(coordenadas cartesianas) em coordenadas para a viewport(pixels)
##viewport.transformarCoordenadas(window)

##Cria um arquivo xml, contendo a saida das coordenadas transformadas
##window_viewport_to_xml("saida.xml",window, viewport)

##Cria uma janela e renderiza os objetos da window, com suas coordenadas ja transformadas para a viewport, na tela
gui_controller = GUIController(window)
gui_controller.init_gui(window,viewport)

