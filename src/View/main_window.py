from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6 import QtCore, QtGui, QtWidgets
from Model.window import Window, WindowTransformations
from Model.viewport import Viewport
from View.object_render import ObjectRender,RENDERER_DIMENSIONS
from View.window_transformations import WindowTransformationsGroup

WINDOW_TITLE = "viewport"

class MainWindow(QtWidgets.QWidget):

    onTransformationApplied = pyqtSignal(WindowTransformations)

    def __init__(self, viewport:Viewport, window:Window):
        super().__init__()
        
        self.window:Window = window
        self.viewport:Viewport = viewport

        self.setWindowWidgetProperties()
        self.mainContainer = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.mainContainer)
        self.objectsRenderer = ObjectRender(viewport, window)
        self.mainContainer.addWidget(self.objectsRenderer)
        self.initUI()

    def paintEvent(self, event):
        self.objectsRenderer.update()

    def setWindowWidgetProperties(self):
        width = RENDERER_DIMENSIONS[0]
        height = RENDERER_DIMENSIONS[1] 
        self.setFixedSize(QtCore.QSize(width, height))
        self.setWindowTitle(WINDOW_TITLE)

    def initUI(self):
        self.initMainContainer
        self.initSidePanel()
    
    def initMainContainer(self):
        self.mainContainer = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.mainContainer)

    def initSidePanel(self):
        self.sidePanel = QtWidgets.QVBoxLayout()
        self.sidePanel.setAlignment(Qt.AlignmentFlag.AlignTop)

        title = QtWidgets.QLabel(WINDOW_TITLE)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sidePanel.addWidget(title)

        self.initWindowTransformationsGroup()

        self.mainContainer.addLayout(self.sidePanel)

    def initWindowTransformationsGroup(self):
        windowTransformationsGroup = WindowTransformationsGroup()
        windowTransformationsGroup.onButtonClicked.connect(lambda t : self.onTransformationApplied.emit(t))
        self.sidePanel.addWidget(windowTransformationsGroup)