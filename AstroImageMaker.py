"""
    AstroImageMaker
    
    Authors:
    Nathan Deg
    Nikhil Arora
    
    This program is designed to make mock astronomical images from
    a Gadget-2 N-body simulation
    
    """


import numpy as np
import RuntimeInputs as RT
import Initializations as Inis
import GadgetIOs as GIO
import GenerateDustDistribution as GDD
import ParticleSplit as PS
import GalaxyAdjust as GA
import CalcObservedGalaxyCoords as COG
import DistanceCubeDef as DCD
import CalcLuminosities as CL
import GenerateScatteredParticles as GSP
import CalcExtinctions as CE
import ApplyFilter as AF
import CalcPSF as CP
import CameraDef as CD
import AddNoise as AN

print "Welcome to Astro Image Maker"


####    Some dummy variables for skeleton tests...should be set in
####    runtime routines
GalInFile='TestFile'
Switch=2
OutputFile='TestImage.fits'
####
####

"""

#       General Parallel set up
SetUpParallel()
"""
#       Runtime Inputs
RT.GetRuntimeInputs()

#       Initialize all general objects
LocalGasDC,LocalDustDC,LocalImage=Inis.InitializeAllObjects()

###       In the Master processor only
#       Read in N-body file
Gal=GIO.GadgetReadIn(GalInFile)

#       Downsample as needed
Gal=GIO.GadgetDownSample(Gal)

#       Select the gas component
Gas=GIO.SelectGasParticles(Gal)

#       Select the observed component
Observed=GIO.SelectObservedParticles(Gal)

#       Generate dust particles
Dust=GDD.GenerateDustParticles(Gas,Switch)
### End of Master only section

#       Split Particles across processors
LocalGas=PS.ParticleSplit(Gas)
LocalDust=PS.ParticleSplit(Dust)
LocalObserved=PS.ParticleSplit(Observed)

#       Do all particle (r,v) adjustments for observations
GA.ParticleAdjust(LocalGas)
GA.ParticleAdjust(LocalDust)
GA.ParticleAdjust(LocalObserved)

#       Calculate the observed coordinates of particles
COG.GetObservedCoords(LocalGas)
COG.GetObservedCoords(LocalDust)
COG.GetObservedCoords(LocalObserved)

#       Fill Gas and Dust distance-cubes ->the dimensions of these should be determined in the Initializations
LocalGasDC.FillDistanceCube(LocalGas)
LocalDustDC.FillDistanceCube(LocalDust)

###         Distance Cube Parallel Section
#       Combine local cubes from each processor into single master distance-cubes
MasterGasDC=DCD.DistanceCubeCombine(LocalGasDC)
MasterDustDC=DCD.DistanceCubeCombine(LocalDustDC)

#       Share the master cubes across all processors
DCD.ShareMasterDistanceCube(MasterGasDC)
DCD.ShareMasterDistanceCube(MasterDustDC)
###         End Distance Cube Parallel Section


#       Get total luminosities for each particle
CL.CalcTotalLuminosity(LocalObserved)

#       Get the luminosity in the observed band
CL.CalcBandLuminosities(LocalObserved)



###      ???   Keep this in one loop to reduce memory load ???
#       Create Dust-Scattered Particles
for i in range(Gal.GH.nPart):
    SelectedParticle=LocalObserved.P[i]
    ScatteredParticles=GSP.DustScattering(SelectedParticle,MasterDustDC)
    GSP.SplitLightBetweenScatteredAndObservedParticles(SelectedParticle,ScatteredParticles)

#       Calculate the extinctions
    CE.GetGasExtinction(SelectedParticle,MasterGasDC)
    CE.GetDustExtinction(SelectedParticle,MasterDustDC)

    CE.GetGasExtinction(ScatteredParticles,MasterGasDC)
    CE.GetDustExtinction(ScatteredParticles,MasterDustDC)

#       Apply any extra filter reduction
    AF.ApplyFilterReduction(SelectedParticle)
    AF.ApplyFilterReduction(ScatteredParticles)

#       Spread Light across PSF and Add to camera
    ObservedPSF=CP.CalcPSF(SelectedParticle,LocalImage)
    CP.AddPSFToImage(ObservedPSF,LocalImage)

    ScatteredPSF=CP.CalcPSF(ScatteredParticles,LocalImage)
    CP.AddPSFToImage(ScatteredPSF,LocalImage)
###             End the particle loop


###         Camera Parallel Section
#       Combine the local images into a master image
MasterImage=CD.CombineLocalImage(LocalImage)
###         End Camera Parallel Section


###        In Master Processor Only
#       Convert to signal units
MasterImage.ConvertImageUnits(Switch)

#       Add noise
AN.AddImageNoise(MasterImage)

#Output Image
MasterImage.SaveImage(OutputFile)
