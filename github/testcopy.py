#!/usr/bin/env python
 
import sys
import vtk
from PyQt5 import QtCore, QtWidgets
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPlanes
from vtkmodules.vtkFiltersSources import vtkFrustumSource
from vtkmodules.vtkCommonColor import vtkNamedColors
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
    vtkCamera,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
from math import *

 
class MainWindow(QtWidgets.QMainWindow):

    def __getCameraFrustum(self, focalLength=8.3, pxHeight=1200, pxWidth=1920, nearZ=1000.0, farZ=2200.0, pixelToMetricScale=0.00586):
        camera = vtkCamera()
        width = pxWidth * pixelToMetricScale
        height = pxHeight * pixelToMetricScale
        viewAngle = 2*degrees(atan(height*0.5/focalLength))
        
        camera.SetParallelProjection(False)
        camera.SetClippingRange(nearZ, farZ)
        camera.SetPosition(0.0,0.0,0.0)
        camera.SetFocalPoint(0.0,0.0,focalLength)
        camera.SetUseExplicitAspectRatio(True)
        camera.SetExplicitAspectRatio(width/height)
        camera.SetViewAngle(viewAngle)
        camera.SetViewUp(0.0,-1.0,0.0)

        planesArray = [0] * 24
        camera.GetFrustumPlanes(1.0, planesArray)

        planes = vtkPlanes()
        planes.SetFrustumPlanes(planesArray)

        frustumSource = vtkFrustumSource()
        frustumSource.SetPlanes(planes)
        return frustumSource

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.setWindowTitle("Warning")
        
        width = 1024
        hieght = 600
        self.setFixedWidth(width)
        self.setFixedHeight(hieght)

        self.frame = QtWidgets.QFrame()
        self.setCentralWidget(self.frame)
        self.vl = QtWidgets.QHBoxLayout()
        self.frame.setLayout(self.vl)
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtkWidget)
 
        self.renTop = vtk.vtkRenderer()
        self.renFront = vtk.vtkRenderer()
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
        #self.iren.SetInteractorStyle(vtkInteractorStyleImage())

        self.colors = vtkNamedColors()

        self.frustumSource = self.__getCameraFrustum()
        self.frustumMapper = vtkPolyDataMapper()
        self.frustumMapper.SetInputConnection(self.frustumSource.GetOutputPort())
        self.frustumActor = vtkActor()
        self.frustumActor.SetMapper(self.frustumMapper)
        self.frustumActor.GetProperty().EdgeVisibilityOn()
        self.frustumActor.GetProperty().SetColor(self.colors.GetColor3d("green"))
        self.frustumActor.GetProperty().SetOpacity(0.3)

        self.targetSphere = vtk.vtkSphereSource()
        self.targetSphere.SetRadius(50.0)
        self.targetSphereMapper = vtk.vtkPolyDataMapper()
        self.targetSphereMapper.SetInputConnection(self.targetSphere.GetOutputPort())
        self.targetSphereActor = vtk.vtkActor()
        self.targetSphereActor.SetMapper(self.targetSphereMapper)
        self.targetSphereActor.GetProperty().SetColor(self.colors.GetColor3d("red"))

        self.colors = vtkNamedColors()

        self.filename = "holecube.stl"

        self.reader = vtkSTLReader()
        self.reader.SetFileName(self.filename)

        self.mapper = vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.reader.GetOutputPort())

        self.phantom = vtkActor()
        self.phantom.SetMapper(self.mapper)
        self.phantom.GetProperty().SetDiffuse(0.8)
        self.phantom.GetProperty().SetDiffuseColor(self.colors.GetColor3d('LightSteelBlue'))
        self.phantom.GetProperty().SetSpecular(0.3)
        self.phantom.GetProperty().SetSpecularPower(60.0)
        self.phantom.SetScale(1.0/200, 1.0/200, 1.0/200)
        
        self.renTop = vtkRenderer()
        self.renTop.AddActor(self.actor)
        self.renTop.AddActor(self.phantom)
        self.renTop.SetBackground(vtkNamedColors().GetColor3d("grey"))
        self.renTop.SetViewport(0.5, 0.0, 1.0, 1.0)
 
        self.renTop.AddActor(self.targetSphereActor)
        self.renTop.AddActor(self.frustumActor)
        self.renTop.SetBackground(vtkNamedColors().GetColor3d("grey"))
        self.renTop.SetViewport(0.5, 0.0, 1.0, 1.0)

        self.renFront.AddActor(self.frustumActor)
        self.renFront.SetBackground(vtkNamedColors().GetColor3d("grey"))
        self.renFront.SetViewport(0.0, 0.0, 0.5, 1.0)

        # Set the cameras far enough
        self.renTop.GetActiveCamera().SetParallelProjection(True)
        self.renTop.GetActiveCamera().SetPosition(0, 2*1200*0.00586*2200/8.3, 0.5*2200)
        self.renTop.GetActiveCamera().SetFocalPoint(0, 0, 0.5*2200)
        self.renTop.GetActiveCamera().SetViewUp(-1,0,0)
        #self.renTop.GetActiveCamera().SetWindowCenter(0.5,0)

        self.renFront.GetActiveCamera().SetParallelProjection(True)
        self.renFront.GetActiveCamera().SetPosition(0, 0, -10*2200)
        self.renFront.GetActiveCamera().SetFocalPoint(0, 0, 0)
        self.renFront.GetActiveCamera().SetViewUp(0,-1,0)
        #self.renFront.GetActiveCamera().SetFocalPoint(0, 0, 1)

        self.vtkWidget.GetRenderWindow().AddRenderer(self.renTop)
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renFront)
        self.vtkWidget.GetRenderWindow().Render()
        self.iren.Start()
        
        self.show()
 
if __name__ == "__main__":
 
    app = QtWidgets.QApplication(sys.argv)
 
    window = MainWindow()
 
    sys.exit(app.exec_())