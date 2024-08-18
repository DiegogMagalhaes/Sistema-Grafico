from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6  import QtCore, QtWidgets
from Model.window import WindowTransformations


class WindowTransformationsGroup(QtWidgets.QGroupBox):
  onButtonClicked = pyqtSignal(WindowTransformations)

  def __init__(self):
    super().__init__('Window Transformations')

    windowTransformationsLayout = QtWidgets.QGridLayout()

    zoomInButton = QtWidgets.QPushButton('🔍+')
    zoomInButton.clicked.connect(lambda : self.onButtonClicked.emit(WindowTransformations.ZOOM_IN))
    windowTransformationsLayout.addWidget(zoomInButton, 0, 0)

    moveUpButton = QtWidgets.QPushButton('˄')
    moveUpButton.clicked.connect(lambda : self.onButtonClicked.emit(WindowTransformations.MOVE_UP))
    windowTransformationsLayout.addWidget(moveUpButton, 0, 1)

    zoomOutButton = QtWidgets.QPushButton('🔍-')
    zoomOutButton.clicked.connect(lambda : self.onButtonClicked.emit(WindowTransformations.ZOOM_OUT))
    windowTransformationsLayout.addWidget(zoomOutButton, 0, 2)

    moveLeftButton = QtWidgets.QPushButton('<')
    moveLeftButton.clicked.connect(lambda : self.onButtonClicked.emit(WindowTransformations.MOVE_LEFT))
    windowTransformationsLayout.addWidget(moveLeftButton, 1, 0)

    resetButton = QtWidgets.QPushButton('RESET')
    resetButton.clicked.connect(lambda : self.onButtonClicked.emit(WindowTransformations.RESET))
    windowTransformationsLayout.addWidget(resetButton, 1, 1)

    moveRightButton = QtWidgets.QPushButton('>')
    moveRightButton.clicked.connect(lambda : self.onButtonClicked.emit(WindowTransformations.MOVE_RIGHT))
    windowTransformationsLayout.addWidget(moveRightButton, 1, 2)

    rotateLeft = QtWidgets.QPushButton('↩')
    rotateLeft.clicked.connect(lambda : self.onButtonClicked.emit(WindowTransformations.ROTATE_LEFT))
    windowTransformationsLayout.addWidget(rotateLeft, 2, 0)

    moveDownButton = QtWidgets.QPushButton('˅')
    moveDownButton.clicked.connect(lambda : self.onButtonClicked.emit(WindowTransformations.MOVE_DOWN))
    windowTransformationsLayout.addWidget(moveDownButton, 2, 1)

    rotateRight = QtWidgets.QPushButton('↪')
    rotateRight.clicked.connect(lambda : self.onButtonClicked.emit(WindowTransformations.ROTATE_RIGHT))
    windowTransformationsLayout.addWidget(rotateRight, 2, 2)

    self.setLayout(windowTransformationsLayout)