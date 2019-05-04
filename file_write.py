#to write into a file
file = open('/tmp/paswd','w')  # contents will be cleared if the file already existed
file.write('yukiko, good morning\n') # the contents is still in buffer, so you can not read them in command line.

file.flush()   # flush the content from buffer into disk

file.writelines(['2nd line hello yukiko\n, 3rd line hello my friend\n']) # the correct format

file.close()    # the content would be written into disk automatically