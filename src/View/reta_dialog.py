from Model.ponto import Ponto
from Model.reta import Reta
from PyQt6  import QtCore, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal

class RetaInsertionDialog(QtWidgets.QDialog):
    onLineInserted = pyqtSignal(Reta)
    x = []
    y = []

    def __init__(self) :
        super().__init__()
        self.setWindowProperties()
        self.initUI()

    def setWindowProperties(self):
        self.setModal(True)
        self.setFixedSize(300, 150)

    def initUI(self):
        self.initFormContainer()
        self.initForm()
        self.initButtons()

    def initFormContainer(self):
        self.formContainer = QtWidgets.QVBoxLayout()
        title = QtWidgets.QLabel()
        title.setText("Inserir Botão")
        self.formContainer.addWidget(title)
        self.setLayout(self.formContainer)

    def initForm(self):
        self.formLayout = QtWidgets.QGridLayout()
        self.formContainer.addLayout(self.formLayout)
        self.initInsertForm()

    def initInsertForm(self):
        rowName1 = QtWidgets.QLabel('Ponto inicial')
        self.formLayout.addWidget(rowName1, 0, 0)

        xLabel1 = QtWidgets.QLabel('X')
        xLabel1.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.addWidget(xLabel1, 0, 1)

        xInput1 = QtWidgets.QDoubleSpinBox()
        xInput1.setMinimum(-10000)
        xInput1.setMaximum(10000)
        self.formLayout.addWidget(xInput1, 0, 2)

        yLabel1 = QtWidgets.QLabel('Y')
        yLabel1.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.addWidget(yLabel1, 0, 3)

        yInput1 = QtWidgets.QDoubleSpinBox()
        yInput1.setMinimum(-10000)
        yInput1.setMaximum(10000)
        self.formLayout.addWidget(yInput1, 0, 4)

        rowName2 = QtWidgets.QLabel('Ponto final')
        self.formLayout.addWidget(rowName2, 1, 0)

        xLabel2 = QtWidgets.QLabel('X')
        xLabel2.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.addWidget(xLabel2, 1, 1)

        xInput2 = QtWidgets.QDoubleSpinBox()
        xInput2.setMinimum(-10000)
        xInput2.setMaximum(10000)
        self.formLayout.addWidget(xInput2, 1, 2)

        yLabel2 = QtWidgets.QLabel('Y')
        yLabel2.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.addWidget(yLabel2, 1, 3)

        yInput2 = QtWidgets.QDoubleSpinBox()
        yInput2.setMinimum(-10000)
        yInput2.setMaximum(10000)
        self.formLayout.addWidget(yInput2, 1, 4)
 
        self.x.append(xInput1)
        self.x.append(xInput2)
        self.y.append(yInput1)
        self.y.append(yInput2)

    def initButtons(self):
        rowButtons = QtWidgets.QHBoxLayout()
        addPointButton = QtWidgets.QPushButton('Adicionar Reta')

        addPointButton.clicked.connect(lambda : self.onLineInserted.emit(self.getReta()))
        rowButtons.addWidget(addPointButton)

        self.formContainer.addLayout(rowButtons)

    def getReta(self):
        ponto1 = Ponto(self.x[0].value(),self.y[0].value())
        ponto2 = Ponto(self.x[1].value(),self.y[1].value())
        reta = Reta(ponto1,ponto2)
        return reta