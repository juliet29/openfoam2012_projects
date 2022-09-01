# trace generated using paraview version 5.10.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get animation scene
animationScene1 = GetAnimationScene()

# Properties modified on animationScene1
animationScene1.AnimationTime = 500.0

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# get active source.
hotRoom6E_2foam = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
hotRoom6E_2foamDisplay = GetDisplayProperties(hotRoom6E_2foam, view=renderView1)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# Properties modified on animationScene1
animationScene1.AnimationTime = 200.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 300.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 400.0

# Properties modified on animationScene1
animationScene1.AnimationTime = 0.0

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1390, 690)

# current camera placement for renderView1
renderView1.CameraPosition = [10.0, 5.742087517793363, 22.39109589717917]
renderView1.CameraFocalPoint = [10.0, 1.4999999701976776, 1.5000000000000004]
renderView1.CameraViewUp = [0.0, 0.9800002781470601, -0.1989961176296781]
renderView1.CameraParallelScale = 14.310608667492833

# save animation
SaveAnimation('/Users/julietnwagwuume-ezeoke/cfd/of2012_projects/hotRoom6E_2/pViewU/U.png', renderView1, ImageResolution=[1390, 690],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    FrameRate=1,
    FrameWindow=[0, 5], 
    # PNG options
    CompressionLevel='5',
    MetaData=['Application', 'ParaView'],
    SuffixFormat='.%04d')

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
renderView1.CameraPosition = [10.0, 5.742087517793363, 22.39109589717917]
renderView1.CameraFocalPoint = [10.0, 1.4999999701976776, 1.5000000000000004]
renderView1.CameraViewUp = [0.0, 0.9800002781470601, -0.1989961176296781]
renderView1.CameraParallelScale = 14.310608667492833

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).