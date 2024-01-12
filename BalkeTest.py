import spectral as sp
import matplotlib.pyplot as plt
from matplotlib.widgets import slider

# specify the paths to your .hdr file and .hyspex data file
all_30_hdr_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/all_layers_part/30_cm/30_cm_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T132131_raw.hdr'
all_30_data_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/all_layers_part/30_cm/30_cm_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T132131_raw.hyspex'  # replace with the actual .hyspex file name
all_30_img = sp.envi.open(all_30_hdr_file, all_30_data_file)

all_30_w_hdr_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/all_layers_part/30_cm/white_ref_30_cm_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T131933_raw.hdr'
all_30_w_data_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/all_layers_part/30_cm/white_ref_30_cm_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T131933_raw.hyspex'
all_30_w_img = sp.envi.open(all_30_w_hdr_file, all_30_w_data_file)

all_1m_30d_hdr_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/all_layers_part/1_meter/30deg/_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T122359_raw.hdr'
all_1m_30d_data_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/all_layers_part/1_meter/30deg/_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T122359_raw.hyspex'
all_1m_30d_img = sp.envi.open(all_1m_30d_hdr_file, all_1m_30d_data_file)

all_1m_60d_hdr_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/all_layers_part/1_meter/60deg/_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T122825_raw.hdr'
all_1m_60d_data_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/all_layers_part/1_meter/60deg/_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T122825_raw.hyspex'
all_1m_60d_img = sp.envi.open(all_1m_60d_hdr_file, all_1m_60d_data_file)

all_1m_w_hdr_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/all_layers_part/1_meter/white_ref/_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T124034_raw.hdr'
all_1m_w_data_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/all_layers_part/1_meter/white_ref/_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T124034_raw.hyspex'
all_1m_w_img = sp.envi.open(all_1m_w_hdr_file, all_1m_w_data_file)

few_1m_hdr_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/few_layers_part/1_meter/white_ref_and_few_layers_part/_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T125814_raw.hdr'
few_1m_data_file = r'/media/markus/Business/Datasets/Balke_Hyperspectral/few_layers_part/1_meter/white_ref_and_few_layers_part/_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T125814_raw.hyspex'
few_1m_img = sp.envi.open(few_1m_hdr_file, few_1m_data_file)

#few_30_hdr_file =
#few_30_data_file =
#feq_30_img = envi.open(few_30_hdr_file, few_30_data_file)

# display the band data
band_data = few_1m_img.read_band(150)

plt.imshow(band_data, cmap='gray')
plt.show()
