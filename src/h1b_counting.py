#!/usr/bin/env python

## Open csv file
csvInput = './input/h1b_input.csv'

## Identify the entries that we are interested in by analyzing the title labels
## Pre: first line of the file opened
## Post: index of the relevant data, namely, application status, occupation and state
def indexExtraction(titles):
    statusIndexList = []
    occupationIndexList = []
    stateIndexList = []

    for i, elem in enumerate(titles):
        if "STATUS" in elem:
            statusIndexList.append(i)
        elif "SOC" in elem and "NAME" in elem:
            occupationIndexList.append(i)
        elif "WORK" in elem and "STATE" in elem:
            stateIndexList.append(i)
            
    ## Keep the index of the first occurrence of specific entries
    return statusIndexList[0],occupationIndexList[0],stateIndexList[0]

## Count occurrence of each unique item and return the result with occurrence count and formatted percentages
## Pre: a list of relevant data
## Post: a list of sorted tuples that consist of unique entry names, occurrence count, and percentage weight of total data 
def countOccurance(datalist):
    ## Get the list of unique data
    uniqueItem = list(set(datalist))
    ## count the total number of data entries
    totalOccurance = len(datalist)
    itemCount = []
    ## count occurrence of each unique item
    for item in uniqueItem:
        singleCount = datalist.count(item);
        ## format data as name of the entry, occurrence count and percentage
        itemCount.append((item.strip('"'),singleCount, "{0:.1f}".format(singleCount/totalOccurance * 100)+'%'))
    ## return the list of tuples sorted by occurrence counts in reverse order and alphabetic when the counts reach a tie 
    return sorted(itemCount, key = lambda x: (-x[1],x[0]))

## output result in the desired dictionary
## Pre: the category of the relevant data, namely, states or occupations
## Post: none
def outputResult(category, resultList):
    ## keep the top 10 if the resultList is too long
    if len(resultList) > 10:
        resultList = resultList[:10]
    ## create output file in desired directory
    f = open('./output/top_10_%s.txt' % category, 'w')
    ## write the title of the table
    f.write("TOP_%s;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n" % category.upper())
    ## output each entry in the desired format
    for t in resultList:
        line = ';'.join(str(x) for x in t)
        f.write(line + '\n')
    f.close()
    

## Main
## read in the csv file
with open(csvInput, 'r') as f:
    #read from csv line by line, rstrip remove '\n' at the end of line
    lines = [line.rstrip() for line in f] 

## Identify the title, format title to be all uppercase
titles = list(map(lambda x:x.upper(),lines.pop(0).split(';')))

## Keep the index of the first occurrence of specific entries
statusIndex, occupationIndex, stateIndex = indexExtraction(titles)

## Define two new lists to keep track of data we are interested in
occupation = []
state = []

## Keep the relevant data on each line
for line in lines:
    words = line.split(';')#get each item in one line
    ##Only document the relevant data of certified candidates
    if words[statusIndex].upper() == 'CERTIFIED':
        occupation.append(words[occupationIndex])
        state.append(words[stateIndex])

## count occurrence and output formatted result
outputResult('states', countOccurance(state))
outputResult('occupations', countOccurance(occupation))
# stateCount = countOccurance(state)
# if len(stateCount) > 10:
#     outputResult('states', stateCount[:10])
# else:
#     outputResult('states', stateCount)

    
# occupationCount = countOccurance(occupation)
# if len(occupationCount) > 10:
#     outputResult('occupations', occupationCount[:10])
# else:
#     outputResult('occupations', occupationCount)
