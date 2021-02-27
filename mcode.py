import wave
import math
import struct 

mdict = {
    "a": ". - ",
    "b": "- . . . ",
    "c": "- . - . ",
    "d": "- . . ",
    "e": ". ",
    "f": ". . - . ",
    "g": "- - . ",
    "h": ". . . . ",
    "i": ". . ",
    "j": ". - - - ",
    "k": "- . - ",
    "l": ". - . . ",
    "m": "- - ",
    "n": "- . ",
    "o": "- - - ",
    "p": ". - - . ",
    "q": "- - . - ",
    "r": ". - . ",
    "s": ". . . ",
    "t": "- ",
    "u": ". . - ",
    "v": ". . . - ",
    "w": ". - - ",
    "x": "- . . - ",
    "y": "- . - - ",
    "z": "- - . . ",
    "1": ". - - - - ",
    "2": ". . - - - ",
    "3": ". . . - - ",
    "4": ". . . . - ",
    "5": ". . . . . ",
    "6": "- . . . . ",
    "7": "- - . . . ",
    "8": "- - - . . ",
    "9": "- - - - . ",
    "0": "- - - - - ",
    " ": "     "
}

print("only allowed: a-z, A-Z, 0-9, space")
inp_text = str.lower(input("Enter string text to convert to morse code:"))
freq = int(input("Enter sound frequency:"))
fname = input("Enter full file name:")
mcode = []
for c in inp_text:
    mcode.append(mdict.get(c, ""))
    mcode.append("  ")
print("generating morse code...")
t = 3307
sr = 44100
channels = 1
swidth = 2
comptype = "NONE"
compname = "not compressed"

samples = []

mlist = list("".join(mcode))
print("generating sound file...")
for c in mlist:
    if c == ".":
        for i in range(t):
            samples.append(math.sin(2*math.pi*freq*(i/sr)))
    elif c == "-":
        for i in range(3*t):
            samples.append(math.sin(2*math.pi*freq*(i/sr)))
    elif c == " ":
        for i in range(t):
            samples.append(0)

nframes = len(samples)

f = wave.open(fname, "w")
f.setparams((channels, swidth, sr, nframes, comptype, compname))

for s in samples:
    f.writeframes(struct.pack("h", int(32767*s)))

f.close()

print("done.")