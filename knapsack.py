filepath = 'data.txt'
# opens file and stores in fp
with open(filepath) as fp:
    # reads first line of file
    line = fp.readline()
    # while there are still existing lines
    while line:
        print(line)
        # read next line
        line = fp.readline()