"""Insert your solutions for exercise 5 here."""
import vtk


def visualize(data_source, renderer):
    # create a plane source as the source for the three planes
    plane = vtk.vtkPlaneSource()
    plane.SetResolution(50, 50) # more resolution means thighter mesh

    # Create three planes using transform filters on the plane
    # source and position them inside the dataset
    # ----------------------------------------------
    
    # get the center coordinates of the dataset to position the planes
    center = data_source.GetCenter()
    
    # transform the first plane 
    plane_trans1 = vtk.vtkTransform() # creates a transform object (to position the first plane)
    plane_trans1.Translate(center[0]+ 5, center[1], center[2] + 3.25)  # moves the plane to the back of the dataset
    plane_trans1.Scale(11, 11, 4.75)  # size of the plane to cover that specific area of the dataset
    plane_trans1.RotateY(90)  # rotates the plane to be vertical
    
    # apply the transform
    plane_filter1 = vtk.vtkTransformPolyDataFilter() # creates a filter to apply the transform (it modifies the geometry of the plane)
    plane_filter1.SetInputConnection(plane.GetOutputPort()) # connects the plane source to the filter
    plane_filter1.SetTransform(plane_trans1) # sets the transform to the filter
    plane_filter1.Update() # updates the filter to apply the transform

    # show the outline 
    outline1 = vtk.vtkOutlineFilter() # creates an outline filter (to see the edges of the plane)
    outline1.SetInputConnection(plane_filter1.GetOutputPort()) # connects the transformed plane to the outline filter

    outline_mapper1 = vtk.vtkPolyDataMapper() # creates a mapper for the outline (to convert the data to graphics primitives)
    outline_mapper1.SetInputConnection(outline1.GetOutputPort()) # connects the outline filter to the mapper

    outline_actor1 = vtk.vtkActor() # creates an actor for the outline (to represent the outline in the scene)
    outline_actor1.SetMapper(outline_mapper1) # connects the mapper to the actor
    outline_actor1.GetProperty().SetColor(0, 0, 0) # sets the color of the outline to black 

    # ----------------------------------------------

    # ----------------------------------------------
    # do the same to create another plane
    
    plane_trans2 = vtk.vtkTransform() # creates a transform object (for the second plane)
    plane_trans2.Translate(center[0] + 1, center[1], center[2]+ 0.75) # moves the plane to be in h

    plane_trans2.Scale(11, 11, 8.25) # size of the plane to cover that specific area of the dataset
    plane_trans2.RotateY(90)  # rotates the plane to be vertical

    plane_filter2 = vtk.vtkTransformPolyDataFilter() # creates a filter to apply the transform
    plane_filter2.SetInputConnection(plane.GetOutputPort()) # connects the plane source to the filter
    plane_filter2.SetTransform(plane_trans2) # sets the transform to the filter
    plane_filter2.Update() # updates the filter to apply the transform

    outline2 = vtk.vtkOutlineFilter() # creates an outline filter
    outline2.SetInputConnection(plane_filter2.GetOutputPort()) # connects the transformed plane to the outline filter

    outline_mapper2 = vtk.vtkPolyDataMapper() # creates a mapper for the outline
    outline_mapper2.SetInputConnection(outline2.GetOutputPort()) # connects the outline filter to the mapper

    outline_actor2 = vtk.vtkActor() # creates an actor for the outline
    outline_actor2.SetMapper(outline_mapper2) # connects the mapper to the actor
    outline_actor2.GetProperty().SetColor(0, 0, 0) # sets the color of the outline to black

    # ----------------------------------------------

    # ----------------------------------------------
    # and do that to create a third one
    
    plane_trans3 = vtk.vtkTransform() # creates a transform object (for the third plane)
    plane_trans3.Translate(center[0] - 4.5, center[1], center[2] - 1.5) # moves the plane to the back of the dataset
    plane_trans3.Scale(11, 11, 9.5)  # size of the plane to cover that specific area of the dataset
    plane_trans3.RotateY(90) # rotates the plane to be vertical

    plane_filter3 = vtk.vtkTransformPolyDataFilter() # creates a filter to apply the transform
    plane_filter3.SetInputConnection(plane.GetOutputPort()) # connects the plane source to the filter
    plane_filter3.SetTransform(plane_trans3) # sets the transform to the filter
    plane_filter3.Update() # updates the filter to apply the transform

    outline3 = vtk.vtkOutlineFilter() # creates an outline filter
    outline3.SetInputConnection(plane_filter3.GetOutputPort()) # connects the transformed plane to the outline filter

    outline_mapper3 = vtk.vtkPolyDataMapper() # creates a mapper for the outline
    outline_mapper3.SetInputConnection(outline3.GetOutputPort()) # connects the outline filter to the mapper

    outline_actor3 = vtk.vtkActor() # creates an actor for the outline
    outline_actor3.SetMapper(outline_mapper3) # connects the mapper to the actor
    outline_actor3.GetProperty().SetColor(0, 0, 0) # sets the color of the outline to black

    # ----------------------------------------------

    # ----------------------------------------------
    # Create probe geometry by appending planes
    
    append_planes = vtk.vtkAppendPolyData() # creates an append filter to combine the three planes (it allows to use them as a single geometry)
    append_planes.AddInputConnection(plane_filter1.GetOutputPort()) # adds the first plane to the append filter
    append_planes.AddInputConnection(plane_filter2.GetOutputPort()) # adds the second plane to the append filter
    append_planes.AddInputConnection(plane_filter3.GetOutputPort()) # adds the third plane to the append filter
    append_planes.Update() # updates the append filter to combine the planes

    # Create probe geometry filter
    
    probing_filter = vtk.vtkProbeFilter() # creates a probe filter to sample the data on the planes (it lets to extract data values from the dataset at the locations defined by the planes)
    probing_filter.SetInputConnection(append_planes.GetOutputPort())  # sets the combined planes as the input geometry for probing
    probing_filter.SetSourceData(data_source)  # sets the dataset as the source for probing
    probing_filter.Update() # updates the probing filter to perform the data sampling

    # Create contours using contour filter
    
    contour_filter = vtk.vtkContourFilter() # creates a contour filter to generate contour lines (it extracts lines of constant data values from the probed data)
    contour_filter.SetInputConnection(probing_filter.GetOutputPort()) # sets the probed data as the input for contouring
    contour_filter.GenerateValues(50, data_source.GetScalarRange())  # generates 50 contour values across the scalar range of the dataset

    # Create mapper and actor

    # ----------------------------------------------
    
    contour_mapper = vtk.vtkPolyDataMapper() # creates a mapper for the contours (it converts the contour data to graphics primitives)
    contour_mapper.SetInputConnection(contour_filter.GetOutputPort()) # connects the contour filter to the mapper
    contour_mapper.SetScalarRange(data_source.GetScalarRange()) # sets the scalar range for coloring the contours

    contour_actor = vtk.vtkActor() # creates an actor for the contours (it represents the contours in the scene)
    contour_actor.SetMapper(contour_mapper) # connects the mapper to the actor

    # ----------------------------------------------
    # Add actors to the renderer
    
    renderer.AddActor(outline_actor1) # adds the first outline actor to the renderer
    renderer.AddActor(outline_actor2) # adds the second outline actor to the renderer
    renderer.AddActor(outline_actor3) # adds the third outline actor to the renderer
    renderer.AddActor(contour_actor) # adds the contour actor to the renderer

    # ----------------------------------------------
    
    # ----------------------------------------------------------
    
 

    
