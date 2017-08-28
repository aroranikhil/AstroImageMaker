#           Astro Image Maker File List
#
#
    Authors: Nathan Deg 
             Nikhil Arora

#           Mains
AstroImageMaker.py              -- The image maker program
MainTest.py                     -- A file for testing various routines and classes

#           Class Definitions
ParticleDef.py                  -- Defines the particle class
GalaxyDef.py                    -- Defines the galaxy class and contains some methods for it
CameraDef.py                    -- Defines the camera class and some important methods
DistanceCubeDef.py              -- Defines the distance-cube class and some important methods

#       Input Routines
RuntimeInputs.py                -- Gets the various runtime inputs needed
GadgetIOs.py                    -- Reads in a Gadget snapshot

#       Initialization Routines
Initializations.py              -- Initializes various global objects

#       Parallelization Routines
ParticleSplit.py                -- Splits a galaxy class between processors

#       Galaxy-focused routines 
GalaxyAdjust.py                 -- Adjusts (r,v) for all particles in a galaxy
CalcObservedGalaxyCoords        -- Gets (d,l,b,v_r,v_l,v_b) for all particles in a galaxy

#       Dust-focused Routines 
GenerateDustDistribution.py     -- Generates a distribution of dust particles
GenerateScatteredParticles.py   -- Generates fake particles from particle light scattered by the dust distribution

#       Luminosity-focused routines 
CalcLuminosities.py             -- Calculates the luminosity of particles
CalcExtinctions.py              -- Reduces the luminosity according to the extinction laws
ApplyFilter.py                  -- Applies any reduction to the particle luminosity from the filter

#       Camera-focused Routines 
CalcPSF.py                      -- Spreads the light across a PSF on the camera
AddNoise.py                     -- Adds noise to the image
