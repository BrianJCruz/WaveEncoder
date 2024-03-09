import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

class SignalPlot:

    # Constructor
    def __init__(self, f = 1, k = 10, initTime = 0, endTime = 2, ptAccuracy = 800):

        # --- Fields ---
        self.f = f
        self.k = k
        self.initTime = initTime
        self.endTime = endTime
        self.ptAccuracy = ptAccuracy

    # Main method, function to graph
    def getWaveValue(t, f, cycles):

        # Using Fourier's equation
        # Σ [ 1/k sin( 2Π(kf)t ) ], where k is odd, k > 0 and k = ∞
        
        total = 0

        # For value in the domain
        for k in np.arange(0, cycles + 1, 0.1):
            
            # filter the odd values
            if k % 2 == 1:
                
                # Calculate and add them
                total += 1/k * np.sin(2 * np.pi * k * f * t)
                
        # Retrieve the total amount
        return total

    # Called when a slider is used
    def update(self, val):
        line.set_ydata( SignalPlot.getWaveValue(t, freqSlider.val, kSlider.val) )
        fig.canvas.draw_idle()

    def reset(self, event):
        freqSlider.reset()
        kSlider.reset()
          
    def start(self):
        
        global line
        global freqSlider
        global kSlider
        global fig
        global ax
        global fn
        global t

        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.35)
        t = np.linspace(self.initTime, self.endTime, self.ptAccuracy)
        fn = SignalPlot.getWaveValue(t, self.f, self.k)
        line, = ax.plot(t, fn, lw=2)
        
        ax.set_xlabel('Time [s]')

        # Define the 'Frequency' slider 
        position = fig.add_axes([0.25, 0.20, 0.45, 0.03])
        freqSlider = Slider(
            ax=position,
            label='Frequency [Hz]',
            valmin=0,
            valmax=20,
            valinit=self.f,
        )

        position = fig.add_axes([0.25, 0.15, 0.45, 0.03])
        kSlider = Slider(
            ax=position,
            label='Cycles',
            valmin=0,
            valmax=30,
            valinit=self.k,
        )

        # Define the 'k' slider
        # Define the 'End Time' slider
        # Define the 'Point Accuracy' slider 

        # Add callback function
        freqSlider.on_changed(self.update)
        kSlider.on_changed(self.update)
        
        # Define reset button
        position = fig.add_axes([0.8, 0.025, 0.1, 0.04])
        resetButton = Button(position, 'Reset', hovercolor='0.975')
        resetButton.on_clicked(self.reset)

        # Set grid lines visibility
        ax.grid(True)

        # Display Window
        plt.show()


s = SignalPlot()
s.start()
    
