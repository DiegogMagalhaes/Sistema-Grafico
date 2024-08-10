from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets
from Model.window import Window
from Model.viewport import Viewport
from View.object_render import ObjectRender,RENDERER_DIMENSIONS

WINDOW_TITLE = "viewport"

class MainWindow(QtWidgets.QWidget):

    def __init__(self, viewport:Viewport, window:Window):
        super().__init__()
        
        self.window:Window = window
        self.viewport:Viewport = viewport

        self.setWindowWidgetProperties()
        self.mainContainer = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.mainContainer)
        self.objectsRenderer = ObjectRender(viewport, window)
        self.mainContainer.addWidget(self.objectsRenderer)

    def setWindowWidgetProperties(self):
        width = RENDERER_DIMENSIONS[0]
        height = RENDERER_DIMENSIONS[1] 
        self.setFixedSize(QtCore.QSize(width, height))
        self.setWindowTitle(WINDOW_TITLE)