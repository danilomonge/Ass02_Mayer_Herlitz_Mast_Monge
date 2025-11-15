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
    center_of_dataset = data_source.GetCenter()
    
    # transform the first plane 
    plane1_transform = vtk.vtkTransform() # creates a transform object (to position the first plane)
    plane1_transform.Translate(center_of_dataset[0]+ 5, center_of_dataset[1], center_of_dataset[2] + 3.25)  # moves the plane to the back of the dataset
    plane1_transform.Scale(11, 11, 4.75)  # size of the plane to cover that specific area of the dataset
    plane1_transform.RotateY(90)  # rotates the plane to be vertical
    
    # apply the transform 
    plane1_transform_filter = vtk.vtkTransformPolyDataFilter() # creates a filter to apply the transform (it modifies the geometry of the plane)
    plane1_transform_filter.SetInputConnection(plane.GetOutputPort()) # connects the plane source to the filter
    plane1_transform_filter.SetTransform(plane1_transform) # sets the transform to the filter
    plane1_transform_filter.Update() # updates the filter to apply the transform

    # show the outline 
    plane1_outline = vtk.vtkOutlineFilter() # creates an outline filter (to see the edges of the plane)
    plane1_outline.SetInputConnection(plane1_transform_filter.GetOutputPort()) # connects the transformed plane to the outline filter

    plane1_outline_mapper = vtk.vtkPolyDataMapper() # creates a mapper for the outline (to convert the data to graphics primitives)
    plane1_outline_mapper.SetInputConnection(plane1_outline.GetOutputPort()) # connects the outline filter to the mapper

    plane_1_outline_actor = vtk.vtkActor() # creates an actor for the outline (to represent the outline in the scene)
    plane_1_outline_actor.SetMapper(plane1_outline_mapper) # connects the mapper to the actor
    plane_1_outline_actor.GetProperty().SetColor(0, 0, 0) # sets the color of the outline to black 

    # ----------------------------------------------

    # ----------------------------------------------
    # do the same to create another plane
    
    plane2_transform = vtk.vtkTransform() # creates a transform object (for the second plane)
    plane2_transform.Translate(center_of_dataset[0] + 1, center_of_dataset[1], center_of_dataset[2]+ 0.75) # moves the plane to be in h

    plane2_transform.Scale(11, 11, 8.25) # size of the plane to cover that specific area of the dataset
    plane2_transform.RotateY(90)  # rotates the plane to be vertical

    plane2_transform_filter = vtk.vtkTransformPolyDataFilter() # creates a filter to apply the transform
    plane2_transform_filter.SetInputConnection(plane.GetOutputPort()) # connects the plane source to the filter
    plane2_transform_filter.SetTransform(plane2_transform) # sets the transform to the filter
    plane2_transform_filter.Update() # updates the filter to apply the transform

    plane2_outline = vtk.vtkOutlineFilter() # creates an outline filter
    plane2_outline.SetInputConnection(plane2_transform_filter.GetOutputPort()) # connects the transformed plane to the outline filter

    plane2_outline_mapper = vtk.vtkPolyDataMapper() # creates a mapper for the outline
    plane2_outline_mapper.SetInputConnection(plane2_outline.GetOutputPort()) # connects the outline filter to the mapper

    plane2_outline_actor = vtk.vtkActor() # creates an actor for the outline
    plane2_outline_actor.SetMapper(plane2_outline_mapper) # connects the mapper to the actor
    plane2_outline_actor.GetProperty().SetColor(0, 0, 0) # sets the color of the outline to black

    # ----------------------------------------------

    # ----------------------------------------------
    # and do that to create a third one
    
    plane3_transform = vtk.vtkTransform() # creates a transform object (for the third plane)
    plane3_transform.Translate(center_of_dataset[0] - 4.5, center_of_dataset[1], center_of_dataset[2] - 1.5) # moves the plane to the back of the dataset
    plane3_transform.Scale(11, 11, 9.5)  # size of the plane to cover that specific area of the dataset
    plane3_transform.RotateY(90) # rotates the plane to be vertical

    plane3_transform_filter = vtk.vtkTransformPolyDataFilter() # creates a filter to apply the transform
    plane3_transform_filter.SetInputConnection(plane.GetOutputPort()) # connects the plane source to the filter
    plane3_transform_filter.SetTransform(plane3_transform) # sets the transform to the filter
    plane3_transform_filter.Update() # updates the filter to apply the transform

    plane3_outline = vtk.vtkOutlineFilter() # creates an outline filter
    plane3_outline.SetInputConnection(plane3_transform_filter.GetOutputPort()) # connects the transformed plane to the outline filter

    plane3_outline_mapper = vtk.vtkPolyDataMapper() # creates a mapper for the outline
    plane3_outline_mapper.SetInputConnection(plane3_outline.GetOutputPort()) # connects the outline filter to the mapper

    plane3_outline_actor = vtk.vtkActor() # creates an actor for the outline
    plane3_outline_actor.SetMapper(plane3_outline_mapper) # connects the mapper to the actor
    plane3_outline_actor.GetProperty().SetColor(0, 0, 0) # sets the color of the outline to black

    # ----------------------------------------------

    # ----------------------------------------------
    # Create probe geometry by appending planes
    
    planes_combined = vtk.vtkAppendPolyData() # creates an append filter to combine the three planes (it allows to use them as a single geometry)
    planes_combined.AddInputConnection(plane1_transform_filter.GetOutputPort()) # adds the first plane to the append filter
    planes_combined.AddInputConnection(plane2_transform_filter.GetOutputPort()) # adds the second plane to the append filter
    planes_combined.AddInputConnection(plane3_transform_filter.GetOutputPort()) # adds the third plane to the append filter
    planes_combined.Update() # updates the append filter to combine the planes

    # Create probe geometry filter
    
    probe_geometry_filter = vtk.vtkProbeFilter() # creates a probe filter to sample the data on the planes (it lets to extract data values from the dataset at the locations defined by the planes)
    probe_geometry_filter.SetInputConnection(planes_combined.GetOutputPort())  # sets the combined planes as the input geometry for probing
    probe_geometry_filter.SetSourceData(data_source)  # sets the dataset as the source for probing
    probe_geometry_filter.Update() # updates the probing filter to perform the data sampling

    # Create contours using contour filter
    
    contour_lines_filter = vtk.vtkContourFilter() # creates a contour filter to generate contour lines (it extracts lines of constant data values from the probed data)
    contour_lines_filter.SetInputConnection(probe_geometry_filter.GetOutputPort()) # sets the probed data as the input for contouring
    contour_lines_filter.GenerateValues(50, data_source.GetScalarRange())  # generates 50 contour values across the scalar range of the dataset

    # Create mapper and actor

    # ----------------------------------------------
    
    contour_lines_mapper = vtk.vtkPolyDataMapper() # creates a mapper for the contours (it converts the contour data to graphics primitives)
    contour_lines_mapper.SetInputConnection(contour_lines_filter.GetOutputPort()) # connects the contour filter to the mapper
    contour_lines_mapper.SetScalarRange(data_source.GetScalarRange()) # sets the scalar range for coloring the contours

    contour_lines_actor = vtk.vtkActor() # creates an actor for the contours (it represents the contours in the scene)
    contour_lines_actor.SetMapper(contour_lines_mapper) # connects the mapper to the actor

    # ----------------------------------------------
    # Add actors to the renderer
    
    renderer.AddActor(plane_1_outline_actor) # adds the first outline actor to the renderer
    renderer.AddActor(plane2_outline_actor) # adds the second outline actor to the renderer
    renderer.AddActor(plane3_outline_actor) # adds the third outline actor to the renderer
    renderer.AddActor(contour_lines_actor) # adds the contour actor to the renderer

    # ----------------------------------------------
    
    # ----------------------------------------------------------
    
 

    
