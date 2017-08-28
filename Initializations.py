import numpy as np
import argparse
import DistanceCubeDef as DCD
import CameraDef as CD

def InitializeAllObjects():
    print "Initializing Objects"

    nPixelsTest=[100,200]
    PixelST=0.3
    nDistCells=100
    BasicCube=DCD.DistanceCube(nPixelsTest,PixelST,nDistCells)
    PixelFWHM=1.
    BasicCamera=CD.Camera(nPixelsTest,PixelST,PixelFWHM)
    
    return BasicCube,BasicCube,BasicCamera
