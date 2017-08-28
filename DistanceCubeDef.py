import numpy as np
import GalaxyDef as GD

class DistanceCube(object):
    """ The camera class to be used in our worke

        Attributes:
            nPixels: number of pixel -- 2 element integers
            PixelSize: size of each pixel -- real  (should be in arcseconds)
            PixelLoc:   location of each pixel -- array of reals (2,max(nPixels(0),nPixels(1)))
            nDCells:    number of distance cells -- integer 
            MassInCell: The mass in each cell -- arrary of reals (nPixels(0)xnPixels(1)xnDCells)
            MassAlongColumn:    The cumulative mass along each cell in a column -- arrary of reals (nPixels(0)xnPixels(1)xnDCells)
            DistanceLocs:   The mid-distance for each column --  array of reals (nDCells) (should be in kpc)
            CellSize:   The size of each cell in distance -- real (should be in kpc)
            minD:       The minimum distance of the cube -- real (should be in kpc)
            maxD:       The maximum distance of the cube -- real (should be in kpc)
                """

    def __init__(self,nPixels,PixelSize,nDCells):
        self.nPixels=nPixels
        MaxPix=np.max(nPixels)
        self.PixelSize=PixelSize
        self.PixelLoc=np.empty( (2,MaxPix),dtype=float)
        self.Signal=np.empty( (nPixels[0],nPixels[1]),dtype=float)
        start=np.empty(2)
        start[0]=-PixelSize*float(nPixels[0])/2.
        start[1]=-PixelSize*float(nPixels[1])/2.
        for i in range(2):
            for j in xrange(MaxPix):
                self.PixelLoc[i,j]=start[0]+(j+0.5)*PixelSize
        self.nDCells=nDCells
        self.MassInCell=np.zeros( (nPixels[0],nPixels[1],nDCells),dtype=float )
        self.MassAlongColumn=np.zeros( (nPixels[0],nPixels[1],nDCells),dtype=float )
        self.DistanceLocs=np.zeros(nDCells)
        self.CellSize=0.
        self.minD=1.e20
        self.maxD=0.

    def DetermineCubePhysicalSize(self,Gal):
        """
           This method determines the size of the cube by finding the minimum
            and maximum distances of particles in the Galaxy object and using 
            those to calculate the cellsize and location of each cell
                """

        for i in xrange(Gal.GH.nPart):
            self.maxD=max(self.maxD,Gal.P[i].AngPos[0])
            self.minD=min(self.minD,Gal.P[i].AngPos[0])

        self.CellSize=(self.maxD-self.minD)/float(self.nDCells)
        for i in range(self.nDCells):
            self.DistanceLocs[i]=self.minD+(i+0.5)*self.CellSize

    def FillDistanceCube(self,Gal):
        """
            This method fills the cells of a particular distance cube using
            a galaxy object
        """
        print "Filling Distance Cube with ", Gal.GH.nPart, " particles"

#####



def DistanceCubeCombine(LocalCube):
    """
        This function combines the various local cubes into one master cube
    """
    print "Combining the local cubes"
    MasterCube=LocalCube
    return MasterCube

def ShareMasterDistanceCube(self):
    """
        This method shares the master cube across all processors
    """
    print "Sharing Master distance cube across processors"



