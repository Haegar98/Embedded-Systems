from pydub import AudioSegment
from pydub.playback import play

sound1 = AudioSegment.from_file("moonlight_sonata.wav")
sound1_channels = sound1.split_to_mono()
sound1 = sound1_channels[0].overlay(sound1_channels[1])
sound1 = sound1 + 10 # make sound1 quiter 30dB so that noise is clearly hearable


import pyaudio
MODE = "NOISE_CANCELING_ON"

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024


audio = pyaudio.PyAudio()
audio2 = pyaudio.PyAudio()

player = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
player2 = audio2.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

MICROPHONENAME = "Realtek High Defini"
MICROPHONEINDEX = -1

MICROPHONENAME2 = "Realtek High Defini"
MICROPHONEINDEX2 = -1

def micro_selection(MICROPHONEINDEX, MICROPHONENAME, AUDIO):
    # Check all devices
    for i in range(AUDIO.get_device_count()):
        if AUDIO.get_device_info_by_index(i).get('name') == "Mikrofon ("+MICROPHONENAME:
            MICROPHONEINDEX = i
            print('mikrofon gefunden:')
            print(AUDIO.get_device_info_by_index(i))


    if MICROPHONEINDEX == -1:
        for i in range(AUDIO.get_device_count()):
            if AUDIO.get_device_info_by_index(i).get('name') == "Microphone ("+MICROPHONENAME:
                MICROPHONEINDEX = i
                print('microphone found:')
                print(AUDIO.get_device_info_by_index(i))

    # If device was not found list all devices
    if MICROPHONEINDEX == -1:
        print('No input device found with name:' + MICROPHONENAME)
        print('List of all Devices:')
        for i in range(AUDIO.get_device_count()):
            print(AUDIO.get_device_info_by_index(i))

    AUDIO.input_device_index = MICROPHONEINDEX

def audio_recording(AUDIO, MODE):
    # start Recording
    stream = AUDIO.open(format=FORMAT, channels=CHANNELS,
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

    elif MODE == "NOISE_CANCELING_ONLY":
        while (True):
            mic_data = stream.read(CHUNK)
            mic_sound = AudioSegment(mic_data, sample_width=2, channels=1, frame_rate=RATE)
            mic_sound_duration = len(mic_sound)

            sound1_part = sound1[chunk_number * mic_sound_duration:(chunk_number + 1) * mic_sound_duration]
            sound3 = mic_sound.invert_phase()

            mix_sound = sound1_part.overlay(sound3)
            player.write(mix_sound.raw_data)

            chunk_number = chunk_number + 1

    elif MODE == "ONLY_MIC":
            while (True):
                mic_data = stream.read(CHUNK)
                mic_sound = AudioSegment(mic_data, sample_width=2, channels=1, frame_rate=RATE)
                mic_sound_duration = len(mic_sound)

                sound1_part = sound1[chunk_number * mic_sound_duration:(chunk_number + 1) * mic_sound_duration]
                sound3 = mic_sound

                mix_sound = sound3
                player.write(mix_sound.raw_data)

                chunk_number = chunk_number + 1

    elif MODE == "ONLY_MUSIC":
            while (True):
                mic_data = stream.read(CHUNK)
                mic_sound = AudioSegment(mic_data, sample_width=2, channels=1, frame_rate=RATE)
                mic_sound_duration = len(mic_sound)

                sound1_part = sound1[chunk_number * mic_sound_duration:(chunk_number + 1) * mic_sound_duration]

                mix_sound = sound1_part
                player.write(mix_sound.raw_data)

                chunk_number = chunk_number + 1