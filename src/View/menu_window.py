from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6  import QtCore, QtWidgets
from Model.window import WindowTransformations
from Model.ponto import Ponto
from Model.reta import Reta
from Model.poligono import Poligono
from View.ponto_dialog import PontoInsertionDialog
from View.reta_dialog import RetaInsertionDialog
from View.poligono_dialog import PonigonoInsertionDialog
from enum import Enum

class DialogType(Enum):
  DIALOG_INSERT_PONTO = 1
  DIALOG_INSERT_RETA = 2
  DIALOG_INSERT_POLIGONO = 3

class MenuGroup(QtWidgets.QGroupBox):
  onButtonTransformClicked = pyqtSignal(WindowTransformations)
  onExportXml = pyqtSignal()
  onInsertPonto = pyqtSignal(Ponto)
  onInsertReta = pyqtSignal(Reta)
  onInsertPoligono = pyqtSignal(Poligono)

  def __init__(self):
    super().__init__()
    self.grid = QtWidgets.QGridLayout()
    self.setWindowInsertionsLayout()
    self.setWindowTransfationsLayout()
    self.setWindowOptions()
    self.setLayout(self.grid)

  def setWindowOptions(self):
    insertPontoButton  = QtWidgets.QPushButton("Exportar xml")
    insertPontoButton.clicked.connect(lambda : self.onExportXml.emit())
    self.grid.addWidget(insertPontoButton,4,1)

  def setWindowInsertionsLayout(self):
    
    insertPontoButton  = QtWidgets.QPushButton("Inserir Ponto")
    insertPontoButton.clicked.connect(lambda : self.open_dialog(DialogType.DIALOG_INSERT_PONTO))
    self.grid.addWidget(insertPontoButton,3,0)
    insertPontoButton  = QtWidgets.QPushButton("Inserir Reta")
    insertPontoButton.clicked.connect(lambda : self.open_dialog(DialogType.DIALOG_INSERT_RETA))
    self.grid.addWidget(insertPontoButton,3,1)
    insertPontoButton  = QtWidgets.QPushButton("Inserir Poligono")
    insertPontoButton.clicked.connect(lambda : self.open_dialog(DialogType.DIALOG_INSERT_POLIGONO))
    self.grid.addWidget(insertPontoButton,3,2)
    

  def setWindowTransfationsLayout(self):
    

    zoomInButton = QtWidgets.QPushButton('🔍+')
    zoomInButton.clicked.connect(lambda : self.onButtonTransformClicked.emit(WindowTransformations.ZOOM_IN))
    self.grid.addWidget(zoomInButton, 0, 0)

    moveUpButton = QtWidgets.QPushButton('˄')
    moveUpButton.clicked.connect(lambda : self.onButtonTransformClicked.emit(WindowTransformations.MOVE_UP))
    self.grid.addWidget(moveUpButton, 0, 1)

    zoomOutButton = QtWidgets.QPushButton('🔍-')
    zoomOutButton.clicked.connect(lambda : self.onButtonTransformClicked.emit(WindowTransformations.ZOOM_OUT))
    self.grid.addWidget(zoomOutButton, 0, 2)

    moveLeftButton = QtWidgets.QPushButton('<')
    moveLeftButton.clicked.connect(lambda : self.onButtonTransformClicked.emit(WindowTransformations.MOVE_LEFT))
    self.grid.addWidget(moveLeftButton, 1, 0)

    resetButton = QtWidgets.QPushButton('RESET')
    resetButton.clicked.connect(lambda : self.onButtonTransformClicked.emit(WindowTransformations.RESET))
    self.grid.addWidget(resetButton, 1, 1)

    moveRightButton = QtWidgets.QPushButton('>')
    moveRightButton.clicked.connect(lambda : self.onButtonTransformClicked.emit(WindowTransformations.MOVE_RIGHT))
    self.grid.addWidget(moveRightButton, 1, 2)

    rotateLeft = QtWidgets.QPushButton('↩')
    rotateLeft.clicked.connect(lambda : self.onButtonTransformClicked.emit(WindowTransformations.ROTATE_LEFT))
    self.grid.addWidget(rotateLeft, 2, 0)

    moveDownButton = QtWidgets.QPushButton('˅')
    moveDownButton.clicked.connect(lambda : self.onButtonTransformClicked.emit(WindowTransformations.MOVE_DOWN))
    self.grid.addWidget(moveDownButton, 2, 1)

    rotateRight = QtWidgets.QPushButton('↪')
    rotateRight.clicked.connect(lambda : self.onButtonTransformClicked.emit(WindowTransformations.ROTATE_RIGHT))
    self.grid.addWidget(rotateRight, 2, 2)

  def open_dialog(self,type):
      if type == DialogType.DIALOG_INSERT_PONTO:
          dialog = PontoInsertionDialog()
          dialog.onPointInserted.connect(lambda p: self.onInsertPonto.emit(p))
          dialog.exec()
      elif type == DialogType.DIALOG_INSERT_RETA:
          dialog = RetaInsertionDialog()
          dialog.onLineInserted.connect(lambda r: self.onInsertReta.emit(r))
          dialog.exec()
      elif type == DialogType.DIALOG_INSERT_POLIGONO:
          dialog = PonigonoInsertionDialog()
          dialog.onPolygonInserted.connect(lambda pl: self.onInsertPoligono.emit(pl))
          dialog.exec()