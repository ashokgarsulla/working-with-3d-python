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
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.vtkWidget = QVTKRenderWindowInteractor(self.ui.frame)
        self.ren = vtk.vtkRenderer()
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

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
        # self.phantom.SetScale(1.0/200, 1.0/200, 1.0/200)
        self.phantom.SetScale(3, 3, 3)

        self.ren.AddActor(self.phantom)


        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.vtkWidget.GetRenderWindow().Render()
        
        self.iren.Start()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = BaseWindow()
    win.show()
    sys.exit(app.exec())