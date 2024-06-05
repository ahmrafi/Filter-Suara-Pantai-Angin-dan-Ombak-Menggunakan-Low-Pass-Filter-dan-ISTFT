# Filter Suara Pantai Angin dan Ombak Menggunakan Low Pass Filter dan ISTFT

## Masalah

Pantai adalah tempat yang indah dengan suara angin dan ombak yang menenangkan. Namun, saat merekam audio di sekitar pantai, seringkali terdapat gangguan suara yang dapat mengaburkan suara asli angin dan ombak tersebut. Gangguan tersebut dapat berasal dari berbagai sumber, seperti suara manusia, lalu lintas, atau peralatan pantai.

Gangguan suara ini menjadi masalah serius bagi para penggemar pantai yang ingin merekam atau memperdengarkan suara alam yang murni dan menenangkan. Oleh karena itu, diperlukan solusi yang dapat membantu menghilangkan atau mengurangi gangguan suara tersebut, sehingga suara angin dan ombak dapat dinikmati dengan lebih baik.

## Urgensi

Pengembangan filter suara pantai angin dan ombak menggunakan Low Pass Filter dan Inverse Short-Time Fourier Transform (ISTFT) menjadi penting karena beberapa alasan:

1. **Kualitas audio**: 
   - Dalam berbagai konteks, seperti produksi musik, film, meditasi, atau aplikasi relaksasi, kualitas audio yang baik sangat penting. Dengan menggunakan filter suara yang efektif, rekaman suara pantai dapat ditingkatkan kualitasnya dengan menghilangkan gangguan suara dan memperkuat suara angin dan ombak yang diinginkan.

2. **Kemajuan teknologi**: 
   - Kemajuan dalam pemrosesan sinyal digital dan algoritma pengolahan suara memberikan kesempatan untuk mengembangkan metode yang lebih canggih dalam filterisasi suara pantai. Mengkombinasikan Low Pass Filter dan ISTFT dapat membantu dalam mengurangi gangguan suara yang tidak diinginkan dan memisahkan suara angin dan ombak dari sumber gangguan.

## Tujuan

Tujuan proyek ini adalah mengembangkan filter suara pantai angin dan ombak menggunakan kombinasi Low Pass Filter dan ISTFT untuk meningkatkan kualitas rekaman suara pantai. Filter ini bertujuan untuk mengurangi atau menghilangkan gangguan suara yang tidak diinginkan, seperti suara manusia, kendaraan, atau peralatan pantai, sehingga menghasilkan rekaman yang lebih jernih dan lebih menyerupai pengalaman nyata di pantai.

Dengan berhasil mengembangkan filter ini, diharapkan rekaman suara pantai dapat digunakan dalam berbagai aplikasi, termasuk produksi musik, film, meditasi, dan aplikasi relaksasi. Filter ini akan membantu mempertahankan keaslian suara alam pantai, memberikan pengalaman yang lebih mendalam bagi pendengar, dan meningkatkan kualitas audio secara keseluruhan.

## Filter yang Digunakan

### ISTFT (Inverse Short-Time Fourier Transform)

ISTFT adalah kebalikan dari STFT (Short-Time Fourier Transform). ISTFT digunakan untuk merekonstruksi sinyal waktu-domain dari representasi frekuensi-domain yang diperoleh melalui STFT. STFT membagi sinyal audio menjadi segmen-segmen kecil dan menghitung transformasi Fourier untuk setiap segmen. Ini menghasilkan representasi frekuensi-domain dari sinyal audio dalam bentuk spektrogram. ISTFT melakukan langkah-langkah yang berkebalikan untuk mengembalikan sinyal audio dalam domain waktu dari spektrogram.

### Low-pass Filter

Low-pass filter adalah jenis filter yang memungkinkan melewatkannya hanya frekuensi yang lebih rendah dari frekuensi cutoff tertentu. Filter ini mengurangi atau menghilangkan komponen frekuensi tinggi dalam sinyal audio, sehingga memungkinkan melewatkannya hanya pada komponen frekuensi yang lebih rendah. Dalam konteks ini, low-pass filter digunakan untuk menghilangkan atau meredam noise frekuensi tinggi dalam sinyal audio, sehingga membantu meningkatkan kualitas sinyal audio dengan fokus pada komponen suara yang lebih penting. 

Dalam kode yang diberikan, filter low-pass diterapkan menggunakan fungsi `butter()` dan `lfilter()` untuk menghilangkan noise frekuensi tinggi sebelum melakukan ISTFT pada sinyal audio.

Library yang digunakan

```
import numpy as np
import librosa
import soundfile as sf
from scipy.signal import butter, lfilter
import tensorflow as tf
from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from sklearn.decomposition import NMF
```

