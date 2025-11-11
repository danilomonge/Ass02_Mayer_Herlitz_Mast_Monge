"""Insert your solutions for exercise 3 here."""
import vtk


def visualize(data_source, renderer):
    # Create a plane inside dataset
    center = data_source.GetCenter()
    cutting_plane = vtk.vtkPlane()
    cutting_plane.SetOrigin(center[0],center[1],center[2]-0.5)
    cutting_plane.SetNormal(-3,0,7)

    # Create cutter
    cutter = vtk.vtkCutter()
    cutter.SetInputData(data_source)
    cutter.SetCutFunction(cutting_plane)
    cutter.Update()

    # Create lookuptable
    lut = vtk.vtkLookupTable()
    lut.SetNumberOfColors(256)
    lut.Build()

    # Add mapper and actor
    cutter_mapper = vtk.vtkPolyDataMapper()
    cutter_mapper.SetInputConnection(cutter.GetOutputPort())
    cutter_mapper.SetLookupTable(lut)

    output = cutter.GetOutput()
    scalar_range = output.GetScalarRange()
    cutter_mapper.SetScalarRange(scalar_range)

    actor = vtk.vtkActor()
    actor.SetMapper(cutter_mapper)
    renderer.AddActor(actor)