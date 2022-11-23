
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

        self.actor.GetProperty().SetColor(self.colors.GetColor3d("grey"))
        self.actor.GetProperty().SetRepresentationToSurface()
        self.actor.GetProperty().EdgeVisibilityOn()
        self.actor.GetProperty().SetEdgeColor(255,0,0)
        self.actor.GetProperty().SetOpacity(0.3)

        # Actor two
        self.actor1 = vtkActor()
        self.actor1.SetMapper(self.mapper)
        
        self.actor1.GetProperty().SetColor(self.colors.GetColor3d("tamato"))
        self.actor1.GetProperty().SetRepresentationToSurface()
        self.actor1.GetProperty().EdgeVisibilityOn()
        self.actor1.GetProperty().SetEdgeColor(255,0,0)
        self.actor1.GetProperty().SetOpacity(0.3)
       
    def display_phantom(self):
        self.colors = vtkNamedColors()

        self.filename = "holecube.stl"

        self.reader = vtkSTLReader()
        self.reader.SetFileName(self.filename)

        self.mapper = vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.reader.GetOutputPort())

        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)
        self.actor.GetProperty().SetDiffuse(0.8)
        self.actor.GetProperty().SetDiffuseColor(self.colors.GetColor3d('LightSteelBlue'))
        self.actor.GetProperty().SetSpecular(0.3)
        self.actor.GetProperty().SetSpecularPower(60.0)

        # Create a rendering window and renderer
        self.ren = vtkRenderer()
        self.renWin = vtkRenderWindow()
        self.renWin.AddRenderer(self.ren)
        self.renWin.SetWindowName('ReadSTL')

        # Create a renderwindowinteractor
        self.iren = vtkRenderWindowInteractor()
        self.iren.SetRenderWindow(self.renWin)

        # Assign actor to the renderer
        self.ren.AddActor(self.actor)
        self.ren.SetBackground(self.colors.GetColor3d('DarkOliveGreen'))

        # Enable user interface interactor
        self.iren.Initialize()
        self.renWin.Render()
        self.iren.Start()

    def display(self):
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

        self.ren1 = vtkRenderer()
        self.ren1.AddActor(self.actor)
        self.ren1.AddActor(self.phantom)
        self.ren1.SetBackground(vtkNamedColors().GetColor3d("green"))
        self.ren1.SetViewport(0.5, 0.0, 1.0, 1.0)

        self.ren2 = vtkRenderer()
        self.ren2.AddActor(self.actor1)
        self.ren2.SetBackground(vtkNamedColors().GetColor3d("orange"))
        self.ren2.SetViewport(0.0, 0.0, 0.5, 1.0)

        # Set the cameras far enough
        self.ren1.GetActiveCamera().SetPosition(0, 0, 3)
        self.ren2.GetActiveCamera().SetPosition(0, 0, 2)


        # Finally we create the render window which will show up on the screen.
        # We add our two renderers into the render window using AddRenderer.
        renderWindow = vtkRenderWindow()
        renderWindow.AddRenderer(self.ren1)
        renderWindow.AddRenderer(self.ren2)
        renderWindow.SetWindowName('Warning')

        # Test VTK
        interactor = vtkRenderWindowInteractor()
        interactor.SetRenderWindow(renderWindow)
        renderWindow.Render()
        interactor.Start()

    def sideview(self):
        self.display()
        
test =  WarningWindow()
test.display()
test.display_phantom()

#


# SetWorkingVolume(hFoV, vFov)
# SetWorkingVolumeVisibility(isOn:bool)
# SetPhantomVisibility(isOn:bool)
# SetCurrentPhantomLocation(transform: vtk.vtkTransform)
# SetTargetPhantomLocation(transform: vtk.vtkTransform)
# SetWindowVisibility(isVisibile; bool)