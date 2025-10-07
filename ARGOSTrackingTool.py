#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2025
#--------------------------------------------------------------

#Ask user for a date
user_date = input("Enter a date: ")

#Create a variable pointing to the data file
file_name = './Data/Raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
lineString = file_object.readline()

#Initialize dictionaries
date_dict = {}
location_dict = {}

#Iterate through all lines
while lineString:
    # Check if line is a data line
    if lineString[0] in ("#","u"):
        lineString = file_object.readline()
        continue
   
    #Split the string into a list of data items
    lineData = lineString.split()
   
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Determine if location class criteria is met
    if obs_lc in ("1","2","3"):
        #Add items to ditonaries
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat,obs_lon)
   
    #Print the location of sara
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

    #Read next line
    lineString = file_object.readline()