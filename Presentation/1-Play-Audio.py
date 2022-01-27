import pyaudio
import wave
import time

filename = '../Src//moonlight_sonata.wav'
chunkSize = 8


# Open music file
waveFile = wave.open(filename, 'rb')
print(pyaudio.get_format_from_width(waveFile.getsampwidth()))
# Create an instance of Pyaudio
pyaudio = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = pyaudio.open(format=pyaudio.get_format_from_width(waveFile.getsampwidth()),
                      channels=waveFile.getnchannels(),
                      rate=waveFile.getframerate(),
                      output=True)

# Read data in chunks of 1024 Byte
audioData = waveFile.readframes(chunkSize)

# Play the sound by writing the audio data to the stream
timeFrame = time.perf_counter()
for x in range(10000): # for testing
# while audioData != '': # for testing
#     print("execute", x)
    print(audioData)
    stream.write(audioData)
    audioData = waveFile.readframes(chunkSize)
exactTime = time.perf_counter() - timeFrame
print("exactTime", exactTime)
# Close and terminate the stream
stream.close()
pyaudio.terminate()
