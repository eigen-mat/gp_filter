# gp_filter
The GP filter is a very simple function suitable for filtering out undesired peaks in periodic time series spectra. It uses a geometric progression to define the length of windows where a median filter is applied. The function takes three input parameters to be adjusted: the initial window length, the GP ratio, and a multiplication factor to define the filter threshold.


In the repository you will find a file called "gplib.py" where the GP filter function is. To use it you can copy and paste the code inside the file or import it as a library:

> from gplib import gp_filter

The function takes the parameters pxx, fs, l0, q, k.
  pxx: spectrum of periodic time series
  f: frequency axis (obtained through a FFT function)
  l0: lenght of the first window
  q: ratio of the geometric progression
  k: multiplication factor for the threshold

Remarks: Based on my signals I suggest a small value for l0 (between 5 and 10). The ration q should not be much bigger than 1 (example: 1,0005).

A Matlab function is also found in the repository. It works in a similar way to Python code.

The documentation found in gp_filter_doc.pdf explains in more detail how the filter works.
