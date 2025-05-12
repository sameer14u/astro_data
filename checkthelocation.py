import os
hdf5_file_path = "/Users/sameerchoudhary/Desktop/PROJECT 1/s.h5"
if not os.path.exists(hdf5_file_path):
    print("File NOT found:", hdf5_file_path)
    exit(1)
else:
    print("File found:", hdf5_file_path)
