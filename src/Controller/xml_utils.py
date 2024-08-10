
import re
import xml.etree.ElementTree as ET
from Model.window import Window
from Model.viewport import Viewport
from Model.ponto import Ponto
from Model.reta import Reta
from Model.poligono import Poligono

RESOURCES_PATH = "resources/"

def xmt_to_window_viewport(entrada):
    tree = ET.parse(RESOURCES_PATH + entrada)
    root = tree.getroot()

    viewport:Viewport = Viewport(0,0,0,0)
    window:Window = Window(0,0,0,0)

    e = root[0][1].text

    for child in root:
        if(child.tag == 'viewport'):
            for c in child:
                if(c.tag == 'vpmin'):
                    result = re.findall(r'\d+', str(c.attrib))
                    viewport.xvpmin = result[0]
                    viewport.yvpmin = result[1]
                elif(c.tag == 'vpmax'):
                    result = re.findall(r'\d+', str(c.attrib))
                    viewport.xvpmax = result[0]
                    viewport.yvpmax = result[1]
        
        elif(child.tag == 'window'):
            for c in child:
                if(c.tag == 'wmin'):
                    result = re.findall(r'\d+', str(c.attrib))
                    window.xwmin = result[0]
                    window.ywmin = result[2]
                elif(c.tag == 'wmax'):
                    result = re.findall(r'\d+', str(c.attrib))
                    window.xwmax = result[0]
                    window.ywmax = result[2]
        
        elif(child.tag == 'ponto'):
            result = re.findall(r'\d+', str(child.attrib))
            window.pontos.append(Ponto(result[0],result[1]))
        
        elif(child.tag == 'reta'):
            pontos_reta = []
            for c in child:
                result = re.findall(r'\d+', str(c.attrib))
                pontos_reta.append(Ponto(result[0],result[1]))
            
            window.retas.append(Reta(pontos_reta[0], pontos_reta[1]))
        
        elif(child.tag == 'poligono'):
            pontos_poligono = []
            for c in child:
                result = re.findall(r'\d+', str(c.attrib))
                pontos_poligono.append(Ponto(result[0],result[2]))
            window.poligonos.append(Poligono(pontos_poligono))


    for pl in window.poligonos:
        for p in pl.pontos:
            print("x = {}, y = {}".format(p.x,p.y))

    return window, viewport

def window_viewport_to_xml(nome,window, viewport):
    a = open(RESOURCES_PATH + nome, "w")
    a.write("<?xml version=\"1.0\" ?>\n")
    a.write("<dados>\n\n")
    for p in window.pontos:
        a.write("   <ponto x = \"{}\" y=\"{}\" />\n".format(p.x,p.y))
    
    a.write("\n   <reta>\n")
    for r in window.retas:
        a.write("       <ponto x = \"{}\" y=\"{}\" />\n".format(r.ponto1.x,r.ponto1.y))
        a.write("       <ponto x = \"{}\" y=\"{}\" />\n".format(r.ponto2.x,r.ponto2.y))
    a.write("   </reta>\n")

    a.write("\n   <poligono>\n")
    for pl in window.poligonos:
        for p in pl.pontos:
            a.write("       <ponto x = \"{}\" y=\"{}\" />\n".format(p.x,p.y))
    a.write("   </poligono>\n")
    a.write("\n</dados>\n")