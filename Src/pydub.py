import pydub
from pydub import AudioSegment
from pydub.playback import play

musicFile = "test.wav"
sound1 = AudioSegment.from_file(musicFile, format="wav")

noiseFile = "radiostören.wav"
sound2 = AudioSegment.from_file(noiseFile, format="wav")

sound3 = sound2.invert_phase()

combined = sound1.overlay(sound2.overlay(sound3))
combined.export("outAudio.wav", format="wav")
