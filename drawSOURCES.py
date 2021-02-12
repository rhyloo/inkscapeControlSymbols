#!/usr/bin/python

import numpy as np

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw


class SOURCES(inkBase.inkscapeMadeEasy):
    def add(self, vector, delta):
        # nector does not need to be numpy array. delta will be converted to numpy array. Numpy can then deal with np.array + list
        return vector + np.array(delta)

    # ---------------------------------------------
    def drawConstant(self, parent, position=[0, 0],
                     value='0',label='Constant Source', text_color='black',block_color='black'):

        group = self.createGroup(parent, label)
        elem = self.createGroup(group, label='Text')
        line_style= inkDraw.lineStyle.set(lineColor=block_color)
        if value == "none":
            value = '0'
        pos_text = self.add(position, [0,0])
        if inkDraw.useLatex:
                value = '$' + value + '$'

        groupLatex, BboxMin, BboxMax = inkDraw.text.latex(self, elem,value, pos_text, fontSize=self.fontSize,refPoint='bc',textColor = text_color, preambleFile=self.preambleFile)

        center_group = inkBase.inkscapeMadeEasy.getCenter(self,groupLatex);
        off = 10

        box = inkDraw.line.absCoords(group, [[0,0], [BboxMax[0]-BboxMin[0]+off, 0], [BboxMax[0]-BboxMin[0]+off, -1*(BboxMax[1]-BboxMin[1])-off],[0,-1*(BboxMax[1]-BboxMin[1])-off],[0,0]], self.add(position, [0, 0]),lineStyle=line_style)

        center_box = inkBase.inkscapeMadeEasy.getCenter(self,box);

        inkBase.inkscapeMadeEasy.moveElement(self,box,[-1*(center_box[0]-center_group[0]),-1*(center_box[1]-center_group[1])])

        return group

    def drawStep(self, parent, position=[0,0],value='1',label='Step Source',text_color='black',block_color='black',text_refPoint="up"):

        group = self.createGroup(parent, label)
        elem = self.createGroup(group,label = 'text')
        line_style= inkDraw.lineStyle.set(lineColor=block_color)
        
        pos_text = self.add(position, [0,0])
        
        if inkDraw.useLatex and value != "none":
            value = '$'+ '\\' + 'text{Amplitud: }'+ value + '$'
            
        groupLatex, BboxMin, BboxMax = inkDraw.text.latex(self, elem,value, pos_text, fontSize=self.fontSize,refPoint='tc',textColor = text_color, preambleFile=self.preambleFile)

        center_group = inkBase.inkscapeMadeEasy.getCenter(self,groupLatex);
        off = 15

        box = inkDraw.line.absCoords(group, [[0,0],[20,0],[20,-20],[0,-20],[0,0]], self.add(position, [0, 0]),lineStyle=line_style)
        step = inkDraw.line.absCoords(group, [[2,-4],[9,-4],[9,-16],[18,-16]], self.add(position, [0, 0]),lineStyle=line_style)
        center_box = inkBase.inkscapeMadeEasy.getCenter(self,box)

        if value == "none":
            inkBase.inkscapeMadeEasy.removeElement(self,groupLatex)

        if text_refPoint == "up":
            inkBase.inkscapeMadeEasy.moveElement(self,box,[-1*(center_box[0]-center_group[0]),-1*(center_box[1]-center_group[1])+off])
            inkBase.inkscapeMadeEasy.moveElement(self,step,[-1*(center_box[0]-center_group[0]),-1*(center_box[1]-center_group[1])+off])
        elif text_refPoint == "down":
            inkBase.inkscapeMadeEasy.moveElement(self,box,[-1*(center_box[0]-center_group[0]),-1*(center_box[1]-center_group[1])-off])
            inkBase.inkscapeMadeEasy.moveElement(self,step,[-1*(center_box[0]-center_group[0]),-1*(center_box[1]-center_group[1])-off])
        elif text_refPoint == "left":
            pass
        elif text_refPoint == "right":
            inkBase.inkscapeMadeEasy.moveElement(self,box,[-1*(center_box[0]-center_group[0])-(2.25*off),-1*(center_box[1]-center_group[1])])
            inkBase.inkscapeMadeEasy.moveElement(self,step,[-1*(center_box[0]-center_group[0])-(2.25*off),-1*(center_box[1]-center_group[1])])
        return group


