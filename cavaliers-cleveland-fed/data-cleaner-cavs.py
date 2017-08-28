# Xavier Collantes
# github.com/xcollantes
# Date: 8/28/2017
# File: data-cleaner-cavs.py
# Takes CVS and adds year field to data then exports to new CSV file 

import csv

def main():
    ### ENTER YOUR PATHS HERE ###
    PATH_IN = "./data/SystemicRisk.csv"
    PATH_OUT = "./data/clean-SystemicRisk.csv"
    #############################

    
    # Safeguard against accidental run 
    answer = input("Did you check source code for paths? (y/n)")

    if (start_check(answer)):
        out = open(PATH_OUT, "w+")        
        with open(PATH_IN, "r") as file:
            read = csv.reader(file, delimiter=",")

            inserted_list = []
            
            for element in read:

                insertStr = element[0] # Get str for date 
                year = insertStr[-4:] # Substring last 4 to get year
                
                element.insert(1, year) # Insert year into line  

                out.write(str(element) + "\n") # Write line element to clean-file 

    else:
        main()

    out.close()
    print ("Done. Please check " + PATH_OUT + " for accuracy.")

def start_check(reply):
    if reply == 'Y' or reply == 'y':
        return True
    elif reply == 'N' or reply == 'n':
        return False
    else:
        print ("I'm sorry Dave, I'm afraid I can't do that.  - HAL3000")
        main()
        
main()
