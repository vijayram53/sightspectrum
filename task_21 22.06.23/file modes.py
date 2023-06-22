#Example code:


# for object name file1.
file1 = open("MyFile.txt", "w")
file1.close()



#Example code:
 
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()


 #Example code:
# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()



##Read Only (‘r’) : Open text file for reading. 
##The handle is positioned at the beginning of the file.
## If the file does not exists, raises I/O error. 
##This is also the default mode in which file is opened. 



#Example code:
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)
