import vtk

# ------------------------------------------------------
# Insert the path to your data for the exercise here
data_root = "./"
# here you can choose the mode that should be used to
# visualize the given data
visualization_mode = None  # None, 'color_map', 'cutting', 'isosurf', 'probing'
# ------------------------------------------------------

# Insert explanations for this section------------------
# Creates a PLOT3D (used for computational fluid dynamics data) reader 
pl3d = vtk.vtkMultiBlockPLOT3DReader()
# Gives the path to the file containing the coordinates of the flow points in the 3D space
pl3d.SetXYZFileName(data_root + "combxyz.bin")
# Gives the path to the file containing the flow parameters (like velocity, pressure, temperature, etc.) for each point
pl3d.SetQFileName(data_root + "combq.bin")
# Specifies which scalar function to read from the Q file (100 corresponds to temperature)
pl3d.SetScalarFunctionNumber(100)
# Specifies which vector function to read from the Q file (202 corresponds to velocity vector)
pl3d.SetVectorFunctionNumber(202)
# Adds an additional function to be read from the Q file (153 corresponds to Mach number -> ratio of flow speed to speed of sound)
pl3d.AddFunction(153) 
# Allows the reader to process the data and prepare it for further use, since it charges the data into memory
pl3d.Update()
# Obtains the output data from the reader, specifically the first block (zone) of the multi-block dataset
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
