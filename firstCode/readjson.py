import json
import re

def read_number_of_iteration(file_path):
    # Remove comments (since JSON spec doesn't allow them)
    with open(file_path, 'r') as file:
        content = file.read()
      
    # Parse as JSON
    data = json.loads(content)
    
    # Access the value
    return data["simulation_control"]["number_of_iteration"]

# Example usage
file_path = "control_file.scf"
value = read_number_of_iteration(file_path)
print("number_of_iteration:", value)
