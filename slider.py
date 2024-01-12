import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import spectral as sp

#image = sp.open_image('/media/markus/Business/Datasets/Balke_Hyperspectral/few_layers_part/1_meter/rad/_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T125814_raw_rad.hdr') #Hyspex
image = sp.open_image('/media/markus/Business/Datasets/Peder Balke Centre/Specim IQ Data/2022-11-02_006/results/REFLECTANCE_2022-11-02_006.hdr') #Specim Results
#image = sp.open_image('/media/markus/Business/Datasets/Peder Balke Centre/Specim IQ Data/2022-11-02_006/capture/2022-11-02_006.hdr') #Specim Capture
num_bands = image.shape[-1]

# Initialize the band index to 0
band_idx = 0

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
ax_band = plt.axes([0.25, 0.1, 0.65, 0.03])
band_slider = Slider(ax_band, 'Band', 0, num_bands-1, valinit=0)

# Function to update the image displayed based on the slider value
def update(val):
   global band_idx
   band_idx = int(val)
   band_img = image[:, :, band_idx]
   ax.imshow(band_img, cmap='jet') # Can also use 'hot' or 'gray'
   fig.canvas.draw_idle()

band_slider.on_changed(update)
update(band_slider.val)
plt.show()
