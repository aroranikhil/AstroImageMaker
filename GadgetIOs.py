import numpy as np
import GalaxyDef as GD

def GadgetReadIn(SnapshotFile):
    print "Reading in Gadget Snapshot"
    GadgetIntFlags=(0,1,2)
    GadgetRealFlags=(0.,1.,2.,3.,4.,5.)
    nPart=2
    nPartType=(100,900,0,0,0,0)
    GHeader=GD.GalaxyHeader(nPart,nPartType,GadgetIntFlags,GadgetRealFlags)
    Gal=GD.Galaxy(GHeader)
    return Gal

def GadgetDownSample(Gal):
    print "Down sampling Gadget selection"
    ReducedGal=Gal
    return ReducedGal

def SelectGasParticles(Gal):
    print "Selecting Gas particles"
    Gas=Gal
    return Gas

def SelectObservedParticles(Gal):
    print "Selecting observed particles"
    Observed=Gal
    return Observed
