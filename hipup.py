import os, re

def hipIncrementVersion():
    # SETTINGS ==================
    setToFirstFrame = True # Sets playback frame of saved file to first frame (does not affect open file)
    setToManualUpdate = False # Sets update mode of saved file to manual (does not affect open file)
    autoversion = True # If no versioning exists, create a new version
    autoversionzfill = 3 # digit padding for autoversioning
    debug = 0 # print some items to console
    # ===========================

    orighip = hou.hipFile.name()
    hipname = hou.hipFile.basename()
    hipfile = hipname.split(".")[0]

    # check current filename for version prefix and split accordingly
    # Uses regex so a filename like myfile_verycool_v001.hip will get picked up correctly (not match the first _v)
    versionSections = ""
    versionType = ""
    if len(re.findall('_v(?=\d+)', hipfile)) > 0:
        versionSections = re.split('_v(?=\d+)', hipfile, 1)        
        versionType = "_v"
    elif len(re.findall('_V(?=\d+)', hipfile)) > 0:
        versionSections = re.split('_V(?=\d+)', hipfile, 1)          
        versionType = "_V"      

    # if no version prefix found, create it
    if versionSections == "":
        if(autoversion):
            versionSections = [hipfile, "0"*autoversionzfill]
            versionType = "_v"
            orighip = orighip.replace(hipfile, hipfile + versionType + "0"*autoversionzfill)
            print "No version found in hip name - Autoversioning"
        else:
            print "No version found in hip name - Exiting"
            return 1

    # regex - match numbers after version splitter. Match until non-numeric value is hit.  
    match = re.match('\d+', versionSections[1])    
    if match:
        versionNumber = match.group(0)
    else:
        print "Problem encountered matching version number - Exiting"
        return 1
    
    # Create new filename
    oldVersion = versionType + versionNumber
    if debug:
        print "Old version: " + oldVersion
    newVersion = versionType + str(int(versionNumber) + 1).zfill(len(versionNumber))
    newhip = orighip.replace(oldVersion, newVersion)
    if debug:    
        print "New file: " + newhip

    # Save the file
    confirm = 0
    if os.path.isfile(newhip) :
        text = "Overwrite existing hip file?"
        confirm = hou.ui.displayMessage(text, buttons=("Yes", "No"), severity=hou.severityType.Message, title="New Hip")
    if confirm == 0 :
        # update mode and frame settings
        updateMode = hou.updateModeSetting()
        frame = hou.frame()
        if (setToManualUpdate):
            hou.setUpdateMode(hou.updateMode.Manual)
        if (setToFirstFrame):
            # hou.setFrame(1)
            hou.setFrame(hou.playbar.playbackRange()[0])

        hou.hipFile.save(newhip)
        
        # reset update mode and frame
        hou.setUpdateMode(updateMode)
        hou.setFrame(frame)

hipIncrementVersion()