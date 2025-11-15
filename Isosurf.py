"""Insert your solutions for exercise 4 here."""
import vtk


def visualize(data_source, renderer):

    # Create isosurface
    contour_filter = vtk.vtkContourFilter()
    contour_filter.SetInputData(data_source)
    
    # select isosurface value
    scalar_range = data_source.GetScalarRange()

    isosurface_value = (scalar_range[0] + scalar_range[1]) * 0.5
    contour_filter.SetValue(0, isosurface_value)
    
    

    # Add mapper using velocity magnitude data
    contour_mapper = vtk.vtkPolyDataMapper()
    contour_mapper.SetInputConnection(contour_filter.GetOutputPort())
    
    # "VelocityMagnitude" scalar data for colorization
    contour_mapper.ColorByArrayComponent("VelocityMagnitude", 0)
    
    contour_mapper.SetScalarModeToUsePointFieldData()

    # determine correct range from velocity magnitude data array
    array = data_source.GetPointData().GetArray("VelocityMagnitude")

    if array is None:
        raise RuntimeError("velocity magnitude data array not found")
    
    contour_mapper.SetScalarRange(array.GetRange(0))
    contour_mapper.ScalarVisibilityOn()
    


    # Add actor to renderer
    contour_actor = vtk.vtkActor()
    contour_actor.SetMapper(contour_mapper)
    
    renderer.AddActor(contour_actor)


