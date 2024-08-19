from Model.ponto import Ponto
from PyQt6  import QtCore, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal

class PontoInsertionDialog(QtWidgets.QDialog):
    onPointInserted = pyqtSignal(Ponto)
    x = 0
    y = 0

    def __init__(self) :
        super().__init__()
        self.setWindowProperties()
        self.initUI()

    def setWindowProperties(self):
        self.setModal(True)
        self.setFixedSize(300, 100)

    def initUI(self):
        self.initFormContainer()
        self.initForm()
        self.initButtons()

    def initFormContainer(self):
        self.formContainer = QtWidgets.QVBoxLayout()
        title = QtWidgets.QLabel()
        title.setText("Inserir Ponto")
        self.formContainer.addWidget(title)
        self.setLayout(self.formContainer)

    def initForm(self):
        self.formLayout = QtWidgets.QGridLayout()
        self.formContainer.addLayout(self.formLayout)
        self.initInsertForm()

    def initInsertForm(self):
        rowName = QtWidgets.QLabel('Ponto')
        self.formLayout.addWidget(rowName, 0, 0)

        xLabel = QtWidgets.QLabel('X')
        xLabel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.addWidget(xLabel, 0, 1)

        xInput = QtWidgets.QDoubleSpinBox()
        xInput.setMinimum(-10000)
        xInput.setMaximum(10000)
        self.formLayout.addWidget(xInput, 0, 2)

        yLabel = QtWidgets.QLabel('Y')
        yLabel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.addWidget(yLabel, 0, 3)

        yInput = QtWidgets.QDoubleSpinBox()
        yInput.setMinimum(-10000)
        yInput.setMaximum(10000)
        self.formLayout.addWidget(yInput, 0, 4)
 
        self.x = xInput
        self.y = yInput

    def initButtons(self):
        rowButtons = QtWidgets.QHBoxLayout()
        addPointButton = QtWidgets.QPushButton('Adicionar Ponto')
        addPointButton.clicked.connect(lambda : self.onPointInserted.emit(Ponto(self.x.value(),self.y.value())))
        rowButtons.addWidget(addPointButton)

        self.formContainer.addLayout(rowButtons)
