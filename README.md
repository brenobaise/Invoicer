#Invoicer

#Description
A Command Line interface which automates the extraction of data from  CSV files.

#Prerequisites:
  <i>csv module<i/>
  (sql module) - Currently not implemented.

#Installation:
  For later releases, there will be a feature to select the file through the OS file systems.
  Make sure the file is within the same location as the module. Manually locate the csv file with open('invoice.csv') as csvfile:
  PRODUCTS list is currently holding the items to be searched in the csv file.
  Implementation to be added where the user can select from a list of values the items to be searched for, or an automation of such feature.
  Manually add the items to be searched for, make sure the string of items to be searched for are exactly the same as they are in the csv.

#Current State of the Program:

The system can match given values between a pair of lists. It will search from values of PRODUCTS list and will loop through the csv file.
If a match happens, it updates the dictionary with the item's name and its quantity.

The results are currently saved in a dictionary with the purpose of consolidating them later and maintaining a stock count of the items.
This can also be refered as inventory management.


Joao Baise
last update 06/10/22

  
