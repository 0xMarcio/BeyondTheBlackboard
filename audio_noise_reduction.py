import numpy as np
import matplotlib.pyplot as plt
import librosa

def plot_waveforms(original_audio, denoised_audio, sr):
    """
    Plot the original and denoised waveforms of an audio signal.

    Parameters:
    original_audio (np.ndarray): The original audio signal.
    denoised_audio (np.ndarray): The denoised audio signal.
    sr (int): Sample rate of the audio signal.
    """
    plt.figure(figsize=(12, 8))

    # Plot original audio waveform
    plt.subplot(2, 1, 1)
    times = np.arange(len(original_audio)) / sr
    plt.plot(times, original_audio)
    plt.title('Original Audio Waveform')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')

    # Plot denoised audio waveform
    plt.subplot(2, 1, 2)
    times = np.arange(len(denoised_audio)) / sr
    plt.plot(times, denoised_audio)
    plt.title('Denoised Audio Waveform')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

def reduce_noise(audio, sr):
    """
    Reduce noise from an audio signal using a basic spectral gating method.
    This is a simplified approach and might not be effective for all types of noise.

    Parameters:
    audio (np.ndarray): The audio signal
    sr (int): Sample rate of the audio signal

    Returns:
    audio_denoised (np.ndarray): The denoised audio signal
    """
    # Convert to frequency domain
    stft = librosa.stft(audio)
    magnitude, phase = librosa.magphase(stft)
    
    # Estimate the noise threshold
    mean = np.mean(magnitude, axis=1)
    threshold = mean + 0.5 * np.std(magnitude, axis=1)
    
    # Spectral gating
    magnitude[magnitude < np.tile(threshold[:, np.newaxis], (1, magnitude.shape[1]))] = 0

    # Convert back to time domain
    audio_denoised = librosa.istft(magnitude * phase)
    return audio_denoised

# Load an audio file
file_path = librosa.example('trumpet')  # Replace with your audio file path
audio, sample_rate = librosa.load(file_path)

# Perform noise reduction
audio_denoised = reduce_noise(audio, sample_rate)

# Visualize the original and denoised audio waveforms
plot_waveforms(audio, audio_denoised, sample_rate)

