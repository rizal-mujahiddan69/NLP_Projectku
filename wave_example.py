import wave
obj = wave.open("curious.wav","rb")

print("Number of channels",obj.getnchannels())
print("Sample width",obj.getsampwidth())
print("frame rate",obj.getframerate())
print("Number of Frames",obj.getnframes())
print("Parameters",obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames)/2)

obj_new = wave.open("curious_new.wav","wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)
obj_new.close()