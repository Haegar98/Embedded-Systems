from pydub import AudioSegment
import pyaudio
from pydub.playback import play

sound1 = AudioSegment.from_file("../Src//moonlight_sonata.wav")
sound1 = sound1 + 10


sound1_channels = sound1.split_to_mono()
sound1 = sound1_channels[0].overlay(sound1_channels[1])

FORMAT = 8
CHANNELS = 1
RATE = 44100
CHUNK = 1024
MICROPHONEINDEX = -1

MODE= "CANCEL_ON"

pyAudio = pyaudio.PyAudio()

player = pyAudio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

pyAudio.input_device_index = 2
stream = pyAudio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

chunk_number = 1
while (True):
    mic_data = stream.read(CHUNK, exception_on_overflow = False)
    mic_sound = AudioSegment(mic_data, sample_width=2, channels=1, frame_rate=RATE)

    mic_sound_duration = len(mic_sound)
    sound1_part = sound1[chunk_number * mic_sound_duration:(chunk_number + 1) * mic_sound_duration]
    mix_sound = sound1_part.overlay(mic_sound)
    chunk_number = chunk_number + 1

    player.write(mix_sound.raw_data)