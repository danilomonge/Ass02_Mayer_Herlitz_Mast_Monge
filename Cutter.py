"""Insert your solutions for exercise 3 here."""
import vtk


def visualize(data_source, renderer):
    # Create a plane inside dataset
    center = data_source.GetCenter() # get center coordinates of the dataset
    cutting_plane = vtk.vtkPlane() # create a plane
    cutting_plane.SetOrigin(center[0],center[1],center[2]-0.5) # set position of plane
    cutting_plane.SetNormal(-3,0,7) # defines the orientation of the plane

    # Create cutter
    cutter = vtk.vtkCutter() # create cutter
    cutter.SetInputData(data_source) # connects the cutter with the dataset
    cutter.SetCutFunction(cutting_plane) # set plane as cutting function
    cutter.Update() # update cutter to process the data

    # Create lookuptable
    lut = vtk.vtkLookupTable() # create lookup table
    lut.SetNumberOfColors(256) # settting of colors all hex combinations
    lut.Build()

    # Add mapper and actor
    cutter_mapper = vtk.vtkPolyDataMapper()
    cutter_mapper.SetInputConnection(cutter.GetOutputPort()) # connect cutter to mapper
    cutter_mapper.SetLookupTable(lut) # connecet the table to mapper

    # get scalar range from data for color mapping
    output = cutter.GetOutput()
    scalar_range = output.GetScalarRange()
    cutter_mapper.SetScalarRange(scalar_range)

    # create actor and add to renderer
    actor = vtk.vtkActor()
    actor.SetMapper(cutter_mapper)
    renderer.AddActor(actor)