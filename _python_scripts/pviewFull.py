# trace generated using paraview version 5.10.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
hotRoom6E_2foam = OpenFOAMReader(registrationName='hotRoom6E_2.foam', FileName='/Users/julietnwagwuume-ezeoke/cfd/of2012_projects/hotRoom6E_2/hotRoom6E_2.foam')
hotRoom6E_2foam.MeshRegions = ['internalMesh']
hotRoom6E_2foam.CellArrays = ['Co', 'U', 'epsilon', 'k', 'nut', 'p']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
hotRoom6E_2foamDisplay = Show(hotRoom6E_2foam, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# trace defaults for the display properties.
hotRoom6E_2foamDisplay.Representation = 'Surface'
hotRoom6E_2foamDisplay.ColorArrayName = ['POINTS', 'p']
hotRoom6E_2foamDisplay.LookupTable = pLUT
hotRoom6E_2foamDisplay.SelectTCoordArray = 'None'
hotRoom6E_2foamDisplay.SelectNormalArray = 'None'
hotRoom6E_2foamDisplay.SelectTangentArray = 'None'
hotRoom6E_2foamDisplay.OSPRayScaleArray = 'p'
hotRoom6E_2foamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
hotRoom6E_2foamDisplay.SelectOrientationVectors = 'U'
hotRoom6E_2foamDisplay.ScaleFactor = 2.0
hotRoom6E_2foamDisplay.SelectScaleArray = 'p'
hotRoom6E_2foamDisplay.GlyphType = 'Arrow'
hotRoom6E_2foamDisplay.GlyphTableIndexArray = 'p'
hotRoom6E_2foamDisplay.GaussianRadius = 0.1
hotRoom6E_2foamDisplay.SetScaleArray = ['POINTS', 'p']
hotRoom6E_2foamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
hotRoom6E_2foamDisplay.OpacityArray = ['POINTS', 'p']
hotRoom6E_2foamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
hotRoom6E_2foamDisplay.DataAxesGrid = 'GridAxesRepresentation'
hotRoom6E_2foamDisplay.PolarAxes = 'PolarAxesRepresentation'
hotRoom6E_2foamDisplay.ScalarOpacityFunction = pPWF
hotRoom6E_2foamDisplay.ScalarOpacityUnitDistance = 0.7532020192938514
hotRoom6E_2foamDisplay.OpacityArrayName = ['POINTS', 'p']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
hotRoom6E_2foamDisplay.ScaleTransferFunction.Points = [-0.13913224637508392, 0.0, 0.5, 0.0, 0.001611747546121478, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
hotRoom6E_2foamDisplay.OpacityTransferFunction.Points = [-0.13913224637508392, 0.0, 0.5, 0.0, 0.001611747546121478, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# show color bar/color legend
hotRoom6E_2foamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(hotRoom6E_2foamDisplay, ('POINTS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
hotRoom6E_2foamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
hotRoom6E_2foamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# Properties modified on hotRoom6E_2foam
hotRoom6E_2foam.SkipZeroTime = 0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on animationScene1
animationScene1.AnimationTime = 0.0

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=hotRoom6E_2foam)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [10.0, 1.5, 1.5]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [10.0, 1.5, 1.5]

# Properties modified on hotRoom6E_2foam
hotRoom6E_2foam.CellArrays = ['Co', 'U', 'epsilon', 'k', 'nut', 'p', 'nuTilda', 'omega']

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'p']
slice1Display.LookupTable = pLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'p'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'U'
slice1Display.ScaleFactor = 2.0
slice1Display.SelectScaleArray = 'p'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'p'
slice1Display.GaussianRadius = 0.1
slice1Display.SetScaleArray = ['POINTS', 'p']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'p']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide data in view
Hide(hotRoom6E_2foam, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=slice1,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'U']
streamTracer1.MaximumStreamlineLength = 20.0

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [0.0, 0.0, 1.5]
streamTracer1.SeedType.Point2 = [20.0, 3.0, 1.5]

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = ['POINTS', 'p']
streamTracer1Display.LookupTable = pLUT
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.OSPRayScaleArray = 'p'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 2.0
streamTracer1Display.SelectScaleArray = 'p'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'p'
streamTracer1Display.GaussianRadius = 0.1
streamTracer1Display.SetScaleArray = ['POINTS', 'p']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'p']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide data in view
Hide(slice1, renderView1)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on animationScene1
animationScene1.AnimationTime = 100.0

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=streamTracer1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'Normals']
glyph1.ScaleArray = ['POINTS', 'p']
glyph1.ScaleFactor = 2.0
glyph1.GlyphTransform = 'Transform2'

