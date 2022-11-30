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
        if pointID == 1:
            self.p1Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p1Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 2:
            self.p2Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p2Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
            self.p2Actor.SetVisibility(True)
        elif pointID == 3:
            self.p3Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p3Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 4:
            self.p4Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p4Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 5:
            self.p5Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p5Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 5:
            self.p5Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p5Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 6:
            self.p6Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p6Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 7:
            self.p7Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p7Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 8:
            self.p8Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p8Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 9:
            self.p9Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p9Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 10:
            self.p10Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p10Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 11:
            self.p11Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p11Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 12:
            self.p12Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p12Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 13:
            self.p13Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p13Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 14:
            self.p14Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p14Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 15:
            self.p15Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p15Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 16:
            self.p16Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p16Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 17:
            self.p17Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p17Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 18:
            self.p18Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p18Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 19:
            self.p19Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p19Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 20:
            self.p20Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p20Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 21:
            self.p21Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p21Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 22:
            self.p22Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p22Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 23:
            self.p23Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p23Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 24:
            self.p24Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p24Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 25:
            self.p25Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p25Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 26:
            self.p26Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p26Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 27:
            self.p27Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p27Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 28:
            self.p28Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p28Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 29:
            self.p29Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p29Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 30:
            self.p30Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p30Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 31:
            self.p31Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p31Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 32:
            self.p32Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p32Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 33:
            self.p33Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p33Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 34:
            self.p34Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p34Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 35:
            self.p35Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p35Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 36:
            self.p36Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p36Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 37:
            self.p37Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p37Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 38:
            self.p38Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p38Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 39:
            self.p39Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p39Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 40:
            self.p40Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p40Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 41:
            self.p41Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p41Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 42:
            self.p42Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p42Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 43:
            self.p43Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p43Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 44:
            self.p44Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p44Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 45:
            self.p45Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p45Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 46:
            self.p46Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p46Actor.GetProperty().SetColor(self.colors.GetColor3d(color))
        elif pointID == 47:
            self.p47Actor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
            self.p47Actor.GetProperty().SetColor(self.colors.GetColor3d(color))


    def RemoveHighlight(self,pointID):
        self.targetSphereActor.SetPosition(self.points[pointID][0],self.points[pointID][1],self.points[pointID][2])
        self.targetSphereActor.SetVisibility(False)
    
    def RemoveAllHighlights(self):
        self.targetSphereActor.SetVisibility(False)
        self.p2Actor.SetVisibility(False)
        self.p3Actor.SetVisibility(False)
        self.p4Actor.SetVisibility(False)
        self.p5Actor.SetVisibility(False)
        self.p6Actor.SetVisibility(False)
    

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
            24:[64.99,65.01,0], 
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
        self.targetSphereActor.SetPosition(self.points[1][0],self.points[1][1],self.points[1][2])

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

        # self.SetProbePosition(90,90,90)
        self.SetProbeVisibility(True)

        
        self.p1 = vtk.vtkSphereSource()
        self.p1.SetRadius(5.0)
        self.p1Mapper = vtk.vtkPolyDataMapper()
        self.p1Mapper.SetInputConnection(self.p1.GetOutputPort())
        self.p1Actor = vtk.vtkActor()
        self.p1Actor.SetMapper(self.p1Mapper)

        self.p2 = vtk.vtkSphereSource()
        self.p2.SetRadius(5.0)
        self.p2Mapper = vtk.vtkPolyDataMapper()
        self.p2Mapper.SetInputConnection(self.p2.GetOutputPort())
        self.p2Actor = vtk.vtkActor()
        self.p2Actor.SetMapper(self.p2Mapper)
        # self.p2Actor.SetVisibility(True)
        
        self.p3 = vtk.vtkSphereSource()
        self.p3.SetRadius(5.0)
        self.p3Mapper = vtk.vtkPolyDataMapper()
        self.p3Mapper.SetInputConnection(self.p3.GetOutputPort())
        self.p3Actor = vtk.vtkActor()
        self.p3Actor.SetMapper(self.p3Mapper)

        self.p4 = vtk.vtkSphereSource()
        self.p4.SetRadius(5.0)
        self.p4Mapper = vtk.vtkPolyDataMapper()
        self.p4Mapper.SetInputConnection(self.p4.GetOutputPort())
        self.p4Actor = vtk.vtkActor()
        self.p4Actor.SetMapper(self.p4Mapper)
        
        self.p5 = vtk.vtkSphereSource()
        self.p5.SetRadius(5.0)
        self.p5Mapper = vtk.vtkPolyDataMapper()
        self.p5Mapper.SetInputConnection(self.p5.GetOutputPort())
        self.p5Actor = vtk.vtkActor()
        self.p5Actor.SetMapper(self.p5Mapper)

        self.p6 = vtk.vtkSphereSource()
        self.p6.SetRadius(5.0)
        self.p6Mapper = vtk.vtkPolyDataMapper()
        self.p6Mapper.SetInputConnection(self.p6.GetOutputPort())
        self.p6Actor = vtk.vtkActor()
        self.p6Actor.SetMapper(self.p6Mapper)
        
        self.p7 = vtk.vtkSphereSource()
        self.p7.SetRadius(5.0)
        self.p7Mapper = vtk.vtkPolyDataMapper()
        self.p7Mapper.SetInputConnection(self.p7.GetOutputPort())
        self.p7Actor = vtk.vtkActor()
        self.p7Actor.SetMapper(self.p7Mapper)

        self.p8 = vtk.vtkSphereSource()
        self.p8.SetRadius(5.0)
        self.p8Mapper = vtk.vtkPolyDataMapper()
        self.p8Mapper.SetInputConnection(self.p8.GetOutputPort())
        self.p8Actor = vtk.vtkActor()
        self.p8Actor.SetMapper(self.p8Mapper)

        self.p9 = vtk.vtkSphereSource()
        self.p9.SetRadius(5.0)
        self.p9Mapper = vtk.vtkPolyDataMapper()
        self.p9Mapper.SetInputConnection(self.p9.GetOutputPort())
        self.p9Actor = vtk.vtkActor()
        self.p9Actor.SetMapper(self.p9Mapper)

        self.p10 = vtk.vtkSphereSource()
        self.p10.SetRadius(5.0)
        self.p10Mapper = vtk.vtkPolyDataMapper()
        self.p10Mapper.SetInputConnection(self.p10.GetOutputPort())
        self.p10Actor = vtk.vtkActor()
        self.p10Actor.SetMapper(self.p10Mapper)

        self.p11 = vtk.vtkSphereSource()
        self.p11.SetRadius(5.0)
        self.p11Mapper = vtk.vtkPolyDataMapper()
        self.p11Mapper.SetInputConnection(self.p11.GetOutputPort())
        self.p11Actor = vtk.vtkActor()
        self.p11Actor.SetMapper(self.p11Mapper)

        self.p12 = vtk.vtkSphereSource()
        self.p12.SetRadius(5.0)
        self.p12Mapper = vtk.vtkPolyDataMapper()
        self.p12Mapper.SetInputConnection(self.p12.GetOutputPort())
        self.p12Actor = vtk.vtkActor()
        self.p12Actor.SetMapper(self.p12Mapper)

        self.p13 = vtk.vtkSphereSource()
        self.p13.SetRadius(5.0)
        self.p13Mapper = vtk.vtkPolyDataMapper()
        self.p13Mapper.SetInputConnection(self.p13.GetOutputPort())
        self.p13Actor = vtk.vtkActor()
        self.p13Actor.SetMapper(self.p13Mapper)

        self.p14 = vtk.vtkSphereSource()
        self.p14.SetRadius(5.0)
        self.p14Mapper = vtk.vtkPolyDataMapper()
        self.p14Mapper.SetInputConnection(self.p14.GetOutputPort())
        self.p14Actor = vtk.vtkActor()
        self.p14Actor.SetMapper(self.p14Mapper)

        self.p15 = vtk.vtkSphereSource()
        self.p15.SetRadius(5.0)
        self.p15Mapper = vtk.vtkPolyDataMapper()
        self.p15Mapper.SetInputConnection(self.p15.GetOutputPort())
        self.p15Actor = vtk.vtkActor()
        self.p15Actor.SetMapper(self.p15Mapper)

        self.p16 = vtk.vtkSphereSource()
        self.p16.SetRadius(5.0)
        self.p16Mapper = vtk.vtkPolyDataMapper()
        self.p16Mapper.SetInputConnection(self.p16.GetOutputPort())
        self.p16Actor = vtk.vtkActor()
        self.p16Actor.SetMapper(self.p16Mapper)

        self.p17 = vtk.vtkSphereSource()
        self.p17.SetRadius(5.0)
        self.p17Mapper = vtk.vtkPolyDataMapper()
        self.p17Mapper.SetInputConnection(self.p17.GetOutputPort())
        self.p17Actor = vtk.vtkActor()
        self.p17Actor.SetMapper(self.p17Mapper)

        self.p18 = vtk.vtkSphereSource()
        self.p18.SetRadius(5.0)
        self.p18Mapper = vtk.vtkPolyDataMapper()
        self.p18Mapper.SetInputConnection(self.p18.GetOutputPort())
        self.p18Actor = vtk.vtkActor()
        self.p18Actor.SetMapper(self.p18Mapper)

        self.p19 = vtk.vtkSphereSource()
        self.p19.SetRadius(5.0)
        self.p19Mapper = vtk.vtkPolyDataMapper()
        self.p19Mapper.SetInputConnection(self.p19.GetOutputPort())
        self.p19Actor = vtk.vtkActor()
        self.p19Actor.SetMapper(self.p19Mapper)

        self.p20 = vtk.vtkSphereSource()
        self.p20.SetRadius(5.0)
        self.p20Mapper = vtk.vtkPolyDataMapper()
        self.p20Mapper.SetInputConnection(self.p20.GetOutputPort())
        self.p20Actor = vtk.vtkActor()
        self.p20Actor.SetMapper(self.p20Mapper)

        self.p21 = vtk.vtkSphereSource()
        self.p21.SetRadius(5.0)
        self.p21Mapper = vtk.vtkPolyDataMapper()
        self.p21Mapper.SetInputConnection(self.p21.GetOutputPort())
        self.p21Actor = vtk.vtkActor()
        self.p21Actor.SetMapper(self.p21Mapper)

        self.p22 = vtk.vtkSphereSource()
        self.p22.SetRadius(5.0)
        self.p22Mapper = vtk.vtkPolyDataMapper()
        self.p22Mapper.SetInputConnection(self.p22.GetOutputPort())
        self.p22Actor = vtk.vtkActor()
        self.p22Actor.SetMapper(self.p22Mapper)

        self.p23 = vtk.vtkSphereSource()
        self.p23.SetRadius(5.0)
        self.p23Mapper = vtk.vtkPolyDataMapper()
        self.p23Mapper.SetInputConnection(self.p23.GetOutputPort())
        self.p23Actor = vtk.vtkActor()
        self.p23Actor.SetMapper(self.p23Mapper)

        self.p24 = vtk.vtkSphereSource()
        self.p24.SetRadius(5.0)
        self.p24Mapper = vtk.vtkPolyDataMapper()
        self.p24Mapper.SetInputConnection(self.p24.GetOutputPort())
        self.p24Actor = vtk.vtkActor()
        self.p24Actor.SetMapper(self.p24Mapper)

        self.p25 = vtk.vtkSphereSource()
        self.p25.SetRadius(5.0)
        self.p25Mapper = vtk.vtkPolyDataMapper()
        self.p25Mapper.SetInputConnection(self.p25.GetOutputPort())
        self.p25Actor = vtk.vtkActor()
        self.p25Actor.SetMapper(self.p25Mapper)

        self.p26 = vtk.vtkSphereSource()
        self.p26.SetRadius(5.0)
        self.p26Mapper = vtk.vtkPolyDataMapper()
        self.p26Mapper.SetInputConnection(self.p26.GetOutputPort())
        self.p26Actor = vtk.vtkActor()
        self.p26Actor.SetMapper(self.p26Mapper)

        self.p27 = vtk.vtkSphereSource()
        self.p27.SetRadius(5.0)
        self.p27Mapper = vtk.vtkPolyDataMapper()
        self.p27Mapper.SetInputConnection(self.p27.GetOutputPort())
        self.p27Actor = vtk.vtkActor()
        self.p27Actor.SetMapper(self.p27Mapper)

        self.p28 = vtk.vtkSphereSource()
        self.p28.SetRadius(5.0)
        self.p28Mapper = vtk.vtkPolyDataMapper()
        self.p28Mapper.SetInputConnection(self.p28.GetOutputPort())
        self.p28Actor = vtk.vtkActor()
        self.p28Actor.SetMapper(self.p28Mapper)

        self.p29 = vtk.vtkSphereSource()
        self.p29.SetRadius(5.0)
        self.p29Mapper = vtk.vtkPolyDataMapper()
        self.p29Mapper.SetInputConnection(self.p29.GetOutputPort())
        self.p29Actor = vtk.vtkActor()
        self.p29Actor.SetMapper(self.p29Mapper)

        self.p30 = vtk.vtkSphereSource()
        self.p30.SetRadius(5.0)
        self.p30Mapper = vtk.vtkPolyDataMapper()
        self.p30Mapper.SetInputConnection(self.p30.GetOutputPort())
        self.p30Actor = vtk.vtkActor()
        self.p30Actor.SetMapper(self.p30Mapper)

        self.p31 = vtk.vtkSphereSource()
        self.p31.SetRadius(5.0)
        self.p31Mapper = vtk.vtkPolyDataMapper()
        self.p31Mapper.SetInputConnection(self.p31.GetOutputPort())
        self.p31Actor = vtk.vtkActor()
        self.p31Actor.SetMapper(self.p31Mapper)

        self.p32 = vtk.vtkSphereSource()
        self.p32.SetRadius(5.0)
        self.p32Mapper = vtk.vtkPolyDataMapper()
        self.p32Mapper.SetInputConnection(self.p32.GetOutputPort())
        self.p32Actor = vtk.vtkActor()
        self.p32Actor.SetMapper(self.p32Mapper)

        self.p33 = vtk.vtkSphereSource()
        self.p33.SetRadius(5.0)
        self.p33Mapper = vtk.vtkPolyDataMapper()
        self.p33Mapper.SetInputConnection(self.p33.GetOutputPort())
        self.p33Actor = vtk.vtkActor()
        self.p33Actor.SetMapper(self.p33Mapper)

        self.p34 = vtk.vtkSphereSource()
        self.p34.SetRadius(5.0)
        self.p34Mapper = vtk.vtkPolyDataMapper()
        self.p34Mapper.SetInputConnection(self.p34.GetOutputPort())
        self.p34Actor = vtk.vtkActor()
        self.p34Actor.SetMapper(self.p34Mapper)

        self.p35 = vtk.vtkSphereSource()
        self.p35.SetRadius(5.0)
        self.p35Mapper = vtk.vtkPolyDataMapper()
        self.p35Mapper.SetInputConnection(self.p35.GetOutputPort())
        self.p35Actor = vtk.vtkActor()
        self.p35Actor.SetMapper(self.p35Mapper)

        self.p36 = vtk.vtkSphereSource()
        self.p36.SetRadius(5.0)
        self.p36Mapper = vtk.vtkPolyDataMapper()
        self.p36Mapper.SetInputConnection(self.p36.GetOutputPort())
        self.p36Actor = vtk.vtkActor()
        self.p36Actor.SetMapper(self.p36Mapper)

        self.p37 = vtk.vtkSphereSource()
        self.p37.SetRadius(5.0)
        self.p37Mapper = vtk.vtkPolyDataMapper()
        self.p37Mapper.SetInputConnection(self.p37.GetOutputPort())
        self.p37Actor = vtk.vtkActor()
        self.p37Actor.SetMapper(self.p37Mapper)

        self.p38 = vtk.vtkSphereSource()
        self.p38.SetRadius(5.0)
        self.p38Mapper = vtk.vtkPolyDataMapper()
        self.p38Mapper.SetInputConnection(self.p38.GetOutputPort())
        self.p38Actor = vtk.vtkActor()
        self.p38Actor.SetMapper(self.p38Mapper)

        self.p39 = vtk.vtkSphereSource()
        self.p39.SetRadius(5.0)
        self.p39Mapper = vtk.vtkPolyDataMapper()
        self.p39Mapper.SetInputConnection(self.p39.GetOutputPort())
        self.p39Actor = vtk.vtkActor()
        self.p39Actor.SetMapper(self.p39Mapper)

        self.p40 = vtk.vtkSphereSource()
        self.p40.SetRadius(5.0)
        self.p40Mapper = vtk.vtkPolyDataMapper()
        self.p40Mapper.SetInputConnection(self.p40.GetOutputPort())
        self.p40Actor = vtk.vtkActor()
        self.p40Actor.SetMapper(self.p40Mapper)

        self.p41 = vtk.vtkSphereSource()
        self.p41.SetRadius(5.0)
        self.p41Mapper = vtk.vtkPolyDataMapper()
        self.p41Mapper.SetInputConnection(self.p41.GetOutputPort())
        self.p41Actor = vtk.vtkActor()
        self.p41Actor.SetMapper(self.p41Mapper)

        self.p42 = vtk.vtkSphereSource()
        self.p42.SetRadius(5.0)
        self.p42Mapper = vtk.vtkPolyDataMapper()
        self.p42Mapper.SetInputConnection(self.p42.GetOutputPort())
        self.p42Actor = vtk.vtkActor()
        self.p42Actor.SetMapper(self.p42Mapper)

        self.p43 = vtk.vtkSphereSource()
        self.p43.SetRadius(5.0)
        self.p43Mapper = vtk.vtkPolyDataMapper()
        self.p43Mapper.SetInputConnection(self.p43.GetOutputPort())
        self.p43Actor = vtk.vtkActor()
        self.p43Actor.SetMapper(self.p43Mapper)

        self.p44 = vtk.vtkSphereSource()
        self.p44.SetRadius(5.0)
        self.p44Mapper = vtk.vtkPolyDataMapper()
        self.p44Mapper.SetInputConnection(self.p44.GetOutputPort())
        self.p44Actor = vtk.vtkActor()
        self.p44Actor.SetMapper(self.p44Mapper)

        self.p45 = vtk.vtkSphereSource()
        self.p45.SetRadius(5.0)
        self.p45Mapper = vtk.vtkPolyDataMapper()
        self.p45Mapper.SetInputConnection(self.p45.GetOutputPort())
        self.p45Actor = vtk.vtkActor()
        self.p45Actor.SetMapper(self.p45Mapper)

        self.p46 = vtk.vtkSphereSource()
        self.p46.SetRadius(5.0)
        self.p46Mapper = vtk.vtkPolyDataMapper()
        self.p46Mapper.SetInputConnection(self.p46.GetOutputPort())
        self.p46Actor = vtk.vtkActor()
        self.p46Actor.SetMapper(self.p46Mapper)

        self.p47 = vtk.vtkSphereSource()
        self.p47.SetRadius(5.0)
        self.p47Mapper = vtk.vtkPolyDataMapper()
        self.p47Mapper.SetInputConnection(self.p47.GetOutputPort())
        self.p47Actor = vtk.vtkActor()
        self.p47Actor.SetMapper(self.p47Mapper)

        # calling here function for testing
        self.HighlightPhantomPoint(1,"red")
        self.HighlightPhantomPoint(2,"red")
        self.HighlightPhantomPoint(3,"green")
        self.HighlightPhantomPoint(4,"green")
        self.HighlightPhantomPoint(5,"green")
        self.HighlightPhantomPoint(6,"green")
        self.HighlightPhantomPoint(7,"green")
        self.HighlightPhantomPoint(8,"red")
        self.HighlightPhantomPoint(9,"red")
        self.HighlightPhantomPoint(10,"green")
        self.HighlightPhantomPoint(11,"green")
        self.HighlightPhantomPoint(12,"green")
        self.HighlightPhantomPoint(13,"green")
        self.HighlightPhantomPoint(14,"green")
        self.HighlightPhantomPoint(15,"green")
        self.HighlightPhantomPoint(16,"red")
        self.HighlightPhantomPoint(17,"blue")
        self.HighlightPhantomPoint(18,"blue")
        self.HighlightPhantomPoint(19,"blue")
        self.HighlightPhantomPoint(20,"blue")
        self.HighlightPhantomPoint(21,"green")
        self.HighlightPhantomPoint(22,"green")
        self.HighlightPhantomPoint(23,"green")
        self.HighlightPhantomPoint(24,"green")
        self.HighlightPhantomPoint(25,"green")
        self.HighlightPhantomPoint(26,"red")
        self.HighlightPhantomPoint(27,"green")
        self.HighlightPhantomPoint(28,"blue")
        self.HighlightPhantomPoint(29,"blue")
        self.HighlightPhantomPoint(30,"blue")
        self.HighlightPhantomPoint(31,"green")
        self.HighlightPhantomPoint(32,"green")
        self.HighlightPhantomPoint(33,"green")
        self.HighlightPhantomPoint(34,"green")
        self.HighlightPhantomPoint(35,"green")
        self.HighlightPhantomPoint(36,"red")
        self.HighlightPhantomPoint(37,"blue")
        self.HighlightPhantomPoint(38,"blue")
        self.HighlightPhantomPoint(39,"blue")
        self.HighlightPhantomPoint(40,"blue")
        self.HighlightPhantomPoint(41,"green")
        self.HighlightPhantomPoint(42,"green")
        self.HighlightPhantomPoint(43,"green")
        self.HighlightPhantomPoint(44,"green")
        self.HighlightPhantomPoint(45,"green")
        self.HighlightPhantomPoint(46,"red")
        self.HighlightPhantomPoint(47,"blue")
        # self.RemoveHighlight(20)
        self.RemoveAllHighlights()

        self.ren.AddActor(self.p1Actor)
        self.ren.AddActor(self.p2Actor)
        self.ren.AddActor(self.p3Actor)
        self.ren.AddActor(self.p4Actor)
        self.ren.AddActor(self.p5Actor)
        self.ren.AddActor(self.p6Actor)
        self.ren.AddActor(self.p7Actor)
        self.ren.AddActor(self.p8Actor)
        self.ren.AddActor(self.p9Actor)
        self.ren.AddActor(self.p10Actor)
        self.ren.AddActor(self.p11Actor)
        self.ren.AddActor(self.p12Actor)
        self.ren.AddActor(self.p13Actor)
        self.ren.AddActor(self.p14Actor)
        self.ren.AddActor(self.p15Actor)
        self.ren.AddActor(self.p16Actor)
        self.ren.AddActor(self.p17Actor)
        self.ren.AddActor(self.p18Actor)
        self.ren.AddActor(self.p19Actor)
        self.ren.AddActor(self.p20Actor)
        self.ren.AddActor(self.p21Actor)
        self.ren.AddActor(self.p22Actor)
        self.ren.AddActor(self.p23Actor)
        self.ren.AddActor(self.p24Actor)
        self.ren.AddActor(self.p25Actor)
        self.ren.AddActor(self.p26Actor)
        self.ren.AddActor(self.p27Actor)
        self.ren.AddActor(self.p28Actor)
        self.ren.AddActor(self.p29Actor)
        self.ren.AddActor(self.p30Actor)
        self.ren.AddActor(self.p31Actor)
        self.ren.AddActor(self.p32Actor)
        self.ren.AddActor(self.p33Actor)
        self.ren.AddActor(self.p34Actor)
        self.ren.AddActor(self.p35Actor)
        self.ren.AddActor(self.p36Actor)
        self.ren.AddActor(self.p37Actor)
        self.ren.AddActor(self.p38Actor)
        self.ren.AddActor(self.p39Actor)
        self.ren.AddActor(self.p40Actor)
        self.ren.AddActor(self.p41Actor)
        self.ren.AddActor(self.p42Actor)
        self.ren.AddActor(self.p43Actor)
        self.ren.AddActor(self.p44Actor)
        self.ren.AddActor(self.p45Actor)
        self.ren.AddActor(self.p46Actor)
        self.ren.AddActor(self.p47Actor)
        
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