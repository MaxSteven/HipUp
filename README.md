# HipUp
A version incrementation and file saving script for Houdini. 
- Saves the current file with an increased version number or creates a new version suffix if it does not exist (e.g filename_v001.hip). 
- Includes options for the setting the playback frame and update mode of the saved file (without altering the open file)
- Uses regex for accurate pattern matching 

# Suggested Use
- Create a new Houdini shelf tool and copy the contents of hipup.py into the Script tab
- Adjust the settings at the top of the script to suit your preferences
- Assign a new hotkey to the tool such as Ctrl+Alt+S




- Future Work: Look into the presave/postsave python callback scripts which are new in 16.0.557
