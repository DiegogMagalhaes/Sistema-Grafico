class Window():
    xwmin = 0
    xwmax = 0
    ywmin = 0
    ywmax = 0
    pontos = []
    retas = []
    poligonos = []

    def __init__(self,xwmin, ywmin, xwmax, ywmax): 
        self.xwmin = xwmin
        self.xwmax = xwmax
        self.ywmin = ywmin
        self.ywmax = ywmax

    def getX_Y(self):
        x = self.xwmax - self.xwmin
        y = self.ywmax - self.ywmin
        return x,y
    