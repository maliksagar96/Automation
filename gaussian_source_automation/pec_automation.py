import json
import numpy as np
import os
import shutil

# Update frequency, number of iterations, and sampling interval in the JSON config file.
def change_json_inputs(filename, new_freq, iteration):
  # Load the JSON file.
  with open(filename, 'r') as file:
    data = json.load(file)

  # Update wave frequency in all relevant fields.
  data["boundary_condition"][0]["wave_frequency"] = new_freq
  data["incident_field"]["wave_frequency"] = new_freq
  data["peripheral_operation"]["frequency_domain_analysis"]["surface_data"]["distributed"][0]["frequency"] = new_freq

  # Update iteration count, update frequency, and modify target in the copy script.
  data["simulation_control"]["number_of_iteration"] = iteration
  data["simulation_control"]["update_frequency"] = int(np.ceil(iteration / 20))
  update_next_target("copy_cgns_based_on_iteration.sh", int(np.floor(iteration / 20)) + 2)

  # Update frequency-domain sampling interval.
  data["peripheral_operation"]["frequency_domain_analysis"]["surface_data"]["sampling_interval"] = int(np.floor(iteration / 20))

  # Save the modified JSON file.
  with open(filename, 'w') as file:
    json.dump(data, file, indent=2)

# Modify the target iteration value in the copy script.
def update_next_target(filename, new_target):
  # Read the shell script.
  with open(filename, "r") as file:
    lines = file.readlines()
  
  # Locate and update the next_target line.
  for i, line in enumerate(lines):
    if line.strip().startswith("next_target"):
      lines[i] = f"next_target={new_target}\n"
      break

  # Write back the updated script.
  with open(filename, "w") as file:
    file.writelines(lines)

# Define base directory, filenames for control and script files.
directory = "PEC/"
control_file_name = "control_file_pec.scf"
script_file_name = "copy_cgns_based_on_iteration.sh"

# Define case folders, frequencies, and iteration counts.
file_dir = ["1.7e9", "1.8e9", "2.1e9", "2.2e9", "2.3e9"]
frequency = [1.7e9, 1.8e9, 2.1e9, 2.2e9, 2.3e9]
iterations = [19000, 17940, 15380, 14680, 14040]

for i in range(len(file_dir)):
  # Create a folder for each simulation case.
  os.makedirs(directory + file_dir[i], exist_ok=True)

  # Modify inputs and copy the control and script files into the respective folder.
  change_json_inputs(control_file_name, frequency[i], iterations[i])
  shutil.copy(control_file_name, directory + file_dir[i])
  shutil.copy(script_file_name, directory + file_dir[i])
