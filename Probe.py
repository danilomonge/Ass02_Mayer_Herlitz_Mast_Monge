"""Insert your solutions for exercise 5 here."""
import vtk


def visualize(data_source, renderer):
    # create a plane source as the source for the three planes
    plane = vtk.vtkPlaneSource()
    plane.SetResolution(50, 50)

    # Create three planes using transform filters on the plane
    # source and position them inside the dataset
    # ----------------------------------------------
    # transform the first plane

    # apply the transform

    # show the outline

    # ----------------------------------------------

    # ----------------------------------------------
    # do the same to create another plane

    # ----------------------------------------------

    # ----------------------------------------------
    # and do that to create a third one

    # ----------------------------------------------

    # ----------------------------------------------
    # Create probe geometry by appending planes

    # Create probe geometry filter

    # Create contours using contour filter

    # Create mapper and actor

    # ----------------------------------------------

    # ----------------------------------------------
    # Add actors to the renderer

    # ----------------------------------------------
