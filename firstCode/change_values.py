import os

def change_frequency(folder):
	file_path = os.path.join(folder, "control_file.scf")
	with open(file_path, 'r') as file:
		content = file.read()

	content = content.replace("2.2e9", folder)

	with open(file_path, 'w') as file:
		file.write(content)

change_frequency("2.1e9")
change_frequency("2.3e9")
