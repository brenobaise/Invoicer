# Invoicer
# Developed by Breno Baise
# 29/09/2022

# This program takes a csv invoice and extracts information from the file.
# Key features to add are to allow the application to push content into a database or Json file

import csv
stock = [] # this list is renposible for storing all the content extracted by csvreader
tstock = [] # this list is a container to be used by stock list -- not in use
tempList = [] # this list is responsible for formatting purposes  -- not in use
stockCount = [] # this list is the final holder of items.
myDictionary = {'Item Name:' : [],
                'Quantity:' : []}
PRODUCTS = ['POTATO MIDS', 'MUSHROOM CUP', 'CAULIFLOWER', 'GARLIC PEELED X 1kg', 'LETTUCE CRUNCHY MIX X 250 GM', 'LETTUCE EUROPA SALAD X 500G',
'WASHED BABY MIXED LEAF', 'CORIANDER LOOSE X 100G', 'BROCCOLI','CARROT', 'PEPPER GREEN', 'PEPPER RED', 'PEPPER YELLOW']
with open('invoice.csv', newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    csvReader = csv.reader(csvfile, dialect=dialect, delimiter=',', quoting=csv.QUOTE_MINIMAL)


    for row in csvReader:
        
        for i in row:
                stock.append(i)
                tstock.append(i)


print("*"*200)
print("*"*200)
stock = list(filter(None, stock)) # This simply removes any empty strings in the list
for i in stock:
        print("Index:", stock.index(i)," ", i)
tstock = list(filter(None, tstock))
for i in tstock:
        print("Index:", tstock.index(i)," ", i)

print("*"*200)
print("*"*200)
stock = stock[22:-1]

def searchForValue(itemName, targetList, updateToList):
        """
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
        1- The Dictionary to update
        2- The key of the dictionary to be updated
        3- The new value you, function expects a list as value
        4- The index of the list
        # For further updates, must convert this function to update any kind of data structures.
        """
        # targetDictionary.append({f'{key}':[value[index]]})
        targetDictionary[key].append(value[index])
        #myDictionary.update({'Item Name:':[stockCount[0]]}) // For future reference, example.

# This nested for loops, compares the Products list with the current stock list, any match is added to a new list
for row in stock:
        for item in PRODUCTS:
                if item in row:            
                        searchForValue(item, stock, stockCount) # function that adds the data to a final list
                        index = PRODUCTS.index(item)
                        # for values in myDictionary['Item Name:']:
                        #         myDictionary['Item Name:']  = item
                        break
                else:
                        continue

# print(" [SYSTEM]: STOCK >>> \n", stock ,"\n")
print("----------"*10,)
print(" [SYSTEM]: stockCOUNT >>> \n", stockCount , "\n")


for item in tstock:
        if item in PRODUCTS:
                index = tstock.index(item)
                index -= 2 # off set the index of the list
                tempList.append(tstock[index])
print(tempList)


# currently manually adding items to a dictionary
#                       Further updates: 
# TO consolidate them into a list or tuple for counting the stock.
updateDictionary(myDictionary, 'Item Name:', stockCount, 0)
updateDictionary(myDictionary, 'Quantity:', tempList, 0)


print(" [SYSTEM]: myDict >>> \n", myDictionary, "\n" )

