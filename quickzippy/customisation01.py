#!/usr/bin/env python3

""" """

def main():
    
    # import the zipfile module
    import zipfile
    
    # ask the user for a file to check if it is a .zip or not, store in variable iszip
    iszip = input("Which file do you wish to examine?")

    # check to see if the file is a zip using the .is_zipfile method
    if zipfile.is_zipfile(iszip):
        print("The specified file is a zip file...")
    else:
        print("That file is not a zip file...")



if __name__ == "__main__":
    main()
