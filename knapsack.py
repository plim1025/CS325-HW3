import sys
import copy

# recursively calculates optimal subsets for given value, weight, and table
def allSubsetsHelper(table, curValue, curWeight, curSubset, subsets):
    rows = len(table)
    cols = len(table[0])
    # iterate through table rows backwards
    for i in range(rows-1, -1, -1):
        valueWithoutItem = dp[i-1][curWeight]
        valueWithItem = values[i]
        if curWeight - weights[i] >= 0:
            valueWithItem += dp[i-1][curWeight-weights[i]]
        # stop adding items to optimal subset if finished
        if curValue <= 0:
            break
        # recursively check if there are more than one subset for this row
        elif valueWithItem == valueWithoutItem:
            curSubsetCopy = copy.deepcopy(curSubset)
            curSubsetCopy.append([weights[i], values[i]])
            allSubsetsHelper(table, curValue - values[i], curWeight - weights[i], curSubsetCopy, subsets)
        # if find item that is included in subset, add to current subset
        elif curValue != dp[i-1][curWeight]:
            curSubset.append([weights[i], values[i]])
            curValue -= values[i]
            curWeight -= weights[i]
    subsets.append(curSubset)

# finds all subsets of items that achieve max profit
def allSubsets(table):
    # find composition of optimal subset with DP table
    curValue = dp[-1][-1]
    curWeight = weight - 1
    subsets = []
    allSubsetsHelper(table, curValue, curWeight, [], subsets)
    for i in range(len(subsets)):
        print("\tSubset:")
        for j in range(len(subsets[i])):
            print("\t\tWeight: " + str(subsets[i][j][0]) + " Value: $" + str(subsets[i][j][1]))


# error handling for command line arguments
if len(sys.argv) == 2:
    weights = []
    values = []

    filepath = 'data.txt'
    # opens file and stores in fp
    with open(filepath) as fp:
        # reads first line of file
        line = fp.readline()
        # while there are still existing lines
        while line:
            # split line based on whitespace
            lineArr = line.split()
            # store weight in array
            weights.append(int(lineArr[0]))
            # store value in array
            values.append(int(lineArr[1]))
            # read next line
            line = fp.readline()

    # max weight of knapsack
    weight = int(sys.argv[1])
    # number of items
    itemCount = len(weights)
    # dp table in form of 2D array
    dp = [[0]*weight for i in range(itemCount)]
    # base case - fill in first row of table
    for i in range(weight):
        weight = i + 1
        # if knapsack can fit first item, add that item's value to table's first row
        if weight >= weights[0]:
            dp[0][i] = values[0]
    for i in range(1, itemCount):
        for j in range(weight):
            weight = j + 1
            # if current item not ready to fit into array, then just take previous row's value
            if weight < weights[i]:
                dp[i][j] = dp[i-1][j]
            else:
                valueWithItem = 0
                valueWithoutItem = dp[i-1][j]
                if j - weights[i] < 0:
                    valueWithItem = values[i]
                else:
                    valueWithItem = dp[i-1][j-weights[i]] + values[i]
                dp[i][j] = max(valueWithItem, valueWithoutItem)
    print("Max profit with weight = " + str(weight) + ": $" + str(dp[-1][-1]))

    # print("One subset:")
    # # find composition of optimal subset with DP table
    # curValue = dp[-1][-1]
    # curWeight = weight - 1
    # # iterate through table rows backwards
    # for i in range(itemCount-1, -1, -1):
    #     # stop adding items to optimal subset if finished
    #     if curValue <= 0:
    #         break
    #     # if find item that is included in optimal composition, print out
    #     elif curValue != dp[i-1][curWeight]:
    #         print("\tWeight: " + str(weights[i]) + " Value: $" + str(values[i]))
    #         curValue -= values[i]
    #         curWeight -= weights[i]

    print("All subsets:")
    allSubsets(dp)

else:
    print('Must execute in format: \'python3 knapsack.py [capacity]\' where capacity is an integer')
