import subprocess, os

# List of dependencies to be installed
dependencies = ["libcanberra-gtk-module", "libcanberra-gtk3-module"]

# Path to the PioneerStation directory
pioneer_dir = "PioneerStation"

# Install dependencies
for i in dependencies:
    subprocess.run(f"sudo apt-get install -y {i}", shell=True)

# Change the current working directory to the PioneerStation directory
os.chdir(pioneer_dir)

# Add the current user to the 'dialout' group
subprocess.run(f"sudo adduser $USER dialout", shell=True)
