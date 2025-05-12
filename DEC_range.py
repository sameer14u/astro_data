from astropy.io import fits
import numpy as np


des_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/des.fit"
erosita_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/eFEDS_clusters_V3.2.fits"
sdss_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/sdss.fit"

# Function to get sky coverage from a FITS file
def get_ra_dec_range(fits_path):
    with fits.open(fits_path) as hdul:
        data = hdul[1].data
        colnames = [c.name.upper() for c in hdul[1].columns]

        # Match RA and DEC column names (includes RAJ2000/DEJ2000)
        ra_col = next((c for c in colnames if c in ['RAJ2000', 'RA']), None)
        dec_col = next((c for c in colnames if c in ['DEJ2000', 'DEC']), None)

        if ra_col and dec_col:
            ra_vals = data[ra_col]
            dec_vals = data[dec_col]
            return {
                'file': fits_path,
                'RA_col': ra_col,
                'DEC_col': dec_col,
                'RA_min': float(np.min(ra_vals)),
                'RA_max': float(np.max(ra_vals)),
                'DEC_min': float(np.min(dec_vals)),
                'DEC_max': float(np.max(dec_vals))
            }
        else:
            return {
                'file': fits_path,
                'error': 'RAJ2000/RA or DEJ2000/DEC not found'
            }

# Run for each catalog
for path in [des_path, erosita_path, sdss_path]:
    result = get_ra_dec_range(path)
    print(result)

