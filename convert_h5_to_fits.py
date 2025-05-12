import h5py
import numpy as np
from astropy.io import fits

# Path to the HDF5 input file
# hdf5_file_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/chat gpt final/y3_redmapper_v6.4.22+2_release.h5"
# hdf5_file_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/chat gpt final "
# h5fs_file_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/chat gpt final/Vy3_redmapper_v6.4.22z2_release.h5"
# hdf5_file_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/chat gpt final/y3_redmapper_v6.4.22+2_release.h5 "
hdf5_file_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/s.h5"
# Output path for the FITS file
fits_output_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/s.fits"

# Open and read the HDF5 file
with h5py.File(hdf5_file_path, 'r') as f:
    ra = f['catalog/cluster/ra'][:]
    dec = f['catalog/cluster/dec'][:]
    z_lambda = f['catalog/cluster/z_lambda'][:]
    z_lambda_e = f['catalog/cluster/z_lambda_e'][:]
    lambda_chisq = f['catalog/cluster/lambda_chisq'][:]
    m200m = f['catalog/cluster/m200m'][:]
    maskfrac = f['catalog/cluster/maskfrac'][:]
    id_cent = f['catalog/cluster/id_cent'][:]

# Create FITS columns
cols = fits.ColDefs([
    fits.Column(name='RA', array=ra, format='D'),
    fits.Column(name='DEC', array=dec, format='D'),
    fits.Column(name='Z_LAMBDA', array=z_lambda, format='E'),
    fits.Column(name='Z_LAMBDA_E', array=z_lambda_e, format='E'),
    fits.Column(name='LAMBDA_CHISQ', array=lambda_chisq, format='E'),
    fits.Column(name='M200M', array=m200m, format='E'),
    fits.Column(name='MASKFRAC', array=maskfrac, format='E'),
    fits.Column(name='ID_CENT_0', array=id_cent[:, 0], format='K'),  # First central galaxy ID
])

# Create the FITS HDU and write the file
hdu = fits.BinTableHDU.from_columns(cols)
hdu.writeto(fits_output_path, overwrite=True)

print(f"FITS file created at: {fits_output_path}")
