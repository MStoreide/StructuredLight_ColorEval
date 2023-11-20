import spectral.io.envi as envi
import matplotlib.pyplot as plt

# specify the paths to your .hdr file and .hyspex data file
hdr_file = r'/home/markus/_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T125814_raw.hdr'
data_file = r'/home/markus/_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T125814_raw.hyspex'  # replace with the actual .hyspex file name

# open the image
img = envi.open(hdr_file, data_file)

# display the band data
band_data = img.read_band(100)

plt.imshow(band_data, cmap='gray')
plt.show()
