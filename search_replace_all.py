import os
import  fileinput
word = raw_input("enter word to search:")
replc = raw_input("enter word to replace:")

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths("/home/praveen/NEW/root_dir")
for i in range (len(full_file_paths)):   
        tempFile = open(full_file_paths[i],'r+')
        for line in fileinput.input( full_file_paths[i] ):
                if word in line :
                        tempFile.write( line.replace( word, replc))
                        tempFile.close()
