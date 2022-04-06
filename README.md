# gp_filter
The GP filter is a very simple function suitable for filtering out undesired peaks in periodic time series spectra. It uses a geometric progression to define the length of windows where a median filter is applied. The function takes three input parameters: the initial window length, the GP ratio, and a multiplication factor to define the filter threshold.
