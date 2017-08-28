import numpy as np

class Particle(object):
    """ The particle class to be used in our worke

        Attributes:
            PType: The type of Gadget particle -- integer
            ID:     The id # for the particle -- integer
            Mass:   Mass -- real
            ML:     Mass/Light Ratio -- real
            Luminosity: Bolometric luminosity -- real
            Pos(3): Cartesian Position vector (x,y,z) -- 3 element real array
            Vel(3): Cartesian Velocity vector (v_x,v_y,v_z) -- 3 element real array
            AngPos(3): Galoctocentric position vector (r,l,b) -- 3 element real array
            AngVel(3):  Galactocentric velocity vector (v_r,v_l,v_b) -- 3 element real array
            Temp:       Temperature -- real
            Entropy:    Entropy -- real
                """

    def __init__(self,ID,PType,Mass,Pos,Vel,ML,Entropy):
        self.ID=ID
        self.PType=PType
        self.Mass=Mass
        self.Pos=Pos
        self.Vel=Vel
        self.ML=ML
        self.Luminosity=0.
        self.AngPos=np.zeros(3)
        self.AngVel=np.zeros(3)
        self.Temp=0.
        self.Entropy=Entropy

#        assert(len(Pos)==3 and np.array(type(Pos)=='float').all()==True),"Pos must be 3 element real array"
