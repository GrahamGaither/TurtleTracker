#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Graham Gaither (graham.gaither@duke.edu)
# Date:   Fall 2025
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = 'data//raw//sara.txt'

#Create a file object from the file
file_Object = open('data//raw//sara.txt','r')

#Read each line in file for while loop
lineString = file_Object.readline()

#Iterate through lines
while lineString != "":
    #determine if line starts with # or u; if so, skip
    if lineString[0] in ("#","u"):
        lineString = file_Object.readline()
        continue

    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

    #Move to the next line
    lineString = file_Object.readline()

#Close the file
file_Object.close()