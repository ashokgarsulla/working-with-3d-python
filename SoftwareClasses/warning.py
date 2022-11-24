
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

class WarningWindow():

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

        # Actor one
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)


        self.actor.GetProperty().SetRepresentationToSurface()
        self.actor.GetProperty().EdgeVisibilityOn()
        self.actor.GetProperty().SetEdgeColor(255,0,0)
        self.actor.GetProperty().SetOpacity(0.5)

    def SetWorkingVolume(hFov, vFov):
        pass

    def SetWorkingVolumeVisibility(isOn):
        pass

    def SetPhantomVisibility(self,isOn):
        if isOn:
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
            self.phantom.SetPosition(0,0,0.5)


    def SetCurrentPhantomLocation(transform):
        pass

    def SetTargetPhantomLocation(transform):
        pass

    def SetWindowVisibility(self,isVisibile):
        if isVisibile:
            self.renTop = vtkRenderer()
            self.renTop.AddActor(self.actor)
            # self.renTop.AddActor(self.phantom)
            self.renTop.SetBackground(vtkNamedColors().GetColor3d("grey"))
            self.renTop.SetViewport(0.5, 0.0, 1.0, 1.0)

            self.renFront = vtkRenderer()
            self.renFront.AddActor(self.actor)
            # self.renFront.AddActor(self.phantom)
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


            # Finally we create the render window which will show up on the screen.
            # We add our two renderers into the render window using AddRenderer.
            renderWindow = vtkRenderWindow()
            renderWindow.AddRenderer(self.renTop)
            renderWindow.AddRenderer(self.renFront)
            renderWindow.SetWindowName('Warning')
            renderWindow.SetSize(1024,512)

            # Test VTK
            interactor = vtkRenderWindowInteractor()
            interactor.SetRenderWindow(renderWindow)
            interactor.SetInteractorStyle(vtkInteractorStyleImage())
            renderWindow.Render()
            interactor.Start()
                
test =  WarningWindow()
# test.display()
        

test.SetWindowVisibility(True)


# SetWorkingVolume(hFoV, vFov)
# SetWorkingVolumeVisibility(isOn:bool)
# SetPhantomVisibility(isOn:bool)
# SetCurrentPhantomLocation(transform: vtk.vtkTransform)
# SetTargetPhantomLocation(transform: vtk.vtkTransform)
# SetWindowVisibility(isVisibile; bool)
# SetPhantomPosition (x,y,z : actor)