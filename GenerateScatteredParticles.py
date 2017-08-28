import numpy as np
import ParticleDef as PD
import DistanceCubeDef as DCD

def DustScattering(Particle,DustCube):
    print "Scattering particle", Particle.ID,  "by dust"
    ScatteredPart=Particle
    return ScatteredPart

def SplitLightBetweenScatteredAndObservedParticles(Particle,SParts):
    print "Splitting the light between all scattered particles and the main particle", Particle.ID


