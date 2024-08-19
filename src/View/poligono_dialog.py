from Model.ponto import Ponto
from Model.poligono import Poligono
from PyQt6  import QtCore, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal

class PonigonoInsertionDialog(QtWidgets.QDialog):
    onPolygonInserted = pyqtSignal(Poligono)
    inputs = []
    numPontos = 5

    def __init__(self) :
        super().__init__()
        self.setWindowProperties()
        self.initUI()

    def setWindowProperties(self):
        self.setModal(True)
        self.setFixedSize(300, 300)

    def initUI(self):
        self.initFormContainer()
        self.initForm()
        self.initButtons()

    def initFormContainer(self):
        self.formContainer = QtWidgets.QVBoxLayout()
        title = QtWidgets.QLabel()
        title.setText("Inserir Poligono")
        self.formContainer.addWidget(title)

        name = QtWidgets.QLabel('Numero de Pontos')
        self.formContainer.addWidget(name)

        numInput = QtWidgets.QDoubleSpinBox()
        numInput.setMinimum(3)
        numInput.setMaximum(100)
        numInput.setValue(self.numPontos)
        numInput.valueChanged.connect(lambda : self.changeNumberPoints(numInput.value()))
        self.formContainer.addWidget(numInput)

        self.setLayout(self.formContainer)

    def initForm(self):
        self.formLayout = QtWidgets.QGridLayout()
        formLayoutWrapper = QtWidgets.QWidget()
        formLayoutWrapper.setLayout(self.formLayout)

        formScrollArea = QtWidgets.QScrollArea()
        formScrollArea.setWidget(formLayoutWrapper)
        formScrollArea.setFixedHeight(150)
        formScrollArea.setWidgetResizable(True)
        
        self.formContainer.addWidget(formScrollArea)
        self.initInsertForm()

    def changeNumberPoints(self, num):
        print(num)
        self.numPontos = num
        self.clearForm()
        self.initInsertForm()

    def initInsertForm(self):
              
        rowName = QtWidgets.QLabel('Pontos:')
        self.formLayout.addWidget(rowName, 0, 0)

        i = 1
        while(i<self.numPontos+1):

            xLabel = QtWidgets.QLabel('X')
            xLabel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.formLayout.addWidget(xLabel, i, 1)

            xInput = QtWidgets.QDoubleSpinBox()
            xInput.setMinimum(-10000)
            xInput.setMaximum(10000)
            self.formLayout.addWidget(xInput, i, 2)

            yLabel = QtWidgets.QLabel('Y')
            yLabel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.formLayout.addWidget(yLabel, i, 3)

            yInput = QtWidgets.QDoubleSpinBox()
            yInput.setMinimum(-10000)
            yInput.setMaximum(10000)
            self.formLayout.addWidget(yInput, i, 4)

            self.inputs.append({"x" : xInput, "y":yInput})
            i += 1

    def initButtons(self):
        rowButtons = QtWidgets.QHBoxLayout()
        addPointButton = QtWidgets.QPushButton('Adicionar Poligono')

        addPointButton.clicked.connect(lambda : self.onPolygonInserted.emit(self.getPoligono()))
        rowButtons.addWidget(addPointButton)

        self.formContainer.addLayout(rowButtons)
    
    def getPoligono(self):
        pontos = []
        for i in self.inputs:
            pontos.append(Ponto(i['x'].value(), i['y'].value()))

        return Poligono(pontos)

    def clearForm(self):
        self.inputs = []
        for index in reversed(range(self.formLayout.count())):
            widgetToRemove = self.formLayout.takeAt(index).widget()
            widgetToRemove.setParent(None)
