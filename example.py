# Before using this tool make sure that you downloaded the script JsonHelper.py and put it in the same folder as the script that is using this tool

# import the tool
import JsonHelper as JH

# Create a JsonManager
save = JH.JsonManager()

# Open or Create a .json and load it's contents into the JsonManager
save.open("example#1-data.json")

# Change the value of a key
save.Value("val","wow")

# Set the value of a key to a dictionary 
save.Dict("dict",{"plane":1})

# Change a value for a key inside the selected dictionary
save.DictValue("dict","plane",True)

# Set the value for a key to a list
save.List("list",[0,1])

# Change a value at an index position inside the selected list
save.ListValue("list",1,True)
save.ListValue("list",0,"It works")

# Save.getValue("test-key") gets the value at the provided key
print("Value at key 'val' for save#1: "+str(save.getValue("val")))

# Resets the JsonManager so no file is opened
save.reset()

# Because we reseted the JsonManager, we must re-open a .json file to continue using functions like Value, Dict, List, getValue, ect...
save.open("example#1-data2.json")

# Change the value of a key
save.Value("val",0)

# Save.getValue("test-key") gets the value at the provided key
print("Value at key 'val' for save#2: "+str(save.getValue("val")))
