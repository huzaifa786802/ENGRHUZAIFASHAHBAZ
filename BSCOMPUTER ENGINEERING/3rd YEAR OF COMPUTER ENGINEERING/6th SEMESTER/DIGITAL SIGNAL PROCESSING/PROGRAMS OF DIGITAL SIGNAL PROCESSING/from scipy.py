from scipy.io import wavfile

# Provide the full path to the brahms.wav file
audio_file = r'D:\BSCOMPUTER ENGINEERING\3rd YEAR OF COMPUTER ENGINEERING\6th SEMESTER\DIGITAL SIGNAL PROCESSING\PROGRAMS OF DIGITAL SIGNAL PROCESSING\brahms.wav'

# Read the WAV file
sr, audio_signal = wavfile.read(audio_file)

print("Sample rate:", sr)
print("Audio signal:", audio_signal)