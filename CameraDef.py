import numpy as np

class Camera(object):
    """ The camera class to be used in our worke

        Attributes:
            nPixels: number of pixel -- 2 element integers
            PixelSize: size of each pixel -- real  (should be in arcseconds)
            PixelLoc:   location of each pixel -- array of reals (2,max(nPixels(0),nPixels(1)))
            PSF_FWHM: The FWHM of the Gaussian PSF --real (should be in arcseconds)
            PSF_Sigma: The sigma width of the Gaussian PSF --real (should be in arcseconds)
            Signal:     The signal in each pixel -- array of reals (nPixels(0)xnPixels(1))
                """

    def __init__(self,nPixels,PixelSize,PSF_FWHM):
        self.nPixels=nPixels
        MaxPix=np.max(nPixels)
        self.PixelSize=PixelSize
        self.PSF_FWHM=PSF_FWHM
        self.PixelLoc=np.empty( (2,MaxPix),dtype=float)
        self.Signal=np.empty( (nPixels[0],nPixels[1]),dtype=float)
        self.PSF_Sigma=PSF_FWHM/2.355
        start=np.empty(2)
        start[0]=-PixelSize*float(nPixels[0])/2.
        start[1]=-PixelSize*float(nPixels[1])/2.
        for i in range(2):
            for j in xrange(MaxPix):
                self.PixelLoc[i,j]=start[0]+(j+0.5)*PixelSize

    def ConvertImageUnits(self,UnitSwitch):
        """
           This method converts the luminosity units of the image.
        """
        print "Converting Image luminosities to ", UnitSwitch

    def SaveImage(self,outfile):
        """
                This method saves the image to a fits file
        """
        print "Outputting image to", outfile



####
def CombineLocalImage(LocalImage):
    """
        This function combines the various local images into one master image
    """
    print "Combining the local cubes"
    MasterImage=LocalImage
    return MasterImage
