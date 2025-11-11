import vtk

# ------------------------------------------------------
# Insert the path to your data for the exercise here
data_root = "./"
# here you can choose the mode that should be used to
# visualize the given data
visualization_mode = None  # None, 'color_map', 'cutting', 'isosurf', 'probing'
# ------------------------------------------------------

# Insert explanations for this section------------------
# <explanation here>
pl3d = vtk.vtkMultiBlockPLOT3DReader()
# <explanation here>
pl3d.SetXYZFileName(data_root + "combxyz.bin")
pl3d.SetQFileName(data_root + "combq.bin")
# <explanation here>
pl3d.SetScalarFunctionNumber(100)
# <explanation here>
pl3d.SetVectorFunctionNumber(202)
# <explanation here>
pl3d.AddFunction(153)
#
pl3d.Update()
# <explanation here>
pl3d_output = pl3d.GetOutput().GetBlock(0)
# End section ------------------------------------------

# Create the RenderWindow and Renderer
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# create an outline to your data using the vtkStructuredGridOutlineFiler()
outline = vtk.vtkStructuredGridOutlineFilter()
outline.SetInputData(pl3d_output)
outline_mapper = vtk.vtkPolyDataMapper()
outline_mapper.SetInputConnection(outline.GetOutputPort())
outline_actor = vtk.vtkActor()
outline_actor.SetMapper(outline_mapper)

# ------------------------------------------------------
if visualization_mode == 'color_map':
    import Color_Mapper as color_mapper

    color_mapper.visualize(pl3d_output, renderer)
elif visualization_mode == 'cutting':
    import Cutter as cutter

    cutter.visualize(pl3d_output, renderer)
elif visualization_mode == 'probing':
    import Probe as probe

    probe.visualize(pl3d_output, renderer)
elif visualization_mode == 'isosurf':
    import Isosurf as isosurf

    isosurf.visualize(pl3d_output, renderer)
# ------------------------------------------------------

renderer.AddActor(outline_actor)
renderer.SetBackground(0.1, 0.2, 0.4)
render_window.SetSize(1200, 1200)

cam1 = renderer.GetActiveCamera()
cam1.SetClippingRange(3.94, 50)
cam1.SetFocalPoint(9.7, 0.5, 29.4)
cam1.SetPosition(2.7, -37.3, 38.7)
cam1.SetViewUp(-0.16, 0.26, 0.95)

if __name__ == "__main__":
    render_window_interactor.Initialize()
    render_window.Render()
    render_window_interactor.Start()
