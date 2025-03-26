import numpy as np
import matplotlib.pyplot as plt



bit_sequence = [int(number) for number in input("Bit sequence: ")]

               
bit_duration = 0.2                                # Duracion de cada bit en segundos
sampling_rate = 1000                              # Frecuencia de muestreo en Hz
fc = 10                                           # Frecuencia carrier para ASK y PSK
f0 = 10                                           # Frecuencia para bit 0 en FSK
f1 = 20                                           # Frecuencia para bit 1 en FSK
A = 1                                             # Amplitud 


samples_per_bit = int(bit_duration * sampling_rate)
total_samples = len(bit_sequence) * samples_per_bit
total_time = len(bit_sequence) * bit_duration
t = np.linspace(0, total_time, total_samples, endpoint=False)


signal_ask = np.array([])
signal_psk = np.array([])
signal_fsk = np.array([])


for i, bit in enumerate(bit_sequence):

    t_bit = np.linspace(i * bit_duration, (i + 1) * bit_duration, samples_per_bit, endpoint=False)
    
    # ASK: Amplitud A para 1, 0 para 0
    carrier_ask = -np.cos(2 * np.pi * fc * t_bit + np.pi/2)
    ask = A * carrier_ask if bit == 1 else 0 * carrier_ask
    signal_ask = np.concatenate((signal_ask, ask))
    
    # PSK: Fase 0 para 0, π para 1
    phase = 0 if bit == 0 else np.pi
    psk = np.cos(2 * np.pi * fc * t_bit + phase + np.pi/2)
    signal_psk = np.concatenate((signal_psk, psk))
    
    # FSK: Frecuencia f0 para 0, f1 para 1
    freq = f0 if bit == 0 else f1
    fsk = -np.cos(2 * np.pi * freq * t_bit + np.pi/2)
    signal_fsk = np.concatenate((signal_fsk, fsk))



plt.figure(figsize=(12, 8))

# ASK
plt.subplot(3, 1, 1)
plt.plot(t, signal_ask)
plt.title('ASK')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

# PSK
plt.subplot(3, 1, 2)
plt.plot(t, signal_psk)
plt.title('PSK')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

# FSK
plt.subplot(3, 1, 3)
plt.plot(t, signal_fsk)
plt.title('FSK')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.tight_layout()
plt.show()
