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
CHUNK = 1024

MODE= "CANCEL_ON"

pyAudio = pyaudio.PyAudio()

player = pyAudio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
chunkNumber = 1

if MODE == "CANCEL_OFF":
    mixSound = sound1.overlay(sound2)
    while (True):
        player.write(mixSound.get_frame(chunkNumber))
        chunkNumber = chunkNumber +1

if MODE == "CANCEL_ON":
    sound3 = sound2.invert_phase()
    mixSound = (sound1.overlay(sound2)).overlay(sound3)
    while (True):
        player.write(mixSound.get_frame(chunkNumber))
        chunkNumber = chunkNumber +1