import numpy as np
import librosa
import soundfile as sf
from scipy.signal import butter, lfilter
import tensorflow as tf
from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from sklearn.decomposition import NMF

# Load audio file
audio_path = 'suarahalo.wav'
waveform, sample_rate = librosa.load(audio_path)

# Computasi FFT
fft = np.fft.fft(waveform)

# Computasi  magnitude
magnitude = np.abs(fft)

# Hitung frekuensi yang sesuai dengan komponen FFT
frequencies = np.fft.fftfreq(len(waveform), 1 / sample_rate)

# Plot Hasil FFT
import matplotlib.pyplot as plt

plt.plot(frequencies, magnitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('FFT of suarahalo.wav')
plt.show()

audio_path = 'suarahalo.wav'
waveform, sample_rate = librosa.load(audio_path)

# Hitung spektrogram
spectrogram = librosa.stft(waveform)
magnitude = librosa.amplitude_to_db(np.abs(spectrogram))

# Display spektogram
plt.figure(figsize=(12, 6))
librosa.display.specshow(magnitude, sr=sample_rate, x_axis='time', y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram of suarahalo.wav')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()



# Load audio file
# Pada command ini, file audio dengan nama 
# 'suarahalo.wav' dimuat menggunakan fungsi librosa.load(). 
# Data audio disimpan dalam variabel waveform, sedangkan nilai 
# frekuensi sampel disimpan dalam sample_rate.
audio_path = 'suarahalo.wav'
waveform, sample_rate = librosa.load(audio_path)

# Terapkan filter low-pass untuk menghilangkan noise frekuensi tinggi.
cutoff_frequency = 2000  # Sesuaikan frekuensi cutoff sesuai kebutuhan.
normalized_cutoff = cutoff_frequency / (sample_rate / 2)
b, a = butter(1, normalized_cutoff, btype='lowpass')
filtered_waveform = lfilter(b, a, waveform)

# Simpan audio yang sudah jadi
sf.write('halofilter_lowpass.wav', filtered_waveform, sample_rate)



# Load audio files:
speech, sr = librosa.load('halofilter_lowpass.wav')
noise, _ = librosa.load('suarahalo.wav', sr=sr)

# Menghitung spektrogram daya dari suara dan noise:
speech_power = np.abs(librosa.stft(speech)) ** 2
noise_power = np.abs(librosa.stft(noise)) ** 2

# Mengestimasi spektrogram daya dari noise:
noise_mean = np.mean(noise_power, axis=1)
noise_power = np.tile(noise_mean, (speech_power.shape[1], 1)).T

# Menghitung rasio antara daya suara dan daya noise (SNR ratio):
snr_ratio = speech_power / noise_power

# Menerapkan threshold untuk memasker noise:
mask = snr_ratio >= 3.0

# Menerapkan mask pada spektrogram daya suara:
enhanced_speech_power = speech_power * mask

# Merekonstruksi sinyal suara yang telah ditingkatkan:
enhanced_speech = librosa.istft(np.sqrt(enhanced_speech_power) * np.exp(1j * np.angle(librosa.stft(speech))))

# Save sound yang sudah jadi
sf.write('suarasnrpass.wav', enhanced_speech, sr)



# Load audio files:
enhanced_speech, sr = librosa.load('suarasnrpass.wav')
noise, _ = librosa.load('suarahalo.wav', sr=sr)

# Menghitung spektrogram daya dari suara dan noise:
speech_power = np.abs(librosa.stft(enhanced_speech)) ** 2
noise_power = np.abs(librosa.stft(noise)) ** 2

# Mengestimasi spektrogram daya dari noise:
noise_mean = np.mean(noise_power, axis=1)
noise_power = np.tile(noise_mean, (speech_power.shape[1], 1)).T

# Menghitung spektrogram daya dari suara dan noise:
snr_ratio = speech_power / noise_power

# Menghitung rasio antara daya suara dan daya noise (SNR ratio):
mask = snr_ratio >= 3.0

# Menerapkan threshold untuk memasker noise:
enhanced_speech_power = speech_power * mask

# Mengubah spektrogram daya suara yang telah ditingkatkan:
enhanced_speech_power = enhanced_speech_power ** alpha

# Merekonstruksi sinyal suara yang telah ditingkatkan:
enhanced_speech = librosa.istft(np.sqrt(enhanced_speech_power) * np.exp(1j * np.angle(librosa.stft(enhanced_speech))))

# Save sound yang sudah jadi
sf.write('suarasnrpass_emphasized.wav', enhanced_speech, sr)



# Load audio file
audio_path = 'suarasnrpass_emphasized.wav'
waveform, sample_rate = librosa.load(audio_path)

# Compute the spectrogram
spectrogram = librosa.stft(waveform)
magnitude = librosa.amplitude_to_db(np.abs(spectrogram))

# Display the spectrogram
plt.figure(figsize=(12, 6))
librosa.display.specshow(magnitude, sr=sample_rate, x_axis='time', y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram of halofilter_lowpass.wav')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()


# List of audio files
audio_files = ['suarahalo.wav', 'halofilter_lowpass.wav', 'suarasnrpass.wav', 'suarasnrpass_emphasized.wav']

# Plot the spectrogram for each audio file
plt.figure(figsize=(12, 8))

for i, audio_file in enumerate(audio_files):
    # Load audio file
    waveform, sample_rate = librosa.load(audio_file)
    
    # Compute the spectrogram
    spectrogram = librosa.stft(waveform)
    magnitude = librosa.amplitude_to_db(np.abs(spectrogram))
    
    # Plot the spectrogram
    plt.subplot(2, 2, i+1)
    librosa.display.specshow(magnitude, sr=sample_rate, x_axis='time', y_axis='linear')
    plt.colorbar(format='%+2.0f dB')
    plt.title(audio_file)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    
plt.tight_layout()
plt.show()