
import vtkmodules.vtkInteractionStyle
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

class WorkingVolume():

    def __init__(self):
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
        
        self.actor.GetProperty().SetColor(self.colors.GetColor3d("grey"))
        self.actor.GetProperty().SetRepresentationToSurface()
        self.actor.GetProperty().EdgeVisibilityOn()
        self.actor.GetProperty().SetEdgeColor(255,0,0)
        self.actor.GetProperty().SetOpacity(0.3)

    def display(self):
        # Create a renderer, render window, and interactor
        self.renderer = vtkRenderer()
        self.renderWindow = vtkRenderWindow()
        self.renderWindow.SetWindowName("Pyramid")
        self.renderWindow.AddRenderer(self.renderer)
        self.renderWindowInteractor = vtkRenderWindowInteractor()
        self.renderWindowInteractor.SetRenderWindow(self.renderWindow)

        self.renderer.AddActor(self.actor)

        # Create a nice view
        self.renderer.ResetCamera()
        self.renderer.GetActiveCamera().Azimuth(180)
        self.renderer.GetActiveCamera().Elevation(-20)
        self.renderer.ResetCameraClippingRange()

        self.renderer.SetBackground(self.colors.GetColor3d("green"))

        self.renderWindow.Render()
        self.renderWindowInteractor.Start()
        
test =  WorkingVolume()
test.display()

#


# SetWorkingVolume(hFoV, vFov)
# SetWorkingVolumeVisibility(isOn:bool)
# SetPhantomVisibility(isOn:bool)
# SetCurrentPhantomLocation(transform: vtk.vtkTransform)
# SetTargetPhantomLocation(transform: vtk.vtkTransform)
# SetWindowVisibility(isVisibile; bool)