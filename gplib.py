"""
GP (Geometric Progression) Filter
Mateus Carvalho

"""

import numpy as np
from scipy.signal import medfilt

def gp_filter(pxx, fs, l, q, k):
    pxx_filt = np.zeros(len(pxx))
    pg = []
    while l <= len(pxx):
        l = l*q**(k - 1)
        pg.append(l)
    
    for i in range(len(pg) - 1):
        a = round(pg[i])
        b = round(pg[i + 1])
        pxx_fraction = pxx[a:b]
        L = len(pxx_fraction)
        
        if L % 2 == 0: # check if window length is odd or even
            if L == 0:
                L = 1
            else:
                L = L - 1
                
        median_filter = medfilt(pxx_fraction, L)
        bad_index = abs(pxx_fraction - median_filter) > abs(np.std(pxx_fraction))*k
        pxx_fraction[bad_index] = median_filter[bad_index]
        pxx_filt[a:b] = pxx_fraction
    
    
    return pxx_filt