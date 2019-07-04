mylines = [] 
with open ('./demo.txt', 'rt') as myfile:                   # Open lorem.txt for reading text.
    for myline in myfile:                                   # For each line in the file,
        mylines.append(myline.rstrip('\n'))                 # strip newline and add to list.
for index,element in enumerate(mylines):                    # For each element in the list,
    print(str(index) + ':' + str(element.find("aaaaaa")))