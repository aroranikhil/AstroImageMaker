"""This code is designed to spell out the three different kind of dust distribution model using the extinction that is derieved in a particlular band. In principle this code can be used to calculate the extinction for the complete galaxy using the average optical depth of the object."""

import numpy as np

def dust_extinction(model = 'screen', inclination = 'yes'):
    
    if model == 'screen':
        extinc = 1.086 * tau
        if inclination == 'no':
            return extinc
        else:
            extinc2 = 1.086 * tau * (1/np.cos(i))
            return extinc2
            
    
            
        