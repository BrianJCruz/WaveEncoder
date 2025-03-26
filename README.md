# Signal Wave Encoder for PSK, FSK and ASK with Fourier's visualizer

Fourier's Visualizer example:

<img src="https://github.com/user-attachments/assets/348005fd-0cf6-4b29-a78b-2474351ce4f3" width=620>



Signal Wave Encoder example:

<img src="https://github.com/user-attachments/assets/e610b6c4-3b3a-417c-b039-e0715627ddde" width=620>

This Python script creates an interactive visualization of a Fourier-based waveform using `matplotlib` as well as for PSK, FSK and ASK encoding methods; Users can adjust the frequency and the number of cycles via sliders, dynamically updating the plotted signal.

## Dependencies
The script uses:
- `numpy` for mathematical operations
- `matplotlib.pyplot` for plotting
- `matplotlib.widgets` for interactive UI elements (sliders and buttons)

## Class: `SignalPlot`
The `SignalPlot` class handles the generation and display of the waveform.

### Constructor (`__init__`)
```python
def __init__(self, f = 1, k = 10, initTime = 0, endTime = 2, ptAccuracy = 800):
```
- `f`: Initial frequency of the wave (default: 1 Hz).
- `k`: Number of cycles considered in the Fourier series (default: 10).
- `initTime`, `endTime`: Time range for the plot.
- `ptAccuracy`: Number of points used for plotting.

---

### `getWaveValue(t, f, cycles)`
```python
def getWaveValue(t, f, cycles):
```
Computes the waveform using a Fourier series approximation:
\[
\sum \left(\frac{1}{k} \sin(2\pi k f t)\right)
\]
- Loops through values of `k` from `0` to `cycles`, filtering only **odd** values.
- Accumulates the sine wave contributions.
- Returns the computed signal value.

**Issue**: `getWaveValue` is missing `self` but is used as a static method.

---

### `update(self, val)`
```python
def update(self, val):
```
- Called when sliders are adjusted.
- Updates the plot with new values of frequency and cycles.
- Uses `draw_idle()` to refresh the figure efficiently.

---

### `reset(self, event)`
```python
def reset(self, event):
```
- Resets the sliders to their initial values.

---

### `start(self)`
```python
def start(self):
```
- Initializes the plot and user interface.
- Sets up:
  - A figure and axis for the plot.
  - A time array `t` for the x-axis.
  - An initial waveform plot.
  - Interactive sliders for frequency and cycles.
  - A reset button.
- Calls `plt.show()` to display the interactive plot.

---

## Execution
The script creates an instance of `SignalPlot` and starts the interactive plot:
```python
s = SignalPlot()
s.start()
```





