# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
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


class WorkingVolumeActor(vtkmodules.vtkActor):

  def __init__(self):
    super().__init__()
    self.meshPolyData = vtkmodules.vtkPolyData()
    self.meshMapper = vtkmodules.vtkPolyDataMapper()
    self.meshMapper.SetInputData(self.meshPolyData)
    self.SetMapper(self.meshMapper)

    self.edgesPolyData = vtkmodules.vtkPolyData()
    self.edgesMapper = vtkmodules.vtkPolyDataMapper()
    self.edgesMapper.SetInputData(self.edgesPolyData)
    self.edges = vtkmodules.vtkActor()
    self.edges.SetMapper(self.edgesMapper)

    # prevent edges and mesh from brawling in Z-buffer
    vtkmodules.vtkPolyDataMapper().SetResolveCoincidentTopologyToPolygonOffset()

  def __inspoly(self, polys, id0, id1, id2):
    idList = vtkmodules.vtkIdList()
    idList.InsertNextId(id0)
    idList.InsertNextId(id1)
    idList.InsertNextId(id2)
    polys.InsertNextCell(idList)

  def setNodes(self, pts):
    nodes = vtkmodules.vtkPoints()
    for p in pts:
      nodes.InsertPoint(int(p), pts[p])

    # Mesh
    polys = vtkmodules.vtkCellArray()
    ids = list(pts.keys()) # get all the node ids
    # Define lambda to ensure correct connection every k nodes
    lb = lambda i, k=4: i-k if i%k == 0 else i
    # for each face
    for i in range(0,len(ids)-4):
      self.__inspoly(polys, ids[i], ids[lb(i+1)], ids[i+4]) # first triangle
      self.__inspoly(polys, ids[i+4], ids[lb(i+1)], ids[lb(i+5)]) # second triangle
    
    self.meshPolyData.SetPoints(nodes)
    self.meshPolyData.SetPolys(polys)

    # Edges
    lines = vtkmodules.vtkCellArray()
    # Front edges
    for i in range(0,4):
      lines.InsertNextCell(2, [ids[i], ids[lb(i+1)]])
    # Side edges
    for i in range(0,len(ids)-4,4):
      for k in range(0,4):
        lines.InsertNextCell(2, [ids[i]+k, ids[i]+k+4])
    # Back edges
    for i in range(len(ids)-4,len(ids)):
      lines.InsertNextCell(2, [ids[i], ids[lb(i+1)]])

    self.edgesPolyData.SetPoints(nodes)
    self.edgesPolyData.SetLines(lines)

def main():



    wv = WorkingVolumeActor()
    colors = vtkNamedColors()

    points = vtkPoints()

    p0 = [1.0, 1.0, 1.0]
    p1 = [-1.0, 1.0, 1.0]
    p2 = [-1.0, -1.0, 1.0]
    p3 = [1.0, -1.0, 1.0]
    p4 = [0.0, 0.0, 0.0]

    points.InsertNextPoint(p0)
    points.InsertNextPoint(p1)
    points.InsertNextPoint(p2)
    points.InsertNextPoint(p3)
    points.InsertNextPoint(p4)

    pyramid = vtkPyramid()
    pyramid.GetPointIds().SetId(0, 0)
    pyramid.GetPointIds().SetId(1, 1)
    pyramid.GetPointIds().SetId(2, 2)
    pyramid.GetPointIds().SetId(3, 3)
    pyramid.GetPointIds().SetId(4, 4)

    cells = vtkCellArray()
    cells.InsertNextCell(pyramid)

    ug = vtkUnstructuredGrid()
    ug.SetPoints(points)
    ug.InsertNextCell(pyramid.GetCellType(), pyramid.GetPointIds())

    # Create an actor and mapper
    mapper = vtkDataSetMapper()
    mapper.SetInputData(ug)

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d("gray"))

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName("Pyramid")
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)

    # Create a nice view
    renderer.ResetCamera()
    renderer.GetActiveCamera().Azimuth(180)
    renderer.GetActiveCamera().Elevation(-20)
    renderer.ResetCameraClippingRange()

    # renderer.SetBackground(colors.GetColor3d("Silver"))

    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()