# Properties modified on glyph1
glyph1.MaximumNumberOfSamplePoints = 100

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'p']
glyph1Display.LookupTable = pLUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'p'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'Normals'
glyph1Display.ScaleFactor = 1.9687067346181721
glyph1Display.SelectScaleArray = 'p'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'p'
glyph1Display.GaussianRadius = 0.09843533673090861
glyph1Display.SetScaleArray = ['POINTS', 'p']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'p']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [-0.13447575271129608, 0.0, 0.5, 0.0, -3.772290438064374e-05, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-0.13447575271129608, 0.0, 0.5, 0.0, -3.772290438064374e-05, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# turn off scalar coloring
ColorBy(glyph1Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# Properties modified on glyph1
glyph1.OrientationArray = ['POINTS', 'U']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 1.0

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=slice1.SliceType)

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on slice1Display
slice1Display.Opacity = 0.76

# Properties modified on slice1Display
slice1Display.Opacity = 0.81

# Properties modified on slice1Display
slice1Display.Opacity = 0.59

# set active source
SetActiveSource(hotRoom6E_2foam)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# create a new 'Annotate Time'
annotateTime1 = AnnotateTime(registrationName='AnnotateTime1')

# set active source
SetActiveSource(annotateTime1)

# show data in view
annotateTime1Display = Show(annotateTime1, renderView1, 'TextSourceRepresentation')

# set active source
SetActiveSource(annotateTime1)

# show data in view
annotateTime1Display = Show(annotateTime1, renderView1, 'TextSourceRepresentation')

# create a new 'Annotate Attribute Data'
annotateAttributeData1 = AnnotateAttributeData(registrationName='AnnotateAttributeData1', Input=annotateTime1)
annotateAttributeData1.SelectInputArray = ['ROWS', 'Text']

# set active source
SetActiveSource(annotateAttributeData1)

# show data in view
annotateAttributeData1Display = Show(annotateAttributeData1, renderView1, 'TextSourceRepresentation')

# Properties modified on annotateAttributeData1Display
annotateAttributeData1Display.WindowLocation = 'Lower Center'

# hide data in view
Hide(annotateTime1, renderView1)

# set active source
SetActiveSource(annotateAttributeData1)

# set active source
SetActiveSource(annotateTime1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=annotateTime1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=annotateTime1Display)

# hide data in view
Hide(annotateAttributeData1, renderView1)

# show data in view
annotateTime1Display = Show(annotateTime1, renderView1, 'TextSourceRepresentation')

# destroy annotateAttributeData1
Delete(annotateAttributeData1)
del annotateAttributeData1

# set active source
SetActiveSource(hotRoom6E_2foam)

# create a new 'Annotate Global Data'
annotateGlobalData1 = AnnotateGlobalData(registrationName='AnnotateGlobalData1', Input=hotRoom6E_2foam)
annotateGlobalData1.SelectArrays = 'CasePath'

# set active source
SetActiveSource(annotateGlobalData1)

# show data in view
annotateGlobalData1Display = Show(annotateGlobalData1, renderView1, 'TextSourceRepresentation')

# Properties modified on annotateGlobalData1Display
annotateGlobalData1Display.WindowLocation = 'Lower Center'

# set active source
SetActiveSource(hotRoom6E_2foam)

# hide data in view
Hide(annotateGlobalData1, renderView1)

# show data in view
hotRoom6E_2foamDisplay = Show(hotRoom6E_2foam, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
hotRoom6E_2foamDisplay.SetScalarBarVisibility(renderView1, True)

# destroy annotateGlobalData1
Delete(annotateGlobalData1)
del annotateGlobalData1

# hide data in view
Hide(hotRoom6E_2foam, renderView1)

# set active source
SetActiveSource(hotRoom6E_2foam)

# Properties modified on animationScene1
animationScene1.AnimationTime = 2000.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 1800.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 600.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 200.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 300.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 400.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 500.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 400.0

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1390, 690)

# current camera placement for renderView1
renderView1.CameraPosition = [7.187607817089574, 5.70651516053521, 23.213103781922754]
renderView1.CameraFocalPoint = [10.0, 1.499999999999999, 1.499999999999998]
renderView1.CameraViewUp = [0.0031570351125164778, 0.9818176546251871, -0.18980022706939864]
renderView1.CameraParallelScale = 10.222524150130436

# save animation
SaveAnimation('/Users/julietnwagwuume-ezeoke/cfd/of2012_projects/hotRoom6E_2/pViewU/Ufull.png', renderView1, ImageResolution=[1390, 690],
    FrameWindow=[0, 20])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1390, 690)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [7.187607817089574, 5.70651516053521, 23.213103781922754]
renderView1.CameraFocalPoint = [10.0, 1.499999999999999, 1.499999999999998]
renderView1.CameraViewUp = [0.0031570351125164778, 0.9818176546251871, -0.18980022706939864]
renderView1.CameraParallelScale = 10.222524150130436

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).