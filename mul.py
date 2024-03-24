import os
import subprocess

# Directory where the input files are located
input_directory = '/home/bipasaagrawal/Downloads/smt-kenken-solver/smt'
# Directory where the output files should be saved
output_directory = '/home/bipasaagrawal/Downloads/smt-kenken-solver/sol'

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Loop through each file in the input directory
for filename in os.listdir(input_directory):
    # Check if the file matches the specified pattern
    if filename.endswith("-smtlib.smt"):
        # Construct the full path to the input file
        input_path = os.path.join(input_directory, filename)
        
        # Generate the output file name by replacing '-smtlib.smt' with '-sol.smt'
        output_filename = filename.replace("-smtlib.smt", "-sol.smt")
        # Construct the full path to the output file
        output_path = os.path.join(output_directory, output_filename)
        
        # Call the mathsat program with the input file
        # Redirecting the output to the output file
        subprocess.run(["mathsat", input_path], stdout=open(output_path, "w"))
        
print("Processing complete.")
