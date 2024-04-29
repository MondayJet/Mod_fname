import os

"""
DESCRIPTION:
This script helps in renaming files downloaded from the OceanofPDF website. It removes all the paddings, leaving you with just the name of the file.

USAGE:
1. Ensure that the script is run in the directory where the downloaded files are located.
2. It identifies all the items downloaded from Ocean of PDF, removes "_OceanofPDF.com_" from the filenames, and saves them with the modified names.

NOTES:
- The script was written on Thursday, April 11, 2024.
"""

# Import the required modules
import os

# Change directory to the Downloads folder
os.chdir("C:\\Users\\JohnMonday\\Downloads")

# Print the current working directory to verify the transition
print(os.getcwd())

# Iterate through all items in the directory
for f in os.listdir():
    # Check if the filename starts with "_OceanofPDF.com_"
    if f.startswith("_OceanofPDF.com_"):
        # Split the filename and extension
        fname, fext = os.path.splitext(f)
        
        # Remove "_" characters and join the filename parts
        mod_fname = fname.split("_")
        mod2_fname = " ".join(mod_fname)
        
        # Split the filename by spaces and extract relevant parts
        mod3_fname = mod2_fname.split(" ")[2:]
        d = " ".join(mod3_fname)
        
        # Construct the desired filename
        desired = f"{d}{fext}"
        
        # Print the desired filename
        print(desired)
        
        # Rename the file to the desired format
        os.rename(f, desired)
