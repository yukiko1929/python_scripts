# use for to read lines

file = open('/tmp/passwd')
for line in file:
    print(line, end='')
