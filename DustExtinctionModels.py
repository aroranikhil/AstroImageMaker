"""This code is designed to spell out the three different kind of dust distribution model using the extinction that is derieved in a particlular band. In principle this code can be used to calculate the extinction for the complete galaxy using the average optical depth of the object."""
__Author__ = 'Nathan Deg and Nikhil Arora'
__email__ = 'nikhil.arora@queensu.ca'
__version__ = '1.0'

import numpy as np

def dust_extinction(tau, i, model = 'screen', inclination = 'yes'):
    
    if model == 'screen':
        extinc = 1.086 * tau
        if inclination == 'no':
            return extinc
        else:
            extinc2 = 1.086 * tau * (1/np.cos(i))
            return extinc2
       
    if model == 'slab':
        extinc = -2.5 * np.log10((1 - np.exp(-tau))/(tau))
        if inclination == 'no':
            return extinc
        else:
            extinc2 = -2.5 * np.log10((1 - np.exp(-tau * (1/np.cos(i))))/(tau * (1/np.cos(i))))
            return extinc2       
