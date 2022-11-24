#!/usr/bin/env python
 
import sys
import vtk
from PyQt5 import QtCore, QtWidgets
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPyramid,
    vtkUnstructuredGrid
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOGeometry import vtkSTLReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

 
class MainWindow(QtWidgets.QMainWindow):
 
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
 
        self.frame = QtWidgets.QFrame()
 
        self.vl = QtWidgets.QVBoxLayout()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtkWidget)
 
        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
 
        # # Create source
        # source = vtk.vtkSphereSource()
        # source.SetCenter(0, 0, 0)
        # source.SetRadius(5.0)

        self.colors = vtkNamedColors()

        self.points = vtkPoints()

        self.p0 = [1.0, 1.0, 1.0]
        self.p1 = [-1.0, 1.0, 1.0]
        self.p2 = [-1.0, -1.0, 1.0]
        self.p3 = [1.0, -1.0, 1.0]
        self.p4 = [0.0, 0.0, 0.0]

        self.points.InsertNextPoint(self.p0)
        self.points.InsertNextPoint(self.p1)
        self.points.InsertNextPoint(self.p2)
        self.points.InsertNextPoint(self.p3)
        self.points.InsertNextPoint(self.p4)

        self.pyramid = vtkPyramid()
        self.pyramid.GetPointIds().SetId(0, 0)
        self.pyramid.GetPointIds().SetId(1, 1)
        self.pyramid.GetPointIds().SetId(2, 2)
        self.pyramid.GetPointIds().SetId(3, 3)
        self.pyramid.GetPointIds().SetId(4, 4)

        self.cells = vtkCellArray()
        self.cells.InsertNextCell(self.pyramid)

        self.ug = vtkUnstructuredGrid()
        self.ug.SetPoints(self.points)
        self.ug.InsertNextCell(self.pyramid.GetCellType(), self.pyramid.GetPointIds())

        # Create an actor and mapper
        self.mapper = vtkDataSetMapper()
        self.mapper.SetInputData(self.ug)
 
        # # Create a mapper
        # mapper = vtk.vtkPolyDataMapper()
        # mapper.SetInputConnection(source.GetOutputPort())
        
 
        # # Create an actor
        # actor = vtk.vtkActor()
        # actor.SetMapper(mapper)
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)
 
        # self.ren.AddActor(actor)
        self.ren.AddActor(self.actor)
 
        # self.ren.ResetCamera()
        self.ren.ResetCamera()
    
        self.actor.GetProperty().SetRepresentationToSurface()
        self.actor.GetProperty().EdgeVisibilityOn()
        self.actor.GetProperty().SetEdgeColor(255,0,0)
        self.actor.GetProperty().SetOpacity(0.5)



        self.frame.setLayout(self.vl)
        self.setCentralWidget(self.frame)
 
        self.show()
        self.iren.Initialize()


        
 
 
if __name__ == "__main__":
 
    app = QtWidgets.QApplication(sys.argv)
 
    window = MainWindow()
 
    sys.exit(app.exec_())