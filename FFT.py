'''
Feature Extraction For Music Recommendation
Convert mp3 to wav using Audacity or some other way of conversion to 16 bit PCM
Use FFT and extract Features from it

Generally , Music is expressed in the form of 2 channels , for stereo effect . We consider each
channel seperately , as it might lead to more accuracy , compared to taking average of the two channels
for each attribute

It is still not in training form and is meant to work only for one file . Modifications have to made
for this to get access to multiple files simultaneously
'''


import numpy
import pylab
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
fs , data = wavfile.read('Saathiya.wav')
iteri = [0,1]
for i in iteri:

	a = data.T[i];
	zerocrossing= [0,0];
	spectral_average = [0,0];
	centroid = [0,0];
	flag = [0,0];
	energy = [0,0];
	roloffcalc = [0,0];
	sumroll = [0,0];
	eff_length = 0;
	iteri1 = numpy.arange(len(a) - 2)
	for j in iteri1 :
		if abs(a[j+1]) == 0:
			eff_length = eff_length + 1
			if abs(a[j]) != 0 or abs(a[j+2]) != 0: 
				zerocrossing[i] = zerocrossing[i] + 1

	print("zerocrossing =")
	print zerocrossing[i]

	

	b=[(ele/2**16.)*2-1 for ele in a]
	c = fft(b)
	'''
	spectral_average[i]	 = sum(abs(c[:5000*len(a)/fs]))/(len(c[:5000*len(a)/fs]))
	print("average =")
	print spectral_average[i]
	print("length =")
	print len(c[:5000*len(a)/fs])
	'''

	l = numpy.arange(len(c))
	T = len(c)/fs
	d = l/T

	centroid[i] = sum(d*abs(c))/sum(abs(c))
	print("centroid =")
	print centroid[i]

	roloffcalc[i] = 0.85*sum(abs(c[:5000*len(a)/fs]))
	for ele in c:
		flag[i] = flag[i] + 1;
		sumroll[i] = sumroll[i] + abs(ele);
		if sumroll[i] > abs(roloffcalc[i]) :
			break
	print("roloff =")
	print flag[i]

	energy[i] = sum(pow(abs(c[:5000*len(a)/fs]),2))
	print("energy =")
	print energy[i]

	
