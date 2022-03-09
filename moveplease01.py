#!/usr/bin/env python3
"""Moving files about and renaming """


# import the OS and shutil modules
import shutil

import os

# define the function
def main():

    # set the folder we are looking at
    os.chdir('/home/student/mycode/')

    # use shutil to move the raynor.obj to ceph_storage directory
    shutil.move('raynor.obj','ceph_storage')

    # request the user to enter a new name for the kerrigan.obj file
    xname = input('What is the new name for the kerrigan.obj ?')

    # use shutil to move and rename the kerrigan.obj
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
