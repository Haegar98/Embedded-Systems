import time

from pydub import AudioSegment
import pyaudio
from pydub.playback import play

sound1 = AudioSegment.from_file("../Src//moonlight_sonata.wav")
sound2 = AudioSegment.from_file("../Src//radiostören.wav")
sound1 = sound1 + 10
sound2 = sound2 - 30  # make sound1 quiter 30dB so that noise is clearly hearable

sound1_channels = sound1.split_to_mono()
sound1 = sound1_channels[0].overlay(sound1_channels[1])

sound2_channels = sound2.split_to_mono()
sound2 = sound2_channels[0].overlay(sound2_channels[1])

FORMAT = 8
CHANNELS = 1
RATE = 44100
CHUNK = 128
MICROPHONEINDEX = -1

MODE= "CANCEL_ON"

pyAudio = pyaudio.PyAudio()

player = pyAudio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

pyAudio.input_device_index = 2
stream = pyAudio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

chunk_number = 1
if MODE == "CANCEL_OFF":
    mixSound = sound1.overlay(sound2)
    while (True):
        player.write(mixSound.get_frame(chunk_number))
        chunk_number = chunk_number +1

if MODE == "CANCEL_ON":
    while (True):
        timeFrame = time.perf_counter()

        mic_data = stream.read(CHUNK, exception_on_overflow = False)
        mic_sound = AudioSegment(mic_data, sample_width=2, channels=1, frame_rate=RATE)

        # mic_sound_duration = len(mic_sound)
        # sound1_part = sound1[chunk_number * mic_sound_duration:(chunk_number + 1) * mic_sound_duration]
        # mix_sound = sound1_part.overlay(mic_sound)
        #
        # chunk_number = chunk_number + 1
        player.write(mic_sound.raw_data)
        exactTime = time.perf_counter() - timeFrame
        print("exactTime", exactTime)
    #
    #     # player.write(mixSound.get_frame(chunkNumber))
    #     # chunkNumber = chunkNumber +1