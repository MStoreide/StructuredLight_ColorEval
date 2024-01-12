import spectral as sp

hdr = sp.envi.open(r'/media/markus/Business/Datasets/Balke_Hyperspectral/all_layers_part/30_cm/30_cm_SWIR_384_SN3189_HSNR1_7831us_2023-10-05T132131_raw.hdr')
wvl = hdr.bands.centers
rows, cols, bands = hdr.nrows, hdr.ncols, hdr.nbands
meta = hdr.metadata

step = 5
for x in range(0, rows, step):
   rows = hdr.read_subregion((x, x+step), (0, cols))
   print(rows)

