# Opening and Closing a file "MyFile.txt"
# for object name file1.
file1 = open("MyFile.txt", "r")
file1.close()
    
    # Open function to open the file "MyFile1.txt"
# (same directory) in read mode and
file1 = open("MyFile.txt", "r")
	
# store its reference in the variable file1
# and "MyFile2.txt" in D:\Text in file2
file2 = open(r"D:\Text\MyFile2.txt", "r+")
