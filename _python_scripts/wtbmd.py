from __future__ import unicode_literals, print_function

import math

from ofblockmeshdicthelper import BlockMeshDict, Vertex, SimpleGrading

# geometries
wt_length = 20 # wt  = wind tunnel
wt_height = 3
wt_depth = 3
box_size = 1

# prepare ofblockmeshdicthelper.BlockMeshDict instance to
# gather vertices, blocks, faces and boundaries.
bmd = BlockMeshDict()

# set metrics
bmd.set_metric('m')

# base vertices of wind tunnel 
basevs = [
    Vertex(0, 0, 0, 'v0'),
    Vertex(wt_length, 0, 0, 'v1'),
    Vertex(wt_length, 0, wt_depth, 'v2'),
    Vertex(0, 0, wt_depth, 'v3')]