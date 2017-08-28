import numpy as np
import argparse
import TestFunction as TP
import ParticleDef as PD
import GalaxyDef as GD
import CameraDef as CD
import DistanceCubeDef as DCD

print "Main Test"

PosCheck=[1.,2., "Thing"]
VelCheck=[0.4,-0.5,3.5]
MCheck=15.3
MLTest=0.5
Entropy=3.
ID=1
PType=0
PTest=PD.Particle(ID,PType,MCheck,PosCheck,VelCheck,MLTest,Entropy)

#print PTest.Pos[0]+PTest.Pos[2]
print PTest.Luminosity

PTest.Luminosity=float(PTest.Mass)/float(PTest.ML)
print PTest.Luminosity


GadgetIntFlags=(0,1,2)
GadgetRealFlags=(0.,1.,2.,3.,4.,5.)
GadgetFlags=GD.GadgetFlags(GadgetIntFlags,GadgetRealFlags)

print GadgetFlags.Cooling, GadgetFlags.Hubble

nPart=1000000
nPartType=(100,900,0,0,0,0)
GH=GD.GalaxyHeader(nPart,nPartType,GadgetIntFlags,GadgetRealFlags)

print GH.Flags.Hubble

Gal=GD.Galaxy(GH)
print Gal.GH.nPart
#print Gal.P[0].ID, Gal.P[GH.nPart-1].ID

nPixelsTest=[100,200]
PixelST=0.3
PixelFWHM=1.

CameraTest=CD.Camera(nPixelsTest,PixelST,PixelFWHM)

print np.shape(CameraTest.PixelLoc)

nDistCells=100

DCube=DCD.DistanceCube(nPixelsTest,PixelST,nDistCells)



DCube.DetermineCubePhysicalSize(Gal)
