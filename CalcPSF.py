import numpy as np
import ParticleDef as PD
import CameraDef as CD

def CalcPSF(Particle,Camera):
    print "Spreading the light from ", Particle.ID, "across the PSF"
    PSF=np.zeros([2,2])
    return PSF

def AddPSFToImage(PSF,Camera):
    print "Adding the PSF to the Image"

