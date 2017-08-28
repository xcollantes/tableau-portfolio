

import csv

def main():
    out = open("./clean-SystemicRisk.csv", "w+")
    with open("./SystemicRisk.csv", "r") as file:
        read = csv.reader(file, delimiter=",")

        inserted_list = []
        
        for element in read:

            insertStr = element[0] # Get str for date 
            year = insertStr[-4:] # Substring last 4 to get year
            
            element.insert(1, year) # Insert year into line  

            out.write(str(element) + "\n") # Write line element to clean-file 



    out.close()
main()
