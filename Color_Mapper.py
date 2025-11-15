"""Insert your solutions for exercise 2 here."""
import vtk


def visualize(data_source, renderer):
    # Create plane inside dataset
    geometry_filter = vtk.vtkStructuredGridGeometryFilter()
    geometry_filter.SetInputData(data_source)

    extent = data_source.GetExtent()
    k_mid = (extent[4] + extent[5]) // 2
    geometry_filter.SetExtent(extent[0], extent[1], extent[2], extent[3], k_mid, k_mid)
    geometry_filter.Update()

    # Create lookuptable
    table = vtk.vtkLookupTable()
    table.SetHueRange(0.0, 0.670)
    table.SetSaturationRange(1.0, 1.0)
    table.SetValueRange(1.0, 1.0)
    table.Build()

    # Add mapper and actor

    color_mapper = vtk.vtkPolyDataMapper()
    color_mapper.SetInputConnection(geometry_filter.GetOutputPort())
    color_mapper.SetLookupTable(table)
    scalar_min_max_range = data_source.GetScalarRange()
    color_mapper.SetScalarRange(scalar_min_max_range)
    actor = vtk.vtkActor()
    actor.SetMapper(color_mapper)
    renderer.AddActor(actor)