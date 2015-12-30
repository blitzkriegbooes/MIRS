'''
Testing to find difference Between Channels
'''


import numpy
import pylab
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
fs , data = wavfile.read('Saathiya.wav')
a = data.T[0]
wavfile.write('thuli_channel0.wav', fs , a)
