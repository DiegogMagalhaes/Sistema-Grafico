from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets
from Model.window import Window
from Model.viewport import Viewport

RENDERER_DIMENSIONS = (640, 480)

class ObjectRender(QtWidgets.QWidget):
    
    def __init__(self, viewport:Viewport, window:Window):
        super().__init__()
        
        self.viewport = viewport
        self.window = window
        
        self.setWidgetSize()
        self.setBackgroundColor()
    
    def setWidgetSize(self):
        width = RENDERER_DIMENSIONS[0]
        height = RENDERER_DIMENSIONS[1]
        self.setFixedSize(QtCore.QSize(width, height))

    def setBackgroundColor(self):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.GlobalColor.black)
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def paintEvent(self, event):
        self.draw()

    def draw(self):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen(Qt.GlobalColor.red)
        painter.setPen(pen)

        for p in self.window.pontos:
            painter.drawPoint(int(p.x), int(p.y))

        for r in self.window.retas:
            qtPoint1 = QtCore.QPointF(int(r.ponto1.x), int(r.ponto1.y))
            qtPoint2 = QtCore.QPointF(int(r.ponto2.x), int(r.ponto2.y))
            qtLine = QtCore.QLineF(qtPoint1, qtPoint2)
            painter.drawLine(qtLine)

        for pl in self.window.poligonos:
            qtPolygon = QtGui.QPolygonF()
            for p in pl.pontos:
                qtPolygon.append(QtCore.QPointF(int(p.x), int(p.y)))
            painter.drawPolygon(qtPolygon)

        painter.end()
