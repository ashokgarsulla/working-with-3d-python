from Ui_Base import *
import vtk
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOGeometry import vtkSTLReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkCamera,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import sys

class BaseWindow(QMainWindow):

    def SetProbeVisibility(self,isVisible:bool):
        self.probeActor.SetVisibility(isVisible)

    def SetProbePosition(self,x=100,y=100,z=100):
        self.probeActor.SetPosition(x,y,z)

    def HighlightPhantomPoint(self,pointID:int,color:str):
        pass

    def RemoveHighlight(self,pointID):
        pass

    def RemoveAllHighlights(self):
        pass
    

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.vtkWidget = QVTKRenderWindowInteractor(self.ui.frame)
        self.vtkWidget.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding))
        self.vtkWidget.setMinimumSize(950,650)
        self.ren = vtk.vtkRenderer()
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        self.colors = vtkNamedColors()

        self.filename = "AccuracyTestingJigMainBody.stl"

        self.reader = vtkSTLReader()
        self.reader.SetFileName(self.filename)

        self.mapper = vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.reader.GetOutputPort())

        self.targetSphere = vtk.vtkSphereSource()
        self.targetSphere.SetRadius(50.0)
        self.targetSphereMapper = vtk.vtkPolyDataMapper()
        self.targetSphereMapper.SetInputConnection(self.targetSphere.GetOutputPort())
        self.targetSphereActor = vtk.vtkActor()
        self.targetSphereActor.SetMapper(self.targetSphereMapper)
        self.targetSphereActor.GetProperty().SetColor(self.colors.GetColor3d("red"))
        # self.SetTargetSphereScale(3)
        self.targetSphereActor.SetScale(0.1, 0.1, 0.1)
        self.targetSphereActor.SetPosition(22, 22, 22)

        self.phantom = vtkActor()
        self.phantom.SetMapper(self.mapper)
        self.phantom.GetProperty().SetDiffuse(0.8)
        self.phantom.GetProperty().SetDiffuseColor(self.colors.GetColor3d('LightSteelBlue'))
        self.phantom.GetProperty().SetSpecular(0.3)
        self.phantom.GetProperty().SetSpecularPower(60.0)
        self.phantom.SetScale(1, 1, 1)

        # Probe
        self.probefilename = "holecube.stl"

        self.probereader = vtkSTLReader()
        self.probereader.SetFileName(self.probefilename)

        self.probemapper = vtkPolyDataMapper()
        self.probemapper.SetInputConnection(self.probereader.GetOutputPort())

        self.probeActor = vtkActor()
        self.probeActor.SetMapper(self.probemapper)
        self.probeActor.GetProperty().SetDiffuse(0.8)
        self.probeActor.GetProperty().SetDiffuseColor(self.colors.GetColor3d('LightSteelBlue'))
        self.probeActor.GetProperty().SetSpecular(0.3)
        self.probeActor.GetProperty().SetSpecularPower(60.0)
        self.probeActor.SetScale(1.2, 1.2, 1.2)

        self.SetProbePosition(120,120,120)
        self.SetProbeVisibility(True)

        self.ren.AddActor(self.targetSphereActor)
        self.ren.AddActor(self.probeActor)
        self.ren.AddActor(self.phantom)

        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.vtkWidget.GetRenderWindow().Render()
        
        self.iren.Start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = BaseWindow()
    win.show()
    sys.exit(app.exec())

# SetProbeVisibility(isVisible:bool)
# SetProbePosition(position)
# HighlightPhantomPoint(pointID, color)
# RemoveHighlight(pointID)
# RemoveAllHighlights()