import json
import numpy as np
import os
import shutil

# Changing the frequency and number of iterations.
def change_json_inputs(filename, new_freq, iteration):
  #Read the json file.
  with open(filename, 'r') as file:
    data = json.load(file)

  # Change the frequency where ever required.
  data["boundary_condition"][0]["wave_frequency"] = new_freq
  data["incident_field"]["wave_frequency"] = new_freq
  data["peripheral_operation"]["frequency_domain_analysis"]["surface_data"]["distributed"][0]["frequency"] = new_freq

  # Change number of Iterations, update frequency and in the copy cgns files script file.
  data["simulation_control"]["number_of_iteration"] = iteration
  data["simulation_control"]["update_frequency"] = int(np.ceil(iteration/20))
  update_next_target("copy_cgns_based_on_iteration.sh", int(np.floor((iteration)/20))+2)

  #Change sampling_frequency.
  data["peripheral_operation"]["frequency_domain_analysis"]["surface_data"]["sampling_interval"] = int(np.floor((iteration)/20))

  #Write the json file.
  with open(filename, 'w') as file:
    json.dump(data, file, indent=2)

# Updating the copy cgns file.
def update_next_target(filename, new_target):
  
  # Open script file.
  with open(filename, "r") as file:
    lines = file.readlines()
  
  # Modify the data.
  for i, line in enumerate(lines):
    if line.strip().startswith("next_target"):
      lines[i]=f"next_target={new_target}\n"
      break
  # Write the copy cgns file.      
  with open(filename, "w") as file:
    file.writelines(lines)

# File directories for different cases. Setting the frequency and iterations.
file_dir = ["1.7e9","1.8e9", "2.1e9", "2.2e9", "2.3e9"]
frequency = [1.7e9, 1.8e9, 2.1e9, 2.2e9, 2.3e9]
iterations = [15240,14380,12340,11780,11260]

for i in range(len(file_dir)):
  #Making the directories for different simulations
  os.makedirs("NO_PEC/" + file_dir[i], exist_ok=True)

  #Changing and copying the control file and copy cgns to each folder.
  change_json_inputs("control_file_no_pec.scf", frequency[i], iterations[i])
  shutil.copy("control_file_no_pec.scf", "NO_PEC/" + file_dir[i])
  shutil.copy("copy_cgns_based_on_iteration.sh", "NO_PEC/" + file_dir[i])


