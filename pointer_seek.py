# to set pointer location with seek()

file = open('/tmp/passwd','rb')
file.read(3)   # pointer:3
file.read(2)   # pointer:5
file.seek(-2,2) # to move the point to the last 2 bytes form the end
file.read()   # can only read the last two bytes

file.seek(0,0) # to reset pointer to the beginning
file.read()   # read all the content in the file