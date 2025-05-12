import h5py
import numpy as np
from astropy.io import fits

# ✅ Update this path if needed
# hdf5_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/chat gpt final/y3_redmapper_v6.4.22+2_release.h5"
hdf5_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/s.h5"
fits_output_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/s.fits"

# Open the file and extract all datasets from 'catalog/cluster'
with h5py.File(hdf5_path, 'r') as f:
    group = f['catalog/cluster']
    data = {name: group[name][:] for name in group}

# Prepare FITS columns
cols = []
for name, array in data.items():
    if array.ndim == 1:
        # Simple 1D array
        fmt = 'D' if array.dtype.kind in {'f', 'd'} else 'K'
        cols.append(fits.Column(name=name.upper(), array=array, format=fmt))
    elif array.ndim == 2:
        # 2D array, split each column
        for i in range(array.shape[1]):
            col_name = f"{name.upper()}_{i}"
            fmt = 'D' if array.dtype.kind in {'f', 'd'} else 'K'
            cols.append(fits.Column(name=col_name, array=array[:, i], format=fmt))
    else:
        print(f"Skipping {name} with shape {array.shape}")

# Create and write the FITS file
hdu = fits.BinTableHDU.from_columns(cols)
hdu.writeto(fits_output_path, overwrite=True)

print(f"FITS file saved at: {fits_output_path}")
