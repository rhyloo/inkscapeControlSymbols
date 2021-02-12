#!/usr/bin/python

import numpy as np

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw


class BLOCKS(inkBase.inkscapeMadeEasy):
    def add(self, vector, delta):
        # nector does not need to be numpy array. delta will be converted to numpy array. Numpy can then deal with np.array + list
        return vector + np.array(delta)

    # ---------------------------------------------
    def drawTransFcn(self, parent, position=[0, 0],
                     value='H(s)',label='Transfer function', text_color='black',block_color='black'):

        group = self.createGroup(parent, label)
        elem = self.createGroup(group, label='Text')
        line_style= inkDraw.lineStyle.set(lineColor=block_color)
        
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

    def drawIntegrator(self, parent, position=[0, 0],
                     value='$\dfrac{1}{s}$',label='Continuous integrator', text_color='black',block_color='black'):
        group = self.createGroup(parent, label)
        elem = self.createGroup(group, label='Text')
        line_style= inkDraw.lineStyle.set(lineColor=block_color)
        
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

    def drawDerivative(self, parent, position=[0, 0],
                     value='$\frac{\Delta u}{\Delta t}$',label='Derivative', text_color='black',block_color='black'):
        group = self.createGroup(parent, label)
        elem = self.createGroup(group, label='Text')
        line_style= inkDraw.lineStyle.set(lineColor=block_color)
        
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

    def drawSpacestate(self, parent, position=[0, 0],
                     value='test',label='Space State', text_color='black',block_color='black'):
        group = self.createGroup(parent, label)
        elem = self.createGroup(group, label='Text')
        line_style= inkDraw.lineStyle.set(lineColor=block_color)

        value = '\genfrac ..{0pt}{2}{\dot{x} = Ax+By}{y = Cx+Du}'
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
    
    # root_layer = self.document.getroot()     # retrieves the root layer of the document
    # mySimpleStyle = inkDraw.textStyle.setSimpleBlack(fontSize=20,justification='center')  # creates a simple text style.
    # myText='foo bar who-hoo!\\nsecond line!'
    # inkDraw.text.write(self, text=myText, coords=[5.0,6.0], parent=root_layer, textStyle=mySimpleStyle, fontSize=None, justification=None, angleDeg=0.0)
    # inkDraw.line.absCoords(elem, [[-20, 0], [0, -25], [20, 0],[-20,0]], self.add(position, [0, 0]))
    # inkDraw.line.absCoords(elem, [[-25, 0], [25,0]], self.add(position, [0, 0.25]))

    # inkDraw.line.relCoords(elem, [[-(15.5 + wireExtraSize), 0]], self.add(position, [-9.5, 0]))
    # inkDraw.line.relCoords(elem, [[19, 0], [0, -6], [-19, 0], [0, 6]], self.add(position, [-9.5, 3]))
    # inkDraw.line.relCoords(elem, [[15.5 + wireExtraSize, 0]], self.add(position, [9.5, 0]))
