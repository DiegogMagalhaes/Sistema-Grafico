from Model.window import Window

class Viewport:

    xvpmin = 0
    xvpmax = 0
    yvpmin = 0
    yvpmax = 0
    margem = 10
        
    def __init__(self,xvpmin, yvpmin, xvpmax, yvpmax):
        self.xvpmin = xvpmin - self.margem
        self.xvpmax = xvpmax + self.margem
        self.yvpmin = yvpmin - self.margem
        self.yvpmax = yvpmax + self.margem
    
    def getX_Y(self):
        x = self.xvpmax - self.xvpmin
        y = self.yvpmax - self.yvpmin
        return x,y
    
    def calcularTransformacaoCoordenadas(self, window:Window, x, y):
        x = (float(x) - float(window.xwmin)) / (float(window.xwmax) - float(window.xwmin))
        x = float(x) * (float(self.xvpmax)-float(self.xvpmin))

        y = (float(y) - float(window.ywmin)) / (float(window.ywmax) - float(window.ywmin))
        y = 1 - float(y)
        y = float(y) * (float(self.yvpmax) - float(self.yvpmin))
        
        return int(x),int(y)

    def transformarCoordenadas(self, window: Window):
        self.transformarCoordenadasPonto(window.pontos, window)
        self.transformarCoordenadasRetas(window.retas, window)
        self.transformarCoordenadasPoligonos(window.poligonos, window)

    def transformarCoordenadasPonto(self,pontos, window: Window):
        for p in pontos :
            p.x, p.y = self.calcularTransformacaoCoordenadas(window,p.x,p.y)
    
    def transformarCoordenadasRetas(self, retas, window: Window):
        for r in retas :
            pontos = [r.ponto1, r.ponto2]
            self.transformarCoordenadasPonto(pontos,window)

    def transformarCoordenadasPoligonos(self,poligonos, window: Window):
        for pl in poligonos :
            self.transformarCoordenadasPonto(pl.pontos,window)
