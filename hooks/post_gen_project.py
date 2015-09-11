"""
The script will run after built the project
"""
import os
import shutil


# Get the root project directory
project_directory = os.path.realpath(os.path.curdir)
'''
# Determine the local_setting_file_location
local_setting_file_location = os.path.join(
    project_directory,
    'config/settings/local.py'
)

# Open locals.py
with open(local_setting_file_location) as f:
    local_py = f.read()

# Generate a SECRET_KEY that matches the Django standard

# Replace "CHANGEME!!!" with SECRET_KEY
local_py = local_py.replace('CHANGEME!!!', "have_changed")

# Write the results to the locals.py module
with open(local_setting_file_location, 'w') as f:
    f.write(local_py)
'''
