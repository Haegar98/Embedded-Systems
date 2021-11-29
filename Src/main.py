import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

MICROPHONENAME = "3- G533 Gaming Headse"
MICROPHONEINDEX = -1

# Check all devices
for i in range(audio.get_device_count()):
    if audio.get_device_info_by_index(i).get('name') == "Mikrofon ("+MICROPHONENAME:
        MICROPHONEINDEX = i
        print('microphone found:')
        print(audio.get_device_info_by_index(i))

# If device was not found list all devices
if MICROPHONEINDEX == -1:
    print('No input device found with name:' + MICROPHONENAME)
    print('List of all Devices:')
    for i in range(audio.get_device_count()):
        print(audio.get_device_info_by_index(i))

# TODO: Fehlermeldung wenn Format nicht übereinstimmt.
# TODO: Echzeitaufnahme eimspeisen statts speichern <==> abhängig von Falkos Ausgabeformat.
#       Eventuelle Visualisierung zur besseren Verarbeitung.
audio.input_device_index = MICROPHONEINDEX

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print("recording...")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("finished recording")
# print(frames)

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
