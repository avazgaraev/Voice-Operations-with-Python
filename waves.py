import wave

obj = wave.open("StarWars3.wav", "rb")

print("channel numbers:", obj.getnchannels())
print("sample width:", obj.getsampwidth())
print("frame rate:", obj.getframerate())
print("number of frames:", obj.getnframes())
print("parameters:", obj.getparams())
print("readframe:", obj.readframes(-1))

t_audio = obj.getnframes() / obj.getframerate()

print(t_audio)

# frames = obj.readframes(-1)
# obj_wr = wave.open("NewRec.wav", "wb")

# obj_wr.setnchannels(1)
# obj_wr.setsampwidth(2)
# obj_wr.setframerate(40050.0)
# obj_wr.writeframes(frames)

# obj_wr.close()