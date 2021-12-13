from pydub import AudioSegment
from pydub.playback import play

sound1 = AudioSegment.from_file("test.wav")
sound1_channels = sound1.split_to_mono()
sound1 = sound1_channels[0].overlay(sound1_channels[1])
sound1 = sound1 - 30  # make sound1 quiter 30dB so that noise is clearly hearable


import pyaudio
MODE = "NOISE_CANCELING_OFF"

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

audio = pyaudio.PyAudio()
player = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

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

audio.input_device_index = MICROPHONEINDEX

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print("recording...")


# chunk_time_in_seconds = int(RATE/CHUNK)
chunk_number = 0


if MODE == "NOISE_CANCELING_ON":
    while (True):
        mic_data = stream.read(CHUNK)
        mic_sound = AudioSegment(mic_data, sample_width=2, channels=1, frame_rate=RATE)
        mic_sound_duration = len(mic_sound)

        sound1_part = sound1[chunk_number * mic_sound_duration:(chunk_number + 1) * mic_sound_duration]
        sound3 = mic_sound.invert_phase()

        mix_sound = sound1_part.overlay(sound3).overlay(mic_sound)
        noise_sound = sound3
        player.write(mix_sound.raw_data)


        chunk_number = chunk_number + 1
elif MODE == "NOISE_CANCELING_OFF":
    while (True):
        mic_data = stream.read(CHUNK)
        mic_sound = AudioSegment(mic_data, sample_width=2, channels=1, frame_rate=RATE)
        mic_sound_duration = len(mic_sound)

        sound1_part = sound1[chunk_number * mic_sound_duration:(chunk_number + 1) * mic_sound_duration]

        mix_sound = sound1_part.overlay(mic_sound)
        player.write(mix_sound.raw_data)

        chunk_number = chunk_number + 1