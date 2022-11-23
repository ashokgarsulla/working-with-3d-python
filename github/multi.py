# fmt: off
## The 3 followings line are a temp solution until I upgrate to bokeh 2.0.2 (now it 2.0.1) and won't be necessary later
# from bokeh.settings import settings  # noqa isort:skip
# settings.resources = 'cdn'  # noqa isort:skip
# settings.resources = 'inline'  # noqa isort:skip
# # fmt: on
# import panel as pn
import vtk

# Create the arrow and the associated mapper and actor.
arrow = vtk.vtkArrowSource()
arrowMapper = vtk.vtkPolyDataMapper()
arrowMapper.SetInputConnection(arrow.GetOutputPort())
arrowActor = vtk.vtkActor()
arrowActor.SetPosition(-0.5, 0, 0)
arrowActor.SetMapper(arrowMapper)

# Create the sphere and the associated mapper and actor.
sphere = vtk.vtkSphereSource()
sphere.SetRadius(0.1)
sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphere.GetOutputPort())
sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMapper)


# Create two renderers and assign actors to them. A renderer renders into a
# viewport within the vtkRenderWindow. It is part or all of a window on the
# screen and it is responsible for drawing the actors it has.
# We can add the same actor to two different renderers;
# it is okay to add different actors to different renderers as well.
ren1 = vtk.vtkRenderer()
ren1.AddActor(arrowActor)
ren1.SetBackground(vtk.vtkNamedColors().GetColor3d("DarkSlateGray"))
ren1.SetViewport(0.0, 0.0, 0.5, 1.0)

ren2 = vtk.vtkRenderer()
ren2.AddActor(sphereActor)
ren2.SetBackground(vtk.vtkNamedColors().GetColor3d("LightSlateGray"))
ren2.SetViewport(0.0, 0.7, 0.3, 1.0)

# Set the cameras far enough
ren1.GetActiveCamera().SetPosition(0, 0, 3)
ren2.GetActiveCamera().SetPosition(0, 0, 2)


# Finally we create the render window which will show up on the screen.
# We add our two renderers into the render window using AddRenderer.
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(ren1)
renderWindow.AddRenderer(ren2)


# Test Panel
# a = pn.pane.VTK(renderWindow)
# a.show()

# Test VTK
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWindow)
renderWindow.Render()
interactor.Start()