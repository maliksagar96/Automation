import shutil
import os

#base directory
base_dir = "2.2e9"
target_dir = ["2.1e9", "2.3e9"]


# Files to copy
files_to_copy = [
    "control_file.scf",
    "copy_cgns_based_on_iteration.sh",
    "dipole_aperture.cgns",
    "ref_sruface.stl"
]

for target in target_dir:
  os.makedirs(target)
  for file in files_to_copy:
    src_path = os.path.join(base_dir, file)
    dst_path = os.path.join(target, file)
    shutil.copy(src_path, dst_path)


    