import realtimeInputTest as realtime
import pyaudio
from pydub import AudioSegment
from pydub.playback import play

sound1 = AudioSegment.from_file("moonlight_sonata.wav")
sound1_channels = sound1.split_to_mono()
sound1 = sound1_channels[0].overlay(sound1_channels[1])
# sound1 = sound1 - 30  # make sound1 quiter 30dB so that noise is clearly hearable


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

def main():
    realtime.micro_selection(MICROPHONEINDEX, MICROPHONENAME, audio)
    realtime.audio_recording(audio, MODE)

if __name__ == "__main__":
    main()