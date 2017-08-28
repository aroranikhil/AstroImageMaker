import numpy as np
import ParticleDef as PD
from abc import ABCMeta, abstractmethod


class GadgetFlags(object):
    """The simulation flags for a specific Gadget snapshot
        SFR:    Star formation flag -- integer
        Feedback:   Feedback flag -- integer
        Cooling:    Cooling flag -- integer
        Time:   The snapshot time -- real
        Redshift: The snapshot redshift -- real
        Omega0: Omega0 for the simulation -- real
        OmegaLambda: Omega-Lambda for the simulation -- real
        Hubble: The Hubble constant value for the simulation -- real
        Box: The box dimensions -- real
    """
    __metaclass__ = ABCMeta

    def __init__(self,IntFlags,RealFlags):
        self.SFR=np.asarray(IntFlags[0])
        self.Feedback=IntFlags[1]
        self.Cooling=IntFlags[2]
        self.Time=RealFlags[0]
        self.Redshift=RealFlags[1]
        self.Omega0=RealFlags[2]
        self.OmegaLambda=RealFlags[3]
        self.Hubble=RealFlags[4]
        self.Box=RealFlags[5]



class GalaxyHeader(object):
    """     The galaxy header class to be used in our work.  It is designed
            to be used for Gadget 2 snapshots, thus the references to   
            simulation values for some of the attributes.
        
        Attributes:
        nPart:  The total number of particles -- integer
        nPartType: The number of particles in each Gadget type -- 6 element integer
        GadgetFlags: The Gadget snapshot flags -- one 3 element integer, one 6 element real
        """

    def __init__(self,nPart,nPartType,GadgetIntFlags,GadgetRealFlags):
        self.nPart=nPart
        self.nPartType=nPartType
        self.Flags=GadgetFlags(GadgetIntFlags,GadgetRealFlags)

class Galaxy(object):
    """     The galaxy class to be used in our work.  
        
        Attributes:
        GH:  The header for the galaxy -- a Galaxy Header object
        P: Particles -- an empty array of particle objects
        """
    def __init__(self,GH):
        self.GH=GH
        M=ML=Entropy=0.
        Pos=Vel=[0.,0.,0.]
        ID=PType=-1
        self.P=np.empty( (GH.nPart),dtype=PD.Particle )
        for i in xrange(GH.nPart):
            self.P[i]=PD.Particle(i,PType,M,Pos,Vel,ML,Entropy)
            self.P[i].AngPos[0]=float(i)






