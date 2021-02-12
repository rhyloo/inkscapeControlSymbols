#!/usr/bin/python

import math
import os

from drawBLOCKS import BLOCKS
from drawSOURCES import SOURCES

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw


# ---------------------------------------------
class ControlSymbols(BLOCKS,SOURCES):
    def __init__(self):
        
        #Define los parámetros de la imagen o al menos eso es lo que
        #creo ya que es una función init que luego se reparte.
        inkBase.inkscapeMadeEasy.__init__(self)
        
        #esto conecta con la interfaz de usuario de inkscape además si
        #en la consola de comando hacemos un python circuit... -h
        #salen todos los arugmentos posible, es necesario definirlo,
        #no olvidemos que luego se guarda en un varible options
        #inicializadas algo que no entiendo xdd

        #dest - El nombre del atributo que será añadido al objeto
        #retornado por parse_args().
        # arg_parser es el nombre del objeto creado en inkex
        self.arg_parser.add_argument("--tab", type=str, dest="tab", default="object")
        self.arg_parser.add_argument("--blocksCONTINUOUS", type=str, dest="blocksCONTINUOUS", default='transfcn')
        self.arg_parser.add_argument("--blockCONTINUOUSVal", type=str,dest="blockCONTINUOUSVal", default='H(s)')
        self.arg_parser.add_argument("--blockTEXTColor", type=str,dest="blockTEXTColor", default='black')
        self.arg_parser.add_argument("--blockBLOCKColor", type=str,dest="blockBLOCKColor", default='black')
        self.arg_parser.add_argument("--source", type=str, dest="source", default='step')
        self.arg_parser.add_argument("--sourceVal", type=str,dest="sourceVal", default='none')
        self.arg_parser.add_argument("--sourceTEXTColor", type=str,dest="sourceTEXTColor", default='black')
        self.arg_parser.add_argument("--sourceBLOCKColor", type=str,dest="sourceBLOCKColor", default='black')
        self.arg_parser.add_argument("--sourceREFPoint", type=str,dest="sourceREFPoint", default='up')
    def effect(self):

        #Guarda los valores que se configuran en inkscape, hay un
        #cuello de botella y es que por cada configuración guarda los
        #valores que cuando no se muestra ningún mensaje no va lento
        #pero es verdad que si estoy imprimiendo un condensador para
        #qué quiero una resistencia posible mejora a implementar

        # llama options a los valores añadidos, options se define en inkex
        so = self.options
        #inkDraw.displayMsg(str(so))
        #Indica en qué ventana estoy de la barra de arriba cosa
        #curiosa 
        
        so.tab = so.tab.replace('"', '')  # removes de exceeding double quotes from the string

        
        # latex related preamble (ruta completa del archivo)
        self.preambleFile = os.getcwd() + '/' + 'circuitSymbolsPreamble.tex'

        #inkDraw.displayMsg(str(self.preambleFile))

        #genera un svg (supongo que está relacionado con el svg del
        #__init___ inkscapeMadeEasy)
        root_layer = self.document.getroot()

        
        # text size and font style
        self.fontSize = 5
        self.fontSizeSmall = 4

        self.textOffset = self.fontSize / 1.5  # offset between symbol and text
        self.textOffsetSmall = self.fontSizeSmall / 2  # offset between symbol and text
        # Estilo de texto, que se modifica mediante inkdraw base de inkex
        self.textStyle = inkDraw.textStyle.setSimpleBlack(self.fontSize, justification='center')
        self.textStyleSmall = inkDraw.textStyle.setSimpleBlack(self.fontSizeSmall, justification='center')

        
        # sets the position to the viewport center, round to next 10.
        position = [self.svg.namedview.center[0], self.svg.namedview.center[1]]
        position[0] = int(math.ceil(position[0] / 10.0)) * 10
        position[1] = int(math.ceil(position[1] / 10.0)) * 10


        # ---------------------------
        # BLOCKS
        # ---------------------------
        if so.tab == 'BLOCKS':
            if so.blocksCONTINUOUS == "transfcn":
                self.drawTransFcn(root_layer, position, value=so.blockCONTINUOUSVal,text_color=so.blockTEXTColor,block_color=so.blockBLOCKColor)

            if so.blocksCONTINUOUS == "integrator":
                self.drawIntegrator(root_layer, position,text_color=so.blockTEXTColor,block_color=so.blockBLOCKColor)

            if so.blocksCONTINUOUS == "derivative":
                self.drawDerivative(root_layer, position,text_color=so.blockTEXTColor,block_color=so.blockBLOCKColor)

            if so.blocksCONTINUOUS == "spacestate":
                self.drawSpacestate(root_layer, position,text_color=so.blockTEXTColor,block_color=so.blockBLOCKColor)


        # ---------------------------
        # SOURCES
        # ---------------------------
        if so.tab == 'SOURCES':
            if so.source == "constant":
                self.drawConstant(root_layer, position, value=so.sourceVal,text_color=so.sourceTEXTColor,block_color=so.sourceBLOCKColor)
            if so.source == "step":
                self.drawStep(root_layer, position, value=so.sourceVal,text_color=so.sourceTEXTColor,block_color=so.sourceBLOCKColor,text_refPoint=so.sourceREFPoint)
            if so.source == "ramp":
                self.drawRamp(root_layer, position, value=so.sourceVal,text_color=so.sourceTEXTColor,block_color=so.sourceBLOCKColor)
            if so.source == "impulse":
                self.drawImpulse(root_layer, position, value=so.sourceVal,text_color=so.sourceTEXTColor,block_color=so.sourceBLOCKColor)
                

                
if __name__ == '__main__':
    control = ControlSymbols()
    control.run()
