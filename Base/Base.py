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

    class Point():
        def __init__(self, position=[0.0,0.0,0.0], radius=5.0, color="red", visibility = False):
            self.__colors = vtkNamedColors()
            self.__sphereSource = vtk.vtkSphereSource()
            self.__sphereSource.SetRadius(radius)
            self.__sphereMapper = vtk.vtkPolyDataMapper()
            self.__sphereMapper.SetInputConnection(self.__sphereSource.GetOutputPort())
            self.__sphereActor = vtk.vtkActor()
            self.__sphereActor.SetMapper(self.__sphereMapper)
            self.__sphereActor.GetProperty().SetColor(self.__colors.GetColor3d(color))
            self.__sphereActor.SetVisibility(visibility)
            self.__sphereActor.SetPosition(position[0],position[1],position[2])

        def GetActor(self):
            return self.__sphereActor

        def Highlight(self, color:str):
            self.__sphereActor.SetVisibility(True)
            self.__sphereActor.GetProperty().SetColor(self.__colors.GetColor3d(color))
        
        def SetVisibility(self, isVisible:bool):
            self.__sphereActor.SetVisibility(isVisible)
        

    def SetProbeVisibility(self,isVisible:bool):
        self.probeActor.SetVisibility(isVisible)

    def SetProbePosition(self,x=100,y=100,z=100):
        self.probeActor.SetPosition(x,y,z)

    def HighlightPhantomPoint(self,pointID:int,color:str):
        self.points[pointID].Highlight(color)

    def SetPhantomPointVisibilityOff(self,pointID=None):
        if pointID is None:
            for pointID in self.points.keys():
                self.points[pointID].SetVisibility(False)
        else:
            self.points[pointID].SetVisibility(False)
    

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.vtkWidget = QVTKRenderWindowInteractor(self.ui.frame)
        self.vtkWidget.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding))
        self.vtkWidget.setMinimumSize(950,650)
        self.ren = vtk.vtkRenderer()
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        # points
        self.points = {
            1:self.Point([0,0,0]), 
            2:self.Point([0,14.44,0]), 
            3:self.Point([14.44,0,0]), 
            4:self.Point([0,28.89,0]), 
            5:self.Point([28.88,0,0]), 
            6:self.Point([0,43.33,0]), 
            7:self.Point([43.32,0,0]), 
            8:self.Point([0,57.78,0]), 
            9:self.Point([57.76,0,0]), 
            10:self.Point([0,72.22,0]), 
            11:self.Point([72.20,0,0]), 
            12:self.Point([0,86.66,0]), 
            13:self.Point([86.64,0,0]), 
            14:self.Point([0,101.11,0]),
            15:self.Point([101.08,0,0]), 
            16:self.Point([0,115.55,0]), 
            17:self.Point([115.52,0,0]), 
            18:self.Point([0,130.00,0]), 
            19:self.Point([129.96,0,0]), 
            20:self.Point([32.50,32.50,0]), 
            21:self.Point([16.25,113.75,0]),
            22:self.Point([32.50,97.50,0]), 
            23:self.Point([48.74,81.25,0]), 
            24:self.Point([64.99,65.01,0]), 
            25:self.Point([81.24,48.76,0]), 
            26:self.Point([97.49,32.51,0]), 
            27:self.Point([113.73,16.26,0]), 
            28:self.Point([35.36,130.00,10.28]),
            29:self.Point([59.34,115.91,10.28]), 
            30:self.Point([68.54,96.82,10.28]), 
            31:self.Point([87.63,87.63,15.28]), 
            32:self.Point([96.82,68.54,15.28]), 
            33:self.Point([115.91,59.34,15.28]), 
            34:self.Point([130.00,35.36,15.28]), 
            35:self.Point([65.87,129.99,36.62]),
            36:self.Point([97.94,97.94,36.63]), 
            37:self.Point([130.00,65.87,65.87]), 
            38:self.Point([88.44,116.72,43.20]), 
            39:self.Point([116.72,88.44,43.20]), 
            40:self.Point([84.43,130.01,49.75]), 
            41:self.Point([107.23,107.23,49.77]), 
            42:self.Point([130.01,84.43,49.75]),
            43:self.Point([101.89,130.00,56.35]), 
            44:self.Point([130.00,101.89,56.35]), 
            45:self.Point([120.18,120.18,56.35]), 
            46:self.Point([118.81,130.00,56.35]), 
            47:self.Point([130.00,118.81,56.35])
        }
        self.colors = vtkNamedColors()

        self.filename = "AccuracyTestingJigMainBody.stl"

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
        self.phantom.SetPosition(0,0,0)

        # Probe
        self.probefilename = "HandheldProbeStemLong.stl"

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
        self.probeActor.SetVisibility(False)

        self.ren.AddActor(self.probeActor)

        # self.SetProbePosition(90,90,90)
        self.ren.AddActor(self.phantom)

        for pointID in self.points:
            self.ren.AddActor(self.points[pointID].GetActor())

        self.points[1].Highlight("green")
        self.points[2].Highlight("green")
        self.points[3].Highlight("green")

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