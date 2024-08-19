from enum import Enum
import copy
import math

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
    pontos = []
    retas = []
    poligonos = []
    rotation = 0

    def __init__(self,xwmin, ywmin, xwmax, ywmax): 
        self.xwmin = xwmin
        self.xwmax = xwmax
        self.ywmin = ywmin
        self.ywmax = ywmax

    def new_original_value(self):
        self.original_xwmin = copy.deepcopy(self.xwmin)
        self.original_xwmax = copy.deepcopy(self.xwmax)
        self.original_ywmin = copy.deepcopy(self.ywmin)
        self.original_ywmax = copy.deepcopy(self.ywmax)
        self.original_pontos = copy.deepcopy(self.pontos)
        self.original_retas = copy.deepcopy(self.retas)
        self.original_poligonos = copy.deepcopy(self.poligonos)

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
        elif(type == WindowTransformations.ROTATE_LEFT):
            self.apply_rotation(float(-10))
        elif(type == WindowTransformations.ROTATE_RIGHT):
            self.apply_rotation(float(10))
        elif(type == WindowTransformations.ZOOM_IN):
            self.apply_zoom(int(10))
        elif(type == WindowTransformations.ZOOM_OUT):
            self.apply_zoom(int(-10))
        elif(type == WindowTransformations.RESET):
            self.reset_window()

    def reset_window(self):
        self.xwmin = copy.deepcopy(self.original_xwmin)
        self.xwmax = copy.deepcopy(self.original_xwmax)
        self.ywmin = copy.deepcopy(self.original_ywmin)
        self.ywmax = copy.deepcopy(self.original_ywmax)
        self.pontos = copy.deepcopy(self.original_pontos)
        self.retas = copy.deepcopy(self.original_retas)
        self.poligonos = copy.deepcopy(self.original_poligonos)
        self.rotation = 0
        self.apply_rotation(self.rotation)

    def apply_zoom(self, zoom_percentage):
        self.xwmax -= self.xwmax * zoom_percentage / 100
        self.ywmax -= self.ywmax * zoom_percentage / 100

    def translation_x(self, value):
        self.xwmin -= int(value)
        self.xwmax -= int(value)
        print(self.xwmax)
    
    def translation_y(self, value):
        self.ywmin -= int(value)
        self.ywmax -= int(value)

    def apply_rotation(self, degrees):
        self.rotation += degrees

        for p in self.pontos:
            self.calculate_rotation(p,degrees)
        
        for r in self.retas:
            self.calculate_rotation(r.ponto1,degrees)
            self.calculate_rotation(r.ponto2,degrees)

        for pl in self.poligonos:
            for p in pl.pontos:
                self.calculate_rotation(p,degrees)

    def calculate_rotation(self,ponto,degrees):

        radius = math.radians(degrees)
        rotation_cos = math.cos(radius)
        rotation_sin = math.sin(radius)

        ponto.x = ponto.x * rotation_cos - ponto.y * rotation_sin
        ponto.y = ponto.x * rotation_sin + ponto.y * rotation_cos

        print(ponto.x)
        print(ponto.y)