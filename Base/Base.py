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

        # points
        points = {
            1:[0,0,0], 
            2:[0,14.44,0], 
            3:[14.44,0,0], 
            4:[0,28.89,0], 
            5:[28.88,0,0], 
            6:[0,43.33,0], 
            7:[43.32,0,0], 
            8:[0,57.78,0], 
            9:[57.76,0,0], 
            10:[0,72.22,0], 
            11:[72.20,0,0], 
            12:[0,86.66,0], 
            13:[86.64,0,0], 
            14:[0,101.11,0],
            15:[101.08,0,0], 
            16:[0,115.55,0], 
            17:[115.52,0,0], 
            18:[0,130.00,0], 
            19:[129.96,0,0], 
            20:[32.50,32.50,0], 
            21:[16.25,113.75,0],
            22:[32.50,97.50,0], 
            23:[48.74,81.25,0], 
            24:[64.99,65.01], 
            25:[81.24,48.76,0], 
            26:[97.49,32.51,0], 
            27:[113.73,16.26,0], 
            28:[35.36,130.00,10.28],
            29:[59.34,115.91,10.28], 
            30:[68.54,96.82,10.28], 
            31:[87.63,87.63,15.28], 
            32:[96.82,68.54,15.28], 
            33:[115.91,59.34,15.28], 
            34:[130.00,35.36,15.28], 
            35:[65.87,129.99,36.62],
            36:[97.94,97.94,36.63], 
            37:[130.00,65.87,65.87], 
            38:[88.44,116.72,43.20], 
            39:[116.72,88.44,43.20], 
            40:[84.43,130.01,49.75], 
            41:[107.23,107.23,49.77], 
            42:[130.01,84.43,49.75],
            43:[101.89,130.00,56.35], 
            44:[130.00,101.89,56.35], 
            45:[120.18,120.18,56.35], 
            46:[118.81,130.00,56.35], 
            47:[130.00,118.81,56.35] 
        }
        self.colors = vtkNamedColors()

        self.filename = "AccuracyTestingJigMainBody.stl"

        self.reader = vtkSTLReader()
        self.reader.SetFileName(self.filename)

        self.mapper = vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.reader.GetOutputPort())

        self.targetSphere = vtk.vtkSphereSource()
        self.targetSphere.SetRadius(5.0)
        self.targetSphereMapper = vtk.vtkPolyDataMapper()
        self.targetSphereMapper.SetInputConnection(self.targetSphere.GetOutputPort())
        self.targetSphereActor = vtk.vtkActor()
        self.targetSphereActor.SetMapper(self.targetSphereMapper)
        self.targetSphereActor.GetProperty().SetColor(self.colors.GetColor3d("red"))
        # self.SetTargetSphereScale(3)
        # self.targetSphereActor.SetScale(0.1, 0.1, 0.1)
        self.targetSphereActor.SetPosition(points[44][0],points[44][1],points[44][2])

        self.phantom = vtkActor()
        self.phantom.SetMapper(self.mapper)
        self.phantom.GetProperty().SetDiffuse(0.8)
        self.phantom.GetProperty().SetDiffuseColor(self.colors.GetColor3d('LightSteelBlue'))
        self.phantom.GetProperty().SetSpecular(0.3)
        self.phantom.GetProperty().SetSpecularPower(60.0)
        self.phantom.SetPosition(0,0,0)
        # self.phantom.SetScale(1, 1, 1)

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
        self.probeActor.SetPosition(0,0,0)

        # self.SetProbePosition(90,90,90)
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