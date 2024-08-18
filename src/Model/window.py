from enum import Enum

class WindowTransformations(Enum):
  MOVE_UP = 1
  MOVE_DOWN= 2
  MOVE_RIGHT = 3
  MOVE_LEFT = 4
  ROTATE_LEFT = 5
  ROTATE_RIGHT = 6
  ZOOM_IN = 7
  ZOOM_OUT = 8
  RESET = 9

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

    def apply_windows_transformation(self, type):
        if(type == WindowTransformations.MOVE_UP):
            self.translation_y(int(1))
        elif(type == WindowTransformations.MOVE_DOWN):
            self.translation_y(int(-1))
        elif(type == WindowTransformations.MOVE_RIGHT):
            self.translation_x(int(1))
        elif(type == WindowTransformations.MOVE_LEFT):
            self.translation_x(int(-1))

    def translation_x(self, value):
        self.xwmin -= int(value)
        self.xwmax -= int(value)
        print(self.xwmax)
    
    def translation_y(self, value):
        self.ywmin -= int(value)
        self.ywmax -= int(value)
