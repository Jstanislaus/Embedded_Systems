import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np

def visualize(path: str): 
    
    # reading the audio file 
    raw = wave.open(path) 
      
    # reads all the frames  
    # -1 indicates all or max frames 
    signal = raw.readframes(-1) 
    signal = np.frombuffer(signal, dtype ="int16") 
      
    # gets the frame rate 
    f_rate = raw.getframerate() 
  
    # to Plot the x-axis in seconds  
    # you need get the frame rate  
    # and divide by size of your signal 
    # to create a Time Vector  
    # spaced linearly with the size  
    # of the audio file 
    time = np.linspace( 
        0, # start 
        len(signal) / f_rate, 
        num = len(signal) 
    ) 
  
    # using matplotlib to plot 
    # creates a new figure 
    plt.figure(1) 
      
    # title of the plot 
    plt.title("Sound Wave") 
      
    # label of x-axis 
    plt.xlabel("Time") 
     
    # actual plotting 
    plt.plot(time, signal) 
      
    # shows the plot  
    # in new window 
    plt.show() 
  
    # you can also save 
    # the plot using 
    # plt.savefig('filename') 




form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 3 # seconds to record
dev_index = 1 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file
#
audio = pyaudio.PyAudio() # create pyaudio instantiation

# create pyaudio stream
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)
print("recording")
frames = []
ampl =[]
# loop through stream and append audio chunks to frame array
for ii in range(0,int((samp_rate/chunk)*record_secs)):
    data = stream.read(chunk)
    print(data[0:20])
    print(data[0:2])
    #print(data[1:3])
    #print(data[2])
    print(int.from_bytes(data[0:1], "big"))
    ampl.append(int.from_bytes(data[0:2], "big"))
    frames.append(data)
print("LENGTH "+str(len(data)))
print("finished recording")

# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()

# save the audio frames as .wav file
wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()
plt.figure()
plt.plot(ampl)
plt.show()
visualize(wav_output_filename)