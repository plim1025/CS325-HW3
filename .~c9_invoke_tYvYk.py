import sys

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
    print(dp[-1][-1])

else:
    print('Must execute in format: \'python3 knapsack.py [capacity]\' where capacity is an integer')
