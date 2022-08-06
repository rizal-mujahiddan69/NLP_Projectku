from pydub import AudioSegment

audio = AudioSegment.from_wav("curious.wav")

# increase the volume by 6 dB
audio = audio + 6

audio = audio * 2

audio = audio.fade_in(2000)

audio.export("mashup.mp3",format="mp3")

audio = AudioSegment.from_mp3("mashup.mp3")
