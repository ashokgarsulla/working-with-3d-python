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
        self.setCentralWidget(self.frame)
        self.vl = QtWidgets.QHBoxLayout()
        self.frame.setLayout(self.vl)
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtkWidget)
 
        self.renTop = vtk.vtkRenderer()
        self.renFront = vtk.vtkRenderer()
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
        self.iren.SetInteractorStyle(vtkInteractorStyleImage())

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
 
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)
        self.actor.GetProperty().SetRepresentationToSurface()
        self.actor.GetProperty().EdgeVisibilityOn()
        self.actor.GetProperty().SetEdgeColor(255,0,0)
        self.actor.GetProperty().SetOpacity(0.5)
 
        self.renTop.AddActor(self.actor)
        self.renTop.SetBackground(vtkNamedColors().GetColor3d("red"))
        self.renTop.SetViewport(0.5, 0.0, 1.0, 1.0)

        self.renFront.AddActor(self.actor)
        self.renFront.SetBackground(vtkNamedColors().GetColor3d("grey"))
        self.renFront.SetViewport(0.0, 0.0, 0.5, 1.0)

        # Set the cameras far enough
        self.renTop.GetActiveCamera().SetPosition(0, 10, 0.5)
        self.renTop.GetActiveCamera().SetParallelProjection(True)
        self.renTop.GetActiveCamera().SetFocalPoint(0,0,0.5)
        self.renTop.GetActiveCamera().SetViewUp(1,0,0)

        self.renFront.GetActiveCamera().SetPosition(0, 0, -10)
        self.renFront.GetActiveCamera().SetParallelProjection(True)
        self.renFront.GetActiveCamera().SetFocalPoint(0,0,0)
        self.renFront.GetActiveCamera().SetViewUp(0,1,0)



        self.vtkWidget.GetRenderWindow().AddRenderer(self.renTop)
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renFront)
        self.vtkWidget.GetRenderWindow().Render()
        self.iren.Start()
        
        self.show()


        
 
 
if __name__ == "__main__":
 
    app = QtWidgets.QApplication(sys.argv)
 
    window = MainWindow()
 
    sys.exit(app.exec_())