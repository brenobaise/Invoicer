# Invoicer
# Developed by Breno Baise
# 29/09/2022

# This program takes a csv invoice and extracts information from the file.
# Key features to add are to allow the application to push content into a database or Json file
import csv
rawCsvList = [] # this list is renposible for storing all the content extracted by csvreader
extractedCsv = [] # this list is a container to be used by rawCsvList list -- not in use
quantityList = [] # Quantity of items extracted from the csv File.
itemsList = [] # Items extracted from the csv File.
DictionaryDB = {'Item Name:' : [],
                'Quantity:' : []}
PRODUCTS = ['POTATO MIDS', 'MUSHROOM CUP', 'CAULIFLOWER', 'GARLIC PEELED X 1kg', 'LETTUCE CRUNCHY MIX X 250 GM', 'LETTUCE EUROPA SALAD X 500G',
'WASHED BABY MIXED LEAF', 'CORIANDER LOOSE X 100G', 'BROCCOLI','CARROT', 'PEPPER GREEN', 'PEPPER RED', 'PEPPER YELLOW']
with open('invoice.csv', newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    csvReader = csv.reader(csvfile, dialect=dialect, delimiter=',', quoting=csv.QUOTE_MINIMAL)


    for row in csvReader:

        for i in row:
                rawCsvList.append(i)
                extractedCsv.append(i)

# Formatting of the lists
rawCsvList = list(filter(None, rawCsvList)) # This simply removes any empty strings in the list
extractedCsv = list(filter(None, extractedCsv))# This simply removes any empty strings in the list
rawCsvList = rawCsvList[22:-1] # Deletes unecessary data from the csv variable, such as address.


def searchForValue(itemName, targetList, updateToList):
        """
        This function is responsible searching for a value in a specified list \n
        This function takes as parameters:\n
        1-the name of the item to be queried,\n
        2-a list to be searched,\n
        3-the list to append the fetched item.\n
        """
        # for every index in the target list
        for item in range(len(targetList)):
                #check if the item being searched is in the queried list
                if itemName in targetList[item]:
                        # if True, assign the value of this item into a variable
                        i = targetList[item]
                        # push the variable into a new list
                        updateToList.append(i)
                        break


def updateDictionary(targetDictionary, key, value, index ):
        """
        This fuction takes as parameters:
        1- The Dictionary to update \n
        2- The key of the dictionary to be updated \n
        3- The new value you, function expects a list as value \n
        4- The index of the list \n
        This function should only be used to update dictionaries.
        #TO implement: convert this function to update any kind of data structures.
        """
        # targetDictionary.append({f'{key}':[value[index]]})
        #DictionaryDB.update({'Item Name:':[itemsList[0]]}) // For future reference, example.
        targetDictionary[key].append(value[index])
        

# This nested for loops, compares the Products list with the current rawCsvList list, any match is added to a new list
for row in rawCsvList:
        for item in PRODUCTS:
                if item in row:            
                        searchForValue(item, rawCsvList, itemsList) # function that adds the data to a final list
                        index = PRODUCTS.index(item)
                        break
                else:
                        continue

# This loop uses the items in PRODUCTS list and compares them to the csv rawCsvList.
# If there is a match it finds the index of such item and sends it to the quantityList.
for item in extractedCsv:
        if item in PRODUCTS:
                index = extractedCsv.index(item)
                index -= 2 # off set the index of the list
                quantityList.append(extractedCsv[index])
print(quantityList)

print(" [SYSTEM]: itemsList >>> \n", itemsList , "\n")




# currently manually adding items to a dictionary
#                       Further updates: 
# To consolidate them into a list or tuple for counting the rawCsvList.
updateDictionary(DictionaryDB, 'Item Name:', itemsList, 0)
updateDictionary(DictionaryDB, 'Quantity:', quantityList, 0)


print(" [SYSTEM]: myDict >>> \n", DictionaryDB, "\n" )


